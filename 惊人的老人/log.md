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
