# robotics-research-writing

一个面向机器人科研写作的 Codex skill：从真实论文和作者反馈中提取有出处、有适用条件的写作规则，再用于贡献定位、论证组织、段落修改和忠实中英转换。

它把阅读与写作连接起来：**材料 → 理解 → 观察 → 条件化规则 → 应用 → 检验 → 修订**。每条规则都需要回答：来源在哪里、为什么有用、适用于什么情境、遇到什么反例时需要调整。

**本仓库公开的是工作流程、空白状态模板和可选下载脚本。已蒸馏的文献、实际个人规则库、作者材料与验证记录均不包含在内。** 首次使用时，个人状态只根据你实际提供的材料建立；安装本身不代表已经读过论文或验证了写作效果。

## 适合用来做什么

- 从论文中学习问题与缺口如何提出、贡献如何定位、设计与证据如何组织。
- 把文献观察整理为带来源、迁移条件和反例的个人规则。
- 根据已有方法、结果和图表，重组作者论文的叙事与段落。
- 逐处检查防御性写作，去除无信息的退缩，同时保留必要的测试条件与科学不确定性。
- 忠实地进行中文到英文转换，保留数字、单位、术语、公式和引用关系。
- 根据真实写作反馈修订个人规则，而不是每次重新从零开始。

单纯格式转换交给转换工具；全文中英对照阅读可结合 `nature-reader`；统计计算需要原始数据与相应分析工具。未指定期刊时，本 skill 根据研究类型与读者组织文本，不默认套用某一家期刊的风格。

## 安装

### 让 Codex 安装

在 Codex 中发送：

```text
请使用 skill-installer，从 Liuhy329/robotics-research-writing 仓库安装
robotics-research-writing 子目录里的 skill。
安装路径参数为 --path robotics-research-writing。
如果本机已有同名 skill，请停止，不要覆盖我的个人版本。
```

仓库地址：[Liuhy329/robotics-research-writing](https://github.com/Liuhy329/robotics-research-writing)。应安装仓库里的 `robotics-research-writing/` 子目录，该目录包含 `SKILL.md`。安装完成后，在下一轮对话中显式调用 `$robotics-research-writing`。

如使用系统提供的 `install-skill-from-github.py`，对应参数是：

```text
--repo Liuhy329/robotics-research-writing --path robotics-research-writing
```

### Windows PowerShell 手动安装

需要已安装 Git。以下命令使用 `CODEX_HOME`；未设置时使用当前用户的 `.codex`。如果目标 skill 或下载目录已经存在，会停止，避免覆盖已有个人版本。

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

同样需要 Git，目标存在时不复制。

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

## 依赖与可选工具

核心阅读与写作流程由 Codex 执行，没有必须安装的 Python 包。可选工具按当前任务加载，不要求一次安装全部辅助 skill。

| 场景 | 可选依赖 |
| --- | --- |
| PDF / Word 转 Markdown | `markitdown` skill 或其他本地转换工具；转换异常时回看原页 |
| 全文对照阅读 | `nature-reader` skill |
| 引文逐项核验 | `nature-ref-verifier` skill 或作者、出版者原始页面 |
| ScienceDirect 检索与取链接 | 当前可用的内置浏览器 skill；也可结合 `sd-search` / `sd-download` |
| 运行随附 PDF 下载脚本 | Python、`pypdf`、`curl.exe` 或 `curl` |

下载脚本依赖可在仓库根目录安装：

```powershell
py -3 -m pip install -r requirements.txt
py -3 robotics-research-writing/scripts/sciencedirect_download.py --help
```

Linux / macOS 可将 `py -3` 换成 `python3`。转换工具的依赖由各自工具说明管理。

ScienceDirect 下载需要你已有合法的机构、订阅或开放获取访问权限。先在内置浏览器中完成正常登录，再让 Codex 检索和取得真实 PDF 链接；脚本负责传输及 PDF 校验。不要导出浏览器 Cookie、保存账号密码，或把带签名的下载链接写入公开日志。具体流程见 [sciencedirect-acquisition.md](robotics-research-writing/references/sciencedirect-acquisition.md)。

## 个人材料保存在哪里

安装目录保留通用流程与空模板。使用时，个人状态保存到**你的研究项目工作区**中的 `.robotics-writing/`，而不是写回公开 skill 的 `references/`。

```text
你的研究项目/
└── .robotics-writing/
    ├── profile-state.md     # 当前需求、能力状态与覆盖范围
    ├── writing-rules.md     # 实际个人规则、来源与适用条件
    ├── source-index.md      # 实际文献索引、版本关系与材料路径
    ├── validation.md        # 实际验证与修订记录
    ├── distillations/       # 单篇学习记录
    ├── literature/          # 原始文献，可关联已有文献目录
    └── processed/           # Markdown 转换与清理材料
```

所需状态文件按需从空模板初始化，不要求首次填写完整画像。已有私人文献管理目录可以继续使用；先按核实后的正式标题命名，再沿用已有分类。没有分类体系时，不为单篇论文强行创建主题子目录。

本仓库已忽略 `.robotics-writing/`。如果你在另一个 Git 项目中使用，也应在那个项目的 `.gitignore` 中加入：

```gitignore
.robotics-writing/
```

已有同名私人 skill 的用户，应先备份和核对差异，再决定迁移方式；直接覆盖安装目录可能丢失旧规则和来源记录。

## 可以直接复制的使用示例

### 从一篇论文蒸馏写作方法

```text
$robotics-research-writing
请学习我提供的这篇机器人论文，只蒸馏写作方法，不修改我的初稿。
PDF / Word 先转 Markdown，保留原件和章节、页码、图表锚点。
先说明实际读到的范围，再做问题—主张—证据梳理和反向提纲。
提取有增量的观察，并写清来源、作用、迁移条件与反例。
把实际学习记录保存到当前项目的 .robotics-writing/。
没有作者材料时，迁移示例只能使用明确标记的结构占位符。
```

预期得到：实际材料与阅读范围、论文理解与反向提纲、带锚点的观察、候选规则与已有规则的关系，以及已保存记录的位置。摘要或节选不能被登记为全文已读。

### 批量学习，限定篇数和方向

```text
$robotics-research-writing
本次授权处理 3 篇机器人机构设计论文，重点学习
“工程问题 → 结构产生动作的方式 → 实验如何证明设计价值”的组织方法。
先检查当前项目来源索引并去重；优先处理我提供的本地文件。
缺少文件时，在已有合法访问权限下检索和下载，并核实论文身份。
逐篇转换、阅读、保存和检查，完成 3 篇后停止。
只做文献蒸馏，不改作者初稿，不建立定时任务。
如果无法取得 3 篇，报告实际完成篇数与尚缺材料，不虚构完成状态。
```

将 `3 篇` 与研究方向替换成你本次实际授权的范围。同一研究的预印本、正式版和补充材料需要关联，不能直接按独立研究累加。

### 重组论文叙事

```text
$robotics-research-writing
请根据下面的初稿、结果和图表重组引言与结果部分。
先列中心主张、最强的已确认优势和支撑它的证据链，再给出修改稿。
按“问题 → 缺口 → 思路 → 最硬的已确认结果”组织叙事；
结果按论证职责安排，不按做实验的先后顺序排列。
缺口必须有来源支持，数字、条件、引用和结果含义保持一致。
正文与修改说明分开，材料中没有的结果列为缺项。
```

请同时提供实际初稿与结果材料；结构模板不能替你生成研究缺口、测量数值或创新证据。

### 逐处检查防御性写作

```text
$robotics-research-writing
请检查下面文本中的防御性写作，逐处给出：
原文 → 问题类型 → 必留信息 → 改法 → 科学含义是否变化。
围绕已经证实的优势组织表达，不替审稿人总结弱点。
真实不确定性、比较条件与测试范围必须保留在影响理解的位置。
不要用更强语气把观测改成机制验证，或把最高测试点改成全局最优。
```

### 忠实中文到英文转换

```text
$robotics-research-writing
请把下面论文段落译成自然、准确的学术英文。
先忠实再自然，保留数字、单位、术语、公式、引用与主张强度。
不要扩大适用范围，不把未测性能写成结果。
交付英文正文；术语歧义和影响含义的缺项单独说明。
```

### 把真实反馈转为规则修订

```text
$robotics-research-writing
下面是原段落、修改稿和我的具体反馈。
请先检查当前项目已有规则，再判断这是新增规则、支持、范围修订、
反例、冲突还是一次性修改。只更新受影响的条目并保留来源。
把实际变更与理由保存到 .robotics-writing/，不要改其他 skill 或全局记忆。
```

## 输出与证据要求

- PDF、Word 先转换为 Markdown 再阅读；双栏、公式、OCR 或跨页表有异常时回看原页。
- 观察事实、对写法的解释、可迁移规则分开记录；单篇写法不会自动升级为领域标准。
- 作者事实与文献结果分开；没有材料支持的数字、实验、引用和结论不补写。
- 机器人结果核对仿真 / 硬件、开环 / 闭环、供能条件、样本单位、测量定义与比较条件。
- 写作稿不夹带规则编号或内部日志；实际保存与验证到哪一步，就报告到哪一步。
- 结构检查或构造案例不能替代真实写作效果验证；本公开版未包含个人验证结果。

## 公开范围与再次发布

| 可以公开的框架文件 | 应留在个人项目中的材料 |
| --- | --- |
| `SKILL.md`、`agents/openai.yaml` | 原始论文、补充材料、PDF / Word 文件 |
| 空白状态模板与字段说明 | 提取全文、Markdown 转换稿、单篇蒸馏记录 |
| 通用获取流程与下载脚本 | 实际书目来源索引、个人规则库、研究画像 |
| README、依赖文件、忽略规则 | 作者初稿、实验数据、反馈和验证日志 |

个人材料不自动提交或推送。再次发布时逐项核对待提交文件；`.gitignore` 不会停止跟踪已经提交过的文件。API 密钥、登录凭据、Cookie 和带签名下载链接不进入仓库。
