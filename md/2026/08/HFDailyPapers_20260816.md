

# 每日HFDailyPapers-2026年08月16日

## 世界模型与视频生成

多份研究聚焦于交互式视频世界模型的能力边界与优化路径。[Alaya-EVOKE](https://arxiv.org/abs/2608.13546) 通过外部化世界状态（将场景几何存储于相机索引的全局状态库）和重新设计教师模型的长程监督能力，实现了线性扩展的内存与计算成本，在单张H200上以384×640分辨率实现了每1.5秒2.11秒的生成速度，并在WBench上达到SOTA。[DreamX-Phi 1.0](https://arxiv.org/abs/2608.13489) 面向机器人操作场景，通过注入SE(3)几何编码和轻量深度分支确保动作可控性与物体一致性，在WorldArena 2.0挑战赛中获Track 1第一名。[PlayWorld](https://arxiv.org/abs/2608.13552) 提出基于多模态智能体玩家的长程交互式基准测试，涵盖171个场景，评估几何一致性、交互保真度等维度，实验揭示当前模型在长程交互目标下仍不可靠。[H2R-Bench](https://arxiv.org/abs/2608.13049) 则评估视频世界模型将人类操作视频迁移到机器人视角的能力，发现现有模型在形态一致性、功能交互等方面仍有局限。[Context-Matched Distillation (CMD)](https://arxiv.org/abs/2608.13391) 针对自回归视频蒸馏的因果对齐问题，提出因果教师框架替代双向全片段评分，在前缀评分和稳定性方面有所改进。分析表明，世界模型正从静态视频生成向交互式、长程一致性和因果对齐方向演进，但在跨形态迁移和长期空间一致性上仍有显著缺口。

## 视频与图像生成效率

[UniSwap](https://arxiv.org/abs/2608.11752) 提出首个流式音视频联合身份替换框架，通过交换-重建训练管线和高效自强制DMD将采样从30步降至3步，实现了稳定的长形式生成。[LiveAnimate](https://arxiv.org/abs/2608.11745) 构建了一个14B参数视频DiT，通过Pose-Retrieval Sink Attention（PR-Sink）机制实现有界KV缓存，在两张H100上达到19.63 FPS的流式推理，三分钟视频保持近乎恒定的感知质量和身份一致性。[PixSDS](https://arxiv.org/abs/2608.12997) 分析潜在SDS产生噪声像素的机制，提出VAE一致性梯度修复方法，减少结构化伪影而不需重训扩散模型。分析显示，视频生成领域正通过蒸馏、因果对齐和缓存机制突破实时长程生成的效率瓶颈。

## 智能体系统与长期记忆

[AutoDesign](https://arxiv.org/abs/2608.13560) 提出元工具优化框架，引导代码智能体递归改进工具以完成长程设计任务，在论文到海报生成任务上以不到3美元成本完成253次工具调用， surpass Claude Design 7.45分。[LycheeMemory V2](https://arxiv.org/abs/2608.12990) 将LLM智能体的内存巩固粒度从交互轮次提升至语义段落级，在LoCoMo上较A-Mem减少86%构建token。[Spatial Memory Agent](https://arxiv.org/abs/2608.12743) 探索冻结VLM通过经验自演化提升空间推理的路径，无需参数更新即可实现跨基准的最佳精度。[DarwinX](https://arxiv.org/abs/2608.07545) 将智能体自我改进视为冻结模型下的工具选择问题，通过群体选择和存档机制实现跨基准的能力迁移，在WebArena-Infinity上将pass@1从43.5%提升至93.0%。[SKILLER](https://arxiv.org/abs/2608.10538) 采用语言级强化学习为小模型自动生成可复用技能，在SkillsBench上匹配闭源模型性能。分析表明，智能体系统的优化重心正从模型权重训练转向工具编排、内存结构和技能演化。

## 科学AI与多模态推理

[Intern-S2-Preview](https://arxiv.org/abs/2608.13505) 构建面向科学发现的多模态智能体基础模型，支持科学文档理解、多任务强化学习和长时间序列预测，其时间序列模块提升SciTS上的信号理解能力。[OmniScientist](https://arxiv.org/abs/2608.13558) 提出端到端多模态AI科学家，直接从异构原始证据（图像、信号、视频、3D结构等）进行多学科研究，在36个真实案例中完成从原始数据到编译论文的全流程。分析显示，科学AI正从单一模态文本推理向全生命周期多模态感知与自主实验演化。

## 模型效率与推理优化

[Thought-Level Beam Search (Gambit)](https://arxiv.org/abs/2608.08020) 将推理过程形式化为计算分配问题，通过思维级束搜索动态聚焦计算资源，在HMMT-24上较剪枝基线提升6.7%绝对准确率，token消耗减少68.5%。[AI4AI视觉Token剪枝 (AutoPrune)](https://arxiv.org/abs/2608.07193) 利用LLM自动设计视觉Token剪枝策略，在移除94.4%视觉Token的情况下保持99%以上性能，FLOPs降低9.9倍。[LLMRouter](https://arxiv.org/abs/2608.06867) 提供统一的LLM路由基础设施，涵盖16种代表性路由器，在xRouteBench上验证学习型路由较固定模型基线相对提升14.6%。[Knowing When to Quit (CaRL)](https://arxiv.org/abs/2607.29211) 诊断LLM在超出能力任务上的无效推理现象，通过能力对齐强化学习激励模型在无效推理时主动放弃。分析表明，推理效率优化已从统一的 token 削减转向更精细的计算分配、路由选择和能力边界对齐。

## 模型架构与训练方法

[Full-bandwidth Transformer](https://arxiv.org/abs/2608.08888) 通过潜在反馈机制拓宽自回归Transformer的垂直反馈通道，在1.5倍训练token等效下达到或超越标准Transformer性能，并生成更短的推理链。[Maglev](https://arxiv.org/abs/2608.02870) 提出滑动递归记忆架构，通过预填器和解码器的耦合模型实现固定大小内存，训练时可并行化。[Hybrid-Policy Self-Editing (HPSE)](https://arxiv.org/abs/2608.11660) 针对无结构知识编辑的可组合性问题，提出混合 rollout 策略实现主动自蒸馏。[Massive Activations in HLA LLMs](https://arxiv.org/abs/2608.12149) 系统研究混合线性注意力模型中的大规模激活现象，发现其遵循预注意力尖峰和尖峰间平台两种形态。分析显示，架构创新正从纯注意力机制扩展至反馈通道设计、递归记忆和激活模式理解。

## 安全、公平性与评估

[Low-Frequency Safety Risks in LALMs](https://arxiv.org/abs/2608.09158) 发现大音频语言模型存在低频不可闻信号的安全风险，提出间歇性低频封锁方法使准确率下降达67个百分点，并设计分布重查询守卫缓解该风险。[Gender Bias in MT](https://arxiv.org/abs/2608.08606) 针对英语到罗马尼亚语机器翻译中的性别偏差，提出LLM分类+标签感知的神经翻译管线，在WinoMT基准上提升40个百分点以上。[Rhetoric Reward-Hacking](https://arxiv.org/abs/2608.08975) 分析修辞选择对AI同行评审的影响，发现证据框架和 novelty 立场对评分影响最大，且受评审者初始分数调节。[Instruction Tuning and Confidence](https://arxiv.org/abs/2608.13430) 研究表明指令微调虽然提升推理性能，但也导致词汇多样性下降和过度自信现象。[CW-BASS v2](https://arxiv.org/abs/2608.12773) 针对基础模型教师下置信度饱和问题，提出饱和度感知的伪标签选择方法，在ADE20K上提升1.5 mIoU。[TailBooster](https://arxiv.org/abs/2608.11951) 通过双生成框架处理极端事件预测，使极端到达延误预测的MAE降低29-57%。分析表明，模型评估正从单纯的性能指标扩展至安全边界、公平性、鲁棒性和极端场景覆盖。

## 其他动态

[Specification-first Refactoring Case Study](https://arxiv.org/abs/2608.12440) 报告了一个AI编程智能体在规范优先协议下完成的717k行代码库架构重构案例，涉及189个文件、201个缺陷修正，耗时三天、成本2430美元。[AVA-Encoder](https://arxiv.org/abs/2608.12313) 提出智能体原生视频表示学习框架，将视频转化为知识图谱并通过文本梯度优化实现20.7个百分点的精度提升。[RibAssist 3D](https://arxiv.org/abs/2608.06914) 探索从CT投影中进行肋骨骨折的3D定位，交叉视图对应关系是当前主要瓶颈。