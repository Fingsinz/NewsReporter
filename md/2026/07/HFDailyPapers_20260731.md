

# 每日HFDailyPapers-2026年07月31日

## GUI与计算机使用代理

近日，多份研究聚焦于让AI代理在真实计算机和移动设备上进行可靠操作。[Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227) 提出了Qwen-UI-Agent，这是一个面向真实世界的GUI基础代理，统一了移动设备、计算机使用、浏览器和DeepSearch环境。其核心设计包括跨平台的动作空间（交织GUI操作与CLI执行）、支持超过100轮的在线强化学习，以及基于AutoResearch范式的数据飞轮。该模型在MobileWorld-Real上达到92.2%，在AndroidDaily上达到97.5%，显著优于现有前沿模型。

[Echoverse: Deep, Evolving Environments for Training Computer-Use Agents at Scale](https://arxiv.org/abs/2607.28074) 从训练数据角度切入，指出当前计算机使用代理的训练瓶颈已从环境数量转向单个环境的"行为深度"。Echoverse通过编译规范生成状态化应用，并将每一次graded rollout同时用于环境修复和模型训练，形成协同进化循环。实验显示，在12个深度环境中训练的9B模型，跨14个评估分组的得分从36.5%提升至67.1%，而浅层环境则导致性能下降。这表明训练环境的交互深度和可修复性是决定代理真实桌面能力的核心因素。

分析表明，GUI代理研究正从单一环境 benchmark 转向构建能够自我演化的训练生态。数据飞轮与协同进化机制的引入，使代理不仅能学习固定任务，还能通过环境反馈持续改进，这对推动AGI型桌面助手落地具有关键意义。

## 记忆系统与长期记忆

多篇工作探索了LLM记忆的不同实现路径。[Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory](https://arxiv.org/abs/2607.27919) 将记忆模型扩展至6.9B参数，在300B token上预训练，并通过分布式Faiss索引和稀疏batch-wise加载解决了大规模检索的成本瓶颈。研究发现，将参数分配给记忆模块比单纯扩大基础模型更具参数效率：在Pythia-410M上附加6.9B记忆模块可使其均分从29.86提升至37.34，超越参数量为其近30倍的Pythia-12B。

[MemHarness: Memory Is Reconstructed, Not Replayed](https://arxiv.org/abs/2607.28272) 批判了现有记忆代理将检索经历作为静态记录直接重放的范式，指出这会引发负迁移。MemHarness引入统一策略模型，在每一步决策时根据当前状态对检索经历进行批判和重构。实验显示其在ALFWorld和WebShop上显著优于纯RL和静态记忆基线，且该重构目标在训练中充当隐式引导，从根本上提升了代理的推理能力。

[Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2607.27958) 面向多智能体场景，提出记录个体能力证据和同伴关系证据的在线可靠记忆。基于Weyl不等式的谱变化边界分析，Σ-Mem支持无需重训练的在线自适应，并在跨5个Qwen模型的OOD评估中，直接记忆读取性能优于多数投票和最优固定同伴。

[Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](https://arxiv.org/abs/2607.26637) 对文件系统记忆进行了系统性验证，将代理拆分为管理、搜索和执行三个角色。研究发现，虽然结构化存储可将检索成本减半，但除最强管理代理外，组织质量均随记忆增长而退化，且当前代理尚未能将组织本身转化为更好的答案——工具集的改变对存储形态的影响与更换模型相当。

分析表明，记忆研究正从"存储量"转向"记忆质量与适应性"。参数化记忆的训练成本、多智能体中的可靠度建模、以及记忆重构与重放的本质区别，均为未来代理系统设计提供了新的设计维度。

## 视频生成与世界模型

视频生成领域的研究呈现出两条技术路线：一端是提升物理一致性的世界模型，另一端是优化生成效率的扩散架构。[PhiZero: A World Model Built Around Physical Language](https://arxiv.org/abs/2607.28624) 提出"先推理后渲染"的范式，通过自监督从真实视频中学到物理语言（compact discrete representation of world-state transitions），并以此显式推理物理世界演化。该方法在生成和理解基准上均验证了物理一致性建模的有效性，并在零样本动作迁移上展现出潜力。

[ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow](https://arxiv.org/abs/2607.28362) 通过"阴影对"机制解决动作泛化问题：同一动力学在独立重采样外观下的视频对，使得模型能学习到与外观无关的统一动力学表示。该方法无需动作标签或运动估计，即可将演示视频转化为可复用的动作资产，在跨动力学家族的rollout比较中达到86%的盲评胜率。

[VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System](https://arxiv.org/abs/2607.27380) 采用双引擎架构：编码代理将文本提示转化为可执行的Blender代码，仿真引擎生成确定性的时空草稿，再由生成式视频引擎进行写实化编辑。该分解实现了过程级推理与高保真视觉实现的分离，在PhyGenBench上将OmniWeaving从0.475提升至0.558。

[Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://arxiv.org/abs/2607.28611) 针对长上下文视觉生成中的二次计算成本，提出混合注意力架构：Kimi Delta Attention（O(N)长程状态追踪）、Multi-head Latent Attention（全局交互）与模态感知短卷积的组合，并引入HeteroP超参数迁移方案以拟合Chinchilla最优定律。11B参数模型（2B激活）在预训练扩散损失上达到匹配基线1.7倍的计算效率，完整系统达7.3倍。

[Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation](https://arxiv.org/abs/2607.27372) 提出探索性建模（XMs），通过探索K个候选匹配来训练而非直接拟合数据分布，从而将"探索"作为除参数和数据之外的第三个预训练维度。随着数据规模增大，探索增益从7%升至36%；FLOP效率提升4.1倍，样本效率提升6.2倍，并解锁了端到端重构生成能力，在控制任务上与扩散模型相当但推理步数减少16-256倍。

分析表明，视频生成正从单一模型优化转向"表征学习+物理约束+架构效率"的协同设计。物理语言、阴影对、可执行代码等机制的引入，标志着生成模型开始内化对世界动力学的显式理解，而非仅拟合视觉统计。

## 推理与评估框架

多份研究聚焦于提升多模态和视觉推理的可靠性与评估科学性。[Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595) 从模式自适应（MA）和工具效应（TE）两个维度重新审视智能视觉推理，发现现有模型的工具调用缺乏必要性感知，且工具在难题上的收益常被在易题上的额外错误所抵消。Beacon通过"必要性感知自适应奖励"和"提示引导能力扩展"机制实现更强的整体性能和真实的工具增益。

[See2Think: Do Multimodal Models Really Use Intermediate Visual States?](https://arxiv.org/abs/2607.26769) 指出当前评估难以诊断模型是否真正依赖中间视觉状态。See2ThinkBench包含1200个视觉依赖问题，VAoT协议记录四种受控推理设置下的文本思考、视觉动作、渲染状态和后续推理。实验显示忠实渲染仍是清晰瓶颈，而在任务相关反馈被损坏时，模型准确率下降超过10个百分点，证实了对视觉状态的依赖。

[LedgerMind: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger](https://arxiv.org/abs/2607.28374) 将多模态代理轨迹视为来源约束的状态机，工具输出被规范化为结构化证据账本，下游推理仅能引用活跃账目条目。三层接地协议、自适应双路径分发器和事件触发验证修复引擎共同作用，显著改善了答案准确性和轨迹忠实度，同时抑制了未支持的中间推理、实体幻觉和过度推理等失败模式。

[MPIE-Bench: Benchmarking Anatomically Plausible Multi-Person Interaction Editing](https://arxiv.org/abs/2607.27616) 针对多图编辑中的解剖合理性问题，提出基于多人体网格重建的评估轴（Anatomy和Interaction），发现VLM-as-a-judge在交互评估上普遍饱和（>0.95），而人类评分器与mesh评估轴高度一致，当前没有任何编辑模型能同时在两个轴上表现优异。

[ReToken: One Token to Improve Vision-Language Models for Visual Retrieval](https://arxiv.org/abs/2607.28627) 提出单一可学习嵌入作为显式检索目标，从预填充视觉KV缓存中选择稀疏的相关token，在Visual Haystacks上使Qwen3VL-8B提升13.4点，且训练和长视频推理均可在单张H100上完成。

[RefCaptioner: Multi-Reference Image-Grounded Video Captioning](https://arxiv.org/abs/2607.28509) 引入多参考图像接地视频描述任务，通过混合数据SFT与分层覆盖折扣GRPO联合改进参考选择、短语级绑定和跨参考一致性。

分析表明，推理与评估研究正从"追求最终答案准确率"转向"追踪推理过程的忠实性与工具使用效率"。来源约束、过程级评估和工具必要性感知成为提升系统可靠性的关键方向。

## AI4AI与自我改进

[Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](https://arxiv.org/abs/2607.28568) 提出OpenMLE，一个面向递归自我改进（RSI）的全栈开源系统，包含OpenMLE-Gym（可验证任务环境）、OpenMLE-RL（算子学习）和OpenMLE-Evo（长程搜索）。Frontis-MA1（35B）作为元进化代理，围绕四种原子程序演化算子（Draft、Improve、Debug、Crossover）进行训练，将学习与进化耦合于单一循环中。在12小时/任务、单张RTX 4090（12GB VRAM）预算下，Medal Average从39.39%提升至71.21%，接近GPT-5.6 Sol和2.8T Kimi K3。该工作首次展示了在固定框架下通过模型替换和环境替换均可显著提升性能的可复现RSI研究路径。

[AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis](https://arxiv.org/abs/2607.28618) 面向化学文献综合，提出以"主张"为检索单位的基础设施。每篇论文被转换为原子化、类型化的主张，由来源DOI和逐字引用或证据定位器接地。AskChem索引240万条主张（14.7万篇论文），并暴露分层分类学、证据图和探索性活分类法。在AskChem-Bench上，GPT-5.5读取器接地后实现100%可解析DOI（对比无检索的88.3%），且引用密度在五个测试系统中最高。

分析表明，AI4AI正从概念验证走向工程化落地。Frontis-MA1展示了可复现的元进化路径，而AskChem则验证了结构化知识表示对领域代理的关键支撑作用。两者共同指向：自我改进系统的有效性取决于训练环境的质量、任务的可验证性以及知识的可组合性。

## 模型架构与训练方法

近期工作从多个角度改进了Transformer架构和训练范式。[Multi-Head Attention Residuals](https://arxiv.org/abs/2607.27230) 提出MHAR，将路由查询重塑为H个每子空间头，使每个特征子空间能独立读取深度历史。在Nemotron语料上的从零训练显示，MHAR在100M至1B参数规模上均优于标准Transformer、Attention Residuals等四种方法，且H=8为大规模模型的最优选择。通过delta残差的身份-preserving转换，支持8B模型的mid-training，在GSM8K和GPQA上分别提升3.2和3.1分。

[β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation](https://arxiv.org/abs/2607.28582) 将vanilla OPSD识别为β=1的广义策略优化家族成员，推导出参考策略与教师策略的几何插值最优解，并通过token级logits混合高效实现蒸馏目标。数学推理基准上，β-OPSD在优化稳定性和下游推理性能上均一致优于vanilla OPSD。

[Flux-OPD: On-Policy Distillation with Evolving Contexts](https://arxiv.org/abs/2607.28022) 分析上下文在反向KL目标中的作用：学生被蒸馏至上下文条件教师的几何均值，目标中的冲突项衡量教师间的冲突。Flux-OPD将上下文差异信号作为纠正项注入，并用冲突项加权，在开放域任务上优于现有OPD范式。

[Harness-G: A Graph-Structured Harness for Search Agents](https://arxiv.org/abs/2607.27652) 指出Search-R1训练中存在的检索等价坍塌问题：相同问题的轨迹生成不同查询但累积证据集趋于重叠，导致检索对比信号失效。Harness-G将自由查询生成重构为有限动作选择，并通过结构化非短视信用分配（SNC）使下游增益归因于前置动作，在六个QA基准上以1.5B模型超越Graph-R1达10.74分。

[SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them](https://arxiv.org/abs/2607.27703) 提出三阶段框架：Call暴露专家视觉模型作为空间工具，Learn通过冷启动SFT和代理RL改进工具使用，Internalize将通过成功轨迹的言语化内化专家感知能力。在MindCube上，Qwen3-VL-8B-Instruct从29.3%提升至84.6%（带工具），内化后保留73.8%（不带工具），超越GPT-5.6 Sol带工具结果（72.1%）。

[INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/abs/2607.26056) 提出端到端JEPA架构，将物理意图与未来目标意图通过相同四槽语法和共享参数对齐，实现无需搜索的意图到动作映射。在四个LeWM任务上，单次epoch零搜索模型达到85.78%-100%成功率，可选CEM采样仅需384序列即可将宏观成功率提升至96.86%，采样量减少23.44倍。

[Revisiting Lossy Verification in Speculative Decoding](https://arxiv.org/abs/2607.26627) 系统分析有损验证机制，将其分类为截断式与协作式两类，并揭示截断式方法因分布畸变导致性能退化，协作式方法的关键在于控制草稿概率相对于目标概率的上溢。

分析表明，架构与训练创新正从"单一模块优化"转向"表征-推理-执行"的全链路协同设计。MHAR、β-OPSD和INTACT等工作分别在注意力机制、策略优化和意图-动作映射上提出了具有理论支撑的新方案，反映出领域对效率与可靠性的双重追求。

## 其他动态

[Can Large Language Models Execute Parent Orders?](https://arxiv.org/abs/2607.28410) 提出PACE框架，将父订单执行分解为长程规划和短程执行，在深圳交易所Level-1数据上优于TWAP、Almgren-Chriss和学习基线，超越最强基线0.65 bps。行为分析显示LLM比人类更早交易且高置信度预测更优表现。

[Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations](https://arxiv.org/abs/2607.28319) 提出轻量级结构干预方法，通过最小对比提示对识别GLU架构中对人口统计学属性差异化响应的神经元。零化最多40个神经元（Llama-3.2-1B中<0.031% MLP宽度）可在保持99.49%推理和通用知识能力的同时改变模型对人口统计变量的响应，但存在双向偏差去稳定的风险。

[Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing](https://arxiv.org/abs/2607.28308) 通过Expert Subspace Separation Index等工具区分路由连贯性、候选质量和上下文交互，发现专家子空间存在显著重叠但实际路由仍优于匹配替代方案，提出"相干重叠"概念解释为何几何相似度不足以决定冗余或剪枝价值。

[AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emotion Recognition](https://arxiv.org/abs/2607.25289) 面向端侧语音情感识别，通过每批次SVM加权提升教师可靠性，并通过关系蒸馏损失捕获教师-学生相似度矩阵中的结构信息，在IEMOCAP和CREMA-D上优于单教师蒸馏基线。

[Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions](https://arxiv.org/abs/2607.20891) 通过MisKnow-Agent框架生成5933个可控权威级别的误导性实例，发现即使有限接触也能导致最终报告采纳错误结论，且集中验证与工作流程级证据使用之间存在脱节。

[AI Tour Meeting: Group Travel Planning by LLM Agents](https://arxiv.org/abs/2607.18806) 提出多LLM代理协作的旅游规划框架，代理具化不同人格并通过自然语言讨论寻求满足约束的行程方案。

[Pedestrian Archetypes Extension](https://arxiv.org/abs/2607.16922) 在先前12种行人原型基础上，新增7种通过YouTube行车记录仪视频观察到的行为原型。