#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取 arXiv 论文 → raw/<scraped>_arxiv_<shortid>_<slug>.md

规则见 AGENTS.md：
  - raw/ 不可变：按 arxiv_id 判重，已存在的论文一律跳过，不覆盖
  - published = 论文首次提交日（不是抓取日）；scraped = 实际抓取日期
  - 全文从 arxiv.org/html 抓取，失败降级 ar5iv，再失败降级 abs 页只存摘要
  - 只存正文（标题层级 + 段落 + 列表 + 数学文本），参考文献/图/表跳过

两种模式：
  python3 scripts/ingest_arxiv.py --query 'abs:"video game" AND abs:"level generation"'
  python3 scripts/ingest_arxiv.py --ids 2609.16679,2610.19213
  python3 scripts/ingest_arxiv.py --ids 2609.16679 --dry-run

无第三方依赖，仅用标准库。
"""

import argparse
import datetime as dt
import hashlib
import os
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser

API = "https://export.arxiv.org/api/query"
HTML_BASE = "https://arxiv.org/html"
AR5IV_BASE = "https://ar5iv.labs.arxiv.org/html"
ABS_BASE = "https://arxiv.org/abs"

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(VAULT, "raw")
LOG = os.path.join(VAULT, "log.md")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

SLEEP = 1.2  # 串行 + sleep，遵守 arXiv 3 req/s 约定

# 黑名单：检索候选时按标题+摘要排除，避免博弈论/区块链噪声混入
BLACKLIST = [
    "blockchain", "mining", "auction", "blotto", "wargaming",
    "equilibrium computation", "proof-of-work", "bitcoin", "cryptocurrency",
    "mean field game", "quantum game", "majority coloring", "coloring game",
    "nash equilibrium", "mechanism design",
]


def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def slugify(title):
    """把论文标题转成文件名 slug。"""
    s = re.sub(r"[^a-zA-Z0-9]+", "-", title).strip("-").lower()
    return s[:60].strip("-") or "paper"


def short_id(arxiv_id):
    """2609.16679v2 -> 2609.16679"""
    return re.sub(r"v\d+$", "", arxiv_id)


class Entry:
    def __init__(self, xml):
        def g(name):
            m = re.search(rf"<{name}>(.*?)</{name}>", xml, re.S)
            return clean(m.group(1)) if m else ""

        self.arxiv_id = g("id").split("/abs/")[-1].strip()
        self.title = g("title")
        self.summary = g("summary")
        self.published = g("published")[:10]
        self.updated = g("updated")[:10]
        authors = re.findall(r"<name>(.*?)</name>", xml, re.S)
        self.authors = ", ".join(clean(a) for a in authors if clean(a))
        self.version = self.arxiv_id.split("v")[-1] if "v" in self.arxiv_id else "1"


def query_arxiv(term, max_results=15):
    """返回候选条目列表（不写文件）。"""
    url = (f"{API}?search_query={term}&start=0&max_results={max_results}"
           f"&sortBy=submittedDate&sortOrder=descending")
    xml = fetch(url)
    entries = [Entry(e) for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S)]
    return entries


def passes_blacklist(entry):
    hay = (entry.title + " " + entry.summary).lower()
    return not any(b in hay for b in BLACKLIST)


def fetch_fulltext(arxiv_id):
    """返回 (markdown 正文, source_url, full_text_available)。

    优先 arxiv.org/html，失败降级 ar5iv，再失败降级 abs 页（只留摘要）。
    """
    sid = short_id(arxiv_id)
    for base in (HTML_BASE, AR5IV_BASE):
        url = f"{base}/{arxiv_id}"
        try:
            html = fetch(url)
            if len(html) < 5000:
                continue  # 太短，多半是 404 页面
            body = extract_body(html)
            if body and len(body) > 500:
                return body, url, True
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
            continue
    # 降级：abs 页只有摘要，正文标注不可用
    return "", f"{ABS_BASE}/{sid}", False


class BodyExtractor(HTMLParser):
    """从 LaTeXML 生成的 arXiv HTML 里提取正文 markdown。

    只保留：h1-h4 标题、ltx_p 段落、ltx_itemize/enumerate 列表、math 文本。
    跳过：script/style/nav/header/footer/figure/table/picture、
         参考文献 ltx_biblist、目录 ltx_TOC、LaTeX 错误命令 ltx_ERROR。
    """

    # 需要整体跳过的块级标签（含其所有子节点）
    SKIP_TAGS = {"script", "style", "nav", "header", "footer",
                 "figure", "table", "picture", "form", "svg", "math"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []          # markdown 行
        self.buf = []          # 当前行内文本缓冲
        self.skip = 0          # >0 时在跳过块内部
        self.in_bib = False    # 进入参考文献后截断
        self.in_toc = False    # 目录块内

    def _flush(self):
        t = clean("".join(self.buf))
        self.buf = []
        return t

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")

        if self.skip:
            self.skip += 1
            return
        if self.in_bib:
            return

        if tag in self.SKIP_TAGS:
            self.skip += 1
            return

        # 参考文献块：进入后截断（后面全跳过）
        if tag == "ul" and "ltx_biblist" in cls:
            self.in_bib = True
            return
        # 目录块：进入后整体跳过
        if tag == "div" and "ltx_TOC" in cls:
            self.in_toc = True
            return
        # LaTeX 错误命令（ltx_ERROR）：跳过该 span 的所有子节点
        if "ltx_ERROR" in cls:
            self.skip += 1
            return

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._flush()
            self.out.append(("\x00H", tag))  # 标题标记
            return
        if tag == "p":
            self._flush()
            return
        if tag == "li":
            self._flush()
            self.out.append(("\x00LI", None))
            return

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        if self.in_bib:
            return

        # 目录块结束
        if self.in_toc:
            if tag == "div":
                self.in_toc = False
            return

        if tag in self.SKIP_TAGS:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            t = self._flush()
            if t:
                lvl = int(tag[1])
                self.out.append("#" * lvl + " " + t)
            return
        if tag == "p":
            t = self._flush()
            if t:
                self.out.append(t)
            return
        if tag == "li":
            t = self._flush()
            if t:
                self.out.append("- " + t)
            return

    def handle_data(self, data):
        if self.skip or self.in_bib or self.in_toc:
            return
        if data:
            self.buf.append(data)

    def result(self):
        self._flush()
        # 折叠空行，丢弃未闭合的标题标记
        out, blank = [], False
        for ln in self.out:
            if isinstance(ln, tuple):
                continue  # 未闭合的控制标记，丢弃
            if not ln.strip():
                if not blank:
                    out.append("")
                blank = True
            else:
                out.append(ln)
                blank = False
        return "\n".join(out).strip()


def extract_body(html):
    """从 arXiv HTML 提取正文。"""
    # 定位 <article>，没有则用全文
    m = re.search(r"<article\b", html)
    seg = html[m.start():] if m else html
    p = BodyExtractor()
    try:
        p.feed(seg)
    except Exception:
        pass
    return p.result()


def build_markdown(entry, body, source_url, full_text, scraped):
    sid = short_id(entry.arxiv_id)
    content_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()

    note = []
    if not full_text:
        note.append(
            "> **full_text: unavailable** —— arXiv 无 HTML 版且 ar5iv 抓取失败，"
            "本文仅含摘要，编译前需回查原文。")
    note_text = ("\n".join(note) + "\n\n") if note else ""

    fm = [
        "---",
        f"title: {entry.title}",
        "type: source",
        "stage: raw",
        "source_kind: paper",
        f"source_url: {source_url}",
        f"arxiv_id: {entry.arxiv_id}",
        f"authors: {entry.authors}",
        f"source_version: {entry.version}",
        f"published: {entry.published}",
        f"scraped: {scraped}",
        "source_updated: " + entry.updated,
        "classified_as: concept",
        f'content_hash: "{content_hash}"',
        "review_status: resolved",
        "tags:",
        "  - 游戏设计",
        "  - raw",
        "  - arXiv",
        "  - AI",
        "---",
        "",
        "> **来源性质**：arXiv 预印本，多数未经同行评审。"
        "编译成 Wiki 页时应标 `confidence: low`，并核对实验条件（数据集、游戏类型、样本量）。",
        "",
        note_text,
        "## 摘要",
        "",
        entry.summary,
        "",
        "---",
        "",
        body,
        "",
    ]
    return "\n".join(fm), content_hash, sid


def append_log(lines):
    if not lines:
        return
    with open(LOG, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", help="检索 arXiv，只打印候选（应用黑名单），不写文件")
    ap.add_argument("--ids", help="逗号分隔的 arXiv id，抓全文写 raw/")
    ap.add_argument("--max-results", type=int, default=15)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    scraped = dt.date.today().isoformat()

    if args.query:
        try:
            entries = query_arxiv(args.query, args.max_results)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"ERROR: 检索失败：{e}", file=sys.stderr)
            return 2
        print(f"共 {len(entries)} 条，黑名单过滤后：\n")
        for e in entries:
            mark = "" if passes_blacklist(e) else "  [排除]"
            print(f"[{e.arxiv_id}] {e.title[:90]}{mark}")
            print(f"     {e.published} | {e.authors[:70]}")
            print(f"     {e.summary[:180]}")
            print()
        return 0

    if not args.ids:
        print("ERROR: 需要 --query 或 --ids", file=sys.stderr)
        return 2

    ids = [x.strip() for x in args.ids.split(",") if x.strip()]
    os.makedirs(RAW, exist_ok=True)

    written, skipped, failed = [], [], []

    for arxiv_id in ids:
        sid = short_id(arxiv_id)
        # 按 arxiv_id 判重：raw 里任何文件 frontmatter 含该 id 即跳过
        exists = False
        if os.path.isdir(RAW):
            for fn in os.listdir(RAW):
                if fn.endswith(".md"):
                    try:
                        head = open(os.path.join(RAW, fn), encoding="utf-8").read(600)
                        if f"arxiv_id: {arxiv_id}" in head:
                            exists = True
                            break
                    except OSError:
                        pass
        if exists:
            skipped.append(arxiv_id)
            continue

        if args.dry_run:
            print(f"[dry-run] 将抓取 {arxiv_id}")
            continue

        try:
            xml = fetch(f"{API}?id_list={arxiv_id}&max_results=1")
            entries = [Entry(e) for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S)]
            if not entries:
                print(f"WARN: {arxiv_id} 无元数据", file=sys.stderr)
                failed.append((arxiv_id, "无元数据"))
                continue
            entry = entries[0]
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"WARN: {arxiv_id} 元数据抓取失败：{e}", file=sys.stderr)
            failed.append((arxiv_id, str(e)))
            continue

        try:
            body, source_url, full_text = fetch_fulltext(entry.arxiv_id)
        except Exception as e:
            print(f"WARN: {arxiv_id} 全文抓取失败：{e}", file=sys.stderr)
            failed.append((arxiv_id, str(e)))
            continue

        if not full_text:
            body = entry.summary  # 降级：正文=摘要
            source_url = f"{ABS_BASE}/{sid}"

        slug = slugify(entry.title)
        dest = os.path.join(RAW, f"{scraped}_arxiv_{sid}_{slug}.md")
        content, chash, _ = build_markdown(entry, body, source_url, full_text, scraped)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content)
        rel = os.path.join("raw", os.path.basename(dest))
        written.append((arxiv_id, rel, len(content), chash[:12]))
        print(f"✓ {rel}  {len(content)} 字符  hash={chash[:12]}")
        time.sleep(SLEEP)

    if not args.dry_run and written:
        log_lines = [
            "",
            f"## [{scraped}] ingest | arXiv 论文 ×{len(written)}",
            "",
        ]
        for aid, rel, n, h in written:
            log_lines.append(f"- `{rel}` — paper {aid}，{n} 字符，hash {h}")
        if skipped:
            log_lines.append(f"- 跳过（已存在）{len(skipped)} 篇：{', '.join(skipped)}")
        if failed:
            log_lines.append(f"- 失败 {len(failed)} 篇：" + "、".join(f"{x[0]}({x[1]})" for x in failed))
        log_lines.append("- 来源：arXiv 预印本，多数未经同行评审")
        append_log(log_lines)

    print()
    print(f"写入 {len(written)} | 跳过（已存在）{len(skipped)} | 失败 {len(failed)}")
    for aid, e in failed:
        print(f"  ✗ {aid}: {e}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
