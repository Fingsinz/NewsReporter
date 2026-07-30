# 每日HFDailyPapers-2026年07月30日

## Vision-Language-Action (VLA) 模型优化

TurboVLA 提出了一种直接的 V + L to A 映射范式，通过独立编码视觉观察与语言指令，并利用轻量级双向交互来预测动作连续块，从而显著降低了推理的算力和内存开销。在 LIBERO 基准上，该模型以 0.2B 参数实现了 97.7% 的平均成功率，且在消费级显卡上的延迟为 31.2 ms、显存占用 0.9 GB [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205)。另一项研究引入 HumanCLAW 评估框架，将决策与底层执行解耦，以量化 VLM 的主体感知能力；结果表明最佳模型仅达到 16.8% 的成功率，缺乏具身自我意识是主要瓶颈 [HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180)。这两项工作分别从提升效率和诊断缺陷的角度，揭示了视觉、语言与动作连接的关键技术趋势。

## 多智能体技能学习与强化学习

SkillRise 构建了一个统一的强化学习框架，旨在通过渐进式任务序列和单一策略在跨任务间提取并复用可转移的技能文档，其在 ALFWorld、WebShop 等基准上的 Pass@1 性能优于现有基线 2.3 至 8.5 个百分点 [SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution](https://arxiv.org/abs/2607.26784)。此外，CAST 利用游戏求解器的状态变化作为教师信号，将其转化为回合级别的信用分配优势注入到稀疏奖励强化学习中，在 Sokoban、Minesweeper 及长程游戏代理任务中均表现出卓越的表现 [CAST: Game Solvers as Turn-Level Teachers for LLM Agents](https://arxiv.org/abs/2607.25308)。CoRT 则提出基于反事实回放（counterfactual replay）的方法，在不引入辅助评分模型的情况下实现令牌级的信用重加权，提升了基于准则强化学习的训练效果 [CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization](https://arxiv.org/abs/2607.25659)。这些进展表明，通过更精细的信号解耦和通用技能的跨任务迁移，正在显著增强自主体的规划与执行能力。

## 评测基准与安全评估

在评测领域，OmegaUse-OfficeVal 引入了包含经济成本信号（人力时间与任务价格代理）的基准，用于衡量长周期办公流程任务的 LLM 代理能力，结果显示虽然智能体效率高但质量尚未达人类水平 [OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](https://arxiv.org/abs/2607.27155)。SecRespond 则是首个针对安全运营中“后妥协”场景的基准，评估智能体处理取证报告与漏洞修复计划的能力，结果显示所有模型都无法在任何单一场景中完成全面的检测与修复 [SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response](https://arxiv.org/abs/2607.26791)。StealthBench 专注于评估自主进攻性安全代理的操作隐蔽性（OPSEC），结果指出没有模型能超过 54% 的安全成功率，系统性失败普遍存在 [StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents](https://arxiv.org/abs/2607.26314)。GPT-Red 展示了通过大规模自对战自动化红队测试来发现新攻击并向导抗训练的方法，成为目前最大的 LLM 安全训练运行之一 [GPT-Red: Automated Red Teaming via Self-Play at Scale](https://arxiv.org/abs/2607.26115)。综合来看，当前的智能体在标准化工程任务或静态指标下表现尚可，但在需要高置信度完整性判定、主动挖掘隐匿威胁及保持低暴露风险的复杂现实场景中仍存在明显不足。

## 生成模型、视频理解与知识系统

StatePlay 提出了一种状态感知的游戏世界模型架构，结合混合变压器（MoT）结构与独立的视觉与状态分支，以维持依赖内部状态的游戏机制一致性，相比未建模显式状态的模型，其生成内容的机制保真度提升了 18.6% [StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation](https://arxiv.org/abs/2607.26754)。TriLayer 项目构建了包含三元组对齐视频的大规模数据集，用于支持 RGB 复合层与 RGBA 前景层的联合生成，显著改善了视频对象插入与分解任务的真实性 [Explicit Layer Modeling for Video Object Insertion and Layer Decomposition](https://arxiv.org/abs/2607.25802)。CLBench-V 针对多模态上下文学习能力进行了新的基准构建，涵盖科学、金融等多个领域，最高分仅为 0.2847，表明在多模态语境下定位上下文并获取新知识的能力仍有较大提升空间 [CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition](https://arxiv.org/abs/2607.25294)。在知识传承方面，一篇研究借鉴了伊斯兰圣学中的 isnad-rijal 体系，提出了面向多智能体系统的声明级溯源框架，通过分级传播链评估来处理自动化的知识聚合问题 [Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems](https://arxiv.org/abs/2607.24117)。同时，关于大模型记忆机制的综述文章系统梳理了其架构维度，为未来的统一设计提供了理论支撑 [Memory for Large Language Models](https://arxiv.org/abs/2607.25380)。这些研究共同推动了对多模态生成内容准确性与可追溯性的深入探索。

## 科研自动化与技术蒸馏

针对人工智能是否能开展开放式前沿研究的疑问，研究者采用了“影子评估”方案，让代理接手未发表论文的核心研究问题并由原作者打分，证据显示当前智能体虽能完成工程实现，但在研究设计判断与资源规划方面仍存在局限 [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191)。在教学与蒸馏方面，DecoEvo 采用了解耦协同进化策略，在文本空间内同步更新求解器技巧与评述生成器技巧，避免了因评述固定而导致的优化盲区，取得了相对增益 [DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space](https://arxiv.org/abs/2607.25675)。CADENCE 框架则针对知识蒸馏过程中的冷启动崩溃、分布调度不当及奖励稀疏问题提出了一系列修正机制，成功在小参数量学生模型上实现了接近教学水平的推理能力 [CADENCE: Closing the Reasoning Gap via Coverage-Adaptive On-Policy Distillation](https://arxiv.org/abs/2607.16955)。上述工作表明，尽管自动化研究与模型压缩取得了一定成效，但要达成真正的全闭环自动化研发过程或极致高效的知识传递，仍需对认知逻辑与适应性算法进行更深层次的创新。