# robotics-research-writing

[中文](README.md) · [English](README.en.md) · [真实文献蒸馏示例 / Distillation showcase](examples/literature-distillation-showcase.md)

从真实机器人论文与作者反馈中提炼**有出处、有适用条件、可以检验的写作规则**，再用于贡献定位、论证组织、段落修改与忠实中英转换。

这个 Codex skill 关注写作决策：如何让读者理解工程问题、结构如何产生所需作用、什么证据证明设计价值，以及每个实验在论证中承担什么职责。规则与来源、使用条件和反例一起保存，使后续修改有据可查。

**公开范围：工作流程、空白状态模板、可选下载脚本，以及一份用户授权公开的代表性蒸馏示例。其余已蒸馏语料、实际个人规则库、研究画像、作者材料和验证日志均保留私有。**

精选示例位于仓库的 `examples/`，不在安装子目录内。官方安装器只安装 `robotics-research-writing/` 中的框架和空模板；首次使用根据你实际提供的材料建立个人状态。

## 用途与工作方式

适合用来：

- 从论文中学习问题与缺口如何提出、贡献如何定位、设计与证据如何组织。
- 将阅读观察归纳为带出处、迁移条件与反例的个人规则。
- 根据作者已有方法、结果和图表，组织最强优势与最短充分证据链。
- 逐处检查防御性写作，改进表达并保留影响理解的科学条件。
- 忠实地进行中文到英文转换，保留事实、术语与主张强度。
- 根据真实反馈修订规则，记录什么发生了变化、为什么变化。

流程如下：

| 阶段 | 做什么 | 产出或检查 |
| --- | --- | --- |
| 材料 | 核实身份、版本与实际可读范围；PDF / Word 先转 Markdown | 来源记录、原件和转换稿 |
| 理解 | 梳理问题、方案、主要主张和关键证据 | 最小理解、反向提纲 |
| 观察 | 定位具体写法，区分原文事实与分析解释 | 页码 / 章节 / 段落 / 图表锚点 |
| 条件化规则 | 写清动作、适用条件、反例及已有规则关系 | 候选规则或范围修订 |
| 应用 | 根据作者事实组织中心主张，再写正文 | 修改稿、事实与证据核对 |
| 检验 | 检查事实忠实、结构、清晰度和任务适配 | 实际验证记录 |
| 修订 | 只更新受影响条目，保留来源和变更理由 | 可追溯的个人规则版本 |

单篇写法可以成为候选观察，不自动成为领域标准。研究缺口需要文献支持；写作模板不创造实验、引用、测量数值或创新证据。

### 三种模式

| 模式 | 典型请求 | 主要交付 |
| --- | --- | --- |
| A：从文献学习 | “学习这篇论文的写法”“批量蒸馏 3 篇” | 论文理解、反向提纲、来源观察、条件化规则、归档记录 |
| B：用于作者论文 | “重组结果部分”“检查防御性写作”“忠实翻译” | 正文或修改稿、必要说明、证据缺项 |
| C：更新与检验 | “把这次反馈纳入规则”“验证某条规则” | 受影响规则的修订、理由、实际检查记录 |

只要求下载时交付归档结果；只要求蒸馏时不自动改作者初稿。局部润色不重构全文。纯文本修改可以直接交稿，不必先建立完整资料库。

未指定期刊时，根据研究类型与读者组织文本；默认中文解释，英文写作交付英文正文。全文对照阅读、单纯转换或统计计算按任务选择相应工具。

## 真实文献蒸馏示例

[查看中英对照精选示例](examples/literature-distillation-showcase.md)：Ishida 等人的 *Exploration of fin stiffness for asymmetric thrust in a swimming robot*，RoboSoft 2024，[DOI](https://doi.org/10.1109/ROBOSOFT60065.2024.10522008)。

示例展示如何从一篇真实机构论文建立反向提纲、提取三条有适用条件的候选规则、核对指标与证据，以及构造明确标记的写作迁移模板。

这是一份经筛选、转述的原有蒸馏记录。原记录中的观察与为本次展示新构造的示例分开标记；候选规则未被称为独立验证结论。示例不包含 PDF、论文全文、原图、作者初稿或写作提升百分比，也不会自动回填到安装后的个人规则库。

## 安装

### 推荐：让 Codex 安装

在 Codex 中发送：

```text
请使用 skill-installer，从 Liuhy329/robotics-research-writing 仓库安装
robotics-research-writing 子目录里的 skill。
安装参数为 --repo Liuhy329/robotics-research-writing
和 --path robotics-research-writing。
如果本机已有同名 skill，请停止，不要覆盖我的个人版本。
```

仓库地址：[Liuhy329/robotics-research-writing](https://github.com/Liuhy329/robotics-research-writing)。应安装包含 `SKILL.md` 的子目录。安装完成后，在下一轮对话中显式调用 `$robotics-research-writing`。

使用系统提供的 `install-skill-from-github.py` 时，对应参数为：

```text
--repo Liuhy329/robotics-research-writing --path robotics-research-writing
```

安装器默认目标是 `$CODEX_HOME/skills/`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills/`。目标同名目录已存在时，安装器会停止。不要直接覆盖已有私人版本；先备份，再核对流程与资料存放差异。

### Windows PowerShell 手动安装

需要 Git。以下命令先检查目标和下载目录；遇到已有目录会停止。

```powershell
$skillRoot = if ([string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
    Join-Path $HOME '.codex\skills'
} else {
    Join-Path $env:CODEX_HOME 'skills'
}
$skillDir = Join-Path $skillRoot 'robotics-research-writing'
$repoDir = Join-Path (Get-Location) 'robotics-research-writing-public'
if (Test-Path -LiteralPath $skillDir) { throw "目标已存在，请先备份个人版本：$skillDir" }
if (Test-Path -LiteralPath $repoDir) { throw "下载目录已存在，请换一个空目录：$repoDir" }
git clone https://github.com/Liuhy329/robotics-research-writing.git $repoDir
if ($LASTEXITCODE -ne 0) { throw 'Git 下载失败，尚未复制 skill。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $repoDir 'robotics-research-writing') -Destination $skillDir -Recurse
```

### Linux / macOS 手动安装

需要 Git。目标存在时不复制；下载成功后只复制安装子目录。

```bash
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
skill_dir="$skill_root/robotics-research-writing"
repo_dir="$PWD/robotics-research-writing-public"
if [ -e "$skill_dir" ] || [ -e "$repo_dir" ]; then
  printf '%s\n' '目标 skill 或下载目录已存在，请先备份或换一个空目录。'
else
  git clone https://github.com/Liuhy329/robotics-research-writing.git "$repo_dir" &&
  mkdir -p "$skill_root" &&
  cp -R "$repo_dir/robotics-research-writing" "$skill_dir"
fi
```

## 五分钟开始使用

1. 打开你的研究项目工作区，准备一篇论文或一个待修改段落。
2. 指定模式、篇数或章节、希望交付什么，以及允许保存到哪个研究目录。
3. 显式调用 `$robotics-research-writing`；PDF / Word 先转换为 Markdown。
4. 核对实际阅读范围、证据锚点和生成文件位置，再选择是否应用规则。

第一次文献学习可以发送：

```text
$robotics-research-writing
请蒸馏我提供的这篇论文，重点学习“设计如何与实验论证连接”。
只做文献学习，不修改作者初稿。先转换 Markdown，再阅读并核对关键图表。
个人记录保存到当前研究项目的 .robotics-writing/。
没有作者材料时，迁移示例使用明确标记的结构占位符。
交付实际阅读范围、反向提纲、条件化候选规则和已保存文件的位置。
```

### 输入清单

提供实际掌握的材料即可，不需要首次填满画像：

| 输入 | 有助于确定什么 |
| --- | --- |
| PDF、Word、可访问 HTML、DOI 或已提供正文 | 实际可以阅读和核实的来源 |
| 研究方向、研究类型、目标读者 / 期刊 | 哪些观察与规则适用 |
| 单篇或明确批量篇数、筛选方向 | 本次任务范围与停止位置 |
| 作者初稿、方法、结果、图表、引用 | 可用于修改的真实事实与证据 |
| 修改幅度、语言、术语表、保留要求 | 正文交付形式与修改边界 |
| 研究工作目录、已有文献管理方式 | 个人记录和文件的保存位置 |

缺少某项时，说明它影响哪一步并继续可完成的工作。只有摘要时记录摘要范围；全文蒸馏不能从题名或摘要推断完成。

### 预期输出

| 任务 | 你应看到的交付 |
| --- | --- |
| 文献学习 | 身份与阅读范围、最小理解、反向提纲、带锚点观察、候选规则及其关系 |
| 作者写作 | 可直接阅读的正文 / 修改稿，正文之外的调整说明和未解决缺项 |
| 防御性检查 | 原文、问题类型、必留信息、改法、科学含义是否变化 |
| 规则更新 | 实际修订条目、来源、理由、覆盖变化与已完成验证 |

保存型任务同时报告生成路径和实际完成状态。无文件写入能力时交付可保存内容，并说明尚未写入。

## 个人资料与状态

公开安装目录中的 `references/` 始终保留空模板与方法说明。实际知识按需保存到**你的研究项目工作区**中的 `.robotics-writing/`：

```text
你的研究项目/
└── .robotics-writing/
    ├── profile-state.md     # 研究需求、覆盖范围和当前状态
    ├── writing-rules.md     # 实际个人规则、来源与适用条件
    ├── source-index.md      # 实际文献索引、版本关系与材料路径
    ├── validation.md        # 实际检查、验证和修订记录
    ├── distillations/       # 单篇学习记录
    ├── literature/          # 原始文献，或关联已有资料库
    └── processed/           # Markdown 转换与清理材料
```

所需状态文件按需从模板建立，不要求一次创建全部目录。已有文献资料库可以继续使用，登记关联路径即可，不自动移动原件或重编来源编号。

文件按核实后的正式标题命名，非法字符作兼容处理；版本或附件加必要后缀。重名时先比较哈希和版本，避免覆盖。分类沿用你的目录；没有分类时先按标题存放，细分信息用标签表达。

本仓库已忽略 `.robotics-writing/`。在另一个 Git 项目中使用时，应在**那个项目**的 `.gitignore` 中加入：

```gitignore
.robotics-writing/
```

原始论文若保存在该目录之外，也需要在对应项目中单独管理其分享范围。`.gitignore` 不会停止跟踪已经提交过的文件。

### 来源记录字段

完整字段见 [source-index.md](robotics-research-writing/references/source-index.md)。主要内容包括：

| 字段组 | 内容 |
| --- | --- |
| 身份 | 稳定编号、正式题名、作者、年份、期刊、DOI / 稳定来源页；未核实字段明示 |
| 版本与角色 | 正式版 / 预印本 / 修订稿；主文 / 正文加补充 / 独立附件；关联版本 |
| 文件 | 原件与 Markdown 路径、页数、字节数、SHA-256 |
| 获取 | 检索条件、查看范围、入选理由、时间、正常访问路线 |
| 阅读 | 实际章节、页码、图表范围、转换缺项与全文 / 摘要 / 节选限制 |
| 蒸馏 | 单篇记录位置、规则支持 / 修订、反例 / 冲突或无增量理由 |

临时签名下载地址、Cookie、账号令牌和凭据不进入来源索引。

### 条件化规则字段

完整字段见 [writing-rules.md](robotics-research-writing/references/writing-rules.md)。一条可用规则需要：

| 字段 | 记录要求 |
| --- | --- |
| 稳定编号、名称与状态 | 清楚说明改变什么决策；状态依据实际证据填写 |
| 动作 | 什么条件下采取什么写法 |
| 适用 / 不适用条件 | 研究类型、读者、章节职责、证据需求和反例 |
| 可观察事实 | 来源编号、锚点、短引文或忠实转述 |
| 解释与依据 | 写法承担的论证作用，与原文事实分开 |
| 证据范围 | 实际阅读范围、研究独立性、支持与反例 |
| 应用示范 | 已授权作者事实，或明确标记的占位符 / 构造示例 |
| 检验与变更 | 验证记录、实际结果、日期、原状态、变更与理由 |

候选规则与已有规则比较为新增、支持、范围修订、反例、冲突、重复或不吸收。没有增量时登记已读或增加例证，不堆叠同义条目。规则编号不进入论文正文。

## 六组可直接复制的提示词

### 1. 单篇文献蒸馏

```text
$robotics-research-writing
请学习我提供的这篇机器人论文，只蒸馏写作方法，不修改我的初稿。
PDF / Word 先转 Markdown，保留原件及页码、章节、段落、图表锚点。
说明实际读到的范围，再做问题—主张—证据梳理和反向提纲。
提取有增量的观察，写清来源、作用、迁移条件与反例。
保存到当前研究项目的 .robotics-writing/；无作者材料时只用标记占位符。
```

### 2. 限定方向与数量的批量学习

```text
$robotics-research-writing
本次授权处理 3 篇机器人机构设计论文，重点学习
“工程问题 → 结构产生动作的方式 → 实验如何证明设计价值”。
先查来源索引并去重，优先使用我的本地文件；缺少时在合法访问下获取。
逐篇核实身份、转换、阅读、保存和检查，完成 3 篇后停止。
只蒸馏，不改作者初稿，不建立定时任务。
不足 3 篇时报告实际完成数与缺项，不虚构完成状态。
```

替换篇数与方向以匹配实际授权。同一研究的预印本、正式版和补充材料关联登记；文件数、论文版本数和独立研究数分别计数。

### 3. 组织作者论文的主线

```text
$robotics-research-writing
请根据下面的初稿、结果和图表重组引言与结果部分。
先列中心主张、最强的已确认优势与支撑它的证据链，再给出修改稿。
按“问题 → 缺口 → 思路 → 最硬的已确认结果”组织；
结果按论证职责安排，不按实验先后排列。缺口需要来源支持。
数字、条件、引用和结果含义保持一致；缺少材料的地方单独列出。
正文与修改说明分开。
```

### 4. 逐处检查防御性写作

```text
$robotics-research-writing
请检查下面文本，逐处给出：
原文 → 问题类型 → 必留信息 → 改法 → 科学含义是否变化。
围绕已证实优势组织表达，不替审稿人总结弱点。
真实不确定性、比较条件和测试范围保留在影响理解的位置。
不要把观测改成机制验证，或把最高测试点改成全局最优。
```

### 5. 忠实中文到英文转换

```text
$robotics-research-writing
请把下面论文段落译成自然、准确的学术英文。
先忠实再自然，保留数字、单位、术语、公式、引用与主张强度。
不要扩大适用范围，不把未测性能写成结果。
交付英文正文；术语歧义与影响含义的缺项单独说明。
```

### 6. 根据真实反馈更新规则

```text
$robotics-research-writing
下面是原段落、修改稿和我的具体反馈。
先查已有规则，再判断是新增、支持、范围修订、反例、冲突或一次性修改。
只更新受影响条目，保留编号、来源、原状态、变更与理由。
记录保存到 .robotics-writing/，不改其他 skill 或全局记忆。
需要检验时，区分真实作者材料与构造案例，并报告实际检查范围。
```

## 科学证据与比较口径

围绕最强且可证实的优势组织叙事，主动讲清优势为何重要、什么结果支持它。每个实验应有论证职责，摘要和引言明确问题、缺口、思路与关键结果，结论强化已经证明的记忆点。

评价维度服务研究目标，比较条件需要公开说明。目标差异与合理权衡可以解释结果，但不能通过删掉已报告结果、换分母或隐瞒条件制造优势。

机器人写作逐项核对：

- 仿真 / 硬件、定点受力 / 自由运动、单次展示 / 重复试验。
- 帧 / 周期 / 试次 / 独立样机；最优 / 代表 / 均值。
- 开环 / 闭环、预设执行 / 自主决策、外部供能或计算 / 整机独立运行。
- 单环境 / 泛化、组件 / 系统、观测 / 机制验证、显著性 / 工程意义。
- 速度、负载、能耗、效率、精度、附着力、成功率的定义、单位、分母和统计单位。
- 尺寸、质量、供能、载荷、环境、任务、控制设置与汇总方式。

物理量名称须与计算一致；例如力—时间积分不能写成机械功。条件不同的文献表不是受控领先实验；最高测试点不等于全局最优。文献结果、未测变量和相邻实验的重复数不移入作者结果。

## 依赖与可选工具

核心阅读与写作由 Codex 执行，没有必装 Python 包。先检查当前安装能力，再按任务选最小工具组合。

| 场景 | 可选工具与用途 |
| --- | --- |
| PDF / Word 转 Markdown | `markitdown` 或本地提取工具；转换异常回看原页 |
| 全文精读 / 中英对照 | `nature-reader`，按用户要求的实际范围执行 |
| 引文逐项核验 | `nature-ref-verifier` 或原文、作者 / 出版者页面 |
| ScienceDirect 页面获取 | 当前浏览器 skill，可结合 `sd-search` / `sd-download` |
| 特定期刊风格 | 用户要求时选 `nature-writing` / `nature-polishing` |
| 统计表述 / 防御性表达 | `nature-statistics` / `anti-defensive-writing`；前者不代替原始数据分析 |
| 本地 PDF 下载脚本 | Python 3.9+、`pypdf`、`curl.exe` 或 `curl` |

可选辅助 skill 不随本仓库安装；名称列出不代表你当前环境一定可用。缺少转换工具时可以用本地提取生成带锚点 Markdown，未恢复内容保留源图并记录。

### ScienceDirect 可选下载流程

需要你已有合法的机构、订阅或开放获取权限。先在浏览器中正常登录，由 Codex 沿实际页面取得 PDF 地址；随附脚本负责本地传输与结构校验，不提供登录或访问权限。

在仓库根目录安装可选依赖并查看参数：

```powershell
py -3 -m pip install -r requirements.txt
py -3 robotics-research-writing/scripts/sciencedirect_download.py --help
```

Linux / macOS 用 `python3` 替换 `py -3`。从已安装 skill 使用时，脚本位于其 `scripts/` 子目录，依赖只需按需要安装 `pypdf`。

Codex 从实际浏览器请求生成专用临时 JSON；不要让用户手工导出 Cookie。调用必须显式指定个人资料目录：

```text
python scripts/sciencedirect_download.py --request /path/to/temporary-request.json --library-dir /path/to/research/.robotics-writing/literature --route system-proxy
```

以上命令在 skill 目录执行，路径由本次任务的实际位置替换。可选 `direct` 只控制本次传输路线，不改变访问授权；认证、验证码或权限拒绝需要正常解决后继续。

脚本先写 `.pdf.part`，通过结构、页数和加密状态检查并记录 SHA-256 后改为 `.pdf`。`pdf_structure_valid_identity_pending` 仍需题名 / DOI 核验；打开阅读器、触发下载和本地落盘是不同状态。专用请求文件在该次尝试结束后删除，不公开签名地址或下载日志。

完整流程、有限恢复与状态解释见 [sciencedirect-acquisition.md](robotics-research-writing/references/sciencedirect-acquisition.md)。

## 常见问题与检验范围

| 情况 | 处理方式 |
| --- | --- |
| 安装后规则模板为空 | 这是公开框架的初始状态；根据真实输入在项目 `.robotics-writing/` 中建立记录 |
| 已有同名私人 skill | 安装器停止；先备份并核对差异，避免覆盖旧规则和来源 |
| 下一轮没有发现 skill | 检查安装目录是否包含 `SKILL.md`、名称是否正确，再显式调用；文件存在不等于实际加载 |
| PDF 不完整、返回 HTML 或只有 `.part` | 不计为成功获取；保留断点，有限恢复并重新校验 |
| 签名地址过期或机构登录失效 | 回到正常文章入口取新链接；登录验证由用户完成，不无限重试 |
| 当前无浏览器或转换 skill | 先处理已有本地材料；所缺阶段说明需要什么工具，不假称已下载或完整阅读 |
| 双栏、公式或表格转换错位 | 保留原转换，回看原页修复锚点；无法恢复处标记并保留源图 |
| 只有摘要、节选或缺关键图表 | 按实际范围完成分析，缺项影响的结论单列，不登记全文完成 |
| 不同论文产生冲突规则 | 检查研究类型、章节职责与证据差异；保留反例，必要时限定范围或降低优先级 |

[验证流程](robotics-research-writing/references/validation.md) 区分格式检查、构造案例与真实写作迁移。行为检验优先使用未参与提炼的真实材料，固定事实和任务，检查事实忠实、主张—证据匹配、结构、清晰度、术语与任务适配。

不要用词汇难度、篇幅或“像顶刊”代替效果检验。针对某个案例调过规则后，该案例不再是独立验证。安装成功、格式通过和脚本离线检查均不等于写作效果或真实机构下载已经验证。

## 公开文件与分享边界

```text
README.md / README.en.md                  # 双语使用说明
examples/literature-distillation-showcase.md # 唯一授权精选示例
robotics-research-writing/
├── SKILL.md
├── agents/openai.yaml
├── references/                          # 空状态模板和通用流程
└── scripts/sciencedirect_download.py
requirements.txt / .gitignore / .gitattributes
```

其余论文原件、补充材料、提取全文、蒸馏记录、实际来源索引、个人规则库、研究画像、作者初稿、实验数据和反馈日志保留在个人项目。精选示例的公开授权不扩展到这些材料。

个人生成物不自动提交或推送，也不写回公开模板。再次发布前核对待提交文件；API 密钥、登录凭据、Cookie 和签名下载地址不进入仓库。外部服务处理私人材料需要相应授权，原件不覆盖。
