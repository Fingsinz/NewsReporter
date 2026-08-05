

# 每日HFDailyPapers-2026年08月05日

## 实时视频编辑与生成

多份研究聚焦于视频生成与编辑的效率提升与架构创新。JoyAI-Video-Edit 提出一种16B参数的自回归扩散框架，实现720p视频在单卡B200 GPU上约30 FPS的实时编辑，通过分块自回归适配、源锚定分布匹配蒸馏（SA-DMD）和长程自回归蒸馏缓解训练-推理不匹配和时序漂移 [](https://arxiv.org/abs/2608.03974)。UniWorld-Design 则将图像生成从像素层面重新定义为图层原生设计，引入Text-to-RGBA和Image-to-Layer两个模型，支持语义RGBA图层作为生成的原子单元，在Crello基准上相对Qwen-Image-Layered提升34%的Alpha Soft IoU [](https://arxiv.org/abs/2608.03971)。MiniWorld 提供从头训练流式视频世界模型的轻量可复现框架，在预训练视频VAE的潜空间中使用块因果Video Diffusion Transformer结合Flow Matching，可在单台8卡服务器上数天内完成训练 [](https://arxiv.org/abs/2608.01127)。

分析表明，实时视频编辑正从离线系统向流式因果生成范式迁移，核心挑战在于如何在有限计算资源下维持时序一致性与源保真度。图层原生设计为视频编辑引入了可解释的操作空间，而视频世界模型从预训练微调转向从头训练趋势反映了社区对因果建模与效率的重新审视。

## 多模态视频理解与Agent

Video-DeepResearch 将多模态Agent从静态图像扩展至连续视频流，提出解耦的感知-探索流水线与分阶段工具解锁机制，Video-DeepResearch-35B-A3B在自建的Video-DR-Bench上达到64.0%准确率，超越Claude-4.5-Sonnet 5.0个百分点 [](https://arxiv.org/abs/2608.03979)。GROVE 是一种免训练的框架，支持从连续视频流中因果增长时间分层记忆，涵盖细粒度感知证据、时间戳时刻、连贯片段和跨日模式，在MM-lifelong和EgoServe基准上达到最佳结果 [](https://arxiv.org/abs/2608.02392)。TurnSight 提出轮次级后见之明自蒸馏框架，从执行条件的后见之明中提取监督信号，通过多前瞻视界交叉验证选择可靠监督，在三个基准上验证了有效性 [](https://arxiv.org/abs/2608.04007)。V2N 首次实现完整的视觉钢琴转录系统，通过共享时间主干和任务特定头联合训练 onset、offset、按键保持和力度，在PianoVAM和R3基准上创出新纪录 [](https://arxiv.org/abs/2608.03419)。

分析表明，视频理解研究正从单帧或多帧分析转向连续流式处理，核心瓶颈在于时空密集定位与开放网络探索的结合。Agent架构设计中，工具使用偏置和参数知识泄漏被识别为关键问题，分阶段解锁和后见监督为缓解这些问题提供了可行路径。

## Agent技能学习与安全

四项研究关注Agent技能的生命周期管理及其安全风险。PAST-Bench 通过开启/关闭保留经验的对照实验，系统评估个人Agent的递归自我改进能力，发现跨七种基础模型和四种Agent框架，改进存在但策略执行路径的证据不一致，并据此开发Hermes+提升经验利用的清晰度 [](https://arxiv.org/abs/2608.04003)。ContinualSkillBench 评估在上下文持续技能学习中技能的演化能力，发现虽然顺序执行普遍改善性能，但低能力模型倾向于积累更碎片化的技能集合 [](https://arxiv.org/abs/2608.03874)。SkillJack 揭示自我进化Agent的新攻击面：恶意经验可被Agent自身转化为持久行为制品，在SkillX和Anything2Skill上实现56.2%和89.2%的攻击成功率，80%的技能介导攻击在原始记录删除后仍存在 [](https://arxiv.org/abs/2608.03509)。AntiSkillBench 评估人格技能管道的隐私泄露与冒充风险，发现风险跨Agent骨干和蒸馏协议持续存在，现有防御在多种配置下效果有限 [](https://arxiv.org/abs/2608.03700)。

分析表明，Agent技能的学习与固化机制正成为安全研究的新焦点。经验到技能的转化虽能提升效率，但也放大了 poisoning 攻击的隐蔽性和持久性，技能提取过程中的 sanitization whitewashing 和 persistence isolation 现象提示需建立溯源感知的技能生命周期保护机制。

## 扩散语言模型与Efficiency优化

LLaDA MoE v2 系统表征混合专家扩散语言模型的扩展行为，发现最优名义批次规模增长更快、最优学习率衰减更快，IsoFLOP分析显示轻微的数据端倾斜，训练30B-A3B模型在23.5T token上预训练，接近Qwen3性能 [](https://arxiv.org/abs/2608.03457)。AURORA-LM 提出连续潜变量扩散语言模型，将可解码文本表示的构建与分布建模分离，使用基于查询的编码器-解码器组织文本为高容量前缀对齐潜序列，结合块因果Diffusion Transformer，在OpenWebText和XSum上达到最强性能 [](https://arxiv.org/abs/2608.02602)。OmniPack 是一种免训练的统一令牌压缩框架，协调LLM前的结构压缩与LLM内的语义精炼，在Qwen2.5-Omni-7B上将FLOPs降至16.7%同时保留98%性能 [](https://arxiv.org/abs/2608.03812)。Any-OPD 提出跨架构的在线策略蒸馏框架，通过冻结的视觉表示桥接不同模型，将12B FLUX.1-dev蒸馏至2.5B SD3.5-Medium，PickScore从0.846提升至0.884 [](https://arxiv.org/abs/2608.03316)。RestoreKV 通过参数高效自蒸馏恢复激进KV缓存驱逐下的性能，仅优化0.4%参数，在5%预算下将KVzip在RULER-4K上的得分从38.2提升至73.2 [](https://arxiv.org/abs/2608.01247)。

分析表明，扩散语言模型的扩展规律与传统自回归模型存在定量差异，数据分配策略需相应调整。模型压缩与蒸馏技术正从同架构迁移转向跨架构泛化，通过表示空间桥接和轨迹对应恢复，使知识蒸馏突破架构绑定限制。

## 3D生成与多模态统一模型

Hunyuan3D-Buffalo 1.0 提出统一的3D多模态框架，支持3D理解、文本到3D生成、指令引导3D编辑和文本 grounded 部分生成，构建87M规模3D多模态语料库，结合Hunyuan3D-VLM与Hunyuan3D DiT架构，在多项3D生成与编辑基准上达到SOTA [](https://arxiv.org/abs/2608.02711)。ST-WAM 提出语义-时间世界动作模型，使用DINOv3作为未来预测与历史检索的共享语义表示，同时保留VAE细粒度动态，在LIBERO上达到98.7%成功率，在视觉分布偏移下的零样本LIBERO-Plus性能提升21.3个百分点 [](https://arxiv.org/abs/2607.28993)。CAPEval 解耦图像描述评估为Coverage和Precision两个维度，发现Coverage与理解性能相关性更强，Precision是生成性能的主导预测因子 [](https://arxiv.org/abs/2608.02589)。

分析表明，3D生成正从单一任务模型向统一多模态架构演进，理解与生成的联合训练被证明可相互促进。世界模型的研究从纯像素级预测转向语义-动态联合建模，以缓解视觉分布偏移带来的泛化瓶颈。

## 评估基准与方法论

五项研究提出新型评估基准。ChronoLens 在统一分析空间中测量跨语言、历史时期和语言层面的变化，涵盖1803-2026年四千万文档，发现形态、句法、语义和语用变化幅度相当但轨迹各异 [](https://arxiv.org/abs/2608.03507)。MerchantBench 构建365天订单级电商模拟，评估Agent的长期一致性，最佳LLM配置仅达成人类参与者27.3%的净资产 [](https://arxiv.org/abs/2607.28956)。ExplainBench 自动评估代码Agent生成的解释质量，发现解释质量是独立的评估维度，且解释常错误声称补丁正确性 [](https://arxiv.org/abs/2607.26451)。FinIndices 评估LLM在未裁剪财务报表上的结构化推理，揭示知识瓶颈与结构瓶颈两大脆弱性，移除公式提示后性能骤降 [](https://arxiv.org/abs/2607.28661)。PosterMELD 通过模板条件多Agent流水线生成可编辑海报，实现81.3%的Print-Ready率，成本仅为Codex+Skill的3.5% [](https://arxiv.org/abs/2608.02218)。

分析表明，评估基准正从静态单任务向动态长周期、多粒度维度演进。Agent评估特别强调长期一致性和解释可信度，揭示当前模型在持续任务中与人类表现的显著差距。

## PCSD自蒸馏与世界模型概念

PCSD 提出持久一致性自蒸馏框架，从教师信号局部持久性派生令牌级蒸馏权重，结合自适应窗口与指数衰减聚合，在ALFWorld上超越GRPO 15.6和13.3分 [](https://arxiv.org/abs/2608.01837)。《When Attention Goes Blind》识别ALiBi位置编码的线性偏差下溢问题，导致大量注意力权重为零，建议对数缩放距离作为缓解策略 [](https://arxiv.org/abs/2608.03994)。《Quo Vadis, World Modeling?》将世界模型从物理状态预测扩展为代理中心交互式世界代理，归纳为六种功能形式（动力学、空间、执行、记忆/经验、技能、奖励/验证代理）和三个进化层级 [](https://arxiv.org/abs/2608.02713)。

分析表明，RL训练中的监督信号质量直接影响Agent学习效率，持久性信号聚合比瞬时差异更能抵抗噪声。世界模型的概念边界正在扩展，从状态预测转向提供可操作反馈，为Agent的持续改进提供统一框架。

## 其他动态

KGD 提出知识-几何解耦框架用于流式推荐，将可刷新编码器与任务学习器分离，已在Shopee部署，A/B测试显示GMV提升1.75% [](https://arxiv.org/abs/2608.02738)。STAMPlus 解决多模态大语言模型的分割三重困境，通过结构化全掩码预测将12类别延迟从13.5秒降至5.16秒 [](https://arxiv.org/abs/2608.02791)。Decoding Children's Gait 建立儿童步态分析数据集与基线，揭示当前SOTA方法难以捕捉临床细微差异 [](https://arxiv.org/abs/2608.00371)。Push-Wiper 将粘性污渍清洁重新表述为聚合问题，使用扩散策略生成分段推送轨迹，清洁得分较基线提升130% [](https://arxiv
<|mask_start|>