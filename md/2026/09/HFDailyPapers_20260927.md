

# 每日HFDailyPapers-2026年09月27日

## Transformer线性叠加与隐空间语言学特征

两项研究分别从架构行为和表示学习角度揭示LLM内部结构。Superposition Linearity研究证明Transformer具有线性叠加特性：当来自不同文本流的输入线性组合时，模型输出为各单独下一个token分布的叠加，且这种叠加线性是Transformer架构的内生属性，随预训练进展反而减弱，但可通过轻量微调恢复[https://arxiv.org/abs/2609.29845](https://arxiv.org/abs/2609.29845)。SAE隐空间中词性涌现类别研究则表明，稀疏自编码器能够从高维激活中恢复词性区分，但词性类别并非对应单一潜在变量，而是由稀疏特征的紧凑组支持，且开放类与封闭类词性存在显著差异[https://arxiv.org/abs/2609.29362](https://arxiv.org/abs/2609.29362)。

分析表明，Transformer的内生线性为多任务并行推理提供了理论依据，引导解码器可同时生成两个连贯续接的能力值得进一步探索；SAE结果则提示语言学结构在模型表示中以分布式、类别依赖的方式组织，而非原子化语法特征，这为模型可解释性研究提供了新的方向。

## 视频与音频生成：提示增强、联合生成与高效训练

视频生成领域呈现三条技术路线。WanPE通过397B参数模型在1.05M真实视频上训练，采用视频接地反向构建和语义一致性GRPO策略实现电影级提示增强，在5-15秒区间将人类偏好提升10.66-18.84分，30秒区间提升达50.86分[https://arxiv.org/abs/2609.30221](https://arxiv.org/abs/2609.30221)。AV-GRPO针对音视频联合生成中的跨模态同步问题，提出模态锚定扩散强化学习框架，将耦合的多模态偏好学习转化为单模分子问题[https://arxiv.org/abs/2609.29816](https://arxiv.org/abs/2609.29816)。ViRDM则针对少步因果视频生成，提出无需教师模型和判别器的表示分布匹配后训练方法，仅用20次生成器更新即在VBench达到84.87分，仅需16个A100 GPU小时[https://arxiv.org/abs/2609.28923](https://arxiv.org/abs/2609.28923)。

分析表明，视频生成正从单纯质量提升转向多模态联合与计算效率优化，WanPE的提示增强和AV-GRPO的模态解耦反映了跨模态对齐的深入探索，而ViRDM去除训练链路中大部分组件的设计体现了对生成效率的优化需求。

## 世界模型与物理认知

两项研究探索世界模型的认知能力边界。WROP引入物体恒常性和实体性等人造认知先验，构建150个人工设计的认知科学任务，训练16B模型PWM-WROP，在盲测Elo排名中位列第三[https://arxiv.org/abs/2609.28654](https://arxiv.org/abs/2609.28654)。Agent-Editing World Model则提出AEWM，建模推理和行动如何塑造任务进展而非预测工具响应，通过Action Judge区分关键、探索和无噪声决策，并用State Revision编辑污染的历史状态[https://arxiv.org/abs/2609.28416](https://arxiv.org/abs/2609.28416)。

分析表明，世界模型研究从被动预测转向主动认知构建，WROP强调物理常识的内化而AEWM强调任务状态的可编辑性，两者均针对长程Agent任务中的状态污染问题提出了解决方案，体现了世界模型在Agent系统中的实用性转向。

## 机器人操作与具身智能

三项研究聚焦具身Agent的感知-行动闭环。World Action Agent构建视觉动作工作空间，通过接触视图、动作预演和视野内校正实现VLM驱动机器人操作，在LIBERO-Pro达到75.6%成功率[https://arxiv.org/abs/2609.29964](https://arxiv.org/abs/2609.29964)。DeltaWAM针对双臂操作提出增量世界动作模型，联合预测视觉增量和动作，结合流式增量内存降低推理延迟[https://arxiv.org/abs/2609.28811](https://arxiv.org/abs/2609.28811)。OmniEchoBench提出空间音频-视觉感知基准，包含197个真实场景和30个环境的FOA音频数据，OmniEcho模型在此基础上实现空间音频理解[https://arxiv.org/abs/2609.23407](https://arxiv.org/abs/2609.23407)。

分析表明，具身智能正从单一视觉通道向多模态空间感知演进，DeltaWAM的增量预测设计体现了对计算效率的优化，而空间音频的研究填补了多模态感知中听觉维度系统评估的空白。

## Agent系统与自主决策

六项研究覆盖Agent的训练方法、搜索策略与系统架构。Rufus-Air提供基于GLM-4.5-Air-Base的八阶段后训练配方，从SFT到RLHF逐步进阶[https://arxiv.org/abs/2609.29421](https://arxiv.org/abs/2609.29421)。IterSynth通过规划器与合成器的角色解耦减少上下文噪声，在五个深度搜索基准上达到50.7平均分[https://arxiv.org/abs/2609.29444](https://arxiv.org/abs/2609.29444)。Qwen-Planner-Agent构建闭环AI-for-AI框架，通过CARE奖励工程降低推理成本[https://arxiv.org/abs/2609.29892](https://arxiv.org/abs/2609.29892)。Coding Agents在28个模拟环境中验证，Claude Code和Codex配置在广义任务与运动规划上均超过手工规划器[https://arxiv.org/abs/2609.30233](https://arxiv.org/abs/2609.30233)。AgentKernel提出信任原生Agent操作系统，在身份、感知、认知和执行四个支柱上提供强制安全保障[https://arxiv.org/abs/2609.29647](https://arxiv.org/abs/2609.29647)。RGBD20K提供20,000对RGB-D图像和160个细粒度类别的大规模分割数据集[https://arxiv.org/abs/2609.29028](https://arxiv.org/abs/2609.29028)。

分析表明，Agent研究从单一模型能力扩展至系统级工程，Rufus-Air的可复现配方、IterSynth的架构解耦和AgentKernel的安全基础设施反映了该领域对标准化、可解释性和可信性的需求，Coding Agents的有效性验证则为自动化规划提供了新的工具范式。

## AI对齐、评估与数学发现

三项研究关注AI系统的能力边界与可靠性。Jev通过强化学习训练校准决策模型，在RLCDAlignBench的10种对齐失败类型上实现0.886的零样本AUROC，成本仅为LLM裁判的1/63[https://arxiv.org/abs/2609.29429](https://arxiv.org/abs/2609.29429)。ExplorationBench构建可验证的外星世界环境，包含AlienCode和AlienLogic两个沙盒，测试系统获取并应用新规则的能力[https://arxiv.org/abs/2609.30199](https://arxiv.org/abs/2609.30199)。Learning to Discover Interesting Mathematics定义定理有趣度为证明长度与陈述长度之比，优化后模型生成定理与Mathlib的重叠率从91.9%降至30.6%[https://arxiv.org/abs/2609.28603](https://arxiv.org/abs/2609.28603)。

分析表明，AI评估正从性能导向转向可靠性和新颖性导向，Jev的高效对齐检测、ExplorationBench的可验证探索框架和数学有趣度指标均为AI系统的可信与创造性提供了量化标准。

## 游戏AI与空间感知

PUBG Ally展示游戏场景中语音交互与实时决策的融合，在接近39,000场真实玩家对局中收集训练数据，通过模型压缩和运行时防护实现低延迟设备端执行[https://arxiv.org/abs/2609.29837](https://arxiv.org/abs/2609.29837)。Neural Spectral Capacity提出基于权重矩阵奇异值谱的架构评估指标，可在秒级时间内为Transformer和CNN架构选择提供全局最优解[https://arxiv.org/abs/2609.23087](https://arxiv.org/abs/2609.23087)。

分析表明，游戏AI从单纯性能追求转向玩家体验与实时性的平衡，而NSC则为模型架构设计提供了无需训练的快速评估工具，两者分别代表了应用落地和基础研究两个维度的进展。

## 其他动态

图像质量评估方面，IDQD方法将全参考IQA指标近似为输入依赖二次型失真，在VVC编码器中实现14.2-36.7%的BD-rate节省[https://arxiv.org/abs/2609.30077](https://arxiv.org/abs/2609.30077)。