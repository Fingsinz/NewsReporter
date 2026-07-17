# 每日HFDailyPapers-2026年07月17日

## 视频理解与生成：效率、泛化与基准评估

概述方面，视频多模态大模型领域在效率提升与数据泛化上取得显著进展。**VideoChat3** [VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding](https://arxiv.org/abs/2607.14935) 提出了一种完全开源的4B参数视频模型，通过引入膨胀3D视觉Transformer（I3D-ViT）和自适应帧分辨率技术，在降低计算成本的同时提升了跨域泛化能力，其训练数据涵盖通用、长视频及流式视频场景。与此同时，**Wan-Streamer v0.3** [Video = World + Event Stream](https://arxiv.org/abs/2607.15038) 重构了流式交互范式，将视频视为“世界+事件流”，实现了低延迟的全双工视听交互。在生成端，**WanSong v1.0** [WanSong v1.0 Technical Report](https://arxiv.org/abs/2607.14749) 展示了纯扩散模型在长时距、高保真歌曲生成中的优势，支持多语言及双音轨输出。此外，针对视频生成的评估体系也在完善，**KeyFrame-Compass** [KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation](https://arxiv.org/abs/2607.14202) 揭示了当前模型在关键帧忠实度与视频自然性之间的权衡困境，而 **MultiRef-Compass** [MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation](https://arxiv.org/abs/2607.14189) 则建立了多参考音频视频生成的统一评估框架，指出多实体绑定与音视频一致性仍是主要挑战。

分析表明，视频模型正从单一的感知任务向高效、实时且具备强泛化能力的通用系统演进。完全开源生态（如VideoChat3）有助于加速社区迭代，而流式架构（Wan-Streamer）与纯扩散生成（WanSong）代表了不同应用场景下的最优解。同时，基准测试（KeyFrame-Compass, MultiRef-Compass）的精细化表明行业关注点已从“能否生成”转向“生成质量与控制力的平衡”，这对后续模型的结构设计提出了更高要求。

## 智能体强化学习与推理机制优化

在智能体强化学习（RL）与推理优化领域，多项研究致力于解决稀疏奖励、上下文扩展及策略对齐问题。**SEED** [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777) 提出自进化在线策略蒸馏框架，通过将轨迹转化为 hindsight skills 并蒸馏回策略，解决了长期任务中中间决策监督缺失的问题，提升了样本效率。**SearchOS-V1** [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257) 则针对多智能体搜索中的状态追踪难题，设计了显式的上下文管理机制（SOCM）与工具中间件，有效避免了重复搜索循环并提高了吞吐量。在基础模型推理层面，**Partition, Prompt, Aggregate** [Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models](https://arxiv.org/abs/2607.15277) 发现了大型语言模型在概率自洽性上的缺陷，指出细粒度子群体知识未能可靠地聚合到总体估计中，提出了统计自洽性作为新的评估维度。此外，**Demystifying On-Policy Distillation** [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399) 深入剖析了在线策略蒸馏的病态现象，如学生-教师不匹配和长度利用，并通过优势裁剪和日志缩放压缩等轻量级调节手段提升了蒸馏稳定性。

分析显示，强化学习在智能体应用中正从单纯的结果导向转向更精细的过程监督与技能蒸馏。SEED 和 SearchOS 分别通过内部技能提取和外部状态管理优化了智能体的决策质量。与此同时，对 LLM 内在推理机制（如概率自洽性、蒸馏病态）的理论揭示，为构建更鲁棒、更可解释的推理系统提供了关键指导，表明未来的优化重点在于信号质量的调控而非单纯的规模扩张。

## 具身智能与长上下文扩展

具身智能与长上下文处理是本次报告的两大核心技术突破点。**RoboTTT** [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275) 将机器人策略的视觉运动上下文扩展至 8K 时间步，通过引入测试时训练（Test-Time Training）机制，使模型能够压缩历史至权重空间，从而在无需增加推理延迟的情况下实现单样本模仿、在线改进及长程任务完成，性能较基线提升 87%。**LongStraw** [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952) 则聚焦于百万 token 级别的强化学习后训练，通过架构感知的执行栈（如共享提示评估、短分支回放）在固定 GPU 预算下实现了高效的大上下文 RL，验证了其在长轨迹智能体任务中的可行性。此外，**BadWAM** [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207) 警告了世界-动作模型（WAMs）的安全脆弱性，提出了针对此类模型的对抗攻击框架，揭示了模型想象与执行脱节的风险。

分析表明，长上下文能力已成为具身智能和复杂推理的关键瓶颈与突破口。RoboTTT 证明了通过权重空间的上下文压缩可以解锁新的机器人能力，而 LongStraw 解决了大规模 RL 训练的计算效率问题。然而，BadWAM 的研究提醒我们，随着模型处理复杂世界模拟能力的增强，确保动作与预测的一致性至关重要，这为具身智能的安全性评估开辟了新的方向。

## 计算机视觉、3D重建与多模态对齐

在视觉基础模型与3D重建领域，**SUFLECA** [SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment](https://arxiv.org/abs/2607.15058) 提出了一种弱监督的零样本 CAD 对齐框架，通过扩展几何特征学习，实现了亚秒级的物体姿态估计，超越了现有最强基线。**AsySplat** [AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling](https://arxiv.org/abs/2607.10995) 针对长序列场景建模中的计算冗余，设计了非对称架构解耦几何与外观学习，在保持高质量新视图合成的同时实现了近 800 倍的加速。在多模态联合生成方面，**Concurrent Image Understanding and Generation** [Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes](https://arxiv.org/abs/2607.13188) 引入了自我修正耦合马尔可夫跳变过程，实现了图像与文本的同步生成与纠错，提升了联合生成的连贯性。此外，**VIABench** [VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance](https://arxiv.org/abs/2607.14660) 构建了首个面向视障人士辅助的视频基准，揭示了当前 MLLM 在主动提醒和实时响应方面的不足。

分析显示，视觉模型正朝着更高效、更几何一致的方向发展。SUFLECA 和 AsySplat 分别通过特征扩展和架构不对称性解决了特定任务中的精度与效率矛盾。Concurrent Image Understanding and Generation 提出的跨模态耦合机制，为打破理解与生成的界限提供了新思路。VIABench 则强调了多模态模型在社会包容性场景中的应用潜力，指出主动性与实时性是未来研究的重要缺口。

## 模型架构、微调技术与知识库增强

在底层架构与训练技术方面，**DeepLoop** [DeepLoop: Depth Scaling for Looped Transformers](https://arxiv.org/abs/2607.13491) 分析了循环 Transformer 的深度扩展效应，提出了考虑参数访问次数的残差缩放规则，提升了递归深度的稳定性。**MeanFlowNFT** [MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators](https://arxiv.org/abs/2607.15273) 将前向过程强化学习应用于平均速度生成器， bridging 了瞬时速度与平均速度的差距，实现了快速采样下的高性能对齐。**SMALLER** (注：原文未直接提及此缩写，但描述对应 **Smarter and Cheaper at Once**) [Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel](https://arxiv.org/abs/2607.14431) 提出了一种字节精确的 KV 缓存嫁接技术，允许冻结的小模型在不修改权重的情况下注入经过验证的知识，显著提升了推理效率与准确率。**Spectral Rewiring** [Spectral Rewiring for Exploration, Purification, and Model Merging](https://arxiv.org/abs/2607.03065) 则通过谱重连技术提取强化学习更新中的推理核心，去除了干扰成分，促进了多领域能力的合并与纯化。最后，**GRASP** [GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463) 通过强化学习训练智能体自适应协调不同粒度的检索工具，优化了 RAG 系统的上下文管理与推理准确性。

分析表明，模型优化正从单纯的参数规模增长转向更精细的结构设计与知识管理。DeepLoop 和 MeanFlowNFT 分别在架构缩放和生成动力学上提供了理论支撑与实用方法。字节精确的 KV 嫁接和谱重连技术展示了如何在保留原有模型特性的前提下，高效注入新知识或纯化能力，这为低成本部署和模型合并提供了极具潜力的技术路径。GRASP 则体现了智能体在信息检索中自适应控制的重要性。