---
title: Source Index
type: index
domain: 游戏圈
updated: 2026-11-03
---

# 游戏圈知识库 — Source Index

所有原始资料及其被哪些 Wiki 文章引用。

**三个日期分开记**（规则见 [AGENTS.md](../../AGENTS.md)）：`published` 原文发表日 / `scraped` 收录日 / `source_updated` 来源修订日。一条旧新闻今天才收，发表是旧日期、收录是今天。混淆这两个，时间轴就会失真。

## 已编译资料

被至少一篇 Wiki 文章引用的来源：

| 来源 | 发表 | 收录 | 来源修订 | 引用它的文章 |
|---|---|---|---|---|
| [[raw/2026-11-02_游戏行业日报]] | 2026-11-02 | 2026-11-02 | 未知 | [[影之刃零首周末峰值]]、[[买断制单机的前 90 分钟]] |
| [[raw/2026-11-03_游戏百科]] | 2026-11-03 | 2026-11-03 | 未知 | [[像素艺术的抖动技法]]、[[ECS 与 DOTS]]、[[魂系设计语言]] |
| [[raw/2026-11-03_游戏行业日报]] | 2026-11-03 | 2026-11-03 | 未知 | [[买断制立项的成本倒推]]、[[AI 逆向与可防守位置]]、[[影之刃零首周末峰值]] |

### arXiv 论文（2026-11-03 收编）

| 来源 | 发表 | 收录 | 来源修订 | 引用它的文章 |
|---|---|---|---|---|
| [[raw/2026-11-03_arxiv_2605.01783_runtime-evaluation-of-procedural-content-generation-in-an-en]] | 2026-05-03 | 2026-11-03 | 2026-05-03 | [[AI 铺关卡：能用到哪一步]] |
| [[raw/2026-11-03_arxiv_2603.26782_multiverse-language-conditioned-multi-game-level-blending-vi]] | 2026-03-25 | 2026-11-03 | 2026-03-31 | [[AI 铺关卡：能用到哪一步]] |
| [[raw/2026-11-03_arxiv_2606.03857_a-novel-procedural-generation-for-level-design-of-mansions-a]] | 2026-06-02 | 2026-11-03 | 未知 | [[AI 铺关卡：能用到哪一步]]（仅摘要） |
| [[raw/2026-11-03_arxiv_2604.25482_from-world-gen-to-quest-line-a-dependency-driven-prompt-pipe]] | 2026-04-28 | 2026-11-03 | 未知 | [[AI 写任务线与世界设定]] |
| [[raw/2026-11-03_arxiv_2607.09403_fictional-worldbuilding-multi-agent-llm-collaboration-with-h]] | 2026-07-10 | 2026-11-03 | 未知 | [[AI 写任务线与世界设定]] |
| [[raw/2026-11-03_arxiv_2609.02931_llm-guided-reinforcement-learning-for-adaptive-npc-behavior]] | 2026-08-27 | 2026-11-03 | 未知 | [[AI 调 NPC 行为]] |
| [[raw/2026-11-03_arxiv_2606.16014_orchestrated-reality-from-role-play-to-living-playable-game]] | 2026-06-14 | 2026-11-03 | 未知 | [[AI 调 NPC 行为]] |
| [[raw/2026-11-03_arxiv_2610.19213_prefer-from-player-experience-to-personalized-game-refinemen]] | 2026-10-13 | 2026-11-03 | 未知 | [[AI 当设计评审]] |
| [[raw/2026-11-03_arxiv_2606.01976_cobg-learning-from-player-reviews-to-design-critique-and-rev]] | 2026-06-01 | 2026-11-03 | 2026-10-11 | [[AI 当设计评审]] |
| [[raw/2026-11-03_arxiv_2608.11539_player-perceptions-of-generative-ai-in-games-a-steam-review]] | 2026-08-11 | 2026-11-03 | 未知 | [[玩家怎么看 AI 生成内容]] |

## 孤儿资料

`raw/` 中尚未被任何 Wiki 文章引用的原始文件。这些是编译新文章的种子，也是更新已有页面的候选。

### 未编译的 arXiv 论文

| 来源 | 说明 |
|---|---|
| [[raw/2026-11-03_arxiv_2609.16679_ai-for-games-in-the-foundation-model-era]] | 综述。**按收编标准主动不收**：它是 AI 视角的领域版图（四类角色），正是「弄反」的那一侧。留作背景参考，不建页 |

### 飞书文档（术语背景）

| 来源 | 说明 |
|---|---|
| [[raw/2026-11-03_feishu_ai核心概念]] | LLM / Agent / RAG / MCP / Workflow / Harness 的术语链路。仅作编译时的术语底座，**不建页**（超出 purpose.md 范围） |
| [[raw/2026-11-03_feishu_卡帕西知识库]] | Karpathy LLM Wiki 教程版，与本库 AGENTS.md 对照用。**不建页** |

### 未编译的行业日报

**当前 24 份**，全部是 WorkBuddy 游戏行业日报：

| 范围 | 数量 | 说明 |
|---|---|---|
| 2026-10-09 ~ 2026-10-31 | 23 | `scripts/ingest_daily.py` 全量回填 |
| 2026-11-01 | 1 | 同上 |

按天逐条列在 `raw/` 目录里，文件名格式 `YYYY-MM-DD_游戏行业日报.md`。需要时按主题合并编译，不要逐日生成摘要。

## 按收录月份统计

| 年月 | 收录数量 |
|---|---|
| 2026-11 | 39 |

## 待审阅

`review_status: pending` 的资料，需要人工判断：

当前：无

## 数据源说明

- **WorkBuddy 日报 / 百科**：自动生成的二手汇总，文内保留指向原始报道的链接。引用时以原始报道为准
- **arXiv 论文**：预印本，多数未经同行评审。`confidence` 封顶 `medium`，实验条件必须写明
- **飞书文档**：AI 工具与知识库教程类，仅作术语背景，不进 wiki

转载与汇总不构成独立证据。
