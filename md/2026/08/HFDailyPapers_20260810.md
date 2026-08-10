

# 每日HFDailyPapers-2026年08月10日

## 端到端自动驾驶与具身导航

基于视频生成先验的端到端自动驾驶方法 SimWAM 被提出，该方法将视频生成作为训练信号，通过联合流匹配训练视频专家与轻量级动作专家，并在训练后移除视频分支，保留独立的轨迹预测规划器[SimWAM](https://arxiv.org/abs/2608.07468)。在无人机图像目标导航领域，提出 UA-NWM 方法，将轨迹评估建模为条件分布外检测问题，通过不确定性子空间表示合理未来轨迹，仅利用无法解释的残差进行评分，降低了推理延迟[UA-NWM](https://arxiv.org/abs/2608.05597)。分析表明，将世界模型作为训练信号而非推理组件的设计思路，以及将不确定性建模引入轨迹评估的机制，共同指向了在具身决策中降低计算开销与提升鲁棒性的技术路径。

## 视频理解与动态场景建模

针对视频世界模型的长程视觉持久性问题，WorldTrace 框架通过为压缩记忆槽分配独立的虚拟位置来保持可寻址性，提出了用于时序连贯性的 Field 压缩与用于情景回忆的 Landmark 存储两种策略[Addressable Memory](https://arxiv.org/abs/2608.07408)。面向连续流式视频理解，StreamArena 基准揭示了当前系统在历史回溯、主动交互与视觉记忆压缩间的权衡困境，并提出了包含独立前端调度与异步后端内存构建的两级架构 StreamMind[StreamArena](https://arxiv.org/abs/2608.05703)。分析显示，对时序一致性与片段级细节保持的关注，反映了当前视频理解向长上下文、高交互复杂度场景扩展时的核心瓶颈。

## 多模态模型训练与表示学习

为提升多模态嵌入模型的区分度与检索效率，DME 模型通过两阶段训练结合大规模对比学习与隐空间证据推理、交叉条件重建机制[Embedding Model](https://arxiv.org/abs/2608.02148)。FATE 方法通过保留帧级序列并在时间轴上严格对齐，在统一的嵌入空间中联合捕捉语义相似性与时间偏移信息[FATE](https://arxiv.org/abs/2608.01310)。针对视觉内容的保护，研究综述了防识别、防训练、防生成、防自动化访问及溯源等五大类对抗性保护技术，并指出现有方法多基于静态或弱适应性对手验证[Adversarial Protection](https://arxiv.org/abs/2608.04314)。分析表明，多模态表示学习正从单一语义匹配向融合时序、推理与安全性保障的多元目标演进。

## 大模型训练效率与扩展性

在 Scaling Law 方面，Skaling 定律通过引入耦合模型容量与数据量的单一交互指数，改善了标准公式在数据稀缺与过训练极端情况下的预测误差[Scaling Law](https://arxiv.org/abs/2608.07222)。针对 LLM 蒸馏的效率问题，离线 Top-K Logits 缓存结合分块 KL 损失的方法在降低内存占用与提升训练吞吐方面显示出显著效果[Knowledge Distillation](https://arxiv.org/abs/2608.03796)。在多任务学习中，研究通过理论与实证对比了 SFT 与 RL 的冲突机制，发现 RL 的梯度方差限制有助于实现任务间的稀疏正交更新，并据此提出了 Parallel-RL 范式[SFT vs RL](https://arxiv.org/abs/2608.03573)。分析表明，对训练成本、资源效率及多任务兼容性的优化，已成为推动大模型可扩展部署的关键研究方向。

## 推理优化、对齐与评估

针对提示压缩中的结构缺陷，研究定义了引用悬空现象，即独立选择机制可能割裂依赖的证据对，并提出通过重新插入缺失的支持段落或使用轻量级分类器进行自动修复[Prompt Compression](https://arxiv.org/abs/2608.04569)。在评估方面，SA-PPG 指标通过分层聚合问题级概率差距，揭示了现有去污染策略对模型恢复能力的过高估计，而 RailCap 策略在抑制记忆方面表现更优[Benchmark Contamination](https://arxiv.org/abs/2608.07341)。针对多轮智能体，SMRC-SD 方法通过在匹配状态进行选择性路由和上下文自蒸馏，缓解了特权参考与当前执行状态不匹配的问题[Agent Distillation](https://arxiv.org/abs/2608.05219)。分析指出，确保推理链的完整性、建立更严格的去污染评估标准以及优化对齐过程的状态匹配，是提升模型可靠性的关键环节。

## 具身智能与多智能体系统

Capek 0.5 模型围绕执行-centric 的能力分类构建，通过强化学习分别获取空间推理、时间理解、动作指导和状态验证四种能力，并通过权重合并与策略蒸馏整合为统一模型[Capek 0.5](https://arxiv.org/abs/2608.06756)。在多模体智能体环境构建中，Ability-aware Environment Selection (AES) 和 Hierarchical Difficulty Curriculum (HDC) 被提出以优化环境多样性与难度结构[Multimodal Agent](https://arxiv.org/abs/2608.03571)。在智能体搜索优化方面，ReASearch 框架将搜索策略内部化，使智能体能自主决定评估、诊断与编辑行为[Reasoning-Driven Search](https://arxiv.org/abs/2608.06714)。分析表明，具身智能正从单一任务处理向具备多阶段执行能力的统一架构发展，同时环境构建与自主搜索机制的优化成为提升智能体泛化能力的重要支撑。

## 模型可解释性、隐私与安全性

在视网膜眼底图像领域，DualIFM 模型采用 BagNet 骨干网络设计，在预训练阶段即通过小感受野生成类证据图，实现了可解释的预测与表征空间可视化[Retinal Foundation Model](https://arxiv.org/abs/2603.18846)。针对激活预言机的可靠性，研究发现经过微调的激活预言机可能出现特定概念的盲区，其失败源于读出路径而非内部表征不可解码[Activation Oracles](https://arxiv.org/abs/2607.23379)。在隐私方面，PrivacyPeek 基准聚焦于智能体在获取阶段而非仅回复阶段的隐私泄露，发现当前基于提示层的防御措施无法有效缓解广泛存在的数据过度获取问题[Privacy Leakage](https://arxiv.org/abs/2606.00152)。分析显示，对模型内部机制的透明性需求，以及对隐私泄露全生命周期（从获取到披露）的审查，正推动可解释性与安全评估方法的深化。

## 其他动态

研究分析了通过行为数据微调的小规模认知模型在心理实验中的表现，发现小规模模型在分布内预测上与大规模模型相当，但在分布外泛化上存在显著扩展梯度[Small Cognitive Models](https://arxiv.org/abs/2608.05224)。针对音频推理的强化学习框架 AudioRubrics，能够根据音频波形动态生成与模型推理路径自适应的细粒度评分标准[Audio Reasoning](https://arxiv.org/abs/2608.02831)。在情感计算领域，OneEmo 模型通过构建包含显式推理轨迹的多任务数据集及统一多任务奖励分配的强化学习策略 Emo-Chord，实现了情感感知、理解与交互的统一[OneEmo](https://arxiv.org/abs/2608.06013)。此外，针对生产环境中 AI 生成 C++ 代码的实证研究指出，此类代码存在更高的接口耦合负担与资源消耗，但提供分类学反馈可显著降低静态分析警告[Production Code Quality](https://arxiv.org/abs/2608.06640)。测试时训练方法的模块化框架 Modular TTT 通过系统消融揭示了学习率初始化、权重衰减等组件的作用[Modular TTT](https://arxiv.org/abs/2608.07110)。YOLO-PEFT 框架将适配器放置建模为可审计的约束规划问题，在 YOLO 系列中实现了参数高效微调[YOLO-PEFT](https://arxiv.org/abs/2608.07051)。通过成语图像对构建的 C4 评估框架揭示了当前多模态大模型在跨概念创意解码能力上存在显著差距[C4 Evaluation](https://arxiv.org/abs/2608.06501)。针对扩散模型长程推理误差的自监督评估，Round-Trip Consistency 方法利用双向预测的往返差异作为 rollout 误差的代理[Round-Trip Consistency](https://arxiv.org/abs/2608.00675)。研究还分析了人格条件智能体在经历生活事件后的人格演化轨迹，发现当前模型仅能模拟人类人格动态的平均值而非其形状[Personality Evolution](https://arxiv.org/abs/2608.06485)。