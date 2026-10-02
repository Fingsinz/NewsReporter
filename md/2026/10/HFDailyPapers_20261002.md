

# 每日HFDailyPapers-2026年10月02日

## Agent Harness 与课程学习优化

**概述**
ActiveSaddler 提出将训练课程自动化作为 harness 优化的新维度，将演进的课程建模为非平稳 bandit，通过抽象失败模式为 arms 并动态调整优先级，使课程与 harness 共同进化。在 GAIA2 和 Terminal-Bench 2.0 上分别提升 Pass@1 达 4.4 和 7.5 个百分点。

**分析**
该研究揭示了现有 harness 优化方法仅关注更新策略而忽略场景选择的问题，提出课程学习应与 harness 协同演化的思路。实验表明动态构建优化目标、评估其效用及平衡已知弱点与未知探索是性能提升的关键因素，为 agent 训练效率优化提供了新的技术方向。

## 流式视频理解与记忆机制

**概述**
OneStreamer 通过共享的主动生成过程联合学习查询无关的证据记录与任务响应，引入 PHCM 生成时间定位的局部细节描述与事件摘要，并采用 PSTL 减少重复等待状态的主导性，构建了 OneStreamer-1M 数据集。同时，LoCI 提出混合空间记忆架构，在部分 transformer 块中保持 KV 缓存、在其余块中使用基于投影相机几何的条件化循环线性注意力记忆。Memorizon 通过检索共享银行的方式解耦长跨度监督与注意力成本，实现超越上下文窗口的世界模型训练。

**分析**
流式视频理解的核心挑战在于如何在保留历史证据与维持实时感知之间取得平衡。上述方法表明，将记忆机制与生成过程耦合、利用空间/几何约束进行记忆寻址，以及将检索与注意力解耦，均可有效缓解历史信息的遗忘问题。这些设计为长视频理解与流式世界模型提供了可扩展的架构范式。

## 语言模型 Agent 的信念状态与意图管理

**概述**
PoS 提出推理时框架，构建并持续维护显式信念状态作为 agent 的决策上下文，结合当前世界状态估计与未完成任务需求，检测 Belief Trapping 并提供针对性恢复策略。IntentFlux 则研究多轮交互中用户意图漂移问题，提出 StateForge 框架显式维护活跃需求以缓解过时意图对最终输出的影响。

**分析**
两类研究均指向 agent 在复杂多轮任务中的状态跟踪瓶颈。PoS 从信念建模角度提供结构化上下文管理方案，IntentFlux 从意图演化角度量化漂移影响并提出修复机制。分析表明，将隐式历史压缩转化为显式状态维护是提升 agent 可靠性的有效路径，但状态估计误差仍解释部分性能差距，状态重建精度有待进一步优化。

## 扩散语言模型与连续生成

**概述**
HC-DLM 将离散 token 生成与连续潜在轨迹耦合于统一去噪过程，通过变分界推导训练目标，在 Sudoku、Countdown 和 LM1B 上分别优于离散和连续扩散基线。Scaling and Distilling Text Embeddings 研究文本嵌入对连续扩散生成质量的影响，发现将 T5Gemma-2 蒸馏为学生编码器可形成更连通、更具扩散性的潜在空间。E-MoE 提出增强型混合专家架构，在离散共享潜在变量上构建混合分解分布的反向过程，改善少步生成质量。

**分析**
扩散语言模型的核心挑战在于平衡离散 token 的统计依赖与连续去噪的平滑性。HC-DLM 通过联合建模实现 token 读取与潜在更新的双向反馈，Distilling Text Embeddings 则从潜在空间几何角度优化生成可扩散性。技术趋势表明，连续扩散模型的有效性取决于嵌入空间的连通性与去噪器对离散结构的感知能力，混合专家路由为保留位置间相关性提供了参数量可控的解决方案。

## RL 后训练与奖励机制

**概述**
Sharpening Tax 提出诊断指标量化 RL 后训练导致的测试时可伸缩性损失，发现后训练将任务推向"始终解决"或"永不解决"的两个极端，并提出 PTGS 贝叶斯采样器自适应调整采样温度。Make Sparse Rewards Count 研究多奖励 RL 中的奖励贡献不均衡问题，提出密度感知奖励聚合（DARA）方法，通过逆平方根密度校正增强低频激活奖励的信号。CorrGRPO 将成对协方差归一化为 Pearson 相关系数，平衡不同尺度奖励的影响。

**分析**
后训练的 Sharpening Tax 现象揭示了单样本准确率提升与多采样覆盖率下降之间的权衡关系，提示 agentic 任务可能因多轮工具交互而受益于保留的探索能力。多奖励优化方法表明，奖励间的协方差结构直接影响优势估计的尺度，基于密度或相关性的自适应加权可有效缓解信号失衡。技术趋势指向更精细的奖励耦合建模与测试时计算预算的动态分配。

## 世界模型与视频生成控制

**概述**
World Observer 将观察与行动解耦，通过全景观察者在 actor 视野外维持目标对象的视觉演化。4Director 使用显式 4D 场景表示，每个对象从输入图像重建为规范网格并通过刚性变换移动，引入 Motion Adapter 将几何脚手架转化为视频。Honeycomb 提出 HexMemory 固定大小场景记忆，通过 warped 平面融合实现恒定存储的世界模型。

**分析**
视频世界模型的一致性保持依赖于对视野外对象状态的有效建模。上述方法分别通过多视角解耦、刚性几何约束和固定大小记忆实现这一目标。数据显示，4Director 在视觉质量和相机控制上优于现有方法，World Observer 显著改善视野外动态一致性。技术趋势表明，将几何先验显式编码为生成条件，以及将记忆结构与生成过程统一优化，是提升长程视频一致性的有效方向。

## 视频生成评估与文本渲染

**概述**
PROWBench 提供 170 个程序化构建的场景和 600 个代理视频，评估视频模型对程序指定事件的视觉遵循度，引入 Logic-Render Alignment 和 Interaction Success Rate 等 VLM 指标。VTR-Bench 针对视频生成中的文本渲染能力，构建 300 个提示 spanning 五个场景类别，Best 模型的整体词错误率达 0.250。

**分析**
视频生成评估正从视觉质量向语义一致性和程序遵循度扩展。PROWBench 通过可重放的 world record 实现细粒度事件验证，VTR-Bench 揭示现有模型在场景文本渲染上的普遍困难。分析表明，程序化场景与可执行验证的结合为 video world model 评估提供了更严谨的基准，文本渲染准确性仍是视频生成模型的关键短板。

## GUI Agent 与轨迹生成

**概述**
AutoGUIWorld 结合图像生成器的视觉先验与规划器的任务知识，合成 GUI 交互轨迹而无需部署真实软件环境，生成 79,266 个跨 Ubuntu、Windows、macOS 和 Chrome 的空间标注训练样本。Fine-tuning Qwen3.5-35B-A3B 在 OSWorld 上将平均任务得分从 33.0% 提升至 40.8%，在 ScienceBoard 上成功率从 14.0% 提升至 32.2%。

**分析**
GUI agent 的数据瓶颈在于真实交互轨迹的多样性受限与部署成本高昂。AutoGUIWorld 通过图像编辑迭代生成后续观察，利用规范化的界面状态描述和原子动作映射实现高质量合成数据。结果显示合成轨迹可显著改善 agent 在真实桌面和科学任务上的表现，表明视觉生成器与规划器的结合可有效扩展 agent 训练数据的覆盖范围。

## 多模态嵌入与统一生成

**概述**
Omni-Embed-Mini 以 0.9B 参数将文本、语音、音频、图像、视频和视觉丰富文档映射到统一余弦空间，保持文本侧参数完全冻结。Multimodal Flow 提出完全连续的生成架构，将文本块和图像组织为有序连续超块，通过共享 chunk-causal flow backbone 学习单一向量场。

**分析**
多模态统一表征的核心挑战在于模态间对齐与模态内结构的保持。Omni-Embed-Mini 通过冻结骨干网络和级联 caption 教师信号实现零文本退化，Multimodal Flow 则通过连续超块组织避免视觉量化瓶颈。分析表明，完全连续建模虽避免模态依赖目标但需解决空间结构的有序性，而蒸馏方法可在不更新文本参数的条件下实现模态绑定，为轻量化多模态系统提供了可行路径。

## 解码优化与推理效率

**概述**
LoopCD 利用循环 Transformer 中间状态提供弱-强预测对，在 logit 空间和隐藏状态空间分别实现对比解码，减少 22.5%-48.2% 前向 FLOPs 的同时提升性能。AgSpec 为 coding agent pipeline 提供检索式投机解码，从会话、工作区和全局语料库检索，提升生成吞吐量最高 4.76 倍。HeteroFold 实现跨模型家族的预填充自由 KV 缓存转移，在 32K 上下文长度下实现 10.7 倍加速。

**分析**
推理效率优化从模型结构利用和跨模型协同两个维度展开。LoopCD 挖掘 recurrent 结构的内在一致性，AgSpec 针对 agent 重复生成代码的模式优化检索策略，HeteroFold 解决异构模型的缓存对齐问题。数据表明，利用生成过程中的冗余结构（循环层、agent 轨迹、发送方上下文）可显著降低重复计算，跨模型知识复用为多 agent 系统的通信开销优化提供了新路径。

## 机器人操作与技能学习

**概述**
InterEvolve 通过 LLM agent 修订 reward program 结构并结合数值优化调整常量，释放 humanoid 控制器已有的 loco-manipulation 能力。PyRUA-Lean 结合反馈驱动的基元组合与选择性观察，在同等 LLM 调用预算下将成功率从 63.1% 提升至 71.7%，减少 65% 输入 token。DexPolicy 将探索尺度显式建模为训练步数的函数，在真实机器人上 Target 成功率从 25.0% 提升至 85.0%。OTRetarget 通过最优传输联合重映射机器人和对象运动。

**分析**
机器人技能学习正从端到端策略训练转向能力复用与测试时适应。InterEvolve 表明预训练控制器的 competence 可通过 reward program 演化被释放，PyRUA-Lean 通过结构化执行降低 token 开销，DexPolicy 强调探索调度对操作精度的关键影响。分析表明，将规划与控制在测试时解耦、通过可验证的 reward program 而非重训练适应新任务，以及精细控制探索规模，是提升机器人学习效率的有效方向。

## 工具使用与 Agent 评估

**概述**
KaliBench 提供 8,504 个自然语言到 CLI 命令对，覆盖 1,642 个工具，无开放权重模型在宽松设置下超过 42% 精确命令准确率。Argo-Bench 构建纽约市外卖平台模拟环境，包含 235 张表和 75 亿行数据，最强模型仅在 34.8% 任务上得分 95 分以上。Omniseek 通过多轮工具使用协议实现跨模态证据检索，构建 OmniTraj-170K 数据集并采用可验证奖励的 RL 优化。

**分析**
工具使用评估正从知识问答向可执行命令生成和企业级工作流推进。KaliBench 揭示 CLI 精确性的极端难度，Argo-Bench 表明多表推理和动作执行仍是 agent 的显著瓶颈。Omniseek 的跨模态证据检索表明工具调用本身可作为推理过程的一部分而非事后补充。数据指向 agent 评估需同时考虑语义正确性、执行可行性和多步骤协调能力，开放权重模型在工具精确使用上仍存在显著差距。

## 多智能体工作流与技能优化

**概述**
FloWright 通过层次化结构感知奖励范式实现多角色工作流的自进化和协同进化，在六种任务类型上取得最高 +7.41% 性能提升，协同进化多角色比单角色优化增益更大。InFlowOp 提出无标签流内成本度量，双向决定任务分解粒度和智能体分配，并在执行中通过最廉价修复纠正故障。Prompt2Skill 从自然语言任务描述构建技能，通过闭源循环发现/合成数据集并迭代优化。

**分析**
多智能体工作流优化正从固定模板向动态自适应演进。FloWright 的协同进化表明角色间耦合可通过结构化奖励实现联合优化，InFlowOp 的流内定价将构建与运行时优化统一。Prompt2Skill 则展示无需训练数据的技能自动构建路径。分析表明，工作流优化需同时考虑结构感知、成本约束和数据可用性，无标签优化和自然语言驱动的方法降低了技能工程门槛。

## 物理智能与感知评估

**概述**
PhysVista 通过感知-推理-评估闭环评估 VLM 的物理智能，区分事件级和尺度级推理。EgoTools 提供 100 小时工具中心第一人称视频和 1,000 个诊断 QA 对，覆盖从感知到因果推理的四个轨道。BeyondSCe 通过事件先验和当前几何结合选择摄像机视角实现事件引用抓取，在遮挡目标上达 77% 成功率。HIDE 基准评估部分可观测操作中的技能级记忆。

**分析**
物理智能评估从单一视觉理解向多阶段认知闭环扩展。PhysVista 揭示 VLM 在物理合理性和动态推理上的显著缺陷，EgoTools 表明工具使用推理仍是多模态模型的薄弱环节。BeyondSCe 和 HIDE 则从机器人操作角度验证事件引用和记忆维持的重要性。数据表明，物理智能需同时满足感知准确性、推理一致性和评估可行性，当前模型在因果链条和隐藏状态维持上仍存在系统性不足。

## 其他动态

ScholarCatalyst 基准显示代理搜索在文献检索任务上与嵌入检索表现相当（0.42 vs 0.48 Recall@20），揭示专家直觉搜索能力的训练缺口。[ScholarCatalyst](https://arxiv.org/abs/2610.02202) SAKIKO 审计框架表明行为移动不等于修复，+55 净增益干预可能破坏过半基线正确决策。[SAKIKO](https://arxiv.org/abs/2609.36138) Where-OPD 通过合成场景的空间指导实现 MLLM 的自蒸馏，在五个真实世界基准上平均提升 3.23 分。[Where-OPD](https://arxiv.org/abs/2610.02117) JevSpawn 将自然语言动作空间与有限域概率探索结合，通过并行动作生成和反馈驱动分支选择提升 agent 推理效率。[JevSpawn](https://arxiv.org/abs/2610.00437) RouteFM 和 FlexRouter 分别探索路由的基础模型化和互补性建模，前者通过行为上下文泛化跨环境路由，后者利用 DPP 优化答案覆盖率。[RouteFM](https://arxiv.org/abs/2609.37362)[FlexRouter](https://arxiv.org/abs/2609.38585) SAGO 框架在多个行为轴上测量 LLM 泛化不稳定性，发现跨数据集变化可反转模型排名。[SAGO](https://arxiv.org/abs/2610.01428) NEEDLE 方法通过权重正交化实现免训练的后门去除，在代码注入攻击上达 0% 成功率且保持能力安全无损。[NEEDLE](https://arxiv.org/abs/2610.00348) VGBench 诊断音频 LLM 的声学前置门控能力，发现模型在speaker-switch场景下 mute 率仅 14%。[VGBench](https://arxiv.org/abs/2609.32536) DMM 通过离散迭代意图精炼实现去中心化多智能体路径规划，在 MovingAI 基准上解决 1,598/1,600 任务并扩展至百万级智能体。[DMM](https://arxiv.org/abs/2609.32019) OpenTumorBoard 从 YouTube 录制提取 611 病例和 19,157 讨论轮次，最佳模型在临床等效性上得分 3.43/5。[OpenTumorBoard](https://arxiv.org/abs/2609.32810) RLE-Bench 评估 coding agent 作为机器人学习工程师的能力，覆盖交互控制、策略学习、感知估计和机械设计四个工作流。[RLE-Bench](https://arxiv.org/abs/2609.34210) X-Tree 从数据中恢复动作层次结构并训练于 offline RL、online RLVR 和 on-policy 自蒸馏三种设置。[X-Tree](https://arxiv.org/abs/2609.32993) SemanticTok 通过冻结 DINO 特征和轻量重建头实现灵活视频 token 化，201M 模型匹配 3.4 倍大小基线性能。[SemanTok](https://arxiv.org/abs/2610.00686) PixelDense 将 SAM2、Depth Anything v2 等密集预测模型作为 REPA 目标，通过语义/几何双流路由和正交惩罚提升像素扩散质量。[PixelDense](https://arxiv.org/abs/2610.00483) Latent-Foresight 联合学习潜在 token 器和流生成动力学，消除两阶段管道的表示-预测解耦。[Latent-Foresight](https://arxiv.org/abs/2610.01942) PEARL 耦合多模态推理器与冻结图像生成器，通过 reason-reflect 循环实现基于用户历史的个性化图像生成。[PEARL](https://arxiv.org/abs/2610.00737) GraphForge 通过证据图将任务声明和评估标准锚定于真实文件，fine-tuning Qwen3.6-27B 在 Workspace-Bench-Lite 和 SpreadsheetBench II 上分别提升 7.7 和 13.7 分。[GraphForge](https://arxiv.org/abs/2609.38923) PPT 通过平行退火解决 power-sharpened 采样的探索-利用权衡，在有限计算预算下实现优于 RL 后训练的推理时推理增强。[PPT](https://arxiv.org/abs/2609.38104) APPL 将策略结构先验作为技能接口，实现 compositional 和 skill 泛化的统一。[APPL](https://arxiv.org/abs/2609.35690) Tex-Zero 证明仅用 2D 图像即可训练高保真原生 3D 纹理生成模型。[Tex-Zero](https://arxiv.org/abs/2609.34621) SECRET 通过问题中继 steering 缓解 AVLLM 的源混淆接地幻觉，在 CMM 和 AVHBench 上分别提升 18.0 和 7.1 个百分点。[SECRET](https://arxiv.org/abs/2609.37568) DataMagic 通过声明式多智能体编排从原始表格数据自动生成数据视频，效率提升 79.7%。[DataMagic](https://arxiv.org/abs/2609.33403) Architect-Ant 通过 GRPO 优化和布局规则评分生成可编辑的建筑平面家具布局。[Architect-Ant](https://arxiv.org/abs/2606.10953) AutoDataBench 隔离数据智能评估，发现 LLM 对训练数据干预的效果推理仍存在局限。[AutoDataBench](https://arxiv.org/abs/2609.40097) FAR 通过未来感知预测监督训练检索器，自动决定信任哪些检索线索。[FAR](https://arxiv.org/abs/2609.34677) N-OPSD 通过邻域参数扰动构建专家池，在线路由分离锚定方向与支持强度，在数学推理基准上提升 1.67-2.75 分。[N-OPSD](https://arxiv.org/abs/2609.39687) Smaller Models Better Rejects 发现较小冻结模型生成的 rejects 可训练更强学生，优于自生成 rejects。[Rejects](https://arxiv.org/abs/2609.38987) ATR 通过单调对齐建立帧级唇部表示与音素单元的对应，提升配音质检能力。[ATR](https://arxiv.org/abs/2610.00825) TAI 方法提取时序发散向量的峰值层并重新注入后续层，无需训练即可改善 VideoLLM 的时序推理。[TAI](https://arxiv.org/abs/2610.01595) KorGRPO 通过 Pearson 相关归一化平衡多奖励影响，在代码生成和工具调用上取得提升。[KorGRPO](https://arxiv.org/abs/2609.36820) DARA 通过逆平方根密度校正实现自适应多奖励聚合，工具调用格式合规提升 26% 训练步数效率。[DARA](https://arxiv.org/abs/2610.00574) RPTune 耦合 learned catalog curation 与 LLM 后训练，搜索精度提升最高 31.4 个百分点。[RPTune](https://arxiv.org/abs/2610.00964) EgoTools 数据验证显示 SFT 将 Qwen3-VL-8B 在工具使用理解基准上从 50.0% 提升至 60.9%。[EgoTools](https://arxiv.org/abs/2609.39378) HIDE 基准评估揭示现有策略在部分可观测操作记忆任务上的显著局限。[HIDE](https://arxiv.org/abs/2609.38886) R2T 提供预置可执行检查的 Scientific Computing agent 评估，工具组在 30 个任务中完成 29 个。[R2T](https://arxiv.org/abs/2610.00313) Adaptive Reward Routing 通过跨模态影响引导的路由和偏好保留的重加权实现联合音频视频扩散模型的 RL 优化。[ARR](https://arxiv.org/abs/2609.37200) RASO 通过检索增强技能初始化和更新实现 cross-harness 技能迁移。[RASO](https://arxiv.org/abs/2609.38024) Control Decoding Attacks 通过采样分布重建和风险门控残差控制实现黑盒 LLM 的 jailbreak。[CDA](https://arxiv.org/abs/2609.36956) Keyword Harnesses 诊断显示 661M 和 1.1B 模型在宽松指标上得分相近，但 verbatim 检查揭示后者完全无法生成有效工具调用。[KH](https://arxiv.org/abs/2610.02142)