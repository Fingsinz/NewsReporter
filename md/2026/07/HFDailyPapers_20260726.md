# 每日HFDailyPapers-2026年07月26日

## 深度研究与智能体自主改进机制

概述： AREX 提出了一种递归自我改进（RSI）的深层研究代理框架，通过交替执行内部证据收集循环和外部约束审计循环来提升答案质量。该模型引入了自动上下文更新工具以压缩交互历史，并结合中等规模预训练与长程强化学习进行训练，在 BrowseComp、HLE 等基准测试中显著优于同等规模的基线模型 [AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461)。此外，OpenForgeRL 提供了一个开源框架，旨在解耦推理与训练过程，允许在任意环境和使用现有推理解析器（如 Claude Code, OpenClaw）的情况下对智能体进行端到端强化学习训练，验证了其在 GUI 和工具使用任务上的高效性 [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557)。

分析表明，将“发现-验证”的非对称性转化为递归优化动力是提升复杂推理能力的关键路径。通过保留经过验证的证据状态并针对性地解决未决约束，模型能够有效克服长程规划中的稀疏奖励问题。同时，OpenForgeRL 揭示了当前智能体训练的基础设施瓶颈，即专用训练框架往往无法原生支持商业或复杂的推理解析器。这种解耦设计使得研究者能够在真实部署环境中直接优化智能体行为，为提升智能体的可靠性和自我验证能力提供了标准化的基础设施支持。

## 教育场景与大语言模型认知评估

概述： K12-KGraph 构建了源自官方教材的知识图谱，并据此推出了 K12-Bench 和 K12-Train 数据集，专门用于评估和训练模型对课程知识结构和视觉呈现的理解能力。实验显示，尽管主流模型在该基准上表现有限，但针对领域数据的监督微调显著缩小了差距，且文本与视觉监督具有互补性 [K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs](https://arxiv.org/abs/2605.09635)。另一方面，LLMs Get Lost in Evolving User Intent 的研究指出，现有的单轮静态评估无法反映智能体在处理用户意图动态演变时的缺陷，导致模型在协作场景中表现出显著的意图追踪失效 [LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734)。

分析认为，教育领域的 AI 应用正从单纯的答案生成转向对知识结构深层认知的考察。K12-KGraph 的工作强调了将显式课程逻辑融入训练数据的有效性，证明了结构化先验知识对提升特定领域推理的重要性。而在通用对话智能体方面，研究揭示了当前评估范式的局限性：静态基准掩盖了多轮交互中意图漂移带来的性能衰减。这表明未来的智能体系统需要引入动态意图建模机制，并在更具动态性的多轮交互基准上进行持续评估和优化，以适应真实的人机协作需求。

## 视频生成、空间认知与多模态表达

概述： SANA-Video 2.0 采用混合线性注意力架构，在保持高效线性缩放的同时恢复了全 softmax 注意力模型的表达能力，实现了在单 GPU 上快速生成高质量视频 [SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation](https://arxiv.org/abs/2607.21553)。GraphVid 则引入了基于交互图的视频生成方法，通过结构化语义接口实现更精确的多主体控制，并在多个质量控制指标上优于传统运动控制方法 [GraphVid: Interactive Graph-Controllable Video Generation](https://arxiv.org/abs/2607.21580)。在评估方面，ProVisE 提出了一个协议化视觉评估框架，使图像生成模型能够直接在像素空间中提供空间答案，从而更准确地衡量其空间认知能力，结果显示图像生成模型在像素级表达上具备与文本视觉语言模型竞争的潜力 [Show, Don't Tell: Evaluating Spatial Cognition in Generative Pixels Rather Than LLM Text](https://arxiv.org/abs/2607.21072)。

分析显示，视频生成的技术趋势正趋向于在计算效率与长序列建模能力之间寻求平衡。SANA-Video 2.0 通过周期性门控 softmax 锚点解决了纯线性注意力丢失全局信息的问题，证明了混合架构在保证质量的同时大幅降低推理成本的可行性。同时，GraphVid 表明结构化控制信号比单一的像素运动掩码更适合复杂场景的多主体交互控制。ProVisE 的发现挑战了传统的文本输出评估范式，指出对于图像生成模型而言，利用其原生的像素输出能力进行空间推理评估能更真实地反映其理解物理世界的能力，这暗示了未来多模态评估应更加重视输出模态本身的特性而非强制统一为标准符号。

## 机器人感知、导航与操作数据

概述： TableVerse 建立了一个从非结构化网络图像自动重建高保真、物理一致的桌面环境的 Real2Sim 流水线，并发布了包含 10 万个环境及其对应操作轨迹的数据集，旨在解决具身智能训练中缺乏大规模真实数据的问题 [TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation](https://arxiv.org/abs/2607.21017)。Robostral Navigate 是一款仅需单目 RGB 图像即可预测下一个目标位置点的 8B 视觉语言模型，通过在模拟场景中生成大量轨迹并使用前缀缓存训练技巧，它在 R2R-CE 和 RxR-CE 导航基准上取得了新的最先进水平 [Robostral Navigate](https://arxiv.org/abs/2607.20785)。ReferTrack 提出了一种“先指认后跟踪”的具身视觉跟踪范式，通过维护边界框的时间队列和特定的视觉指示符，在单摄像头设置下实现了高精度的具身跟踪 [ReferTrack: Referring Then Tracking for Embodied Visual Tracking](https://arxiv.org/abs/2607.20061)。

分析指出，具身智能的发展高度依赖于感知与行动的解耦设计及高质量数据的供给。TableVerse 的价值在于填补了从自然场景到仿真操作演示之间的数据鸿沟，其物理一致性确保了策略泛化的可靠性。Robostral Navigate 则展示了纯视觉流控制策略在传感器假设最小化方面的优势，摆脱了对深度或多相机的依赖，提升了硬件部署的灵活性。ReferTrack 进一步细化了跟踪任务中的表征方式，证明将抽象的空间推理转化为具体的图像空间检测能显著提升训练的可用性与迁移效果。这些工作共同表明，简化传感器输入要求并构建严格对齐的感知-行动闭环是提升机器人系统鲁棒性的关键方向。

## 模型训练效率、蒸馏与新表征学习

概述： Visual Contrastive Self-Distillation (VCSD) 提出了一种无需特权标签或外部教师的自蒸馏方法，通过对比含图与去图输入下的教师分布差异来生成更锐利的学生目标分布，在 Qwen3-VL 系列模型上显著提升了性能 [Visual Contrastive Self-Distillation](https://arxiv.org/abs/2607.21556)。Sample-Efficient Learning from Agent Experience 提出了经验蒸馏（Experience Distillation）概念，能够在不产生额外环境交互的前提下，利用上下文蒸馏将智能体的交互历史内化为权重，相比直接监督微调保留了大部分上下文学习收益 [Sample-Efficient Learning from Agent Experience](https://arxiv.org/abs/2607.21051)。Multi-Turn On-Policy Distillation with Prefix Replay (ReOPD) 通过复用预先收集的教师轨迹作为回放前缀，解决了多步操作中分布偏移和教师不可靠的问题，实现了比传统在线蒸馏快 4 倍以上的训练速度 [Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/abs/2607.04763)。Dataset Distillation by Influence Matching (Inf-Match) 从结果中心视角出发，通过样本级的影响估计器匹配真实数据集对最终参数的影响，在分类及视语言任务上超越了过程匹配的蒸馏方法 [Dataset Distillation by Influence Matching](https://arxiv.org/abs/2607.16859)。此外，Recurrent Sinusoidal INRs 利用正弦激活的谐波谱特性，通过迭代精炼隐式神经表示，以更少的参数实现了更高的图像和 3D 重建保真度 [Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation](https://arxiv.org/abs/2607.21485)。

分析认为，当前大模型训练的核心痛点已从单纯的算力扩展转向数据利用效率与训练稳定性的优化。VCSD 和相关蒸馏研究证实了通过构造合理的对比信号（如视觉内容存在性、轨迹前缀可靠性），可以在不增加标注成本的前提下显著提升小模型或学生模型的泛化能力。经验蒸馏与前缀重放技术的结合，实质上是打通了上下文学习与权值内化之间的壁垒，为低成本部署提供了新路径。Inf-Match 则标志着数据集蒸馏从模仿训练过程向对齐最终学习效果的范式转变，通过直接优化最终参数的一致性，减少了因过程误差累积导致的性能下降。这些进展共同指向了更高效、更可解释且资源消耗更低的模型演进路线。