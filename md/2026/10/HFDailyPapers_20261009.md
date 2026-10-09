

# 每日HFDailyPapers-2026年10月09日

## Agent学习与自我改进

本期涌现了多篇围绕Agent从经验中学习、自我改进与持续进化的研究。[AgentGarten](https://arxiv.org/abs/2610.12374) 提出将模拟器与游戏引擎通过共享神经渲染器耦合，构建实时交互环境，使Agent通过视觉感知与世界互动，并将每轮经验蒸馏为后续Agent可继承的"Playbook"，仅需4轮即可实现显著学习增益。[Memento 3](https://arxiv.org/abs/2610.11794) 采用外部语义记忆机制，冻结LLM通过维护可修订的"规则手册"持续更新世界模型，并在ARC-AGI-3上达到人类等效动作效率。[ViSkill](https://arxiv.org/abs/2610.12403) 则引入视觉原生技能学习框架，将成功交互编码为视觉技能卡，实现技能积累与策略优化的闭环反馈，在Sokoban等任务上超越PPO。[Embodied Turing Machines](https://arxiv.org/abs/2610.12369) 提出Code-Only-as-Policy (COAP) 范式，用代码替代VLA/VLM进行状态追踪与决策，在RoboDojo上达到70.24%成功率且无需测试时模型。[On-Policy Distillation](https://arxiv.org/abs/2610.09639) 揭示反向KL蒸馏仅 transfer 组合技能而非事实知识，而前向KL可恢复事实迁移。[Frozen Models](https://arxiv.org/abs/2610.09146) 提出模型无关框架，通过技能、知识记忆与多模态知识库让冻结模型从部署经验中学习，在医学任务上提升最高34.2%。[Mara Chain](https://arxiv.org/abs/2609.35855) 将拒绝候选转化为迭代精炼的阶梯，在AppWorld和TerminalBench上显著减少rollout需求。

分析表明，"冻结模型+外部记忆/经验积累"正成为Agent自我改进的主流范式，避免了全量微调的高成本，同时通过结构化经验表示（Playbook、规则手册、技能卡）实现了知识的可复用性与可传播性。

## 导航与空间推理

多篇研究聚焦于提升Agent的空间理解与导航能力。[SuperNav](https://arxiv.org/abs/2610.12126) 不微调MLLM，而是通过导航技能、工具化物理交互与统一视觉-点接口，让模型专注决策而委托运动执行，在HM3D及真实四足机器人上验证了跨场景泛化。[SpaceCast-Bench](https://arxiv.org/abs/2610.12402) 首次系统评估预测性空间推理能力，最强模型仅达58.0%对比人类87.2%，揭示空间智能的显著差距。[SpatialOPSD](https://arxiv.org/abs/2610.11366) 通过策略内自蒸馏将编码Agent的空间推理能力内化，无需外部工具即可实现更高精度。[SatNav](https://arxiv.org/abs/2609.31507) 构建基于卫星影像的城市级UAV导航基准，涵盖118K片段，验证了卫星到真实飞行的迁移可行性。[SpaceFlow](https://arxiv.org/abs/2610.12399) 提出无需训练的局部可控3D生成方法，通过几何原语实现区域级控制强度与外观指定的解耦。

分析显示，空间推理仍是VLM的薄弱环节，现有方法多依赖外部工具或3D扫描数据；将推理能力内化、降低对外部依赖，以及从卫星/全景视角扩展导航范围，是重要的发展方向。

## 视觉生成与编辑

视觉内容生成与编辑领域取得多项进展。[DreamTrue](https://arxiv.org/abs/2610.12468) 提出反事实后训练，通过几何校准与人类标注的交互缺陷数据集，将机器人世界模型的交互缺陷率从48.12%降至6.25%，获AgiBot World Challenge 2026冠军。[OuroWorld](https://arxiv.org/abs/2610.12461) 将静态3D高斯场景转化为无缝循环的3D cinematic，通过傅里叶级数形变场保证循环性。[LEGO](https://arxiv.org/abs/2610.12442) 提出无提升视角的异中心到自中心视频生成，通过概率映射保留结构而细节由扩散模型恢复。[VibeEdit](https://arxiv.org/abs/2610.12229) 引入画布指令界面，用户直接在图像上标注空间标记，实现无需文本提示的对象编辑。[Reasoning-Informed Visual Editing](https://arxiv.org/abs/2610.12343) 构建RISEBench++基准，涵盖65种细粒度任务类型，揭示即使GPT-Image-2.5也仅达56.6%准确率。[Post-Training Text-to-Image](https://arxiv.org/abs/2610.02967) 组合偏好奖励与rubric奖励进行后训练，Flux2dev在Arena达到+69 Elo提升。

分析表明，视觉编辑正从单一文本提示转向多模态、结构化指令，而世界模型的物理合理性与动作忠实性成为机器人应用的关键瓶颈，反事实训练与人类反馈 RL 是重要解决路径。

## 评估基准与度量

本期发布了多项面向不同能力的评估基准。[TestPrism](https://arxiv.org/abs/2610.12289) 指出单一参考解评估高估测试质量，Joint Success Function仅28%对比单参考59.67%，并提出TestHelix通过递归自改进提升8.67-9.00个百分点。[OmniCapBench](https://arxiv.org/abs/2610.12458) 将评估目标从自由文本转为原子化验证单元，揭示当前MLLM在长时程音视频推理中的身份漂移与跨模态错位。[Accurate but Not Humble](https://arxiv.org/abs/2610.12360) 提出认识谦逊(ISE)三维度量，发现高准确率Agent未必能正确表达不确定性。[U-Space](https://arxiv.org/abs/2610.09087) 通过机制可解释性构建低维不确定性子空间，实现token级不确定性映射。[TerraVis](https://arxiv.org/abs/2610.02959) 定义18类世界一致性违例 taxonomy，发现强常规指标模型仍存在显著物理不合理性。[BrickBench](https://arxiv.org/abs/2610.12452) 评估Agent LEGO设计能力，指出Agent满足物理约束但设计质量逊于人类。[Pumpire](https://arxiv.org/abs/2610.12423) 直接评估点对距离估计能力，填补既往评估空白。[AgenticBBO-Bench](https://arxiv.org/abs/2610.12183) 跨域评估黑盒优化Agent，揭示任务语义优于具体先验。

分析显示，评估正从单一准确率转向多维度、结构化、可归因的度量体系，尤其在不确定性表达、物理合理性与跨模态一致性等"隐性能力"上存在显著评测缺口。

## 模型效率与推理加速

推理效率优化涵盖架构设计与系统实现多个层面。[TokenRouter](https://arxiv.org/abs/2610.12242) 针对token级别路由的步级不同步问题，采用请求中心编程与延迟批处理调度，实现2.01-64.15x解码吞吐量提升。[SparseDecoding](https://arxiv.org/abs/2610.12327) 解决自然序列与生成序列的Hessian分布偏移，通过解码感知校准矩阵与N:M稀疏SpMV kernel实现1.48x端到端加速。[V-CoLA](https://arxiv.org/abs/2610.11251) 针对线性注意力架构提出唯一性感知token压缩，以50% token保留99.5%性能，预填充加速1.86-6.15x。[SparseEngine](https://arxiv.org/abs/2609.39068) 从底层构建稀疏优先推理引擎，支持15种稀疏方法，吞吐量较vLLM提升超10x。[SpecFold](https://arxiv.org/abs/2610.04875) 利用扩散语言模型多分支 speculation 中的计算冗余，通过残差门控与折叠注意力实现最高1.99x加速。[MC-Sparse](https://arxiv.org/abs/2610.06801) 解决扩散Transformer稀疏注意力质量退化，缓存元数据实现1.80-2.32x去噪加速。[CARE](https://arxiv.org/abs/2610.08917) 为VLA推理加速提供有限样本保证，在LIBERO上认证9.0-10.8x加速同时保障85.8% episode保留。

分析表明，稀疏化与压缩技术正从"静态校准"转向"动态感知"，针对特定推理阶段（如解码、speculation）的定制化优化成为提升效率的关键。

## 视频世界模型

视频生成与交互世界模型方面，[WorldGuide](https://arxiv.org/abs/2610.12459) 将程序化视频生成建模为闭环任务执行， Planner 预测原子动作而 Executor 直接学习实现，层级视觉记忆维持长时程状态，在WorldGuide-Bench达到33.33%成功率。[SPW-Nav](https://arxiv.org/abs/2610.08941) 构建流式全景世界模型，从单全景图实时流式生成1分钟2K 360度视频，支持指令动态切换。

分析显示，从开环生成向闭环执行转变是视频世界模型的关键进展，规划与执行的联合训练以及层级记忆机制对长时程任务完成至关重要。

## 多模态理解与检索

多模态模型的能力边界与检索系统优化方面，[OneSearch-VL](https://arxiv.org/abs/2610.12419) 提出视觉 grounding 证据图 (VGEG) 统一编码多图像/视频研究依赖，EVGR奖励增强证据可追溯性。[Chaos in the Text](https://arxiv.org/abs/2610.11816) 揭示混合模态检索中"文本混沌"现象——无关文本比无关图像造成更严重性能退化，Trident通过多正视图InfoNCE缓解此偏差。[FreeMatching](https://arxiv.org/abs/2610.12421) 突破时空先验限制，在图像编辑与参考引导生成中建立身份保持对应关系。[MARGIN](https://arxiv.org/abs/2605.22949) 提出多Agent运行时置信度校准，无需重训练即可改善异质模型协调。

分析表明，多模态理解正从"感知融合"迈向"证据可追溯"，而混合模态检索中的模态偏好偏差是需要系统性解决的已知问题。

## 机器人与仿真

机器人学习与仿真环境方面，[USDCraft](https://arxiv.org/abs/2610.11322) 利用预训练LLM编写可执行程序重建铰接3D资产，无需任务特定训练即可支持真实到仿真到真实的操纵转移。[In-context Robot Learning](https://arxiv.org/abs/2609.38173) 明确定义机器人情景学习学习目标，SimpleICL框架无需大规模预训练即实现强性能。[HEERO](https://arxiv.org/abs/2606.03335) 构建GPU并行异构多任务RL基准，IW-ABC方法用50条演示达到90.1%平均成功率并验证实机迁移。

分析显示，机器人学习正从"任务特定微调"转向"通用框架+外部知识"模式，仿真到实物的迁移仍需解决分布偏移与物理建模精度问题。

## 训练与优化方法

训练策略与优化算法方面，[ReSPO](https://arxiv.org/abs/2609.35433) 解决离策略学习中的梯度饥饿问题，通过平滑双分支序列级核替代裁剪机制。[Alpha-Stabler](https://arxiv.org/abs/2609.34344) 发现RL有效流形位于激活主子空间正交补中，通过预测器-控制器框架稳定2000步训练。[EDiS](https://arxiv.org/abs/2610.09059) 将GNN稀疏训练的结构提取与epoch级图组合解耦，在19个基准上取得最高平均得分。[SanSi](https://arxiv.org/abs/2610.07730) 提出循环类型决策模型"System 1.5"，单次前向推理与多次循环间的中间形态。[Station](https://arxiv.org/abs/2610.08927) 通过监督者与元反思机制实现开放-ended科学发现，复现62.7% ICLR论文发现。

分析表明，训练效率与稳定性优化正从"架构改进"扩展到"优化目标设计"与"训练动态管理"，对离策略偏差与梯度流的控制成为关键。

## 语言理解与推理

语言模型内在机制与推理能力方面，[Intent in Multi-Turn Dialogue](https://arxiv.org/abs/2610.06496) 发现模型对已拒绝提议的"提及即生效"混淆，Intent-OPSD通过决策条件蒸馏解决。[Sequential Structure](https://arxiv.org/abs/2610.04977) 揭示更长上下文不改善策略识别，高阶依赖显著降低规则恢复，表面行为忠实性可能掩盖错误生成机制。[RAG monolingual](https://arxiv.org/abs/2610.03136) 证明推理语言与查询/检索文档对齐有助于单语RAG，但仅达母语水平。[Evidence-Grounded Oversight](https://arxiv.org/abs/2610.06406) 提出证据 grounding 行为图帮助监测Agent关键决策。

分析显示，对语言模型推理机制的理解正从"性能测量"深入至"过程可解释性"，多轮对话中的意图跟踪与序列结构的内在表征仍是待解难题。

## 其他动态

[Foundations of Large Language Models](https://arxiv.org/abs/2501.09223) 为LLM基础概念教材，涵盖预训练、生成、提示、对齐、推理与推理六章。[Synthesis Through Simulation](https://arxiv.org/abs/2610.10549) 提出无schema数据合成范式，通过策略API执行生成结构有效企业数据。[MIRA](https://arxiv.org/abs/2610.10355) 为文本到音乐生成构建意图细化Agent，通过rubric验证与树搜索提升意图对齐。[Incidental information](https://arxiv.org/abs/2610.08585) 发现LLM临床记录中 incidental 信息污染问题，35%笔记插入闲聊，3.7%误用临床。