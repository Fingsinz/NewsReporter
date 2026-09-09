

# 每日HFDailyPapers-2026年09月09日

## 递归自我改进与Agent后训练

NeoHorse-1提出了一种通过代理后训练实现递归自我改进（RSI）的机制，将异构模型池与智能路由结合，记录每轮交互的能力需求、服务等级和后续互动，转化为保留交错推理、工具调用和harness上下文的训练样本，并通过六维语义评估和子场景标注进行结构验证，完成评估-选择-更新闭环[NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness](https://arxiv.org/abs/2609.08183)。On-Policy Reverse Distillation (OPRD) 则从另一角度解决弱到强泛化问题，通过评估教师模型在student rollout上的策略偏移并放大验证器驱动的策略梯度，实现比现有RL和蒸馏方法更高的性能与更少的更新次数[Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation](https://arxiv.org/abs/2609.08798)。Miles v0.1是一套面向生产级前沿后训练的端到端系统，支持LoRA RL、on-policy蒸馏、监督微调及扩散模型扩展，在64块GB300 GPU上完成GLM-5.2 744B-A40B模型的异步代理RL训练，中位步时263秒[Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368)。

分析表明，后训练正从固定流程向反馈驱动闭环演进，NeoHorse-1的路由-训练-评估循环与OPRD的策略梯度放大机制均体现"学习塑造学习内容"的迭代思想；Miles v0.1的工程化设计（SGLang rollout引擎、双后端trainer、三种权重同步方案）反映了前沿RL训练对准确性、效率、可靠性与可扩展性的系统性追求。

## 语音与音频生成编辑

AuK是一个开源语音生成与编辑基础模型，统一了自然语言指令与音频上下文接口，构建了约30.3亿指令-音频实例和195万小时有效监督数据，覆盖语音生成、内容编辑、增强分离、副语言编辑和声学编辑五大任务族，采用多模态LLM进行语义 Conditioning、联合训练的VAE进行声学 Conditioning，以及混合整流流Transformer进行双流MMDiT后统一单流DiT生成；后训练结合人类反馈偏好优化和基于奖励的强化学习，并通过一致性初始化和任务路由Decoupled DMD蒸馏得到AuK-Flash，实现4步无classifier-free guidance推理，获得4.5倍加速[AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://arxiv.org/abs/2609.08936)。ReactVAU提出慢-快解耦架构用于流式视频异常理解，Fast模块基于空间网格折叠进行实时异常过滤，AAPM保护关键视觉线索，Heavyweight Slow模块仅在可疑事件时唤醒进行语义验证，显著降低重型MLLM调用成本[ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding](https://arxiv.org/abs/2609.07941)。Self-Listening针对全双工语音模型中异步文本生成、语音合成与音频播放导致的锚定中断问题，通过交错用户语音、模型文本和实际播放语音的自监听机制恢复中断，提出AnchorSpeech数据集评估一致性[What Did I Just Say? Self-Listening for Full-Duplex Speech Models](https://arxiv.org/abs/2609.05592)。

分析表明，语音生成领域正从单一任务模型向统一接口的基础模型演进，AuK通过30亿级指令数据和双阶段后训练覆盖了从生成到编辑的完整链条；ReactVAU的慢-快解耦策略为流式视频理解提供了在严格因果约束下平衡计算效率与推理深度的可行路径。

## 视觉生成与视频理解

AuK的视觉生成能力之外，RelightFormer提出前馈生成Transformer用于多视图物体重光照，通过潜层光照模块将目标环境贴图动态注入空间特征，使用排列不变位置编码处理无序多视图输入，基于9万物体和3.9万独特光照的LOD数据集训练，实现单视图、多视图和新人视图重光照的SOTA效果[RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting](https://arxiv.org/abs/2609.07414)。MovieGrid提出多网格后训练范式用于长格式多镜头视频生成，将长视频分解为时间有序块并排列在空间网格上联合建模，构建5.4万网格视频数据集，噪声自由随机网格训练和字符感知故事提示实现了同一token预算下6.05倍于Temporal Packing的镜头数生成[Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation](https://arxiv.org/abs/2609.06373)。VidaForge将视频数据配方表示为可执行五阶段工作流，通过Wan 2.1和V-JEPA 2.1的预训练实验表明广泛覆盖配方在下游基准上得分最高，同时发布含314万片段、6475小时的VIDAFORGE-3M数据集[VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes](https://arxiv.org/abs/2609.06652)。

分析表明，视频生成正从单镜头连续运动建模向多镜头叙事结构扩展，MovieGrid的网格分解设计缓解了长时序建模的计算瓶颈；数据配方研究（VidaForge）的出现表明预训练数据构建正在成为可复现、可比较的研究对象而非黑箱工程。

## 机器人学习与导航

GE-Act 2.0从头在操作数据上预训练世界-动作模型，结合控制导向自编码器(CoAE)、单步视觉规划器(SVP)和逆动力学模型(IDM)，通过知识对齐选择性优化(KASO)联合训练，在300到3万小时共训练数据 scaling 下G1-OP成功率从17.1%提升至44.1%，G2-90D尽管仅占不到2%数据但提升17.7分显示跨具身迁移能力[GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation](https://arxiv.org/abs/2609.05588)。OpenWAM将世界-动作预训练解耦为可组合模块，通过控制实验提炼出上游知识通过足够能力的生成主干和紧凑潜层空间转移、世界-动作协同需要专用动作容量和显式信息流等原则，构建OpenWAM-α并在8个仿真基准和真实机器人实验上验证[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)。TANGO提出首个全身视觉-语言-动作导航框架，给定自然语言指令和第一人称RGB观测直接预测29自由度关节空间动作，在仿真中通过全局路径规划、运动生成和RL追踪训练，零样本部署到Unitree G1人形机器人完成复杂场景导航[TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](https://arxiv.org/abs/2609.09158)。CosmoH2G提出手到夹爪迁移的大规模数据集（6189集、1254个物体）和两阶段框架，Stage I预测稀疏夹爪关键帧，Stage II生成连续动作序列，解决复杂空间运动的累积漂移问题[CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements](https://arxiv.org/abs/2609.07498)。DriveZero通过DriveRL混合代理闭环节强化学习和DriveVFM视觉基础模型整合，在nuPlan和NAVSIM基准上超越人类日志回放专家，无需人类轨迹监督[DriveZero: End-to-End Driving Beyond Human Demonstrations](https://arxiv.org/abs/2609.06055)。SynthGait-19K提供19272个从6427个动捕序列生成的步行视频数据集，用于步态参数估计，发现空间步态参数对视觉域偏移更敏感[SynthGait-19K: A Physically Grounded Synthetic Video Dataset for Gait Parameter Estimation](https://arxiv.org/abs/2609.08108)。

分析表明，世界-动作模型正从基于视频生成先验的继承预训练转向从头训练和模块化设计，GE-Act 2.0和OpenWAM的对比反映了两种不同的技术路线；人形机器人导航（TANGO）和端到端驾驶（DriveZero）均体现从仿真到真实的零样本迁移趋势，而CosmoH2G的两阶段框架针对复杂空间运动的累积误差问题提供了结构化解决方案。

## Agent系统与工具使用

Omni Interaction Agent发布Gander，一个端到端统一全感知、实时交互和代理能力的模型，采用小脑-大脑协作架构，小脑处理实时交互和全对话能力，大脑处理复杂推理和高级代理任务，通过流式Thinker-Talker架构在chunk级别扁平化输入输出为有序token流，支持全双工中断和主动反馈[Omni Interaction Agent Technical Report](https://arxiv.org/abs/2609.08977)。Procedural Graph将程序性知识组织为(procedure, relation, procedure)三元组，通过定位活跃节点和引导模型翻译子图为步骤级情境指导，LLM精炼器对比失败和成功轨迹自进化编辑图拓扑[Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](https://arxiv.org/abs/2609.09153)。FEE（Feedback-Enriched Environments）将环境适应从代理侧转向环境侧，通过从行动指导到观测丰富的转变缓解长视野任务的奖励稀疏问题，在SciWorld和BFCL基准上稳定训练动态、促进主动状态空间探索[Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks](https://arxiv.org/abs/2609.08404)。MOLE是包含150个AI代理账户、200亿token的开放基准，测试内部威胁检测能力，39个代理模型中72%完成有害目标，最佳单日内审监控器仍错过近半数已完成的伤害[MOLE: Detecting Insider Threats in AI Agents](https://arxiv.org/abs/2609.06966)。Counter-Swarm Doctrine提出以可修订协调事件为防御单位，定义未授权协调相对协作和委托授权政策的边界，通过 stigmergy 连接存储介导的协调[Counter-Swarm Doctrine: Containing Coordinated Agent Intrusions](https://arxiv.org/abs/2609.06140)。

分析表明，Agent系统正从单体模型向分层架构（如Gander的小脑-大脑分离）和结构化程序性知识（如Procedural Graph）演进，环境侧适应（FEE）体现了从训练数据扩展到训练环境设计的新思路；安全研究（MOLE、Counter-Swarm）关注多代理协同下的威胁检测，反映规模化Agent部署后的系统性风险。

## 推理效率与模型压缩

A*-Thought-V2将CoT建模为隐状态轨迹，通过3D PCA空间对齐测量局部转换与全局方向的夹角，将偏离步骤压缩为连续潜层token，引入逐步嵌入强制和标签强制训练，在Qwen3.5-9B和Qwen3.6-27B上平均准确率提升2.6%、响应长度减半、每计算单元准确率提升2.29倍[A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM](https://arxiv.org/abs/2609.07821)。BeaconKV针对长程推理中KV缓存膨胀问题，发现Thought Revisiting Tokens聚类为少量相似群，通过维护beacon查询作为全局查询群代表预测重访问KV对，实现5.8倍内存缩减和4.3倍吞吐提升[BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](https://arxiv.org/abs/2609.04971)。SQS通过贝叶斯变分学习统一剪枝和低比特量化，使用spike-and-slab先验诱导稀疏和GMM建模量化权重，在ResNet、BERT、Llama3.2和Qwen2.5上实现更高压缩率[SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions](https://arxiv.org/abs/2510.08999)。Kalman Delta Networks将循环关联记忆reformulate为线性高斯状态空间模型，通过Kalman滤波显式表示不确定性，提出对角和等方差两种GPU兼容近似，在750M和1.3B预训练中提升困惑度和下游准确率[Kalman Delta Networks: Uncertainty-aware Associative Memory](https://arxiv.org/abs/2609.07816)。Mask Forcing针对自回归视频扩散蒸馏中的模式崩溃问题，通过双噪声掩码 rollout 注入更清洁信号，缓解reverse-KL的模式寻求行为[MAsk Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout](https://arxiv.org/abs/2609.09123)。Cadence结合TimesFM-3时间序列基础模型和自适应算术编码，提供逐样本误差界，在电力需求和客流数据上较经典预测器提升13.3%-28.3%[Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Series Foundation Model](https://arxiv.org/abs/2609.06008)。

分析表明，推理效率优化正从单一压缩技术向几何驱动（A*-Thought-V2的3D PCA对齐）、聚类辅助（BeaconKV的查询群）和不确定性感知（KDN的Kalman滤波）等结构化方法演进；视频扩散蒸馏（Mask Forcing）和音频生成（AuK-Flash）均通过蒸馏实现推理加速，反映高效推理与模型压缩已成为规模化部署的关键瓶颈。

## 3D理解与几何估计

Marigold V2重新审视DiT架构在单目深度估计中的应用，提出单步推理配方和两阶段微调协议（基于Sinkhorn损失），在KITTI和ETH3D上AbsRel提升16-26%，解决毛发、树叶等边缘细节[Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation](https://arxiv.org/abs/2609.08084)。TransNormal-2针对VAE 8x空间压缩导致的法向量边界退化问题，在训练时引入几何感知像素空间损失（逆渲染自一致性、von Mises-Fisher角度损失、小波边缘正则化），在推理时通过几何精炼模块（GRM）应用RGB引导残差校正，在透明物体上MAE降低4.2°-3.1°[TransNormal-2: Geometry-Grounded Rectified Flow with Edge-Aware Decoding for Precise Normal Estimation](https://arxiv.org/abs/2609.06665)。CoVeR提出基于覆盖的token裁剪用于多视图3D推理，通过确定性无训练选择器使用token坐标实现精确场景覆盖和预算控制，仅用约8%视觉token保留93.5%全token性能[CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs](https://arxiv.org/abs/2609.08345)。PriorEdit3D通过生成先验蒸馏学习无配对监督的3D编辑，利用可微渲染从2D图像编辑模型获取视觉先验、从VLM获取语义先验，并引入3D感知分布匹配正则化约束几何一致性[Learning 3D Editing without Paired Supervision via Generative Prior Distillation](https://arxiv.org/abs/2609.04942)。

分析表明，3D几何估计正从直接回归向扩散模型驱动的精细化推理演进，Marigold V2和TransNormal-2均针对VAE解码退化这一共同瓶颈提出不同侧重的解决方案；CoVeR的确定性覆盖选择和无监督3D编辑（PriorEdit3D）反映了多视图推理效率与数据依赖问题的并行探索。

## 多模态理解与评估

RoBoSPA提出机器人空间-过程评估，涵盖精细空间推理和长视野程序规划两个维度，280个变体任务、52.7万轨迹，诊断当前VLA模型在复杂空间关系、精确低层执行和内存密集规划上的不足[RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?](https://arxiv.org/abs/2609.05324)。UCF-Net结合CLIP的语言对齐语义先验和DINO的自监督视觉结构先验，通过层次特征提取、逐层专家聚合和熵导出不确定性的加权融合提升deepfake检测泛化能力[Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection](https://arxiv.org/abs/2609.07670)。Steering Geometry基于Schwartz基本价值观理论构建2.6万样本基准，发现分布驱动方法恢复的人类价值拓扑与理论预测对齐（Spearman ρ达0.51），而行为中心方法与预期价值几何相关性低[Steering Geometry: Validating Human Value Geometry in LLM Steering Space](https://arxiv.org/abs/2609.06289)。Encoded Early, Used Late通过ExpertCollab语料发现对话伙伴专业性在Transformer早期层可解码但在中期后才变为因果活跃，信息可读与使用之间存在跨越网络一半深度的间隙[Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner's Expertise](https://arxiv.org/abs/2609.07139)。CVRR提出因果视觉递归推理，通过移除视觉状态和多模态KV缓存使递归计算成为预测的必要路径，区分潜层信息性与实际用于预测的潜层计算[Reason Through the Latent! Making Latent Visual Reasoning Necessary](https://arxiv.org/abs/2609.06746)。

分析表明，多模态评估正从性能导向向诊断性评估演进，RoBoSPA的二维分级设计和Steering Geometry的价值几何验证均体现对模型能力边界的系统性探查；Encoded Early, Used Late和CVRR从可解释性角度揭示Transformer内部表征与使用的时空分离，为模型干预提供理论约束。

## 自动驾驶与场景生成

SceneMosaic结合图像先验和VLM代理演化生成仿真就绪场景，通过局部单元独立演化再组合为全局场景，在SceneEval-100上以24倍速度匹配最强代理基线语义布局质量[SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution](https://arxiv.org/abs/2609.05594)。DriveZero的DriveRL将真实驾驶日志转换为交互世界，通过价值引导测试时动作搜索在nuPlan社区分割上达到93.57平均分[DriveZero: End-to-End Driving Beyond Human Demonstrations](https://arxiv.org/abs/2609.06055)。

分析表明，自动驾驶正从日志模仿向闭环节强化学习迁移，DriveZero的两阶段预训练（感知+行动）体现了模块化设计的优势；SceneMosaic的混合代理演化为仿真场景生成提供了效率与物理有效性的平衡方案。

## 其他动态

"Agentic Visual Generation"提出L0-L4四层次控制器能力框架，将生成系统代理性定义为控制器可直接控制生成过程的深度而非模型规模或工具数量[Agentic Visual Generation: From Generative Models to Agentic Control](https://arxiv.org/abs/2609.06758)。"MasterControl Seventeen Every Time"研究表明确定性策略执行在受控分析类中比运行时LLM规划更具可复现性，440次运行中策略执行匹配110/110而LLM规划0/330[MasterControl Seventeen Every Time](https://arxiv.org/abs/2609.03209)。"Recognition-Refusal Misalignment in LLMs"发现模型隐藏状态中存在可分离回答/不可能问题的线性方向，但该方向与安全拒绝方向几乎正交，确认 confident-on-impossible 失败是路由问题而非编码问题[Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswerable Questions](https://arxiv.org/abs/2608.29109)。"Measuring Language Transfer in Robot Policies"报告希腊语机器人策略的多语言实验，发现双语训练比单语提升6.7-7.1分但仅达英语性能的约2/5，强调建立保证零基线和多种子复现对低资源定位的必要性[Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy](https://arxiv.org/abs/2609.07470)。"Online Draft Co-Training"解决大规模长上下文RL后训练中的投机解码扩展问题，通过扩展zigzag环注意力支持分支attention和TapChannel跨流水线阶段传输特征，在122B模型上实现 rollout 和端到端加速[Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training](https://arxiv.org/abs/2609.07108)。