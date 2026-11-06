#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""链接体检：报告知识库的链接结构，并给出补链建议。

用途：每次 compile 之后跑一遍，决定要补哪些交叉链接。
纯标准库，只读不写。

用法：
  python3 scripts/link_report.py
  python3 scripts/link_report.py --json     # 机器可读
"""

import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = ('.agents', '.obsidian', '.cache', '.git', '__pycache__')


def read_frontmatter(path):
    """极简 frontmatter 解析，只取顶层标量字段。"""
    try:
        with open(path, encoding='utf-8') as f:
            txt = f.read()
    except OSError:
        return {}, ''
    if not txt.startswith('---'):
        return {}, txt
    end = txt.find('\n---', 3)
    if end == -1:
        return {}, txt
    meta = {}
    for line in txt[3:end].splitlines():
        s = line.strip()
        if not s or s.startswith('#') or ':' not in s:
            continue
        k, v = s.split(':', 1)
        meta[k.strip()] = v.strip()
    return meta, txt


def strip_code(txt):
    txt = re.sub(r'```.*?```', '', txt, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', txt)


def collect():
    files = []
    for p in glob.glob(os.path.join(VAULT, '**', '*.md'), recursive=True):
        rel = os.path.relpath(p, VAULT)
        if any(rel.startswith(d + os.sep) or rel == d for d in SKIP_DIRS):
            continue
        files.append((p, rel))

    by_name = {}
    meta = {}
    for p, rel in files:
        base = os.path.splitext(os.path.basename(p))[0]
        by_name[base] = rel
        by_name[rel[:-3]] = rel
        meta[rel], _ = read_frontmatter(p)

    out = defaultdict(set)
    inb = defaultdict(set)
    for p, rel in files:
        _, txt = read_frontmatter(p)
        body = strip_code(txt)
        for m in re.finditer(r'\[\[([^\]|#]+)', body):
            tgt = m.group(1).strip().rstrip('\\')
            # sources: 里常写成 [[raw/xxx.md]]，带 .md 后缀；索引页写成 [[raw/xxx]]。
            # 两种写法指向同一个文件，统一去掉 .md 再匹配，否则 frontmatter 引用会被漏掉。
            if tgt.endswith('.md') and tgt not in by_name:
                tgt = tgt[:-3]
            if tgt in by_name:
                q = by_name[tgt]
                if q != rel:
                    out[rel].add(q)
                    inb[q].add(rel)

    return files, meta, out, inb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    files, meta, out, inb = collect()

    articles = [rel for _, rel in files
                if rel.startswith('wiki' + os.sep) and '/index/' not in rel
                and os.sep + 'index' + os.sep not in rel]
    raws = [rel for _, rel in files if rel.startswith('raw' + os.sep)]

    def deg(x):
        return len(out.get(x, ())), len(inb.get(x, ()))

    isolated_articles = [a for a in articles if sum(deg(a)) == 0]
    unlinked_raw = [r for r in raws if sum(deg(r)) == 0]

    # 补链建议：同领域但互不相连的文章
    by_domain = defaultdict(list)
    for a in articles:
        by_domain[meta[a].get('domain', '未分类')].append(a)

    suggestions = []
    for domain, group in by_domain.items():
        for i, a in enumerate(group):
            for b in group[i + 1:]:
                linked = b in out.get(a, ()) or a in out.get(b, ())
                if not linked:
                    suggestions.append({
                        'domain': domain,
                        'a': os.path.splitext(os.path.basename(a))[0],
                        'b': os.path.splitext(os.path.basename(b))[0],
                    })

    result = {
        'articles': len(articles),
        'raws': len(raws),
        'linked_raws': len(raws) - len(unlinked_raw),
        'isolated_articles': [os.path.splitext(os.path.basename(a))[0] for a in isolated_articles],
        'unlinked_raw_count': len(unlinked_raw),
        'degrees': {os.path.splitext(os.path.basename(a))[0]: {'out': deg(a)[0], 'in': deg(a)[1]}
                    for a in articles},
        'suggestions': suggestions,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print('═══ 链接体检 ═══')
    print(f'文章 {result["articles"]} 篇 | raw {result["raws"]} 份'
          f'（其中 {result["linked_raws"]} 份被引用，{result["unlinked_raw_count"]} 份是孤儿）')
    print()
    print('文章连接度（出链 / 入链）')
    for name, d in sorted(result['degrees'].items(), key=lambda kv: -(kv[1]['out'] + kv[1]['in'])):
        flag = '  ← 孤立，需补链' if d['out'] + d['in'] == 0 else ''
        print(f'  {d["out"]:2d} 出 / {d["in"]:2d} 入  {name}{flag}')

    print()
    if isolated_articles:
        print(f'⚠ 有 {len(isolated_articles)} 篇文章没有任何链接，属于图谱死角')
    else:
        print('✓ 所有文章至少有一条链接')

    print()
    if suggestions:
        print(f'补链候选（同领域但互不相连，共 {len(suggestions)} 对）')
        for s in suggestions[:15]:
            print(f'  [{s["domain"]}] {s["a"]}  ↔  {s["b"]}')
        if len(suggestions) > 15:
            print(f'  …还有 {len(suggestions) - 15} 对')
    else:
        print('✓ 同领域文章已互连')
    print()
    print('判断标准：文章不是孤岛、同主题互相可达即可。不要为凑数硬链不相关的内容。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
