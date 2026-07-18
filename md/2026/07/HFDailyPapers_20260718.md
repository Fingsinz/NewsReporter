# 每日HFDailyPapers-2026年07月18日

## 长上下文与强化学习训练效率优化

LongStraw 提出了一种针对百万级 Token 上下文的架构感知执行栈，旨在固定 GPU 预算下实现高效的强化学习后训练 [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952)。该方法通过评估共享提示时不保留自动微图、仅保留后续 Token 所需的模型状态以及单支回放短响应分支，显著降低了训练图的显存占用。实验显示其在 Qwen3.6-27B 和 GLM-5.2 模型上能处理高达 4.46M 位置的输入，建立了在固定算力下扩展 RL 训练上下文长度的执行能力基准。这表明解决推理上下文与 RL 训练上下文之间的差距，对于提升 AI Agent 在长轨迹任务中的表现至关重要，尽管目前尚处于验证执行容量阶段，尚未完全解决分布式梯度合成的完整性问题。

## 视频理解与多模态大模型

VideoChat3 是一个完全开源的高效通用视频多模态大模型，旨在解决现有开源模型在泛化性、计算效率和开放性方面的不足 [VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding](https://arxiv.org/abs/2607.14935)。该模型引入了膨胀 3D 视觉 Transformer (I3D-ViT) 和自适应帧分辨率技术以提升时空表示效率，并通过可扩展的数据合成管道构建了涵盖通用、长视频和流式视频的高质量数据集。仅有 4B 参数的 VideoChat3 在多个基准测试中超越了参数量更大或相等的开源模型，实现了广泛泛化与计算效率的平衡。这一进展表明，通过架构创新与高质量数据合成的结合，轻量级模型同样可以在视频理解领域达到先进水平，且完全开源有助于推动社区复现与迭代。

Wan-Streamer v0.3 重构了原生流式交互模型，将视频视为“世界”与“事件流”的组合，从而支持实时全双工音视频交互 [Video = World + Event Stream](https://arxiv.org/abs/2607.15038)。在该框架下，“世界”代表稳定的环境上下文，而“事件流”包含随时间变化的行为和语音，模型据此预测世界的实时响应。该系统保持了低延迟特性（约 200ms 模型侧响应），展示了将视频生成模型转化为实时互动引擎的潜力。这种范式转移使得模型能够像人类一样在动态环境中进行持续的感知-行动循环，为构建具备实时交互能力的智能体提供了新的技术路径。

## 具身智能、机器人控制与世界模型

RoboTTT 引入了测试时训练（Test-Time Training）机制，将机器人的视觉运动上下文扩展到 8K 个时间步，比现有策略高出三个数量级 [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275)。通过将在训练和推理期间通过梯度下降更新快速权重的递归状态，RoboTTT 能够将历史压缩到权重空间中，从而实现一次性模仿学习、在线策略改进以及对扰动的鲁棒性。在真实机器人操作任务中，其性能较单步上下文基线提升了 87%，并成功完成了此前无人能完成的五阶段组装任务。这确立了上下文长度作为机器人基础模型新的缩放维度，表明延长推理时的历史视野能显著提升复杂长程任务的解决能力。

RxBrain 是一个具备联合语言-视觉推理与想象能力的具身认知基础模型，旨在连接高层任务推理与物理状态 [RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination](https://arxiv.org/abs/2607.14187)。不同于仅关注场景理解或未来视觉预测的模型，RxBrain 在一个统一的规划序列中结合语言的抽象结构与视觉想象的物理 grounding，支持语言、图像和视频的理解与生成。通过自动化的具身视频分解管线进行训练，RxBrain 在连续机器人动作生成中表现出良好的现实性能，无需大规模动作数据预训练。这为发展能够同时处理逻辑规划与物理世界模拟的具身智能基础模型提供了初步验证。

BadWAM 揭示了世界-动作模型（WAMs）中存在的脆弱性，提出了一种名为 BadWAM 的统一框架来建模和评估特定的对抗攻击 [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207)。该攻击利用微小的视觉扰动破坏 WAM 中“想象未来”与“执行动作”之间的对齐，分为直接导致任务失败的行动攻击和保持想象合理性但执行错误操作的隐身攻击。实验显示，行动攻击将模型成功率从 96.5% 降至 43.1%，暴露了 WAM 在闭环执行中的安全隐患。这表明仅凭未来状态的合理性不足以保障具身系统的安全，必须加强动作执行与预测之间的鲁棒性对齐。

## 代理智能体、检索增强生成与工具使用

SEED 提出了一种自我演化的在线策略蒸馏框架，用于解决基于结果的强化学习中稀疏奖励导致的监督缺口 [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)。该框架将完成的在线轨迹转化为事后技能，并通过策略模型自身提取这些技能以生成密集的令牌级蒸馏信号，与基于结果的 RL 联合优化。实验表明，SEED 在文本和视觉代理任务中均提高了性能和样本效率，且具备对未见场景的鲁棒泛化能力。代码已开源。这种方法通过让策略模型同时作为收集者和分析师，实现了监督信号的自我进化，有效弥合了 episode 级别结果与 token 级别决策之间的鸿沟。

SearchOS 是一个面向开放域信息搜索的多代理系统级框架，旨在解决代理在长交互历史中难以追踪任务进度及陷入重复循环的问题 [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257)。通过外部化搜索状态至前沿任务、证据图、覆盖图和失败记忆，并结合流水线并行调度机制，SearchOS 能够持续填充未解决的覆盖缺口以提高吞吐量。此外，搜索工具中间件截获模型交互记录证据并防止重复失败模式。在 WideSearch 和 GISA 基准上，SearchOS 在所有指标上优于现有的单代理和多代理基线。这证明了显式状态管理和并行调度对于提升复杂信息搜索代理的稳健性和效率至关重要。

GRASP 是一个用于训练代理检索增强生成（RAG）的强化学习框架，使代理能够自适应地协调语义搜索、关键词搜索和段落阅读等互补检索工具 [GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463)。通过联合考虑答案准确性、接地阅读、互补搜索和回合效率的奖励函数，GRASP 训练出的策略学会了可解释的浏览和扫描行为：使用语义搜索进行广泛探索，段落阅读进行局部验证，关键词搜索进行实体特定证据查找。在多跳推理基准测试中，GRASP 提高了检索召回率和下游问答性能。这表明在代理推理中动态控制上下文粒度并协调多种检索信号，对于减少无关令牌干扰和提升推理正确性具有关键作用。

## 视觉推理、评估基准与生成质量

HDR (Hierarchical Denoising For Multi-Step Visual Reasoning) 提出了一种分层去噪框架，旨在解决视频模型在流式自回归扩散模型推理成本高与双向扩散模型推理延迟高之间的矛盾 [Hierarchical Denoising For Multi-Step Visual Reasoning](https://arxiv.org/abs/2607.15278)。HDR 将视频潜变量组织成树状层次结构，在流式输出前进行从粗到细的推理，并利用稀疏分层注意力模式降低计算成本。在涵盖迷宫导航、汉诺塔等六个任务的基准上，HDR 的成功率相比基线提升了 76.2%，且推理速度比双向扩散快 54.2 倍。此外，它仅需 2% 的训练数据即可保留大部分性能。这展示了分层推理结构在实现低延迟流式视频生成的同时，能够支持复杂的逻辑一致性视觉推理。

VIABench 是一个专为视觉障碍辅助设计的综合视频基准测试，使用视障人士录制的第一人称视频评估多模态大语言模型的能力 [VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance](https://arxiv.org/abs/2607.14660)。该基准定义了主动提醒、视觉问答和视觉引导交互三项核心任务，重点评估模型在实时响应和前瞻性地描述关键导航事件方面的表现。实验结果显示，当前 MLLM 在主动提醒任务中仍面临巨大挑战，难以提供全面的辅助支持。VIABench 的建立填补了专用辅助场景评估的空白，为推动开发针对视障人士的定制化 MLLM 提供了重要的评测标准。代码和数据将开源。

KeyFrame-Compass 是首个全面评估关键帧条件视频生成的基准，旨在检验模型在遵循指定关键帧序列的同时保持整体视频质量的能力 [KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation](https://arxiv.org/abs/2607.14202)。该基准包含 386 个精心策划的样本，涵盖多种应用域和关键帧密度，并引入了自动评估框架，从存在性、保真度、时序顺序等六个维度衡量关键帧执行情况。实验发现，当前模型在忠实执行关键帧与自然视频合成之间存在明显的权衡，且随着关键帧约束变密，性能下降明显，多数开源模型无法正确解读故事板网格输入。这揭示了当前视频生成技术在精确控制方面的局限性。

MultiRef-Compass 是一个统一的多参考到音视频生成（MR2AV）基准，评估模型在多个参考条件下生成连贯音视频内容的能力 [MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation](https://arxiv.org/abs/2607.14189)。相比现有基准，MR2AV 要求模型联合推理多个参考并正确绑定组成实体。基准涵盖多视图主体保留、多实体绑定等场景，并通过基本质量、参考一致性等四个维度的 14 个子指标进行评估。对八个代表性系统的测试显示，现有模型在多个评估维度上仍有很大改进空间。这强调了在复杂音视频生成场景中，建立全面且可解释的评估协议的重要性。

UniVR 是首个从纯视觉演示中同时学习复杂推理、细粒度物理动力学和长期规划的模型，提出了 VR-GRPO 强化学习范式 [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800)。VR-GRPO 通过全局和步骤级奖励的结合，强制执行逻辑一致性和物理一致性，无需任务特定启发式或图文对。在 VR-X 基准（涵盖长程操作、空间谜题和物理推理）上，UniVR 性能提升了高达 25%。这一成果证明了在视觉空间内进行推理的巨大潜力，所有代码、数据和模型均已开源，为纯视觉基础模型的推理能力发展提供了新方向。

## 语言模型训练、微调与评估方法论

Spectral Rewiring (SAR) 提出了一种后编辑方法，通过在谱空间中提取推理有效的更新分量来优化强化学习后的语言模型 [Spectral Rewiring for Exploration, Purification, and Model Merging](https://arxiv.org/abs/2607.03065)。SAR 保留了基模型谱空间中的核心推理能力，同时去除抑制性能或放大跨域干扰的正交分量，仅使用约 0.58% 的参数即可保留超过 99% 的后训练性能。该方法不仅提升了数学推理的高-k 探索能力，还净化了混合域训练更新，并实现了超越单一领域专家模型效果的模型合并。这表明通过参数几何结构提取推理有效更新，是一种无需额外训练即可改善推理和多域性能的有力机制。

Demystifying On-Policy Distillation 系统研究了在线策略蒸馏（OPD）的角色、病理现象及调节机制 [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399)。研究确认 OPD 作为探索催化剂的作用，但也揭示了两种病理现象：学生-教师不匹配（分布差距导致误导）和长度剥削（通过截断或填充规避奖励）。通过优势裁剪和对数尺度压缩等轻量级信号调节，可以有效缓解这些问题。实验表明，受调控的信号质量而非教师规模决定了 OPD 的成功。这为理解和使用 OPD 提供了理论依据，强调了在蒸馏过程中监控和指导信号质量的重要性。

Partition, Prompt, Aggregate 探讨了语言模型估计是否满足概率论中的全概率公式，以此评估其统计自洽性 [Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models](https://arxiv.org/abs/2607.15277)。研究发现，前沿模型在将细分子群体估计聚合回总体估计时，普遍违反了基本的自洽性原则，存在所谓的“宏观谬误”。然而，更细粒度的子群体响应往往比直接的人口水平估计更贴近人类参考数据。这暗示模型拥有相关的子群体知识，但未能可靠地将其传播到聚合估计中。该研究确立了统计自洽性作为评估 LLMs 的一个未饱和且无需参考的标准。

## 3D 重建、CAD 对齐与音频生成

AsySplat 提出了一种非对称 3D 高斯溅射架构，用于高效的长序列场景建模 [AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling](https://arxiv.org/abs/2607.10995)。该架构解耦了几何和外观建模，几何分支处理粗粒度令牌以进行多视角重建，外观分支处理细粒度令牌以捕捉细节，两者通过双边连接交互。这种任务感知的非对称性减少了计算冗余，在 32 视角 960P 输入下，相比优化方法实现了近 800 倍的加速，并超越了最先进零样本模型的性能。这表明在 3D 重建中，根据任务需求差异化分配参数和计算资源可以显著提升效率。

SUFLECA 是一个用于零样本 CAD 对齐的弱监督框架，旨在解决现有方法在遮挡或域偏移下的性能退化问题 [SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment](https://arxiv.org/abs/2607.15058)。SUFLECA 通过在 67.4 万张图像上进行法向对象坐标（NOC）监督，扩展了几何接地特征的学习，并提出了几何一致性的匹配算法。在 ScanNet25k 基准上，SUFLECA 实现了亚秒级的单实例对齐，精度优于最强零样本基线，并首次在该基准上超越了全监督方法。代码已开源。这证明了通过大规模几何监督学习紧凑的特征表示，可以显著提升 CAD 模型与真实图像之间的对齐鲁棒性。

WanSong v1.0 技术报告介绍了一种纯扩散模型方法，用于生成长达 5 分钟、高保真的商业级多语言歌曲 [WanSong v1.0 Technical Report](https://arxiv.org/abs/2607.14749)。与自回归或级联管道不同，WanSong 直接在单次运行中生成高质量歌曲并输出人声和背景音乐双音轨。其扩散框架还支持通过步骤蒸馏加速推理，并为微调定制和下游编辑任务提供了高效途径。这解决了音乐生成中效率、高保真长音频生成与可控性之间的难题，为商业化音乐创作提供了新的技术选项。

Token Time Continuous Diffusion (TTCD) 引入了一种新的扩散语言模型，它在连续空间中运行，并将高斯噪声确定性映射到最终令牌画布，无需进一步采样 [Token Time Continuous Diffusion for Language Modeling](https://arxiv.org/abs/2607.14106)。TTCD 的核心创新在于引入了“每令牌时间”概念，允许不同令牌以不同速率从噪声进展到最终令牌。这种连续空间建模避免了离散空间模型在高加速比下的平行采样误差，而差异化令牌时间有助于更好地建模条件生成和令牌间影响。在 OpenWebText 上的实验显示，TTCD 在高加速比下的条件生成质量优于同类离散模型。这为语言建模提供了一种避免离散采样误差的新范式。