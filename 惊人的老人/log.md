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
