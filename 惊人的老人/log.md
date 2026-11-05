# Log

按时间顺序、仅追加的知识库操作记录。不可修改历史条目。

**条目格式：**

```markdown
## [YYYY-MM-DD] <操作> | <简短描述>

（可选）一段简短上下文、发现或决策
```

**操作类型：** `ingest` · `compile` · `query` · `promote` · `research` · `delete` · `split` · `lint`

**快速查询：**

```bash
grep "^## \[" log.md | tail -10                # 最近 10 条
grep "^## \[.*compile" log.md | wc -l          # 编译总次数
grep "^## \[.*research" log.md | wc -l         # 研究总次数
grep "^## \[YYYY-MM" log.md                    # 某月所有操作
```

---

## [2026-11-02] bootstrap | 知识库初始化

Wiki 目录结构已创建，准备开始 ingest。

## [2026-11-02] bootstrap | 按游戏圈定位重建 Schema 层

- 新增 `AGENTS.md`：三层分工、四领域、三时间规范（published/scraped/source_updated）、更新 vs 新建判据、结构化 Diff、授权边界、禁止事项
- 新增 `raw/assets/`：截图与附件目录
- 新增 `wiki/index/Events Timeline.md`：按事件发生日倒序的大事件时间轴
- 新增四个领域目录：游戏设计 / 游戏新闻 / 厂商团队 / 品类市场（均空，待首批资料）
- 重写 `purpose.md`：游戏圈目标、5 个核心问题、范围边界、待检验假说
- 重写三个索引：Dashboard 补领域表与时间轴导航；Concept Index 改按领域分组；Source Index 加发表/收录/来源修订三列
- 依据：用户确认「保留卡帕西结构，不用萌芽知识库」

## [2026-11-02] ingest | WorkBuddy 游戏行业日报 ×1

- `raw/2026-11-02_游戏行业日报.md` — published 2026-11-02，5649 字符，hash 0150a996d4c0
- 来源：WorkBuddy 自动生成日报，属二手汇总，引用以原始报道为准

## [2026-11-02] ingest | WorkBuddy 游戏行业日报 ×1

- `raw/2026-11-02_游戏行业日报.md` — published 2026-11-02，5564 字符，hash a11a2393f3e7
- 来源：WorkBuddy 自动生成日报，属二手汇总，引用以原始报道为准

## [2026-11-02] ingest | WorkBuddy 游戏行业日报 ×1

- `raw/2026-11-02_游戏行业日报.md` — published 2026-11-02，5937 字符，hash 098153186f43
- 来源：WorkBuddy 自动生成日报，属二手汇总，引用以原始报道为准

## [2026-11-02] compile | 第一天日报 → 2 篇 Wiki

- 来源：`raw/2026-11-02_游戏行业日报.md`（WorkBuddy 二手汇总，单一来源）
- 新建 `wiki/游戏设计/买断制单机的前 90 分钟.md`（pattern，confidence: low）
- 新建 `wiki/游戏新闻/影之刃零首周末峰值.md`（event，event_date: 2026-11-01，confidence: low）
- 更新 Events Timeline / Concept Index / Source Index / Dashboard
- 未沉淀但已识别的 2 个主题（等更多来源再建页，避免一篇来源生成一篇摘要）：
  - AI 创作工具压低原型验证成本 → 同质化提前
  - 发行与研发的「分手条款」应写进立项清单
- 依据：AGENTS.md 三、四、五节

## [2026-11-02] ingest | WorkBuddy 游戏行业日报 ×24

- `raw/2026-11-01_游戏行业日报.md` — published 2026-11-01，5776 字符，hash 754bde4b6935
- `raw/2026-10-31_游戏行业日报.md` — published 2026-10-31，5774 字符，hash 0e74f4e5ba46
- `raw/2026-10-30_游戏行业日报.md` — published 2026-10-30，5594 字符，hash 68560cff6055
- `raw/2026-10-29_游戏行业日报.md` — published 2026-10-29，4460 字符，hash 324980a0ab4d
- `raw/2026-10-28_游戏行业日报.md` — published 2026-10-28，3918 字符，hash 8de56d742ab4
- `raw/2026-10-27_游戏行业日报.md` — published 2026-10-27，5149 字符，hash 960540a78c0b
- `raw/2026-10-26_游戏行业日报.md` — published 2026-10-26，4632 字符，hash 69cb959ac8f3
- `raw/2026-10-25_游戏行业日报.md` — published 2026-10-25，5359 字符，hash 824caf18a41b
- `raw/2026-10-24_游戏行业日报.md` — published 2026-10-24，4328 字符，hash ef47dd3c7e78
- `raw/2026-10-23_游戏行业日报.md` — published 2026-10-23，5681 字符，hash 5d95c31bee84
- `raw/2026-10-22_游戏行业日报.md` — published 2026-10-22，4696 字符，hash fb633a6471b5
- `raw/2026-10-21_游戏行业日报.md` — published 2026-10-21，6290 字符，hash e8ca487a8e9b
- `raw/2026-10-20_游戏行业日报.md` — published 2026-10-20，6338 字符，hash cb4a06537900
- `raw/2026-10-19_游戏行业日报.md` — published 2026-10-19，7161 字符，hash 29cef5e7272d
- `raw/2026-10-18_游戏行业日报.md` — published 2026-10-18，6828 字符，hash 9075d9efa594
- `raw/2026-10-17_游戏行业日报.md` — published 2026-10-17，7291 字符，hash d34a31e7e6e4
- `raw/2026-10-16_游戏行业日报.md` — published 2026-10-16，6617 字符，hash aedc3874b2c6
- `raw/2026-10-15_游戏行业日报.md` — published 2026-10-15，6293 字符，hash 86fdc2536cc9
- `raw/2026-10-14_游戏行业日报.md` — published 2026-10-14，5409 字符，hash 5ad4d8275f20
- `raw/2026-10-13_游戏行业日报.md` — published 2026-10-13，5878 字符，hash 2e3be063c5ec
- `raw/2026-10-12_游戏行业日报.md` — published 2026-10-12，5493 字符，hash e9acf659aa70
- `raw/2026-10-11_游戏行业日报.md` — published 2026-10-11，5467 字符，hash 95644c7a0a5b
- `raw/2026-10-10_游戏行业日报.md` — published 2026-10-10，5753 字符，hash f0825c4f1692
- `raw/2026-10-09_游戏行业日报.md` — published 2026-10-09，4117 字符，hash 74f302478de3
- 来源：WorkBuddy 自动生成日报，属二手汇总，引用以原始报道为准

## [2026-11-03] ingest | WorkBuddy 内容 ×2

- `raw/2026-11-03_游戏行业日报.md` — 日报，published 2026-11-03，6345 字符，hash 27b9082af8ea
- `raw/2026-11-03_游戏百科.md` — 百科词条，published 2026-11-03，2904 字符，hash dde81f3f3c2d
- 来源：WorkBuddy 自动生成，属二手汇总，引用以原始报道为准

## [2026-11-03] compile | 百科词条首次编译 ×3

- 来源：`raw/2026-11-03_游戏百科.md`（WorkBuddy 百科，每天 3 词条，单一二手来源）
- 新建 `wiki/游戏设计/像素艺术的抖动技法.md`（concept，confidence: low）
- 新建 `wiki/游戏设计/ECS 与 DOTS.md`（concept，confidence: low）
- 新建 `wiki/游戏设计/魂系设计语言.md`（pattern，confidence: low）
- 三篇均含「反论与缺口」段，`has_counter_arguments: true`
- 未沉淀：2026-11-03 的行业日报（影之刃零 72 小时 400 万份）留待按事件线合并，未单独建页
- 更新 Concept Index / Source Index / Dashboard
- 依据：AGENTS.md 九（百科词条编译规则）

## [2026-11-03] decision | 规则文件保持内联，不拆分

- 评估过把 `AGENTS.md` 的「九、操作入口」「发布到 GitHub」两节拆成独立文件的方案
- 实测：`AGENTS.md` 6679 字符 ≈ 2760 token，占 64K 上下文 4.3%；L0+L1 合计 ≈ 4260 token
- 成本：单次提问缓存命中约 0.0006 元，每天一次年成本约 2 元
- 不拆的理由：
  1. 现行 `AGENTS.md` 由 Harness 自动注入，不依赖工具调用；拆出后要模型主动去读，漏读风险高于固定的 token 开销
  2. 规则开销固定，正文持续增长，占比会随文章数自然下降（5 篇时约 4300 : 3600，50 篇时会降到 10% 以下）
- 重新评估的触发条件（满足任一才重新考虑）：`AGENTS.md` 超过 12000 字符 / 出现「规则未生效」的实际事故 / 单次固定开销超过 10000 token

## [2026-11-03] compile | 处理积压日报 1 份 → 2 篇 pattern

- 来源：`raw/2026-11-03_游戏行业日报.md`（二手汇总，策划视角小结 3 条洞察）
- 新建 `wiki/游戏设计/买断制立项的成本倒推.md`（pattern，confidence: low）
- 新建 `wiki/游戏设计/AI 逆向与可防守位置.md`（pattern，confidence: low）
- 反链审计：7 篇全部有链接，无孤立；补 2 条真相关反链
  - 买断制单机的前 90 分钟 → 买断制立项的成本倒推
  - 影之刃零首周末峰值 → 买断制单机的前 90 分钟、买断制立项的成本倒推
- 体检给出的另外 5 对「同领域候选」判定为无语义关系，不连（魂系↔AI逆向、魂系↔ECS、魂系↔成本倒推、ECS↔成本倒推、ECS↔抖动、成本倒推↔抖动）
- 跳过未沉淀的 2 个主题（写入 Dashboard 研究缺口）：
  - 版本日历与付费节点（明日方舟重回榜首 + 巨人合同负债）
  - 名越工作室解散（厂商团队领域仍空）
- 未改动 `影之刃零首周末峰值` 的正文：11-03 的 400 万份销量属于事件数据，按规则六需结构化 Diff 确认后再补
- 更新 Concept Index / Source Index / Dashboard

## [2026-11-03] compile | 影之刃零首周末峰值 补录 72 小时数据

- 来源：`raw/2026-11-03_游戏行业日报.md`（二手汇总，原始链接指向证券时报）
- 结构化 Diff 已确认后执行，3 条改动：
  1. 经过表补 10-30 / 11-02 两行，并标注首日 43.4 万与 72.4 万是同一事件的不同时点读数
  2. 新增「曲线怎么读」段：把峰值上升拆成周末效应 + 周一异常值，修正原文对整段上升的口碑归因
  3. 「影响」段补 400 万份 / 三天回本（标注为媒体推算而非财报）；反论段原「本文没有销量数据」已失效，改写为口径与含预购的说明
- 反链审计：7 篇全部有链接，无孤立；`影之刃零首周末峰值` 2 出 / 6 入
- 7 对同领域候选逐对判定为无语义关系，不连
- 更新 Events Timeline / Concept Index / Source Index / Dashboard
- 仍待补：10-29 解锁登顶、10-27 媒体评分解禁、10-26 定档（raw 中已有，未建 event 页）

> 上条修正：经过表实际只补了 1 行（11-02 周一 83 万）。首日 43.4 万与 72.4 万经核对是**同一天的两个时点读数**，不是两天，已合并为一行并在表下注明。

## [2026-11-03] ingest | arXiv 论文 ×1

- `raw/2026-11-03_arxiv_2609.16679_ai-for-games-in-the-foundation-model-era.md` — paper 2609.16679，236688 字符，hash 2483d46f4993
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] ingest | arXiv 论文 ×1

- `raw/2026-11-03_arxiv_2609.16679_ai-for-games-in-the-foundation-model-era.md` — paper 2609.16679，13287 字符，hash c52d9dd93b27
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] ingest | arXiv 论文 ×1

- `raw/2026-11-03_arxiv_2609.16679_ai-for-games-in-the-foundation-model-era.md` — paper 2609.16679，13256 字符，hash 1803e9d62145
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] ingest | arXiv 论文 ×9

- `raw/2026-11-03_arxiv_2603.26782_multiverse-language-conditioned-multi-game-level-blending-vi.md` — paper 2603.26782，22826 字符，hash ed6a37dc2593
- `raw/2026-11-03_arxiv_2606.03857_a-novel-procedural-generation-for-level-design-of-mansions-a.md` — paper 2606.03857，3485 字符，hash 64c3fb9a7621
- `raw/2026-11-03_arxiv_2605.01783_runtime-evaluation-of-procedural-content-generation-in-an-en.md` — paper 2605.01783，23408 字符，hash ea4bb07009b7
- `raw/2026-11-03_arxiv_2604.25482_from-world-gen-to-quest-line-a-dependency-driven-prompt-pipe.md` — paper 2604.25482，59701 字符，hash 22c517248e61
- `raw/2026-11-03_arxiv_2607.09403_fictional-worldbuilding-multi-agent-llm-collaboration-with-h.md` — paper 2607.09403，29449 字符，hash ee0201af3466
- `raw/2026-11-03_arxiv_2609.02931_llm-guided-reinforcement-learning-for-adaptive-npc-behavior.md` — paper 2609.02931，5124 字符，hash 44105716484c
- `raw/2026-11-03_arxiv_2606.16014_orchestrated-reality-from-role-play-to-living-playable-game.md` — paper 2606.16014，23325 字符，hash 2639540c7d59
- `raw/2026-11-03_arxiv_2610.19213_prefer-from-player-experience-to-personalized-game-refinemen.md` — paper 2610.19213，26569 字符，hash 614a8f0cac5f
- `raw/2026-11-03_arxiv_2606.01976_cobg-learning-from-player-reviews-to-design-critique-and-rev.md` — paper 2606.01976，6574 字符，hash 8c5e0b1ebebd
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] ingest | arXiv 论文 ×1

- `raw/2026-11-03_arxiv_2608.11539_player-perceptions-of-generative-ai-in-games-a-steam-review.md` — paper 2608.11539，26184 字符，hash 873cfc22f593
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] ingest | arXiv 论文 ×11

- `raw/2026-11-03_arxiv_2609.16679_ai-for-games-in-the-foundation-model-era.md` — paper 2609.16679，242521 字符，hash 46890727df51
- `raw/2026-11-03_arxiv_2603.26782_multiverse-language-conditioned-multi-game-level-blending-vi.md` — paper 2603.26782，32863 字符，hash b73b43800406
- `raw/2026-11-03_arxiv_2606.03857_a-novel-procedural-generation-for-level-design-of-mansions-a.md` — paper 2606.03857，3485 字符，hash 64c3fb9a7621
- `raw/2026-11-03_arxiv_2605.01783_runtime-evaluation-of-procedural-content-generation-in-an-en.md` — paper 2605.01783，73009 字符，hash cf9676e6102f
- `raw/2026-11-03_arxiv_2604.25482_from-world-gen-to-quest-line-a-dependency-driven-prompt-pipe.md` — paper 2604.25482，63838 字符，hash ff5407e42108
- `raw/2026-11-03_arxiv_2607.09403_fictional-worldbuilding-multi-agent-llm-collaboration-with-h.md` — paper 2607.09403，73674 字符，hash ca15969184b4
- `raw/2026-11-03_arxiv_2609.02931_llm-guided-reinforcement-learning-for-adaptive-npc-behavior.md` — paper 2609.02931，56928 字符，hash 96e8e820dcad
- `raw/2026-11-03_arxiv_2606.16014_orchestrated-reality-from-role-play-to-living-playable-game.md` — paper 2606.16014，23839 字符，hash 2fd466495be2
- `raw/2026-11-03_arxiv_2610.19213_prefer-from-player-experience-to-personalized-game-refinemen.md` — paper 2610.19213，28813 字符，hash 62c2283cd45d
- `raw/2026-11-03_arxiv_2606.01976_cobg-learning-from-player-reviews-to-design-critique-and-rev.md` — paper 2606.01976，12030 字符，hash 720f901f9acd
- `raw/2026-11-03_arxiv_2608.11539_player-perceptions-of-generative-ai-in-games-a-steam-review.md` — paper 2608.11539，61569 字符，hash c59602526252
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] ingest | arXiv 论文 ×11

- `raw/2026-11-03_arxiv_2609.16679_ai-for-games-in-the-foundation-model-era.md` — paper 2609.16679，242582 字符，hash 94183f203b00
- `raw/2026-11-03_arxiv_2603.26782_multiverse-language-conditioned-multi-game-level-blending-vi.md` — paper 2603.26782，34182 字符，hash fa53a5bd01cd
- `raw/2026-11-03_arxiv_2606.03857_a-novel-procedural-generation-for-level-design-of-mansions-a.md` — paper 2606.03857，3485 字符，hash 64c3fb9a7621
- `raw/2026-11-03_arxiv_2605.01783_runtime-evaluation-of-procedural-content-generation-in-an-en.md` — paper 2605.01783，75894 字符，hash b169c6bf0c9a
- `raw/2026-11-03_arxiv_2604.25482_from-world-gen-to-quest-line-a-dependency-driven-prompt-pipe.md` — paper 2604.25482，63856 字符，hash 241a8cd0cba3
- `raw/2026-11-03_arxiv_2607.09403_fictional-worldbuilding-multi-agent-llm-collaboration-with-h.md` — paper 2607.09403，75146 字符，hash 56c7c98d323a
- `raw/2026-11-03_arxiv_2609.02931_llm-guided-reinforcement-learning-for-adaptive-npc-behavior.md` — paper 2609.02931，57780 字符，hash c342bbd1bc08
- `raw/2026-11-03_arxiv_2606.16014_orchestrated-reality-from-role-play-to-living-playable-game.md` — paper 2606.16014，25289 字符，hash c5f82326b68f
- `raw/2026-11-03_arxiv_2610.19213_prefer-from-player-experience-to-personalized-game-refinemen.md` — paper 2610.19213，29297 字符，hash e07ca7a82092
- `raw/2026-11-03_arxiv_2606.01976_cobg-learning-from-player-reviews-to-design-critique-and-rev.md` — paper 2606.01976，31035 字符，hash 2d870a82c2ee
- `raw/2026-11-03_arxiv_2608.11539_player-perceptions-of-generative-ai-in-games-a-steam-review.md` — paper 2608.11539，61766 字符，hash 0b215dbfe864
- 来源：arXiv 预印本，多数未经同行评审

## [2026-11-03] 决策 | AI×游戏 收编范围：并入游戏设计，不新开领域

- 用户指示：不要新开 `wiki/AI 与游戏/`，并入 `wiki/游戏设计/`
- 用户指示二：分页主语必须是**游戏设计领域内的 AI×游戏**（设计师能不能用），不是 AI 研究分类
- 用户指示三：只收「相对有可行性」的成果
- 筛选线：收「AI 做游戏（关卡/任务/世界/NPC）」+「AI 理解玩家（体验建模/设计反馈/玩家态度）」；
  剔除「以游戏为测试床的 AI 评测」（benchmark、速通）与「AI 制作游戏」（编码 agent 产游戏）
- 可行性分级写入 `AGENTS.md` 九：A 本月可试 / B 一个项目周期 / C 不收
- 依据：用户 2026-11-03 对话；`purpose.md` 的「不覆盖与设计无关的内容」

## [2026-11-03] ingest | arXiv 论文 ×11 + 飞书 ×2

- 新建脚本 `scripts/ingest_arxiv.py`（纯标准库，镜像 `ingest_daily.py` 风格）
  - 两种模式：`--query` 只列候选（套黑白名单）、`--ids` 抓全文入库
  - 按 arxiv_id 判重；`published` = 论文首次提交日；额外字段 `arxiv_id` / `authors` / `source_version`
  - 全文链路 `arxiv.org/html` → `ar5iv` → abs 页降级
- **提取器 bug 修复过程（如实记录）**：
  1. 首版把 `figure`/`table` 列入跳过标签 → 第 4 节之后正文全丢（Momentum 只提到 3.1 节）
  2. 首版把 `svg` 列入跳过标签 → ar5iv 把正文渲染在 `<svg><foreignObject>` 内，整篇只剩摘要（CoBG）
  3. 状态机 `in_bib` 提前触发且不退出 → 同样导致截断
  4. 修复：改为 HTML 层面在 `ltx_biblist` 处截断 + skip 改为标签名栈；全部 11 篇重抓，10 篇章节完整，1 篇仅摘要
- 入库 11 篇（`raw/2026-11-03_arxiv_*.md`）：
  - 2609.16679 综述、2603.26782 Multiverse、2606.03857 Mansions（仅摘要）、
    2605.01783 Momentum、2604.25482 World-Gen-to-Quest-Line、2607.09403 AutoWorldBuilder、
    2609.02931 LLM 引导 NPC、2606.16014 Orchestrated Reality、
    2610.19213 PREFER、2606.01976 CoBG、2608.11539 Steam 玩家态度
- 入库 2 篇飞书（`source_kind: documentation`）：`ai核心概念`、`卡帕西知识库`
  - 飞书 wiki 是虚拟滚动，只提到首屏正文，文件内已标注提取范围；零宽字符已剔除
  - **不进 wiki**，仅作术语背景（超出 purpose.md 范围）

## [2026-11-03] compile | AI×游戏 首批 5 篇并入游戏设计

- 新建（均在 `wiki/游戏设计/`）：
  - `AI 铺关卡：能用到哪一步.md`（pattern）— Momentum(A) / Multiverse(B) / Mansions(C 仅参考)
  - `AI 写任务线与世界设定.md`（pattern）— World-Gen-to-Quest-Line + AutoWorldBuilder
  - `AI 调 NPC 行为.md`（pattern）— LLM 战术标签 + Orchestrated Reality
  - `AI 当设计评审.md`（pattern）— PREFER + CoBG
  - `玩家怎么看 AI 生成内容.md`（concept，`confidence: medium`）— Steam 50 万条评论
- 每页均带可行性卡（落地形态/依赖/成本/已验证范围/等级），`confidence` 封顶 medium
- 未建页：
  - 综述 2609.16679 — AI 视角版图，按标准主动不收，留作孤儿背景
  - 飞书 ×2 — 术语背景，不建页
- 协议更新：`purpose.md` 覆盖/不覆盖各加一条；`AGENTS.md` 九加 `ingest_arxiv` 入口与编译规则
- 索引更新：Concept Index（+5 行）、Dashboard（重点文章 +5、最近添加 +1）、Source Index（重建，含孤儿分类）
- 反链审计：12 篇全部有链接，无孤立；补 3 条真相关反链
  - `AI 逆向与可防守位置` → `玩家怎么看 AI 生成内容`（供给侧 vs 需求侧）
  - `AI 写任务线与世界设定` → `AI 调 NPC 行为`、`玩家怎么看 AI 生成内容`
- 其余 30 对同领域候选逐对判定为无语义关系，不连（魂系 ↔ ECS、像素抖动 ↔ AI 低成本倒推 等）
- 断链检查：0 条（含 raw 引用与 wiki 互链）

## [2026-11-04] compile | arXiv 综述建导航页 + 两处纠错

- 抓取：0 新增（26 份日报 + 1 份百科均已在库）
- 新建 `wiki/游戏设计/AI 在游戏生命周期的六个角色.md`（overview，confidence: medium）
  - 来源：`raw/2026-11-03_arxiv_2609.16679_...`（476 行全文，截断问题已修复）
  - 定位为导航页：把已编译的 5 篇 arXiv 文章挂到综述的六角色框架下
  - 页内标明「玩与行动」「构建与维护」两个角色不属于本库收录范围

### 本轮发现并修正的两处问题

1. **我自己造成的重复**：先写 `用玩家数据驱动设计迭代` 再跑体检，发现 `AI 当设计评审`（11-03 已建）已完整覆盖 PREFER + CoBG 两篇，含可行性卡与作者自承局限。已删除重复页，未改动原页。
   - 教训：必须先跑 `link_report.py` / 搜主题，再决定新建还是更新。

2. **Source Index 的一条旧判断有事实错误**：原注记称该综述为「四类角色」，实际是**六类**，其中四类落在本库收编范围内。原「主动不收」结论系基于截断版作出。已改为建导航页，并在 Source Index 保留修正说明。

### 反链审计
- 13 篇全部有链接，0 孤立
- 新综述页补 5 条入链：从 `AI 当设计评审`、`AI 铺关卡`、`AI 写任务线与世界设定`、`AI 调 NPC 行为`、`玩家怎么看 AI 生成内容` 各指回一次
- 补链后新页为 6 出 / 5 入，成为正常 hub

### 索引
- Concept Index 增 1 行（overview）
- Source Index：综述从「未编译」移入「已编译」，孤儿 arXiv 清零
- Dashboard：文章 7→13、原始资料 27→40

### 仍未处理
- 24 份行业日报未编译（按任务规则不批量处理）
- `2606.03857` 仅摘要（`full_text: unavailable`），已在 Source Index 标注

## [2026-11-04] compile | 24 份积压日报按主题合并编译 → 4 篇

- 抓取：0 新增（本次是处理积压）
- 新建 4 篇，覆盖 17 份日报：
  - `wiki/游戏新闻/版号供给与政策定位（2026）.md`（overview）← 10-14、10-30
  - `wiki/厂商团队/2026 年 10 月厂商结构变动.md`（overview）← 10-17、10-21、10-23、10-24
  - `wiki/品类市场/2026 年 10 月产品表现.md`（overview）← 10-09、10-10、10-13、10-15、10-16、10-18、10-20、10-22
  - `wiki/游戏新闻/2026 年 10-11 月赛事节点.md`（overview）← 10-19、10-25、11-01
- 厂商团队 / 品类市场两个领域首次有页

### 剩余 7 份日报未编译的说明

10-11 / 10-12 / 10-26 / 10-27 / 10-28 / 10-29 / 10-31 全是《影之刃零》发售前报道，事实已被 `影之刃零首周末峰值` 的「背景」「经过」覆盖。该页 sources 只列了 11-02/11-03 两篇，因为正文主要由那两篇写成。**未擅自给该页补 sources**（属修改已有页 frontmatter），在 Source Index 里写明了这一点。若需严格溯源，待确认后可补。

### 反链审计
- 17 篇全部有链接，0 孤立
- 新页入链：版号 3、产品表现 3、厂商变动 3、赛事节点 1
- 赛事节点补 1 条真相关入链（来自 `2026 年 10 月产品表现`：赛季运营与赛事节奏是相邻驱动线）
- 未连其余「同领域候选」：赛事与设计类文章无语义关系

### 索引
- Events Timeline 从 1 条补到 6 条，10 月的事件首次登记（政策 2、人事 2、爆款 2）
- Concept Index 补齐四个领域，删掉「暂无」占位
- Dashboard：文章 13→17、事件记录 1→6、被引用 16→33
- Source Index 新增「行业日报」分组，17 行；孤儿说明改为 7 份并附原因

## [2026-11-04] ingest | WorkBuddy 内容 ×2

- `raw/2026-11-04_游戏行业日报.md` — 日报，published 2026-11-04，4146 字符，hash a04124aaa2d2
- `raw/2026-11-04_游戏百科.md` — 百科词条，published 2026-11-04，2629 字符，hash 4ad13e094721
- 来源：WorkBuddy 自动生成，属二手汇总，引用以原始报道为准

## [2026-11-04] compile | 11-04 日报 + 百科 → 4 新页 + 1 处更新

- 抓取：日报 1 份（4146 字符）、百科 1 份（2629 字符）
- 新建 4 篇：
  - `wiki/游戏设计/A* 寻路算法.md`（concept，confidence: low）
  - `wiki/游戏设计/装备词条池.md`（pattern，confidence: low）
  - `wiki/游戏设计/法线贴图.md`（concept，confidence: low）
  - `wiki/厂商团队/国产买断 3A 的体系化供给.md`（pattern，confidence: low）
- 更新 1 篇：`2026 年 10-11 月赛事节点` 补 11-04 iG 3:1 TES 晋级四强，sources 增加 11-04 日报

### 判断说明
- 日报 6 条要闻里只编译了 1 条（索尼中国之星 + 影之刃零登顶周收入榜），因为其余 5 条是零散数据点（DLSS 5 接入、11 月新游档期、无主之地 1 亿份、上古世纪抢先体验），单独建页会碎片化，已在 Dashboard 研究缺口里留了「档期与差异化」「职业模拟流量入口」两条
- 赛事页更新属「已有页承接新事实」，改动为表格外加一段，未改原有判断

### 反链审计
- 21 篇全部有链接，0 孤立
- 补 6 条真相关反链：厂商变动→国产买断、成本倒推→国产买断、抖动技法→法线贴图、AI 调 NPC→A*、ECS→A*、魂系→装备词条池
- 装备词条池入链 1（来自魂系），其余新页入链 ≥2

### 索引
- Events Timeline 增 1 条（11-04 索尼中国之星 + 影之刃零登顶周收入榜）
- Concept Index 增 4 行
- Source Index 增 2 行（11-04 日报、11-04 百科）
- Dashboard：文章 17→21、原始资料 40→42、事件记录 6→7、被引用 33→35

## [2026-11-05] ingest | WorkBuddy 内容 ×2

- `raw/2026-11-05_游戏行业日报.md` — 日报，published 2026-11-05，4747 字符，hash 65c256227464
- `raw/2026-11-05_游戏百科.md` — 百科词条，published 2026-11-05，2318 字符，hash 374400d44097
- 来源：WorkBuddy 自动生成，属二手汇总，引用以原始报道为准

## [2026-11-05] compile | 11-05 百科 3 词条建页 + 赛事补录

- 抓取：日报 1 份（4747 字符）、百科 1 份（2318 字符）
- 新建 3 篇（全部来自百科）：
  - `wiki/游戏设计/旷野之息的化学引擎.md`（pattern，confidence: low）
  - `wiki/游戏设计/有限状态机.md`（concept，confidence: low）
  - `wiki/游戏设计/低多边形.md`（concept，confidence: low）
- 更新 1 篇：`2026 年 10-11 月赛事节点` 补 11-05 GEN 3:0 LYON、LCS 全军覆没、半决赛对阵

### 暂缓的一处更新（等确认）

11-05 日报第 6 条「小游戏平台围剿 AI 复刻流水线」直接冲击 `AI 逆向与可防守位置` 的现有结论：
- 微信小游戏累计处置违规线索超 5 万次
- 抖音阶梯处罚，第四次永久封禁主体
- 原页写的是「Valve 不充当工具监管者，只建议提高作品复杂度」

这是对原判断的实质性补充（多了「平台规则」这条防守线），按 AGENTS.md 第六条需结构化 Diff 确认后再改。本轮未动该页，Diff 见交付报告。

### 跳过的日报内容
- S16 之外的电竞内容：无
- 影之刃零 400 万份：已有页覆盖，仅好评率 90%→91%、峰值 83.3 万两个数字微调，未改原页
- 塞尔达时之笛重制登陆 Switch 2：单点发布信息，无长期判断价值
- A 股三季报（世纪华通/恺英/巨人/完美）：属财报汇总，与已有 `2026 年 10 月厂商结构变动` 主题相邻但不构成新判断，暂不建页

### 反链审计
- 24 篇全部有链接，入链 ≤1 的为 0
- 补 4 条反链：法线贴图→低多边形、抖动技法→低多边形、AI 调 NPC→有限状态机、A*→有限状态机

### 索引
- Events Timeline 未变（本轮无新 event 页）
- Concept Index 增 3 行
- Source Index 增 2 行（11-05 日报、11-05 百科）
- Dashboard：文章 21→24、原始资料 42→44、被引用 35→37
