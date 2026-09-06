# Deep Thinking

[English](README.md)

用于 Codex、Claude Code、原生 Kimi Code 和 zCode 的人机共同思考 Skill。
基础版本为 **0.1.0**，本机安装构建见 [交付记录](RESULT.md)。它将 Clear My Mind 与 Deep Research 放在同一条
可往返的路径中：先对齐需要的 Beta，再寻找值得研究的 Alpha，最终形成有依据、
可修订、能够使用的成果。

## 怎样使用

在宿主中调用主 Skill，给出正在面对的真实问题和已有材料即可。已说明过的背景、
目标和取舍会继续使用，不需要重新完成一套访谈。

主流程为 **定题 → 澄清 ↔ 研究 → 综合 → 检查 → 交付**。每步有产物与转出条件；
已有材料可以满足步骤，新证据可以使问题回退。你可以随时说“先理清这个概念”、
“研究这个假设”、“开一轮圆桌”、“找独立 Agent 审查”、“只用当前 Agent”、
“收束成决策备忘录”、“暂停”或“结束”，不需要学习额外命令语言。

你掌握原意、价值取舍、自己的理解以及是否停止。AI 独立判断证据和推论，主动说明
何时已经足以交付；不能把自己的交付写成你已经接受，也不能把你说停当成目标达成。

## 每次业务会留下什么

默认在已有议题目录中维护两份文件；新议题默认位于工作区的 `thinking/<议题>/`，
开始时会说明实际路径。业务材料不会写入可复用的 Skill 包。

| 文件 | 作用 |
| --- | --- |
| `THOUGHTS.md` | 当前步骤与状态、问题骨架、因子与证据、判断变化、替代解释、分歧及未决项 |
| `RESULT.md` | 可以独立阅读的研究报告、决策备忘录、论证稿或方案，包含关键引用、条件、限制和必要下一步 |

每个阶段更新底稿并说明变化，不要求每阶段、每个 Agent 各写一份报告。
提前结束时，成果会明确标注已知与未完成部分；要求不再整理或不留文件时遵从。

## 按 Ultra 系列规格安装

采用一个原生插件包、一个主 Skill：二者名称均为 `deep-thinking`。
不要再添加同名用户 Skill 或转发命令，以免出现重复入口、旧版本遮蔽。
以下 `<仓库绝对路径>` 指这个项目所在目录。

| CLI | 原生安装方式 | 调用入口 |
| --- | --- | --- |
| Codex | `codex plugin marketplace add <仓库绝对路径>`，再运行 `codex plugin add deep-thinking@rocky-deep-thinking` | 新会话中使用 `$deep-thinking` |
| Claude Code | `claude plugin marketplace add <仓库绝对路径>`，再运行 `claude plugin install deep-thinking@rocky-deep-thinking` | `/deep-thinking:deep-thinking` |
| 原生 Kimi Code | 在 TUI 中使用 `/plugins install <仓库绝对路径>/plugins/deep-thinking`，然后 `/reload` | `/skill:deep-thinking` |
| zCode | 打开侧栏“插件市场”→“添加插件市场”，添加本仓库目录，在“个人”中找到 Deep Thinking 并安装 | 原生 `/skill` 选择器或 `/skill deep-thinking` |

Shell 里的路径参数含空格时需加引号。Kimi Code 0.41.0 的 TUI 安装命令是例外：
直接粘贴完整路径，不加引号；原生解析器会把引号当作路径字符。它的插件命令位于 TUI，
不能照搬为外部 `kimi plugin` 子命令。zCode 的 CLI 不一定在 PATH 中。
四种 manifest 共同引用包内同一份 `skills/deep-thinking`，不会维护四份分叉内容。

改动源文件之后，需要通过宿主原生插件管理刷新并重新安装，再在新会话使用。
源码正确、插件列表出现、实际调用成功是不同层次的证据。
本机当前安装版本、验证结果和局限见 [交付记录](RESULT.md)。

## 论文和方法融入在哪里

| 位置 | 实际用途 |
| --- | --- |
| [SKILL.md](plugins/deep-thinking/skills/deep-thinking/SKILL.md) | 规定主流程、状态、结束权、两份业务产物、Beta/Alpha 与方法选择 |
| [methods.md](plugins/deep-thinking/skills/deep-thinking/references/methods.md) | 引导发现、发散与收敛、信息价值、针对具体问题的智识标准检查 |
| [research.md](plugins/deep-thinking/skills/deep-thinking/references/research.md) | 问题结构关联证据、关键因子与反证、资料适用性、研究推动问题和结论修订 |
| [roundtable.md](plugins/deep-thinking/skills/deep-thinking/references/roundtable.md) | 独立初判、聚焦分歧、交叉质询、成熟方案的对抗审查、基于理由修订判断 |
| [hosts.md](plugins/deep-thinking/skills/deep-thinking/references/hosts.md) | 原生入口、可用工具、跨 Agent 委派边界与读取底稿接续 |
| [assets](plugins/deep-thinking/skills/deep-thinking/assets/) | 过程底稿和最终成果的实际模板 |

来源及其适用限制与方法放在一起，进入相关任务时才读取。借鉴论文中的做法，
不意味着论文已经证明这个 Skill 有效。个人体验、事实正确性、认知吸收和跨问题
效果分别记录；多模型共识、少数新观点或权威来源都不能单独证明正确。

## 边界与检查

包内只有指令、参考与模板，没有后台常驻程序、Stop hooks、固定辩论轮数或
强制服务依赖。研究和委派使用宿主当前可用且已获授权的能力；不可用时如实说明。
读取文件接续也不等于四个宿主都具备自动压缩恢复。

运行 `python3 tests/check_package.py` 检查包结构、版本、入口与本地引用。
实际原生加载和业务流程观察另行记录。[THOUGHTS.md](THOUGHTS.md) 保存本次共创过程，
不随插件安装。
