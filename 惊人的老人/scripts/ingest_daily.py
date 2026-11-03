#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取 WorkBuddy 游戏行业日报 → raw/<日期>_游戏行业日报.md

规则见 AGENTS.md：
  - raw/ 不可变：已存在的日期文件一律跳过，不覆盖
  - published = 日报对应日期；scraped = 实际抓取日期
  - 保留文内「来源」链接，确保可回溯到原始报道

用法：
  python3 scripts/ingest_daily.py              # 抓索引里所有尚未入库的日期
  python3 scripts/ingest_daily.py --date 2026-11-02
  python3 scripts/ingest_daily.py --latest 1   # 只抓最新 N 天
  python3 scripts/ingest_daily.py --dry-run    # 只报告，不写文件

无第三方依赖，仅用标准库。
"""

import argparse
import datetime as dt
import hashlib
import os
import re
import sys
import urllib.error
import urllib.request
from html import unescape
from html.parser import HTMLParser

BASE = "https://game-industry-daily-86691.app.workbuddy.host"
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(VAULT, "raw")
LOG = os.path.join(VAULT, "log.md")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
SLUG = "游戏行业日报"
WIKI_SLUG = "游戏百科"

VOID = {"br", "img", "meta", "link", "hr", "input"}
BLOCK = {"p", "div", "section", "header", "footer", "ol", "ul", "table",
         "blockquote", "h1", "h2", "h3", "h4", "h5", "h6", "article", "li"}


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.children = []
        self.parent = parent

    def text(self):
        out = []
        for c in self.children:
            out.append(c if isinstance(c, str) else c.text())
        return "".join(out)


class TreeBuilder(HTMLParser):
    """把 HTML 建成轻量 DOM。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        nd = Node(tag, attrs, self.cur)
        self.cur.children.append(nd)
        if tag not in VOID:
            self.cur = nd

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        node = self.cur
        while node is not None and node.tag != tag:
            node = node.parent
        if node is not None and node.parent is not None:
            self.cur = node.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def find_all(node, tag):
    out = []
    for c in node.children:
        if isinstance(c, Node):
            if c.tag == tag:
                out.append(c)
            out.extend(find_all(c, tag))
    return out


def first(node, tag):
    r = find_all(node, tag)
    return r[0] if r else None


def clean(s):
    return re.sub(r"[ \t\u3000]+", " ", s.replace("\n", " ")).strip()


def inline_node(c):
    """把单个子节点渲染成行内 markdown，保留它自身的标签语义。

    关键：inline(node) 只遍历 node 的子节点，因此不能拿它去渲染 `a` 节点本身，
    否则 `<a href>` 会被当成普通文本，链接丢失。
    """
    if isinstance(c, str):
        return c
    tag = c.tag
    if tag in ("strong", "b"):
        return "**" + clean(inline(c)) + "**"
    if tag in ("em", "i"):
        return "*" + clean(inline(c)) + "*"
    if tag == "a":
        label = clean(c.text()) or "链接"
        href = c.attrs.get("href", "")
        return f"[{label}]({href})" if href else label
    if tag == "br":
        return "\n"
    if tag == "code":
        return "`" + c.text() + "`"
    if tag == "span" and "sep" in (c.attrs.get("class") or ""):
        return " | "
    return inline(c)


def inline(node):
    """行内渲染：strong -> **，a -> [t](href)。"""
    return "".join(inline_node(c) for c in node.children)


def render_table(tbl):
    rows = []
    for tr in find_all(tbl, "tr"):
        cells = [c for c in tr.children if isinstance(c, Node) and c.tag in ("td", "th")]
        if not cells:
            continue
        rows.append([clean(inline(c)).replace("|", "\\|") for c in cells])
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head = "| " + " | ".join(rows[0]) + " |"
    sep = "|" + "|".join(["---"] * width) + "|"
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows[1:])
    return head + "\n" + sep + ("\n" + body if body else "")


INLINE_TAGS = {"a", "strong", "b", "em", "i", "code", "span", "br",
               "small", "sup", "sub"}


def render_block(node, depth=0):
    """块级渲染，返回 markdown 段落列表。

    行内元素（a / strong / em / span …）先累积到缓冲区，遇到块级元素才 flush。
    否则 <a> 会被当成独立块处理，导致「来源」链接丢失。
    """
    parts = []
    buf = []

    def flush():
        if buf:
            t = clean("".join(buf))
            if t:
                parts.append(t)
            buf.clear()

    for c in node.children:
        if isinstance(c, str):
            buf.append(c)
            continue

        tag = c.tag
        if tag in INLINE_TAGS:
            buf.append(inline_node(c))
            continue

        flush()

        if tag in ("h1", "h2", "h3", "h4"):
            lvl = int(tag[1])
            parts.append("#" * lvl + " " + clean(inline(c)))
        elif tag == "p":
            t = clean(inline(c))
            if t:
                parts.append(t)
        elif tag == "blockquote":
            inner = render_block(c, depth + 1)
            if inner:
                parts.append("\n".join("> " + l for l in "\n".join(inner).splitlines()))
        elif tag in ("ol", "ul"):
            items = [x for x in c.children if isinstance(x, Node) and x.tag == "li"]
            lines = []
            for i, li in enumerate(items, 1):
                marker = f"{i}." if tag == "ol" else "-"
                sub = render_block(li, depth + 1)
                txt = "\n".join(sub).strip()
                if not txt:
                    continue
                txt = txt.replace("\n", "\n   ")
                lines.append(f"{marker} {txt}")
            if lines:
                parts.append("\n".join(lines))
        elif tag == "table":
            t = render_table(c)
            if t:
                parts.append(t)
        elif tag in ("section", "div", "header", "footer", "article"):
            sub = render_block(c, depth + 1)
            if sub:
                parts.append("\n\n".join(sub))
        elif tag in ("br", "hr"):
            parts.append("")
        else:
            sub = render_block(c, depth + 1)
            if sub:
                parts.append("\n\n".join(sub))

    flush()
    return parts


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def parse_index(html):
    """返回 [(date, title, summary), ...]，按日期倒序。"""
    items = []
    for m in re.finditer(r'href="(\d{4}-\d{2}-\d{2})\.html"', html):
        items.append(m.group(1))
    seen, dates = set(), []
    for d in items:
        if d not in seen:
            seen.add(d)
            dates.append(d)
    return sorted(dates, reverse=True)


def build_markdown(date, html, scraped):
    b = TreeBuilder()
    b.feed(html)
    body_node = first(b.root, "body") or b.root

    # 标题：h1
    h1 = first(body_node, "h1")
    title = clean(h1.text()) if h1 else f"游戏行业日报 · {date}"

    blocks = render_block(body_node)
    md = "\n\n".join(x for x in blocks if x.strip())

    # 去掉尾部 WorkBuddy 署名行（已在 frontmatter 记录来源）
    md = re.sub(r"\n*由 WorkBuddy 自动生成.*$", "", md, flags=re.S).strip()

    content_hash = hashlib.sha256(md.encode("utf-8")).hexdigest()

    fm = [
        "---",
        f"title: {title}",
        "type: source",
        "stage: raw",
        "source_kind: report",
        f"source_url: {BASE}/{date}.html",
        f"published: {date}",
        f"scraped: {scraped}",
        "source_updated: 未知",
        "classified_as: event",
        f'content_hash: "{content_hash}"',
        "review_status: resolved",
        "tags:",
        "  - 游戏新闻",
        "  - raw",
        "  - 日报",
        "---",
        "",
        "> **来源性质**：这是 WorkBuddy 自动生成的二手汇总，"
        "文内「来源」链接指向原始报道。引用时以原始报道为准，不要把汇总当一手证据。",
        "",
        md,
        "",
    ]
    return "\n".join(fm), title, content_hash


def build_wiki_markdown(date, html, scraped):
    """游戏百科：每天 3 个词条（美术 / 开发 / 拆解各一）。"""
    b = TreeBuilder()
    b.feed(html)
    body_node = first(b.root, "body") or b.root

    h1 = first(body_node, "h1")
    title = clean(h1.text()) if h1 else f"游戏百科 · {date}"

    blocks = render_block(body_node)
    md = "\n\n".join(x for x in blocks if x.strip())
    md = re.sub(r"\n*由 WorkBuddy 自动生成.*$", "", md, flags=re.S).strip()

    content_hash = hashlib.sha256(md.encode("utf-8")).hexdigest()

    fm = [
        "---",
        f"title: {title}",
        "type: source",
        "stage: raw",
        "source_kind: encyclopedia",
        f"source_url: {BASE}/wiki/{date}.html",
        f"published: {date}",
        f"scraped: {scraped}",
        "source_updated: 未知",
        "classified_as: concept",
        f'content_hash: "{content_hash}"',
        "review_status: resolved",
        "tags:",
        "  - 游戏设计",
        "  - raw",
        "  - 百科",
        "---",
        "",
        "> **来源性质**：WorkBuddy 自动生成的百科词条，每天 3 个（美术 / 开发 / 拆解各一）。"
        "文末「来源」指向公开资料，属于二手整理。词条正文里的判断是生成方的概括，"
        "编译成 Wiki 页时应标 `confidence: low` 并回查原始来源。",
        "",
        md,
        "",
    ]
    return "\n".join(fm), title, content_hash


def parse_wiki_index(html):
    """索引页里的 /wiki/YYYY-MM-DD.html 链接。"""
    dates = []
    seen = set()
    for m in re.finditer(r'href="wiki/(\d{4}-\d{2}-\d{2})\.html"', html):
        d = m.group(1)
        if d not in seen:
            seen.add(d)
            dates.append(d)
    return sorted(dates, reverse=True)



def append_log(lines):
    if not lines:
        return
    with open(LOG, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    global BASE
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="只抓指定日期 YYYY-MM-DD")
    ap.add_argument("--latest", type=int, help="只抓最新 N 天")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--base", default=BASE)
    args = ap.parse_args()

    BASE = args.base.rstrip("/")

    scraped = dt.date.today().isoformat()

    try:
        index_html = fetch(BASE + "/")
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"ERROR: 索引页抓取失败：{e}", file=sys.stderr)
        return 2

    dates = parse_index(index_html)
    if not dates:
        print("ERROR: 索引页里没有找到任何日期链接", file=sys.stderr)
        return 2

    if args.date:
        dates = [d for d in dates if d == args.date]
        if not dates:
            print(f"ERROR: 索引里没有 {args.date}", file=sys.stderr)
            return 2
    elif args.latest:
        dates = dates[: args.latest]

    os.makedirs(RAW, exist_ok=True)
    written, skipped, failed = [], [], []

    for d in dates:
        dest = os.path.join(RAW, f"{d}_{SLUG}.md")
        if os.path.exists(dest):
            skipped.append(d)
            continue
        rel = os.path.join("raw", f"{d}_{SLUG}.md")
        if args.dry_run:
            print(f"[dry-run] 将写入 {rel}")
            continue
        try:
            html = fetch(f"{BASE}/{d}.html")
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"WARN: {d} 抓取失败：{e}", file=sys.stderr)
            failed.append((d, str(e)))
            continue
        content, title, chash = build_markdown(d, html, scraped)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content)
        written.append((d, rel, len(content), chash[:12]))
        print(f"✓ {rel}  {len(content)} 字符  hash={chash[:12]}")

    # ---- 游戏百科（每日 3 词条：美术 / 开发 / 拆解）----
    wiki_dates = parse_wiki_index(index_html)
    if args.date:
        wiki_dates = [d for d in wiki_dates if d == args.date]
    elif args.latest:
        wiki_dates = wiki_dates[: args.latest]

    w_written, w_skipped = [], []
    for d in wiki_dates:
        dest = os.path.join(RAW, f"{d}_{WIKI_SLUG}.md")
        if os.path.exists(dest):
            w_skipped.append(d)
            continue
        rel = os.path.join("raw", f"{d}_{WIKI_SLUG}.md")
        if args.dry_run:
            print(f"[dry-run] 将写入 {rel}")
            continue
        try:
            html = fetch(f"{BASE}/wiki/{d}.html")
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"WARN: 百科 {d} 抓取失败：{e}", file=sys.stderr)
            failed.append((f"wiki/{d}", str(e)))
            continue
        content, title, chash = build_wiki_markdown(d, html, scraped)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content)
        w_written.append((d, rel, len(content), chash[:12]))
        print(f"✓ {rel}  {len(content)} 字符  hash={chash[:12]}")

    if not args.dry_run and (written or w_written):
        log_lines = [
            "",
            f"## [{scraped}] ingest | WorkBuddy 内容 ×{len(written) + len(w_written)}",
            "",
        ]
        for d, rel, n, h in written:
            log_lines.append(f"- `{rel}` — 日报，published {d}，{n} 字符，hash {h}")
        for d, rel, n, h in w_written:
            log_lines.append(f"- `{rel}` — 百科词条，published {d}，{n} 字符，hash {h}")
        if failed:
            log_lines.append(f"- 失败 {len(failed)} 条：" + "、".join(x[0] for x in failed))
        log_lines.append("- 来源：WorkBuddy 自动生成，属二手汇总，引用以原始报道为准")
        append_log(log_lines)

    print()
    print(f"日报  写入 {len(written)} | 跳过（已存在）{len(skipped)}")
    print(f"百科  写入 {len(w_written)} | 跳过（已存在）{len(w_skipped)}")
    print(f"失败 {len(failed)}")
    if failed:
        for d, e in failed:
            print(f"  ✗ {d}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
