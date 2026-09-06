# Deep Thinking：完整实现与四 CLI 交付记录

初次实现验证日期：2026-09-06。下列运行观察记录当时的环境，不是后续发行版本的重新测试或安装版本要求。当前公开包不锁定宿主、模型、提供方或可选工具版本；插件自身的发布版本以四份 manifest 为准。

本轮已把用户接受的运行方案落实为一个可安装、可调用的原生插件：一个 `deep-thinking` 主 Skill，覆盖 Clear My Mind 与 Deep Research，包含业务顺序、状态、文件、收敛、结束权，以及研究、圆桌和对抗审查的选择方式。Codex、Claude Code、原生 Kimi Code 和 zCode 已安装并实际调用。

此前调研的方法与论文已进入相应动作和判断规则。主说明负责贯穿全程的合同，references 负责按需展开的方法、来源与适用限制，assets 提供实际产物模板。下方记录已观察到的运行结果和偏差；本轮没有证明稳定认知效果，也没有替用户记录最终验收。

## 1. 实现放在哪里

规范源码位于本仓库的 `plugins/deep-thinking/`，四端使用同一份内容。

```text
plugins/deep-thinking/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── .zcode-plugin/plugin.json
├── kimi.plugin.json
└── skills/deep-thinking/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── methods.md
    │   ├── research.md
    │   ├── roundtable.md
    │   └── hosts.md
    └── assets/
        ├── thoughts-template.md
        └── result-template.md
```

| 位置 | 具体责任 |
| --- | --- |
| [SKILL.md](plugins/deep-thinking/skills/deep-thinking/SKILL.md) | 入口与接续、六阶段及转换、两份业务文件、六种状态、用户与助手的不同判断权、主动收敛、Alpha/Beta、方法选择和中立对话 |
| [methods.md](plugins/deep-thinking/skills/deep-thinking/references/methods.md) | 针对当前卡点选择提问、综合、发散收敛、信息价值和智识标准；把体验、吸收和判断质量分开观察 |
| [research.md](plugins/deep-thinking/skills/deep-thinking/references/research.md) | 从问题骨架研究自身与环境、关键因子、证据及反证，核对来源与迁移前提，允许研究修订问题及候选方案 |
| [roundtable.md](plugins/deep-thinking/skills/deep-thinking/references/roundtable.md) | 独立初判、找出真正分歧、聚焦质询、基于证据修订；成熟候选可直接进入独立对抗审查 |
| [hosts.md](plugins/deep-thinking/skills/deep-thinking/references/hosts.md) | 四端原生入口、按加载位置读取引用、使用当前可用委派工具、观察超时、会话接续与实际取消边界 |
| [thoughts-template.md](plugins/deep-thinking/skills/deep-thinking/assets/thoughts-template.md) | 思考底稿的当前状态、问题结构、因子与证据、判断变化、未决及搁置分支 |
| [result-template.md](plugins/deep-thinking/skills/deep-thinking/assets/result-template.md) | 独立成果的回答、理由、来源、替代、限制与必要下一步；可以形成报告、备忘录、文章或方案 |

包内共12份文件。仓库外层另有两个原生市场目录、双语 README、结构检查以及本次共创的 `THOUGHTS.md` 和 `RESULT.md`。此前“整个目录最终六份文件”的估计已被用户明确要求的四端原生包装取代；**每个普通业务议题仍默认只维护两份业务文件**。

采用 Ultra 系列的一个原生插件、一个主 Skill 方式，没有另复制用户技能目录、同名别名或转发入口。四份 manifest 指向同一个 `skills/`；Clarify、Research、Roundtable 是主 Skill 内的方法，不拆成四端各自维护的内容。

## 2. 方法和论文怎样转成实际动作

| 方法或原始研究 | 进入哪里、产生什么动作 | 保留的限制 |
| --- | --- | --- |
| [Padesky：Guided Discovery](https://padesky.com/wp-content/uploads/2012/11/socquest.pdf)，第4–6页 | `methods.md`：问用户能够回答的具体问题，听取意外信息，综合已有回答，再联系原问题；事实缺口交给调查 | 借用引导发现，不把用户当患者，不预设必须改变观点 |
| [Design Council：Double Diamond](https://www.designcouncil.org.uk/resources/framework-for-innovation/) | `methods.md` 与主流程：区分问题探索和方案探索，显示何处已够用、何处还需展开，允许试验后重新定题 | 不把四阶段或会议轮数当作事实正确性的证明 |
| [Runge 等：Value of Information](https://www.usgs.gov/publications/a-simplified-method-value-information-using-constructed-scales) | `methods.md` 与主说明：比较“有多不确定”和“了解后会改变什么”，帮助避免在无益分支持续深挖 | 仅作定性启发，不冒称已计算正式信息价值；保留探索本身的价值 |
| [Paul–Elder：Universal Intellectual Standards](https://www.criticalthinking.org/pages/universal-intellectual-standards/527) | `methods.md`：针对具体主张检查清晰、精确、准确、相关、逻辑、深度、广度与公平性；返回缺失前提或可验证问题 | 按当前困难选用，不逐轮背检查表或给用户智力打分 |
| [Co-STORM](https://arxiv.org/html/2408.15232v2)，第3.1–3.5、6节 | `research.md`：将问题、因子、来源和结论影响连接成可修订的图或表；从已检索但未使用的材料发现遗漏；据此综合带来源的结果 | 借用信息组织和发现动作，不复制自动轮流发言来替用户决定；20人体验评估不证明长期思辨提升 |
| [The Socratic Challenger](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1913451/full)，Methods 与 Discussion | `research.md`：文献核验→挑战知识缺口、机制与可行性→修订→复查；区分助手核验、用户核验和真实专家反馈 | 原研究是45名学生的评分与反思，不强制八步或指定服务，不把模型意见充当真人专家反馈 |
| [Du 等：Multiagent Debate](https://arxiv.org/html/2305.14325v1#S5) | `roundtable.md`：先形成实质不同的初判，再针对关键前提交叉检查，整合真正新增的证据和区别 | 原实验也出现自信的错误共识；不使用固定三人、三轮或多数决定正确性 |
| [Smit 等，v3](https://arxiv.org/html/2311.17371v3) | `roundtable.md`：选择是否辩论以及是否继续；允许保持正确初判，避免为了角色而强行反对 | 协议和参数影响结果；不把旧模型的基准表现当作当前业务收益 |
| [Sharma 等：Sycophancy](https://arxiv.org/html/2310.13548v4)，第3–4节 | 主说明与 `roundtable.md`：对用户、助手、参与者使用同样的证据标准；按证据、语境纠正或推理错误修订，并解释原因 | 不因压力改口，也不为了表演独立而固执；该规则没有被证明能消除谄媚 |
| [AI 写作计划认知干预研究](https://arxiv.org/html/2601.18033v1)，第5.2、5.4、7节 | `methods.md`：分别观察体验、实际使用一个认识、判断质量与迁移；保留正向反馈的真实范围 | 用户改口或说“很好”不单独证明有效；不假定叠加干预一定更好 |

这些规则接在实际流程中，进入对应任务才读取细则与来源。正文保留不可丢失的行为，references 承载需要时才展开的内容；模板承担写出产物的任务。

此前查过的 grill-me、grill-with-docs、Ponder、Elicit 等公开说明，仍作为已有做法和比较基线保存在 [共创底稿](THOUGHTS.md)。复用其有用思想，不据此增加未获要求的服务依赖或宣称本 Skill 比它们更优。

## 3. 一次真实业务怎样运行与结束

默认主线为：**定题 → 澄清 ↔ 研究 → 综合 → 检查 → 交付**。

先读取当前问题、已有材料和议题底稿，明确用途与够用条件。澄清发展问题骨架、个人含义、自身及环境；研究调查会影响判断的事实与因子。证据可以改变问题，因此两者可往返。随后形成带前提的候选结论，检查关键推论和遗漏，达到当前用途就主动交付。

普通共思是主线。独立的事实分支可以分工调查；有不同知识、利益或解释值得比较时组织圆桌；成熟候选的关键前提需要检验时直接请独立审阅者。跨宿主只是承载方式，使用宿主当前提供的能力；不同宿主可能使用同一个模型，不能冒称独立证据。

默认业务目录是 `<workspace>/thinking/<topic>/`，已有对应目录和底稿时复用：

- `THOUGHTS.md` 在进入持续议题时创建，重要变化后更新；顶部显示当前步骤、状态、关键缺口及下一步理由。
- `RESULT.md` 在交付或用户结束时创建，脱离对话也能读懂；提前结束则明确写成阶段成果。

状态区分 `active`、`waiting_user`、`waiting_evidence`、`delivered`、`paused`、`ended`。助手判断是否具备继续研究或交付的依据；用户决定自己的含义、价值、理解、满意与是否停止。没有需要用户决定的问题时不强行续问，沉默也不写成接受。用户明确结束时，成果可以已经交付，议题状态应记为 `ended`。

用户可以直接说“研究这个前提”“开一轮圆桌”“找独立 Agent 审查”“只用当前 Agent”“收束成备忘录”“暂停”“结束”。暂停或结束后停止继续调查和派工，已启动工作按实际工具反馈处理；文件接续不等于宿主自动恢复或后台常驻。

你之前确认的目标已经保留：个人 Alpha 经真实吸收可以 Beta 化，外部 Alpha/Beta 的参照系另行判断；新颖不保证正确。“95%”指对当前相关因子和信息的接近完整掌握，不是95%的赢面，也不虚构覆盖率。“Always thinking like 1%”作为探索志向，不记成已测得的排名。

## 4. 四端安装与入口

以下是初次验证时使用的宿主版本，仅用于说明历史观察的适用环境，不是安装约束，也不代表最新版本。公开包按原生插件和 Skill 能力适配，不要求使用这些具体版本。

| 宿主 | 历史验证版本 | 原生调用 | 当时的安装方式与结果 |
| --- | --- | --- | --- |
| Codex | 0.153.4 | `$deep-thinking` | 原生 CLI 注册本地 `rocky-deep-thinking` 市场并安装；真实新进程读取安装目录的 Skill |
| Claude Code | 2.1.261 | `/deep-thinking:deep-thinking` | 原生市场添加、安装及更新成功；新进程报告修正版，展开的 Skill 正文含最新规则 |
| 原生 Kimi Code | 0.41.0 | `/skill:deep-thinking` | TUI `/plugins install` 本地路径成功；更新后新进程通过原生 Skill 工具加载 |
| zCode | 0.16.5 | `/skill deep-thinking` 或原生选择器 | 桌面插件市场添加本地仓库、安装及重装成功；原生 CLI 显示启用、一个 Skill，实际调用产出文件 |

初次验证从宿主实际报告的安装位置比较了四端各12份文件，与当时的规范源码逐字节一致。安装目录由各宿主管理；不要将验证机器的缓存位置作为其他人的安装路径。

可复用安装步骤见 [中文 README](README.zh-CN.md) 和 [English README](README.md)。公开仓库中的修改不会自动更新已安装的插件；通过各宿主原生管理刷新后，在新会话调用。

测试时还遇到两项兼容差异：Kimi TUI 把安装路径中的引号当成路径字符，直接粘贴不带引号的完整路径后成功；zCode 的 CLI 帮助列出了 `--max-turns`，实际解析却拒绝它，移除该参数后调用正常。这些仅是当时的观察，不外推到其他版本。

## 5. 实际验证与未通过的观察

**包与规格检查。** Skill 校验、Codex 插件校验、Claude 原生 manifest 校验均通过。仓库的 [check_package.py](tests/check_package.py) 使用标准库检查四端版本、唯一主 Skill、两个市场目录、模板、包内可移植性及21个本地引用。另一个新上下文 Agent 只读检查七份正文/引用/模板，未发现确定的内部冲突；它没有据此保证模型运行可靠性。

**四端加载与收束。** 两批独立 CLI 进程使用同一受控场景：只有两条匿名演示反馈，没有付费承诺、预算或交付成本数据，检验“应立即开发完整企业版”；只用当前 Agent，不联网、不委派，要求生成阶段成果并结束，不补造用户接受。

每端均以自己的原生命令触发，没有在启动提示里直接提供 Skill 文件绝对路径。两批共8次实际模型调用正常退出，各自生成 `THOUGHTS.md` 与 `RESULT.md`，没有追加用户问题或继续调查，也未宣称商业可行性已验证。zCode 的此种 CLI 输出没有完整工具事件流，其加载依据是原生发现记录、安装内容、产物中的实际读取记录和输出；不把它描述成与其他宿主同等完整的工具轨迹。

**输出质量没有记为全通过。** 首批观察到“匿名所以无法回访”、未经支持的成本排序，以及把明确结束记录为 `delivered` 等问题。主说明因此补充了给定材料的证据身份、缺证据不等于为假或无法获取、不得补造动机/来源/成本排序，以及明确结束的状态优先级；随后通过原生管理更新四端并复查同一场景。

| 修正版复查 | 实际观察 |
| --- | --- |
| Codex | 给定材料、推断与未知分开；保留商业可行性未知；状态 `ended`；未发现首批所述成本推断问题 |
| Kimi | 未再补出样本自选或成本排序；状态 `ended`；一处“无预算”的压缩措辞仍不如“无预算数据”精确，文中其他位置保留了未知边界 |
| zCode | 状态 `ended`，未再断言完整企业版成本最高；样本选择偏差作为“可能”解释出现；部分英文模板标题未翻译 |
| Claude Code | 已确认加载了新增规则，但仍写出“成本极低”“最便宜”等缺少本案依据的判断；状态仍记为 `delivered`，同时实际停止本轮且未补造接受。该项没有算作语义一致性通过 |

这些是有限模型输出的直接观察。它们说明 Skill 已可加载并完成产物路径，同时说明提示规则仍不能保证每次推理精度和状态标注。没有用重复采样挑出一次好结果后宣布问题消失，也没有增加一个代替模型语义判断的硬编码引擎。

**研究到交付的独立试用。** 另一个新上下文 Agent 只拿主 Skill 和虚构业务任务：八人产品团队希望试用“所有争议决策由三个 Agent 辩论三轮、按多数执行”。它实际读取所需引用和模板，核对 Du、Smit 等原始论文，比较适用性，完成条件性两周方案、一页决策卡格式、观察指标与未决前提，同时产出两份业务文件。

该 Agent 执行的是资料研究、综合与自查。它没有调用其他 Agent、接触团队或实施两周试用；结论不代表真实多 Agent 相对效果或团队收益。本次共创中的实际独立审阅也不能替代这些未做的业务观察。

原始运行日志和受控案例产物保存在验证机器上，未随公开仓库发布。上文是观察摘要，不提供外部读者无法访问的本机临时路径；可按已描述的场景自行复测。

## 6. 交付边界

完整运行说明、研究方法、对抗审查、模板、四端原生包装与本地安装已经交付。用户可以在任一宿主提供真实问题，从现有上下文继续，按需要展开研究或收束为结果。

尚未证明的是：跨问题稳定判断质量、长期个人吸收和迁移、减少谄媚或幻觉的效果，以及相对普通对话或其他方法的优势。跨宿主桥的真实多 Agent 圆桌、停止时取消正在运行的外部进程、原生压缩恢复也没有在本轮穷尽测试；文件恢复说明不提供自动恢复能力。上文列出的 Claude 输出偏差仍是已观察到的限制。

没有新增后台循环、hooks、MCP 服务或强制运行依赖，也未执行任何真实业务决策。初次实现交付后，已按用户要求建立并推送 [公开仓库](https://github.com/rocky2431/deepthink-skill)。公开包去除了本机缓存构建时间戳、重复的目录版本字段和不可移植的路径说明，保留插件自身的发布版本与注明日期的验证环境。后续迭代应由具体使用反馈或可复现失败驱动。
