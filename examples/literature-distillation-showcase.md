# 真实文献蒸馏展示 / Real literature distillation showcase

[中文说明](../README.md) · [English guide](../README.en.md)

**把一篇机构论文转成可执行的写作决策：先让读者理解动作，再分配指标职责，最后写清设计选择适用的条件。**

**Turn a mechanism paper into actionable writing decisions: explain the motion, assign each metric a purpose, and specify the conditions behind a design choice.**

本展示精选自一份真实的既有蒸馏记录 **P001**，保留其反向提纲、观察依据、规则适用条件和实际产出。中英文说明为本次公开展示重新编排；后文的前后改写明确标为本次新构造示例。这里展示的是蒸馏产物与写作决策过程。

This showcase is curated from the existing, real distillation record **P001**. It retains the reverse outline, evidence behind the observations, rule conditions, and recorded outputs. The bilingual presentation was prepared for this release; the before/after passage below is explicitly identified as a newly constructed illustration. The demonstrated outcome is the distillation output and its writing decisions.

## 1. 所选论文 / Selected paper

Michael Ishida, Arsen Abdulali, Narges Khadem Hosseini, and Fumiya Iida. **Exploration of fin stiffness for asymmetric thrust in a swimming robot.** In *2024 IEEE 7th International Conference on Soft Robotics (RoboSoft)*, pp. 946–951, 2024. [DOI: 10.1109/ROBOSOFT60065.2024.10522008](https://doi.org/10.1109/ROBOSOFT60065.2024.10522008).

题名、作者顺序、会议、年份与页码来自原有出版版身份核对，并由[第一作者发表列表 C1](https://www.michaelishida.com/publications-cv)交叉支持。页码在下文以 PDF 页序 1–6 表示，对应印刷页 946–951。

The title, author order, conference, year, and page range were checked against the publication version in the original record and are cross-supported by [entry C1 in the first author's publication list](https://www.michaelishida.com/publications-cv). Locations below use PDF pages 1–6, corresponding to printed pages 946–951.

**为什么选它：**这篇论文同时包含机构设计、刚度测量和固定装置受力测试，能在一个案例中展示“结构如何产生动作—测量如何支持主张—比较为何需要条件”。其周期量与峰值指标的分工，也让写作组织和物理定义检查有了具体对象。

**Why this case:** the paper combines mechanism design, stiffness measurement, and force tests on a fixed apparatus. A single case therefore shows how structure produces motion, how measurements support claims, and why comparisons require conditions. Its cycle-level and peak-force metrics provide a concrete example of both evidence organization and physical-definition checks.

## 2. 实际阅读范围 / Actual reading scope

原蒸馏记录日期为 **2026-09-06**。本次整理复用当时已经形成的蒸馏记录及带来源锚点的 Markdown 阅读版。

The original distillation record is dated **2026-09-06**. This public presentation reuses that record and the previously prepared Markdown reader with source anchors.

| 材料 | 原记录的实际范围 |
|---|---|
| 正文 | 6 页会议出版版；摘要与 §§I–V 已读，6 页原页均已查看 |
| 图表 | Figs. 1–5、Tables I–II 已读与核对 |
| 公式 | Eqs. (1)–(6) 已查看原页并保留源图；没有复算推导 |
| 参考文献 | 33 项已提取；未逐条核验或读取其全文 |
| 其他材料 | 未取得补充视频、原始力数据或分析代码 |

| Material | Scope recorded in the original distillation |
|---|---|
| Main paper | Six-page conference publication; abstract and Sections I–V read; all six original pages viewed |
| Figures and tables | Figures 1–5 and Tables I–II read and checked |
| Equations | Equations (1)–(6) checked on the original pages with source images retained; derivations not recomputed |
| References | Thirty-three entries extracted; cited full texts and individual references not independently verified |
| Other material | Supplementary video, raw force data, and analysis code not obtained |

## 3. 最小研究理解 / Minimum research understanding

论文用单个主动输入与双凸轮机构耦合柔性鳍的 yaw 和 roll，比较不同鳍刚度、凸轮角速度下的受力特征。机构图与几何关系承担动作实现的解释；刚度测试定义比较对象；固定装置受力测量支持周期与瞬时力特征的比较。来源位置：§§II–IV，pp. 2–5；[原论文 DOI](https://doi.org/10.1109/ROBOSOFT60065.2024.10522008)。

The paper uses one active input and a dual-cam mechanism to couple a flexible fin's yaw and roll, then compares force characteristics across fin stiffnesses and cam angular speeds. Mechanism diagrams and geometric relations explain the motion; stiffness tests define the compared configurations; fixed-apparatus force measurements support cycle-level and instantaneous-force comparisons. Source locations: Sections II–IV, pp. 2–5; [paper DOI](https://doi.org/10.1109/ROBOSOFT60065.2024.10522008).

从写作角度，中心线索是：**目标动作 → 机构实现 → 定义比较量 → 条件化的力特征**。这条线索让各部分共同支持一个设计问题。

For writing, the central chain is: **target motion → mechanism → defined comparison quantities → condition-dependent force characteristics**. This gives the sections a shared design question.

## 4. 反向提纲：每部分让读者接受什么 / Reverse outline: what each part establishes

| 来源位置 | 内容安排 | 论证职责 |
|---|---|---|
| 摘要，p. 1 | 动作背景、单输入耦合、力的不对称性 | 把机构能力与实验问题相连 |
| §I，pp. 1–2 | 鳍运动、柔性研究、耦合运动问题、研究目标 | 说明为什么需要该机构与刚度比较 |
| §II，pp. 2–4；Figs. 1–3 | 目标动作、机构、几何约束、凸轮轮廓 | 解释各部件为何产生所需动作 |
| §III，p. 4；Fig. 4 | 刚度测量、受力测试 | 分别定义自变量与响应变量 |
| §IV，pp. 4–5；Fig. 5、两表 | 数据处理、周期积分、峰值、条件比较 | 说明不同指标回答的不同问题 |
| §V，pp. 5–6 | 已支持的发现、后续动作与结构问题 | 强化已实现贡献，明确下一步问题 |

| Source location | Organization | Argumentative role |
|---|---|---|
| Abstract, p. 1 | Motion context, single-input coupling, force asymmetry | Connect mechanism capability to the experimental question |
| Section I, pp. 1–2 | Fin motion, compliance, coupled-motion problem, objectives | Explain why the mechanism and stiffness comparison are needed |
| Section II, pp. 2–4; Figures 1–3 | Target motion, mechanism, geometric constraints, cam profiles | Explain how the components produce the required motion |
| Section III, p. 4; Figure 4 | Stiffness measurement and force testing | Define the independent and response variables separately |
| Section IV, pp. 4–5; Figure 5 and both tables | Processing, cycle integral, peaks, condition comparisons | Explain the different questions addressed by the metrics |
| Section V, pp. 5–6 | Supported findings and subsequent motion/design questions | Reinforce the realized contribution and identify the next question |

这种提纲记录的是论证职责。迁移到另一篇论文时，要根据它的贡献依赖和证据顺序重新安排章节。

This outline records argumentative roles. For another manuscript, section order should follow that study's contribution dependencies and evidence.

## 5. 三项观察如何成为规则 / How three observations become rules

### O01 → L001：动作与约束先于零件清单 / Motion and constraints before the component list

**观察。**§II 先解释动力与恢复行程所需的鳍朝向，再引入电机、双凸轮和连杆；柔性接头的作用也联系到局部变形约束。来源：pp. 2–3；Figs. 2–3。

**Observation.** Section II explains the fin orientations required for the power and recovery strokes before introducing the motor, dual cams, and linkage. The flexible joints are also connected to local deformation constraints. Source: pp. 2–3; Figures 2–3.

**解释。**读者知道目标动作后，才能判断每项机构选择的作用。设计叙述因而能沿“需要什么动作—结构如何实现—证据在哪里”推进。

**Interpretation.** Once readers understand the target motion, they can judge the role of each mechanism choice. The design narrative can then progress from required motion to structural realization to evidence.

| 规则字段 / Rule field | 决策 / Decision |
|---|---|
| 触发 / Trigger | 机构论文有明确的动作目标、结构约束和动作证据 / A mechanism paper has an explicit motion objective, structural constraints, and motion evidence |
| 动作 / Action | 先写动作和约束，再说明相关结构及其验证 / State the motion and constraints, then explain the relevant structure and verification |
| 检查 / Check | 每项关键结构能否对应到作用与证据？ / Does every key structural feature connect to a function and evidence? |
| 适用条件 / Applicability | 适合机构或驱动贡献；以算法基准或数学证明为核心时另按其逻辑组织 / Suits mechanism or actuation contributions; algorithm benchmarks and mathematical proofs require their own logic |
| 原始状态 / Original status | L001 候选规则 / L001 candidate rule |

### O02 → L002：周期量与峰值分别承担职责 / Give cycle quantities and peaks separate roles

**观察。**§IV 与两表分别报告周期积分指标和正负峰值差，并讨论它们的趋势差异。来源：pp. 4–5；Fig. 5、Tables I–II。

**Observation.** Section IV and the two tables separately report a cycle-integrated quantity and a positive/negative peak-force difference, then discuss their differing trends. Source: pp. 4–5; Figure 5 and Tables I–II.

**解释。**周期量回答整个周期的净效果；峰值说明瞬时载荷的不对称性。把两者分开，才能同时解释净周期量和短时反向尖峰。这里学习指标的分工；物理名称另按下一节检查。

**Interpretation.** A cycle-level quantity describes the net effect over a cycle; peak differences describe instantaneous-force asymmetry. Separating these roles makes it possible to discuss both a net cycle quantity and brief reverse-force peaks. The transferable lesson is the division of metric roles; physical naming is checked in the next section.

| 规则字段 / Rule field | 决策 / Decision |
|---|---|
| 触发 / Trigger | 周期、间歇或脉冲运动具有不同时间尺度的结果 / Periodic, intermittent, or pulsed motion produces outcomes at different time scales |
| 动作 / Action | 分别定义主要周期指标与相关峰值，并解释各自支持什么 / Define the primary cycle metric and relevant peaks separately, explaining what each supports |
| 检查 / Check | 结论是否用了与研究目标匹配的量、单位和时间窗口？ / Does the conclusion use the quantity, units, and time window that match the research objective? |
| 适用条件 / Applicability | 主要指标由研究目标预先确定；峰值与周期量各有定义 / Choose the main metric from the research objective beforehand; define peaks and cycle quantities separately |
| 原始状态 / Original status | L002 候选规则；不吸收来源中的争议命名 / L002 candidate rule; disputed metric naming is not adopted |

### O03 → L003：排序交叉导向条件化选择 / Ranking changes support conditional choices

**观察。**Table I 与 §IV 的比较显示，中等刚度鳍在最低与最高已测角速度下的周期指标高于另外两种，而中间速度下出现另一种排序。来源：p. 4 Table I；p. 5 条件比较段。

**Observation.** Table I and Section IV show that the intermediate-stiffness fin has the higher cycle quantity at the lowest and highest tested angular speeds, whereas the middle speed gives a different ranking. Source: Table I on p. 4 and the condition-comparison paragraph on p. 5.

**解释。**这使论点从笼统的“哪种材料最好”变成“在所测条件下如何选”。读者得到明确的适用条件，也能看见表格中改变选择的证据。

**Interpretation.** The argument moves from a broad question about the best material to a choice within the tested conditions. Readers receive explicit applicability conditions and can identify the evidence that changes the choice.

| 规则字段 / Rule field | 决策 / Decision |
|---|---|
| 触发 / Trigger | 不同设计在同一指标上的排序随已测条件改变 / Designs change rank on the same metric across tested conditions |
| 动作 / Action | 将设计、指标和条件绑定陈述，解释交叉排序 / Bind each design claim to its metric and condition; explain the ranking change |
| 检查 / Check | 主句能否同时解释表格中各条件，而非只取一个有利点？ / Can the claim account for the tested conditions rather than one favorable point? |
| 适用条件 / Applicability | 描述已测范围；统计交互、连续最优区间和因果机制需各自证据 / Describe the tested range; statistical interaction, continuous optima, and causal mechanisms require their own evidence |
| 原始状态 / Original status | L003 候选规则 / L003 candidate rule |

## 6. 选择性吸收：定义、重复层级与装置范围 / Selective learning: definitions, replication, and apparatus scope

### X01：用计算定义核对指标名 / Check metric names against their definitions

原记录发现：§IV 的文字把力—时间积分称为机械功，而 Table I 报告 N·s。根据给出的定义，`I = ∫ F(t) dt` 对应冲量，单位 N·s；机械功 `W = ∫ F · dx` 的单位为 J。来源：p. 4，§IV 与 Table I。

The original record identified a naming conflict: Section IV describes a force–time integral as work, while Table I reports N·s. Under the stated definition, `I = ∫ F(t) dt` is impulse, with units N·s; mechanical work, `W = ∫ F · dx`, has units J. Source: p. 4, Section IV and Table I.

**写作决策：**保留周期量与峰值的组织方法；应用时按定义和单位命名。此处是量纲审查，没有重算原始力数据，也没有据此推断能量效率。

**Writing decision:** retain the separation of cycle quantities and peaks, and name the quantity from its definition and units. This is a dimensional check; it does not recompute the raw force data or establish energy efficiency.

### X02：重复数属于具体实验 / Replication belongs to a particular experiment

原记录将刚度试验的每鳍三次试验与后续受力测试分开登记；正文未明确给出可据以确认的推力独立试次数。周期、采样点与相邻实验的重复数各有身份。来源：p. 4，§III。

The original record separately registers three trials per fin in the stiffness experiment and the subsequent force tests. The main text does not explicitly establish the independent thrust-test replicate count. Cycles, samples, and replication in an adjacent experiment have distinct roles. Source: p. 4, Section III.

**写作决策：**方法与统计表述把 `n` 绑定到具体试验和统计单位；缺少的信息保留为待确认项。

**Writing decision:** attach `n` to the specific experiment and statistical unit in methods and reporting; leave unspecified information to be confirmed.

### X03：以装置实际测量支持贡献 / Support the contribution with what the apparatus measures

Fig. 5a 的装置固定机器人以测力；§V 把双鳍无缆运动列为未来问题。原记录据此把已测力特征与自由游动、自主控制、整机能效分开。来源：pp. 5–6，Fig. 5a 与 §V。

The apparatus in Figure 5a fixes the robot for force measurements, and Section V identifies untethered motion with a second fin as future work. The original record therefore separates measured force characteristics from free-swimming, autonomous-control, and whole-system-efficiency claims. Source: pp. 5–6, Figure 5a and Section V.

**写作决策：**主句直接呈现已经实现的单输入耦合与所测力特征；扩展能力有自己的验证任务。

**Writing decision:** state the realized single-input coupling and measured force characteristics directly; each expanded capability has its own validation task.

## 7. 防御性写作如何改 / How the record handles defensive writing

以下是原记录中编辑决策的公开转述。全部建议围绕信息职责判断，保留真实几何条件、测量范围与未测收益的性质。

The following paraphrases the editing decisions in the original record. Each decision follows the role of the information and retains real geometric conditions, measurement scope, and the status of unmeasured benefits.

| 来源位置与问题 | 保留什么 | 编辑动作 |
|---|---|---|
| §II，p. 3：以限制口吻介绍单鳍 | 实际测试采用单鳍 | 直接说明测试配置；双鳍扩展另列 |
| §I，p. 2：控制、重量、成本的潜在收益 | 这些收益未定量比较 | 主句突出单输入运动耦合；潜在收益保持其性质 |
| §II.A，p. 3：短杆与系统尺寸的权衡 | 可达角和几何尺寸关系 | 直接解释设计约束如何决定结构选择 |
| §IV，p. 5：噪声来源讨论 | 已观测噪声与推测来源 | 将观测和解释分别陈述 |
| §V，p. 5：模糊的条件范围 | 不同刚度与速度下结果改变 | 把适用条件写具体，使用准确的周期量名称 |
| §V，p. 6：泛化用途式结尾 | 已实现动作与已测力特征 | 用最强的已支持发现收束 |

| Source location and issue | Information to retain | Editing action |
|---|---|---|
| Section II, p. 3: introducing one fin through limitation language | The tested configuration uses one fin | State the configuration directly; separate the two-fin extension |
| Section I, p. 2: potential control, weight, and cost benefits | Those benefits lack quantitative comparisons | Lead with single-input motion coupling; retain the potential status of the benefits |
| Section II.A, p. 3: short-link and system-size tradeoff | Reachable angles and geometric size | Explain how the design constraints determine the structural choice |
| Section IV, p. 5: possible noise sources | Observed noise and hypothesized sources | State observations and interpretations separately |
| Section V, p. 5: a vague condition range | Results change with stiffness and speed | Specify the relevant conditions and use the correct cycle-quantity name |
| Section V, p. 6: broad application-oriented ending | Realized motion and measured force characteristics | Close with the strongest supported finding |

## 8. 前后展示：本次新构造的同源示例 / Before and after: a new same-source illustration

**身份说明：**以下两段为本次公开展示新构造，基于所选论文的事实，用来演示组织变化。它们不是论文原句、用户草稿、原记录中的真实作者改稿或独立测试结果。

**Provenance:** both passages below were newly constructed for this public showcase from the selected paper's facts. They illustrate an organizational change. They are not quotations, a user's manuscript, a real author revision in the original record, or independent test results.

**改前：按工作顺序排列 / Before: arranged by work sequence**

> 我们设计了一个游动机器人，并测试了三种鳍。随后，我们在三种凸轮角速度下测量受力。结果在一些情况下有所不同，这一机构可能用于水下应用。

> We designed a swimming robot and tested three fins. We then measured forces at three cam angular speeds. The results differed in some cases, and the mechanism may be useful for underwater applications.

**改后：以动作、证据职责和适用条件组织 / After: organized around motion, evidence roles, and conditions**

> 单电机通过双凸轮机构耦合鳍的 yaw 与 roll。固定装置下的受力测量分别比较周期净冲量和峰值力不对称性，显示鳍刚度与凸轮角速度组合对应的力特征。机构的动作实现与条件化受力结果共同说明了设计选择应匹配所测工况。

> A single motor couples the fin's yaw and roll through a dual-cam mechanism. Fixed-apparatus force measurements separately compare net impulse per cycle and peak-force asymmetry, showing force characteristics associated with fin stiffness and cam angular speed. The realized motion and condition-dependent force results connect design choices to the tested operating conditions.

变化是可检查的：第一句说明机构价值；第二句给测量及指标分工；第三句解释条件化选择。改后仍以同一论文的事实为依据，并明确装置范围与指标职责；新增细节来自所选论文，删除了泛化应用措辞。此示例没有补入速度、效率、显著性或新数值。

The change is inspectable: the first sentence identifies the mechanism's value; the second assigns roles to the measurements and metrics; the third explains a conditional choice. The revision still uses facts from the same paper and specifies the apparatus scope and metric roles; added details come from that paper, and the broad application language is removed. No speed, efficiency, statistical significance, or new numerical result is added.

## 9. 原记录已经产生什么 / What the original record actually produced

| 已有产出 / Recorded output | 可见价值 / Reader value |
|---|---|
| 一份最小研究理解与反向提纲 / A minimum research account and reverse outline | 能把章节连接到主张和证据 / Connect sections to claims and evidence |
| O01–O03 对应三条候选 L001–L003 / Three observations linked to candidate rules L001–L003 | 把观察转成带触发、动作和范围的决策 / Convert observations into decisions with triggers, actions, and scope |
| X01–X03 的定义、重复层级和系统范围审查 / Checks of definitions, replication, and system scope | 有选择地学习写法，保留准确物理含义 / Learn selectively while retaining physical meaning |
| 六处编辑决策 / Six editing decisions | 区分冗余退缩与必要范围 / Distinguish unnecessary retreat from necessary scope |
| 一份结构占位迁移模板 / A structural transfer template with placeholders | 将所学组织方法用于自己的真实材料 / Apply the organization to one's own factual material |

原记录把 L001–L003 登记为候选，未在该轮升级为核心采用。已有产出是文献蒸馏与结构示范；本案例没有独立作者材料 A/B、专家评分或可量化写作收益。

The original record registered L001–L003 as candidates and did not promote them to core adoption in that round. Its outputs are literature distillation and a structural demonstration; this case has no independent manuscript A/B study, expert scoring, or quantified writing gain.

## 10. 如何迁移到自己的论文 / How to transfer the lesson to your manuscript

下面保留原记录的结构占位思路。所有括号需要由你自己的材料填写。

The template below retains the original record's structural-placeholder approach. Every bracket must be filled from your own material.

> 为实现【目标动作】，我们采用【机构选择】来满足【几何或驱动约束】。在【测试条件与独立试次数】下，【预先定义的周期指标】呈现【已测结果】；【峰值指标】揭示【瞬时载荷特征】。两种设计的排序在【条件】下改变，说明设计选择需要匹配【任务要求】。

> To achieve [target motion], we use [mechanism choice] to satisfy [geometric or actuation constraints]. Under [test conditions and independent replicate count], [predefined cycle metric] shows [measured result], while [peak metric] characterizes [instantaneous loading]. The two designs change rank under [condition], linking the design choice to [task requirement].

使用前核对：目标动作是否由机构或运动证据支持；指标的定义、单位和统计单位是否一致；排序改变是否确实出现在同一指标的可比较条件中。没有排序交叉时，删除相应句子；没有独立重复信息时，先核实该项。来源论文的数据始终属于来源论文。

Before use, check that the motion is supported by mechanism or motion evidence, that metric definitions, units, and statistical units agree, and that a ranking change actually occurs under comparable conditions on the same metric. Omit the ranking-change sentence when it does not apply; confirm missing replication information. Data from the source paper remain data from that paper.

这份公开示例展示了一个完整的选择性学习过程：**理解论文 → 找到论证职责 → 提取带条件的规则 → 核对证据 → 用自己的事实迁移**。

This public example shows a complete selective-learning process: **understand the paper → identify argumentative roles → extract conditional rules → check evidence → transfer using your own facts**.
