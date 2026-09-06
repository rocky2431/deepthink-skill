# Deep Thinking

[English](README.md) · [简体中文](README.zh-CN.md)

Deep Thinking 帮助你与 AI Agent 一起理清想法、研究问题、做出判断。它从问题本身出发，查证依据、比较可能的答案，最后写成可以使用的研究报告、决策备忘录、论证稿或方案。

它以原生插件的形式运行在 Codex、Claude Code、Kimi Code 或 zCode 中。Clear My Mind 用于澄清原意、概念和假设，Deep Research 用于调查外部证据和不同解释。两者交替推进：研究发现可以改变问题，问题变得清楚后，也可能需要调整研究方向。

适合需要持续讨论和调查的议题，例如评估产品方向、检查一个深信不疑的观点。普通事实查询可以直接交给 Agent。

版本：0.1.1。插件包含 Skill、参考文档和模板，模型与工具由宿主提供。

- [安装与开始使用](#安装与开始使用)
- [第一个议题](#第一个议题)
- [议题如何推进](#议题如何推进)
- [文件与进度](#文件与进度)
- [当前限制](#当前限制)
- [文档](#文档)
- [开发](#开发)

## 安装与开始使用

你需要一个能加载原生插件和 Skill 的宿主。Deep Thinking 沿用你的模型与提供方配置，不锁定宿主、模型、提供方或可选工具的版本。插件清单中的版本号用于识别本插件的发布版本。

克隆仓库，再通过宿主的插件管理器安装本地副本：

```sh
git clone https://github.com/rocky2431/deepthink-skill.git
```

进入仓库，将路径用于下面的安装命令：

```sh
cd deepthink-skill
DEEP_THINKING_REPO="$(pwd)"
```

### Codex

```sh
codex plugin marketplace add "$DEEP_THINKING_REPO"
codex plugin add deep-thinking@rocky-deep-thinking
codex plugin list --json
```

Codex 读取 `.agents/plugins/marketplace.json` 和包内的 `.codex-plugin/plugin.json`。

### Claude Code

```sh
claude plugin validate "$DEEP_THINKING_REPO/plugins/deep-thinking" --json
claude plugin marketplace add "$DEEP_THINKING_REPO"
claude plugin install deep-thinking@rocky-deep-thinking
claude plugin list --json
```

Claude Code 使用 `.claude-plugin/marketplace.json`，通过原生插件布局发现包内的 `skills/` 目录。

### Kimi Code

在原生 Kimi Code 的 TUI 中运行 `/plugins install`，传入 `<仓库绝对路径>/plugins/deep-thinking`，然后执行 `/reload`。插件使用 `kimi.plugin.json`，安装位置由 Kimi 管理。

这些是 TUI 命令。如果 Kimi 把引号当成路径字符，直接粘贴不带引号的完整路径，即使路径中含有空格。

### zCode

通过 zCode 的原生插件市场添加本地仓库目录，找到 Deep Thinking 并安装。市场使用 `.claude-plugin/marketplace.json`，包内提供 `.zcode-plugin/plugin.json`。

原生 CLI 的 `plugins list --json` 和 `skills list --json` 可以检查发现结果。CLI 的实际路径取决于安装位置，不一定在 `PATH` 中。

### 插件原生入口

安装后重新加载插件或开启新会话，通过宿主的原生入口调用主 Skill：

| 宿主 | 主 Skill 入口 |
| --- | --- |
| Codex | `$deep-thinking` |
| Claude Code | `/deep-thinking:deep-thinking` |
| Kimi Code | `/skill:deep-thinking` |
| zCode | `/skill deep-thinking`，或在 Skill 选择器中选择 |

插件及其唯一的主 Skill 都叫 `deep-thinking`，四种宿主加载同一份 Skill 内容。每个宿主安装一份即可，避免重复入口或旧的用户 Skill 优先加载。

安装语法和界面名称可能随版本变化，存在差异时以已安装宿主的帮助为准。市场目录引用仓库内的插件路径，不固定发布标签或提交。更新仓库后，通过原生插件管理器刷新并重新安装，再开启新会话；只改源码不会更新已安装的插件缓存。

## 第一个议题

在准备保存议题的工作区中打开 Agent，调用 Deep Thinking，说明问题、已有材料和需要的成果。例如：

> 使用 Deep Thinking，评估这个产品方向是否值得继续投入。先读取项目笔记中的需求和约束，调查可能改变决定的假设，最后写成决策备忘录，保留替代方案和未决问题。

Agent 会先读取已有背景，确定这次需要回答什么。遇到会影响后续工作的个人理解或选择时，一次问一个明确的问题；事实缺口由它使用可用工具调查。已经提供的背景会继续使用。

你决定价值取舍和是否继续。Agent 提出想法和独立判断，说明理由，并在证据或背景修正后调整结论。

## 议题如何推进

默认流程为 **定题 → 澄清 ↔ 研究 → 综合 → 检查 → 交付**。

1. 明确问题、目的、范围和成果形式，确定结果做到什么程度才足以使用。
2. 澄清概念、目标、约束和假设，找出已经知道的内容与可能改变方向的缺口。
3. 调查这些缺口，查阅来源、反证和不同解释，把发现与原问题联系起来。
4. 综合候选答案，比较替代方案，说明每个判断依赖的前提。
5. 对照原始需求检查答案，审查关键推论和遗漏，修正结论或补充适用条件。
6. 交付可以独立阅读的文档，说明答案、依据、条件和剩余限制。

已有材料可以满足某个阶段，新证据也可以让工作回到澄清或研究。流程不规定问答次数或讨论轮数。某个分支开始重复，或需要另一类证据时，Agent 会记录尚未解决的内容及重新展开的理由。

默认使用普通讨论。若研究分支彼此独立，且已有授权，可以交给其他 Agent 调查。不同专长或假设可能改变答案时，使用圆桌比较观点；候选结论或方案已经成形时，可以直接做对抗审查，检查错误和遗漏，一位独立审阅者也可能足够。参与者来自宿主实际提供的能力。

Skill 区分个人学习与外部新颖性。对你而言新出现的洞见是个人 Alpha，理解并吸收后成为个人 Beta。它在某个领域是否少见、证据是否支持它，需要分别判断。熟悉的知识可以有用，新颖的想法也可能出错。

你可以用自然语言调整方向，例如“研究这个假设”“开一轮圆桌”“找独立 Agent 审查”“只用当前 Agent”或“收束成决策备忘录”。

## 文件与进度

持续议题沿用已有目录；新议题默认放在工作区的 `thinking/<议题>/` 下。Agent 会在开始时说明实际路径，议题材料保存在可复用的插件包之外。

| 文件 | 内容 |
| --- | --- |
| `THOUGHTS.md` | 过程底稿：当前阶段与状态、问题结构、证据、替代方案、判断、重要修订和未决分支 |
| `RESULT.md` | 最终产物：研究报告、决策备忘录、论证稿或方案，包含关键引用、条件、限制和必要的下一步 |

Agent 在议题开始时创建底稿，在交付或结束时写出成果。两份文件使用你选择的语言。阶段进展更新到底稿中，无需为每个阶段或参与者单独写报告。

进度说明包括发生了什么变化、还缺什么，以及下一步做什么。约定目的已有依据充分的答案时，Agent 主动交付。交付表示成果已经准备好，是否接受由你决定。

你可以随时说“暂停”或“结束”。提前结束会留下标明未完成部分的阶段成果，除非你要求不再写作。也可以选择只在对话中推进，不保存文件。接续已有议题时，让 Agent 读取对应的 `THOUGHTS.md`，从当前进展继续。

## 当前限制

研究和委派依赖宿主可用的工具与权限。插件不附带后台常驻程序、Hook、MCP 服务、提供方订阅或强制运行依赖。底稿可供接续时读取，但不提供上下文压缩后的自动恢复或后台续跑。

流程仍由模型执行，输出可能出现无依据的推断或错误的进度状态。多个 Agent 意见一致、来源有声望或文档已经写完，都不能单独证明结论正确。

参考文档说明了方法的研究来源及其适用限制。这些研究不等于对本 Skill 的效果验证。跨问题的稳定判断质量、长期学习效果、减少迎合的效果，以及相对普通对话的优势，目前都没有得到证明。

## 文档

- [Skill 指令](plugins/deep-thinking/skills/deep-thinking/SKILL.md)：工作流程、状态、停止规则、产物和方法选择。
- [澄清方法](plugins/deep-thinking/skills/deep-thinking/references/methods.md)：引导发现、探索与收敛、信息价值和推理检查。
- [研究流程](plugins/deep-thinking/skills/deep-thinking/references/research.md)：来源证据、不同解释，以及研究如何修订问题。
- [圆桌与审查](plugins/deep-thinking/skills/deep-thinking/references/roundtable.md)：独立初判、聚焦质询和候选答案审查。
- [宿主说明](plugins/deep-thinking/skills/deep-thinking/references/hosts.md)：原生入口、可用工具、委派和接续。
- [模板](plugins/deep-thinking/skills/deep-thinking/assets/)：过程底稿与独立成果。

## 开发

包检查使用 Python 标准库。在仓库根目录运行：

```sh
python3 tests/check_package.py
```

检查覆盖四份插件清单、版本一致性、唯一主 Skill 入口、市场目录、模板和本地链接。原生插件加载与实际议题的输出质量，需要在宿主中另行检查。
