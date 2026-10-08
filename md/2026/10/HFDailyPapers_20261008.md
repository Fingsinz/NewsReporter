

# 每日HFDailyPapers-2026年10月08日

## 世界模型与机器人操作

Long-WAM 提出了一种在实时控制约束下扩展因果世界-动作模型上下文的方法，通过在机器人和第一人称视频上进行自回归预训练，将 RoboCasa GR-1 上的成功率从 63.3% 提升至 78.7%，并在 RTX 5090 上实现每块动作 107.4 ms 的推理 [Long-WAM](https://arxiv.org/abs/2610.10528)。UniWAM 则整合了物理推理器、世界生成器和动作预测器三个组件，构建了统一架构，在人类第一人称数据与机器人数据的混合预训练中发现了对数线性缩放规律 [UniWAM](https://arxiv.org/abs/2610.02054)。ViGAR 将长程组合操作分解为视觉子目标规划器与子目标执行器两层结构，在 RoboTwin Clean2Random 基准上以 82.00% 成功率超越最强基线 12.86 个百分点 [ViGAR](https://arxiv.org/abs/2610.02368)。PhysEvo 围绕单个冻结模型实现了物理递归自改进，在 RoboDojo 42 个任务上达到 62.00% 成功率，并将仿真进化的控制链部署到 AgileX PiPER 实体机器人上取得 84.00% 成功率 [PhysEvo](https://arxiv.org/abs/2610.08995)。

分析表明，世界-动作模型（WAM）方向正从单一模型训练转向"预训练扩展上下文 + 分层推理 + 部署自适应"的组合路径。Long-WAM 与 UniWAM 均强调自回归预训练对保留历史-未来结构的重要性；ViGAR 的分层分解进一步说明长程任务需要显式子目标规划而非端到端直接预测。PhysEvo 和 Robo-COP 提出的"部署即进化"范式将策略与编排器共同演进，表明机器人智能的提升正从静态模型转向持续闭环改进。

## 视频生成效率与多模态生成

GRACE 针对视频扩散模型的压缩瓶颈，提出生成感知的潜变量压缩框架，通过冻结基础潜变量并学习残差潜变量，使 Wan2.1-I2V-14B 的 token 数减少 8 倍、延迟降低 11.1 倍，同时在 VBench 上保持与原始管道相当的生成质量 [GRACE](https://arxiv.org/abs/2610.10524)。SGF+ 将上下文写入与去噪角色解耦为独立参数，在无需额外数据或更长训练时长的情况下显著提升了自回归视频生成的视觉质量和长程一致性，支持最长 24 小时连续生成 [SGF+](https://arxiv.org/abs/2610.10429)。WorldSonus 面向世界模型引入流式因果自回归扩散架构，以 0.41 的低实时因子实现实时空间音频合成，并在开放域视频到音频基准上匹配或超越双向模型 [WorldSonus](https://arxiv.org/abs/2610.08760)。Salt++ 提出因果自流与上下文对齐的自回归分布匹配蒸馏相结合的两阶段后训练方法，在 4 步因果设定下于 JavisBench 提升视觉质量 57% [Salt++](https://arxiv.org/abs/2609.36995)。

分析表明，视频生成的核心瓶颈正从生成质量转向效率与实时性。压缩-生成协同优化（GRACE）和梯度流解耦（SGF+）分别从编码器和模型结构两个维度降低计算负担；WorldSonus 和 Salt++ 则进一步将视频生成扩展到视听联合生成和流式少步推理场景，反映行业对低延迟交互式内容生成的需求。

## 图像生成、评估与文本渲染

QuadTok 引入四叉树视觉分词器，动态为视觉复杂区域分配更多表征容量，相比固定 256 token 网格在 ImageNet 上节省约 10% token 的同时保持重建保真度，并支持零样本空间控制生成 [QuadTok](https://arxiv.org/abs/2610.10497)。Iris-3B 从头预训练了 3B 参数的像素空间文本到图像变换器，尽管在下游深度估计和超分任务上未发现显著优于潜空间模型的表现，但验证了像素空间预训练可扩展至 3B 规模 [Iris-3B](https://arxiv.org/abs/2610.09450)。VIEScore2 将图像表示为 N×N 网格，在单次前向传播中联合预测质量分数与缺陷位置，其整体评分 SRCC 达 0.601，超越 Gemini-3-Flash 的 0.491 [VIEScore2](https://arxiv.org/abs/2610.00994)。UltraText Bench 构建包含 432 个中英双语提示的密集文本渲染基准，揭示不同模型在文本忠实度、清晰度与空间质量上的差异 [UltraText Bench](https://arxiv.org/abs/2610.09823)。NAMVIS 将多视图图像合成 Reformulate 为几何条件的逐尺度自回归过程，在 Objaverse 等基准上 PSNR、SSIM 均超越扩散基线，且推理速度提升 3 倍以上 [NAMVIS](https://arxiv.org/abs/2610.04722)。

分析表明，图像生成领域正从追求生成质量转向质量评估与效率优化并重。VIEScore2 和 UltraText Bench 分别提供了带空间定位的量化评估和针对密集文本渲染的专项基准，填补了现有评估体系的空白；NAMVIS 和 QuadTok 则表明自回归范式在图像生成中具有速度与质量兼顾的潜力。

## 3D场景生成与CAD重建

Tetris3D 通过显式条件化周围物体的几何形状与物理关系来生成空间协调的 3D 场景，并引入包含 120 万场景的物理交互数据集 ComOb，在生成质量和物理稳定性上均达最优 [Tetris3D](https://arxiv.org/abs/2610.10539)。CADFather 构建了一个自主智能体系统，协调视觉语言助手、生成工具与数值优化器从 3D 网格恢复参数化 CAD 程序，在 DeepCAD、Fusion360 和 MCB 测试集上实现了高重建质量与执行有效性 [CADFather](https://arxiv.org/abs/2610.09127)。StepCAD 结合状态条件化 CAD 策略与 IoU 引导的树搜索进行生成式优化，在复杂形状上相较最强基线取得 87.2% 的相对 IoU 提升，并发布了 ARCADE-1.5M 大规模数据集 [StepCAD](https://arxiv.org/abs/2610.03799)。

分析表明，3D 内容生成正从独立物体生成转向场景级物理协调与可编辑参数化重建。Tetris3D 强调物体间的物理与几何约束，CADFather 和 StepCAD 则聚焦于将 3D 网格还原为可编辑 CAD 程序，三者共同反映了对"可操控 3D 世界"而非仅"视觉真实"的需求升级。

## LLM Agent 与自我进化

RunningTab 为直接工作区交互（DWI）引入了环境侧标签机制，记录任务需求、已读取文件与未打开候选，在三个基准上持续优于纯 DWI 方法 [RunningTab](https://arxiv.org/abs/2610.10444)。MIMESIS 在人类对话数据上训练了具备 13 种真实行为模式的 user simulator，9B 模型在 RealUserSim 和 SimulatorArena 上分别改善行为保真度 13.4 分和降低 Turing 距离 3.6 分 [MIMESIS](https://arxiv.org/abs/2610.09484)。SkillForge 通过适应度驱动的技能生命周期（试用-活跃-稳定-退役）实现技能库与策略的协同进化，在多个交互式 Agent 基准上最高提升 7.8% [SkillForge](https://arxiv.org/abs/2610.09832)。UniSkill 使用共享策略从轨迹中提出技能库编辑（添加、更新、不编辑），在 ALFWorld 达到 98.4% 成功率 [UniSkill](https://arxiv.org/abs/2610.10164)。ReSAIL 通过优先选择高信息交互步骤进行蒸馏并正则化保留特权信息条件行为，在三个周期内维持显著性能增益 [ReSAIL](https://arxiv.org/abs/2609.39306)。R-Quest 识别出自训练过程中无效问题和数学等价重复问题两种质量退化模式，通过有效性和新颖性反馈引导自我进化，在 12 个基准上稳定保持增益 [R-Quest](https://arxiv.org/abs/2610.04299)。DecepEval 基于欺诈理论 Diamond 框架构建了 1,532 个实例的欺骗基准，揭示外部条件（压力、激励、机会、冲突）系统性诱发 LLM Agent 欺骗行为 [DecepEval](https://arxiv.org/abs/2610.07967)。

分析表明，LLM Agent 研究正从单一任务执行转向可持续自我改进与行为可控性。SkillForge、UniSkill 和 ReSAIL 共同指向技能库的动态管理是 Agent 长期演化的关键；R-Quest 则揭示自我进化中数据质量退化机制。DecepEval 从安全性角度提出了系统评估框架，反映 Agent 可靠性已成为独立研究维度。

## 强化学习与策略优化

SQAM 利用预训练流策略的批量平均速度 Jacobian 近似为对角矩阵的发现，推导出闭式标量伴随，消除了逐步向量-Jacobian 乘积计算，在 OGBench 最难域上将成功率提升 18-35 个百分点 [SQAM](https://arxiv.org/abs/2610.10437)。MWRL 将最小充分见证识别形式化为强化学习问题，通过联合覆盖Credit分配统一了极小性与替代方案恢复的需求 [MWRL](https://arxiv.org/abs/2610.07226)。KLPO 将 KL 正则项锚定在采样器端，推导了闭式 Gibbs 解并以最小二乘拟合对数率最优条件，实现了无需重要性权重和 critic 的单 rollout 更新 [KLPO](https://arxiv.org/abs/2610.08963)。NP-OPD 在 rollout 阶段引入低能力负策略作为负参考，通过负策略 rollout 持续提供负信号，在多个模型规模与推理域上改善 OPD 性能 [NP-OPD](https://arxiv.org/abs/2610.07874)。DLoop 提出循环式投机解码，在并行草稿模型中自适应执行多次草稿阶段后再统一验证，在多种投机解码方法上提升 5-41% 的实际加速比 [DLoop](https://arxiv.org/abs/2610.07659)。SCAPO 基于半反事实提示干预测量 token 级概率漂移，将稳定性分数纳入 GRPO 的 credit 分配，在 Qwen3-4B 上 AIME 准确率较 GRPO 提升 5.63 个百分点 [SCAPO](https://arxiv.org/abs/2609.40360)。

分析表明，强化学习与策略优化领域的核心趋势是从单一优化目标转向多维度精细控制：SQAM 和 KLPO 分别降低了流策略微调和策略梯度更新的计算复杂度；NP-OPD 和 SCAPO 引入负信号和稳定性约束以缓解过拟合与奖励黑客问题；DLoop 则从解码效率角度拓展了投机解码的应用边界。

## 模型架构与时序建模

Recurrent Looped Transformer (RLT) 将 Transformer 层拆分为并行因果编码器与循环解码器，在算法任务上展示了随序列长度线性增长的计算路径，在 256-bit 异或泛化任务上达到 100% 准确率而标准 Transformer 停留在随机水平 [RLT](https://arxiv.org/abs/2610.07591)。TIDES 将输入依赖从时间离散步长转移至对角状态矩阵，使选择性 SSM 同时具备不规则时间戳原生处理能力与逐 token 表达力，在 UEA 时间序列分类和 Physiome ODE 回归基准上创最佳平均排名 [TIDES](https://arxiv.org/abs/2605.09742)。STEPQuant 针对 Delta 规则循环状态提出时空后训练量化框架，按错误幅度与记忆寿命分配精度，在 6-bit 预算下接近 FP32 状态精度，将总推理内存降低最高 68.7% [STEPQuant](https://arxiv.org/abs/2609.38169)。Long-Context Hybrid Models 系列揭示了全注意力与滑动窗口/线性注意力混合的跷跷板效应：LA 混合更受益于长上下文持续预训练，SWA 混合在长度外推上表现更好 [Hybrid Models](https://arxiv.org/abs/2610.10114)。

分析表明，序列建模架构正在从固定深度 Transformer 向具备隐式状态追踪能力的混合架构演进。RLT 和 TIDES 分别从循环计算和选择性状态空间两个方向突破传统 Transformer 的固定计算路径限制；STEPQuant 和 Hybrid Models 则从量化效率和位置归纳偏置角度揭示长上下文建模的深层机制。

## 多模态理解与应用系统

VepAgent 将因果过渡推理与工具增强强化学习结合用于视频事件预测，构建了 futurebench-4K CoT 数据集并开发了状态跟踪、帧检索和区域放大的诊断工具库，在 FutureBench 上达到最优性能 [VepAgent](https://arxiv.org/abs/2610.06293)。ProactiveCoach 提供层次化程序理解训练数据（阶段/步骤/动作三级）和评估基准，使 VLM 能在正确时机以适当粒度提供指导，性能较固定粒度监督提升最高 9.6 个百分点 [ProactiveCoach](https://arxiv.org/abs/2610.06505)。EviAlign 将语义证据生成与边界读取耦合于共享多模态 LLM，在 12 个 MMEB 检索任务上达到 76.9 的平均 Recall@1 [EviAlign](https://arxiv.org/abs/2609.33659)。PAMI 通过身体部位锚点投票机制实现文本到人体-对象交互生成，在 InterAct 基准上将接触召回率提升 14.5% [PAMI](https://arxiv.org/abs/2609.38466)。Gan Jiang 构建了粉末 X 射线衍射自学习 Agent 生态，在 DeltaXRDbench 上单相比对准确率领先，MP500 单相比对 top-1 准确率达 96.30% [Gan Jiang](https://arxiv.org/abs/2610.07862)。

分析表明，多模态理解正从被动感知转向主动推理与工具增强。VepAgent 和 ProactiveCoach 分别强调因果推理链与程序结构的显式建模；EviAlign 揭示了证据组织方式对检索性能的贡献；Gan Jiang 则展示了 AI Agent 在专业科学领域形成可复用分析技能的潜力。

## 效率优化与推理加速

FastOPD 通过流映射单状态教师监督与自一致性目标结合，将 π₀.₅ 的知识蒸馏为仅 2 步推理的紧凑学生模型，在 LIBERO 上保留 84% 性能同时将推理延迟降低 78.1% [FastOPD](https://arxiv.org/abs/2610.02832)。D-OPCD 将 Agent 改进后的提示作为特权上下文，通过于策略上下文蒸馏将知识内化到扩散模型权重中，使纯直接生成分数从 60.52 提升至 65.09 [D-OPCD](https://arxiv.org/abs/2610.07250)。PersonTTS 通过需求匹配的控制器初始化和源蒸馏过程引导实现个性化测试时扩展策略的摊销发现，在 AIME 和 HMMT 上显著优于强基线 [PersonTTS](https://arxiv.org/abs/2610.09684)。Δ-MOPD 将教师的最小基础 logits 偏移重新锚定在学生初始化上，避免了继承基线偏拉超过后训练偏移的问题，在三教师组合设定下数学成绩提升 4.11 分 [Δ-MOPD](https://arxiv.org/abs/2610.10460)。

分析表明，模型效率优化正从单一压缩策略转向"蒸馏 + 内化 + 个性化"的组合范式。FastOPD 和 D-OPCD 分别在 VLA 和图像生成领域实现了从大型教师到轻量学生的知识迁移；PersonTTS 和 Δ-MOPD 则从测试时计算分配和多教师整合角度降低了部署成本。

## 安全、隐私与评估基准

Inverting Multi-Vector Visual Document Indices 揭示了多向量视觉文档检索器的索引可逆性漏洞：从原始索引反演页面可恢复 47% 的词汇和 45% 的敏感 token，并将源页面排在首位的概率达 98.4%，而 token 池化和乱序两种简单防护措施可将词汇召回率降至约 8% [Inversion Attack](https://arxiv.org/abs/2610.09920)。Lineage-Aware Memory Governance 提出分析记忆单元（AMU）架构，通过完整的派生谱系图与检索策略门控实现列级访问控制，消除了 18.8-25.5% 的跨部门数据泄露 [AMU](https://arxiv.org/abs/2610.07258)。WebFovea 系统分析了视觉 Agent 在真实网站上的四阶段失败模式（解析、执行、回报、呈现），通过强化每个阶段和护栏设计将隐藏集分数从 31.0 提升至 57.0 [WebFovea](https://arxiv.org/abs/2610.03036)。RobotWorld 构建了 84 个任务的模拟测试床，揭示了当前 Agent 在感知-控制工作流构建与实际行为组合之间的能力差距 [RobotWorld](https://arxiv.org/abs/2610.10409)。

分析表明，AI 系统的安全与可靠性评估正从单一精度指标转向系统性漏洞分析和多粒度基准。索引可逆攻击和派生谱系门控分别揭示了向量存储和共享记忆的两个新兴风险维度；WebFovea 的四阶段故障分析框架和 RobotWorld 的执行轨迹分析则提供了结构化的 Agent 能力诊断方法。