

# 每日HFDailyPapers-2026年08月11日

## 代码Agent与基准测试

**概述**

SWE-Bench ProMax 发布了一个专家策展的多语言代码重构基准，包含170个来自真实commit的实例，覆盖Python、Java、TypeScript、Go、C、C++和Rust七种语言 [https://arxiv.org/abs/2608.09802](https://arxiv.org/abs/2608.09802)。该基准针对现有SWE-bench的问题（约60%未解决问题包含有缺陷的测试）进行了改进，每个实例重写issue描述、人工审核测试套件，平均涉及11.4个修改文件和261.6行代码。A²E（Agent Auditing Engine）提出了一种端到端Agent harness评估框架，通过Agent Task Protocol（ATP）实现快速集成，并使用多维指标（执行效率、工具使用、任务规划、错误恢复）而非仅正确性来评估不同模型-harness组合 [https://arxiv.org/abs/2608.07346](https://arxiv.org/abs/2608.07346)。

**分析**

数据显示，当前前沿模型在SWE-Bench ProMax上的最高解决率仅为41.2%，表明代码重构任务对AI Agent仍是实质性挑战。现有基准的快速饱和和质量问题（测试缺陷、训练数据泄露）凸显了更严格评估的必要性。A²E的实验发现模型-harness组合在不同任务类型上性能差异显著，且无单一组合能在所有任务中持续最优，验证了系统化评估对模型-harness协同发展的必要性。

## 持续学习与模型架构

**概述**

Macaron-V1 是由Mind Lab等团队提出的开放Agent模型家族，围绕"经验智能"（experiential intelligence）两个系统目标构建：通过递归改进版本化模型-harness对实现持续适应，通过Mixture-of-LoRA（MoL）架构实现协作——冻结基础模型、组合专家LoRA适配器、每用户回合选择一个LoRA。旗舰模型Macaron-V1-Venti基于744B GLM-5.2基础，配备四个LoRA（对话、Agent、编码、GenUI） [https://arxiv.org/abs/2608.09819](https://arxiv.org/abs/2608.09819)。Motif 3 是一个314B总参数、每token激活13.2B的解码器MoE语言模型，采用Grouped Differential Latent Attention（GDLA）架构，支持256K上下文长度，在 reasoning、coding、工具使用、长上下文理解等维度表现竞争性 [https://arxiv.org/abs/2608.09119](https://arxiv.org/abs/2608.09119)。

**分析**

MoL架构通过可扩展的LoRA专家支持持续学习，其设计反映了从单体模型向模块化、可组合系统演进的架构趋势。Macaron-V1将算法（Model-Harness Co-design、递归自改进循环）、基础设施（MinT训练平台、LongStraw长上下文RL方法）和模型架构统一设计，展示了系统级优化的思路。Motif 3的稀疏MoE设计（384个专家中选8个）在提供大量专家容量的同时限制计算开销，体现了fine-grained sparsity对扩展性的支持。

## Agent系统与架构

**概述**

RoMeRL（Reduced-Order Memory Reinforcement Learning）针对自演化LLM Agent记忆系统的两个挑战（轨迹索引效用随交互历史增长而分散、无关经验可能获得误导性效用更新导致memory-reward trap）提出解决方案，通过将效用空间表示为固定维度的per-task记忆状态因子分解 [https://arxiv.org/abs/2608.02508](https://arxiv.org/abs/2608.02508)。在ALFWorld和LifelongAgentBench上，RoMeRL将Cold-Q比率降低80.0%、反馈密度提升约6倍、维持记忆规模减少84.4%、LLM调用减少21.1%，代码开源 [https://github.com/YOUNG-fnxm/RoMeRL](https://github.com/YOUNG-fnxm/RoMeRL)。Ouroboros 是一个自演化编码Agent harness，其工具、提示、上下文组装和核心实现通过reviewed commits持续改进，在Terminal-Bench 2.1上达到86.74%（Opus 5）、OSWorld-Verified上达到90.69% [https://arxiv.org/abs/2608.08311](https://arxiv.org/abs/2608.08311)。WeClawArena 是首个面向跨用户Agent协作与安全的可审计沙盒基准，包含124个基础任务和620个场景变体，测试多Agent在个人工作空间上的协作能力与攻击向量 [https://arxiv.org/abs/2608.03499](https://arxiv.org/abs/2608.03499)。CEAA 提出模块化认知架构， bridging high-level reasoning models与real-time embodied execution，用于在交互式虚拟环境中部署具身IVA [https://arxiv.org/abs/2608.09848](https://arxiv.org/abs/2608.09848)。

**分析**

自演化Agent系统（Ouroboros、RoMeRL）代表了Agent从静态部署向持续学习演进的趋势，但这也带来了安全性挑战——Ouroboros研究特别强调operational safety作为核心设计问题。RoMeRL的理论分析表明，reduced-order参数化增加了每个效用坐标的平均反馈，并在generic coordinate-transition模型下刻画了错误坐标的稳态占用。WeClawArena的设计填补了跨用户Agent协作评估的空白，将个人工作空间同时视为操作工具和个人约束，支持审计任务分解、隐私泄露、中毒证据和无效授权路径。

## 安全、隐私与评估

**概述**

一项研究揭示了商业LLM API中encrypted reasoning traces的安全漏洞：客户端接收的加密推理块在不同session、用户和模型间完全兼容可互换 [https://arxiv.org/abs/2608.09867](https://arxiv.org/abs/2608.09867)。攻击者可将强模型的加密推理迹注入弱模型，迫使后者以明文输出，从而绕过anti-distillation机制、提取私人数据（从315,320个块中恢复367个PII和182个凭证）、揭示被隐藏的有害信息，以及执行invisible prompt injection。此研究已在Anthropic、OpenAI和Google完成responsible disclosure。Sci-VBench 评估科学领域知识密集型视频生成，包含1,253个专家标注示例，覆盖自然科学、医疗健康、人文社科和工程四大领域 [https://arxiv.org/abs/2608.09873](https://arxiv.org/abs/2608.09873)。MMOOC 评估多模态大模型在上下文偏移下的拒绝与鲁棒回答能力，包含41K+图像-问题对，涵盖可回答的Shifted IC和不可回答的OOC案例 [https://arxiv.org/abs/2607.27637](https://arxiv.org/abs/2607.27637)。

**分析**

encrypted reasoning traces的互操作性漏洞揭示了当前商用API设计中的系统性安全风险——为保护IP而采用的加密方案若缺乏session隔离，反而成为信息泄露通道。攻击者无需直接jailbreak强模型，即可通过中间层弱模型提取其推理过程，这对推理迹的安全部署提出了新的设计挑战。Sci-VBench评估显示，尽管自动感知质量分数在各系统间高度集中，但Prompt Grounding和Scientific/Causal Correctness存在显著差异，且proprietary-open-source差距明显，表明视觉真实感的进步尚未转化为科学因果动态的可靠建模。

## 机器人学习与具身AI

**概述**

RynnValue 是开源的机器人操作价值基础模型，用temporal distance（从观察到语言指定目标的有向cost-to-go）替代任务内锚点作为监督目标，从超过7,000小时、约3M条instruction-conditioned clips中学习，无需偏好或进度标注 [https://arxiv.org/abs/2608.09853](https://arxiv.org/abs/2608.09853)。在RBM-EVAL-OOD上达到Kendall's tau_a 0.675，超越fully preference-supervised SOTA（0.655），真实策略成功率从52.5%提升至72.5%（online）和63.8%提升至82.5%（offline）。Ego-OSCAR 是开源硬件、低成本（<200美元/单位）的头戴式立体惯性采集设备，用于野外第一人称数据采集，提供完整的软件栈和约550小时带标注的第一人称立体视频数据集 [https://arxiv.org/abs/2608.08285](https://arxiv.org/abs/2608.08285)。

**分析**

RynnValue表明temporal distance可作为可扩展的监督目标，其从时间戳直接派生的特性避免了跨具身形态和数据源的迁移难题。random temporal sampling、temporal-order shuffling和value-isolation attention的组合有效抑制了shortcut学习，使预测对失败和回归敏感。Ego-OSCAR通过开源硬件设计、3D打印部件和商业化组件大幅降低了第一人称数据采集的门槛，550小时的众包数据集为egocentric AI研究提供了低成本可扩展的substrate。

## 视觉理解与多模态

**概述**

Evidence-RL 提出Counterfactual Evidence Disentanglement（CED）训练方法，通过neutralize object-centric Evidence Region并比较支持下降，对VLM接地进行因果审计 [https://arxiv.org/abs/2608.08021](https://arxiv.org/abs/2608.08021)。在九个公开基准和四个backbone上，CED优于先前RL-based post-training方法。Vision-Language Grounding 提出ConCor-1模型，将视觉-语言接地形式化为双向概念对应问题，统一phrase grounding、referring expression grounding和open-vocabulary detection任务，在long-caption数据集上提升correspondence F1 48%，在零样本LVIS上提升29% [https://arxiv.org/abs/2608.07886](https://arxiv.org/abs/2608.07886)。

**分析**

Evidence-RL的CED方法通过answer correctness与evidence path的联合奖励信号，解决了现有perception-aware方法未能测试答案是否因果依赖局部证据的问题。ConCor-1的双向对应框架突破了一维定位范式的局限，通过learnable bridge tokens预测文本mask、图像mask和对应存在分数，统一了多个接地任务，显示了任务 formulation统一化对提升泛化能力的价值。

## 模型系统与效率优化

**概述**

OasisKV 是一种内存为中心的LLM推理系统设计，通过lookahead sparse prefetching在decode阶段将KV Cache与HBM解耦 [https://arxiv.org/abs/2608.08097](https://arxiv.org/abs/2608.08097)。通过speculative decoding预测未来重要token，将相关KV块从更高容量内存层预取至HBM，在2,048-token KV预算下精度损失仅0.7点，推理吞吐量提升1.69倍（reasoning workload）至2.1倍（multi-GPU长上下文），在prefill-decode disaggregation下达到约2倍dense吞吐量。Agent Memory Distillation（AMD）将分层知识从大教师Agent转移至小模型（4B-8B参数），通过Workflow memory、Subtask memory和Function memory三种类型，在AppWorld、BFCL V3和ToolSandbox上平均提升27.2、11.2和3.4个百分点 [https://arxiv.org/abs/2608.07169](https://arxiv.org/abs/2608.07169)。

**分析**

OasisKV利用了decode-time attention的自然稀疏性，通过speculative decoding的lookahead预测将稀疏性转化为吞吐量收益，在HBM容量成为瓶颈的背景下提供了实用的扩展方案。AMD展示了小模型通过外部结构化知识注入可弥合与大人模型的能力差距，Subtask memory贡献最大增益，且4B模型受益最为显著，表明知识蒸馏对小型Agent的实用价值。

## 可解释性与优化理论

**概述**

Scaling Inherently Interpretable Language Models 将可解释性作为训练约束，与语言建模目标联合优化，发现可解释性随scale与capability同步提升而非对立 [https://arxiv.org/abs/2608.07594](https://arxiv.org/abs/2608.07594)。实例化模型Steerling-8B（扩散语言模型）可为生成token组归因于相关输入token、人类可理解概念和训练数据，支持closed-loop intervention。优化器理论工作揭示了梯度下降与Adam在factorized模型上的差异：梯度下降隐含偏向低秩解，而Adam不具gauge equivariance [https://arxiv.org/abs/2608.05136](https://arxiv.org/abs/2608.05136)。

**分析**

Steerling-8B结果表明可解释性可通过训练设计而非事后解释获得，且随scale增强，这挑战了"可解释性是对能力的tax"的常见假设，为 interpretable-by-design 范式提供了实证支持。优化器理论分析表明，basis choice并非调参细节而是决定optimizer选择的插值，Adam在transformer中分离gauge-equivalent初始化的机制导致W_Q^T W_K在per-head层面出现56%的相对Frobenius距离差距，这为优化器选择提供了理论依据。

## 其他动态

**概述**

BDH-CQ 结合in-context学习与recurrent latent reasoning，在ARC-AGI-1上以150M参数达到29.5% pass@2，推理成本$0.0007/task，突破先前Pareto前沿 [https://arxiv.org/abs/2608.09888](https://arxiv.org/abs/2608.09888)。Evo-Bench 评估LLM自主优化harness的能力，在Search和General任务上接近人工-engineered baseline，但在需要精确处理流程的Office任务上表现不足 [https://arxiv.org/abs/2608.09096](https://arxiv.org/abs/2608.09096)。Intent Speaks Louder（UserIDA）通过显式per-turn interaction intent控制用户模拟，在LMSYS-USP上达到86.6% intent准确率 [https://arxiv.org/abs/2608.09420](https://arxiv.org/abs/2608.09420)。SPOT通过sparse probing和outcome-calibrated targets改进on-policy distillation [https://arxiv.org/abs/2608.04419](https://arxiv.org/abs/2608.04419)。What to Edit Next针对图像编辑对话系统，通过多阶段框架将视觉不一致从3.7%降至0.9%，推荐CTR提升32.70% [https://arxiv.org/abs/2608.07565](https://arxiv.org/abs/2608.07565)。Factorized Hypothesis Search解决evidence-to-taxonomy检索中的语义gap，在financial taxonomy和clinical coding任务上取得最佳非oracle性能 [https://arxiv.org/abs/2608.06614](https://arxiv.org/abs/2608.06614)。