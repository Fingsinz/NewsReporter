

# 每日HFDailyPapers-2026年09月04日

## 终端与代码Agent训练：从轨迹重建到环境演化

终端Agent的轨迹数据已积累至大规模，但可执行、可验证的环境仍相对稀缺。[Terminal-Universe](https://arxiv.org/abs/2609.04148) 提出将既有轨迹还原为可复用工作空间：通过回放文件操作恢复修改前状态，再利用补全Agent填补缺失文件与依赖，最终在此之上重建原始任务并合成新任务。该框架还沿"广度"与"深度"两个维度扩展任务——广度上挖掘跨代码库的依赖关系生成多工作空间查询，深度上通过用户Agent将单轮查询延伸为多轮交互。在37.3k任务充足环境上对Qwen3.5-27B进行SFT，Terminal-Bench 2.1单轮性能提升11.9分，EvoCode-Bench v2 MT@4多轮性能提升13.8分。

与此相呼应，[Environment Evolution for Terminal Agents](https://arxiv.org/abs/2609.04128) 关注训练过程中环境难度的持续性供给。现有共演化方法依赖在线 rollout，随着模型能力提升容易产生学习信号衰减。该研究提出"环境演化"策略，通过离线方式沿三个从多轮学习目标推导出的方向增量提升环境难度，并在训练世代间调度演化后的环境。在Qwen3.6-27B与Qwen3.6-35B-A3B上的长程RL训练验证显示，Terminal-Bench 2.1性能分别提升14.4与18.0个百分点。

分析表明，轨迹到环境的可逆还原正在成为终端Agent训练的基础设施路径：一方面解决了环境稀缺问题，另一方面通过系统性难度调度避免了过拟合。结合[DRACO](https://arxiv.org/abs/2609.04094) 对长程Agent的细粒度信用分配机制（在AppWorld上较基线提升15.9分），终端Agent训练体系正从"静态环境+粗粒度奖励"向"动态演化环境+细粒度rubric分配"演进。

## 视觉生成与3D世界建模：从图像到物理一致性

图像生成领域，[LLaDA-Image](https://arxiv.org/abs/2609.03796) 采用纯视觉预训练构建生成先验，再与冻结的LLaDA2.0-Mini视觉语言模块配对，形成6B DiT统一架构。通过无参数RMSNorm与Muon优化器实现可扩展训练，在Qwen-Image-Bench英文与中文赛道分别取得53.53与53.38分，创开源模型新SOTA。同时推出的LLaDA-Image-Turbo支持2-4步快速推理。

3D世界建模方面，[Puffin-World](https://arxiv.org/abs/2609.04196) 提出统一多模态架构，联合建模物理（重力场与纬度）、几何（深度）与外观（图像）三种原生世界状态，并引入Omni-Camera表示支持多样化任务。配套构建的Puffin-16M数据集包含1500万视觉-语言-相机三元组与100万轨迹。在相机条件世界模型奖励建模上，[WorldReward](https://arxiv.org/abs/2609.03952) 利用VLM的统一推理空间将视频分解为动作对齐片段，分别聚合动作一致性与视觉质量偏好，在HY-WorldPlay 1.5的RL后训练中同步改善动作执行与视觉质量。

视频生成的物理一致性仍是挑战。[Principia](https://arxiv.org/abs/2609.04200) 建立依赖关系一致性而非绝对运动测量的评测基准，覆盖重力、摩擦、碰撞等八类牛顿物理现象。测试六款主流视频生成模型发现，所有模型得分均低于0.42，而VLM在检测物理违规方面最佳准确率仅67%。

可编辑视觉设计方面，[Editable Visual Design](https://arxiv.org/abs/2609.04034) 将VLM定位为"创意大脑"负责需求理解与审美判断，图像生成模型作为"视觉世界模拟器"按需合成独立资产，通过"先想象后行动"的闭环工作流生成含解耦图层与真实文本的HTML/CSS产物。

视频渲染效率上，[FlashRender](https://arxiv.org/abs/2609.03563) 通过Representation Transformation and Alignment (RETA) 消除采样步依赖的相机控制误差，结合MeanFlow目标与on-policy流映射蒸馏，在25倍采样成本降低的同时匹配多步基线质量。

分析表明，视觉生成正从单一图像质量竞争转向物理一致性、3D世界建模与可编辑性的多维突破。Principia的评测结果揭示当前生成模型在物理关系推理上仍有显著短板，而Puffin-World与WorldReward的工作表明联合建模多模态世界状态与引入VLM奖励信号是可行的改进路径。

## 模型效率：KV缓存、量化与上下文压缩

推理效率优化方面，[Random Attention](https://arxiv.org/abs/2609.03430) 重新审视长链推理中KV缓存的驱逐策略。传统方法按token重要性打分保留top-k，但该研究证明选择信号贡献几乎为零——保留prompt并随机驱逐其余token即可匹配最强先前行驱逐器，并在vLLM部署中实现32-43%吞吐量提升。控制实验揭示推理轨迹在文本层面（模型重述所需信息）与注意力头层面（各头保留副本）具有自保护冗余性，因此无需复杂打分。

模型量化上，[Why Gated DeltaNet Survives 4-Bit Quantization](https://arxiv.org/abs/2609.04098) 对Qwen3.8-27B混合架构（48层GDN + 16层softmax注意力）实施全量NVFP4 W4A4量化（Minima项目）。六任务平均仅比BF16低0.52分，显存仅17.5 GiB且prefill速度提升14-19%。机制分析揭示四个原因：NVFP4的16元素块缩放局部化残差流异常值；门投影对量化误差最不敏感（压缩约11% GEMM误差至约2%输出误差）；delta规则递推将注入噪声维持在平坦平台并在数百步内遗忘状态脉冲；逐token量化成本随上下文增长被摊薄。

上下文压缩方面，[LatentPress](https://arxiv.org/abs/2609.01507) 提出超越文本与图像的连续记忆token表示。小型读写器适配器（4.2M-26.2M参数）压缩4-16倍，在LongMemEval上达到0.504准确率（ uncompressed为0.490），显著优于文本摘要（0.184）与OCR压缩（0.312-0.426）。写入仅需43ms每轮对话，读取速度为原始上下文或缓存OCR的5-9倍。

长视频多模态模型中视觉Token分配策略的受控实验（[Select, Compress, Reinvest](https://arxiv.org/abs/2609.03820)）显示：选择是最关键杠杆，八帧查询选择较均匀采样十六帧提升6.9分；正交匹配追踪算法可与专用选择器媲美；压缩本身收益有限，但将节省的token再投资于更多压缩帧可额外提升2-3分。

分析表明，KV缓存管理正从精细化选择转向"保留关键部分+随机其余"的简约策略；混合架构全量4比特量化可行性被验证，打破了对递归层高比特保留的直觉；连续token上下文接口为机器对机器压缩提供了新范式。

## 流式多模态理解与音视频生成

流式视频理解方面，[LatentStream](https://arxiv.org/abs/2609.04131) 将记忆范式从"存储-检索"转向"检索-内化"。通过Jenks引导的自适应整合将视觉历史组织为短/中/长期三级分层记忆，查询到达后 latent memory token逐步扩大感受野并迭代检索历史证据，最终整合为固定长度压缩记忆。配合渐进式置信度引导的记忆优化，在在线与离线视频基准上均达SOTA。

组合推理能力上，[CORE](https://arxiv.org/abs/2609.04083) 针对MLLM embedding模型在属性-对象绑定区分上的不足，通过reranker蒸馏将交叉注意力reranker的细粒度排序判断融入embedding模型。引入Rank-KL目标在五层组合匹配度上训练，在COLA、SUGARCREPE++、NEGBENCH三个基准上，CORE-EMBED-8B取得0.666总平均分，超越Jina-Reranker 10.7分。

音视频同步生成中，[Temporal Context Routing (TCR)](https://arxiv.org/abs/2609.02367) 解决脚本驱动生成中时间对齐缺失问题。现有模型仅将脚本 timing 编码在文本表示中而未对齐到视频/音频时间轴，导致音画同步但偏离剧本。TCR将脚本时序映射到共享时间轴并路由至双模态生成位置，在200个测试脚本上将Shot Boundary MAE降低96%（1.11s→0.042s），Dialogue Acc@0.5s从28.3%提升至84.1%。

分析表明，流式理解的记忆机制正从外部检索转向内部压缩表征；组合推理评估揭示了embedding模型与reranker能力鸿沟，蒸馏是有效填平路径；音视频生成中时间维度的显式解耦对齐成为叙事连贯性的关键。

## 模型训练方法论：蒸馏、校准与优化动力学

在线策略蒸馏（OPD）的数据需求方面，[Rethinking On-Policy Distillation](https://arxiv.org/abs/2609.04172) 在单样本极限下检验发现，单查询OPD可持续优化数百步并恢复全数据训练大部分增益。单查询已达全数据状态覆盖率的71.5%，16个语义 diverse 查询可达98.9%。核心发现是OPD"数据过剩但算法饥饿"——rollout快速暴露广泛监督信号，但学生模型吸收速度递减。

校准方法上，[CORD](https://arxiv.org/abs/2609.01072) 提出Prediction-Preserving Repair，在post-hoc校准后修复概率向量以保留原始top-1预测。通过协调修复质量保留校准输出的平均质量，在CIFAR-10/100与ImageNet-1K上实现零TPCR同时降低ECE、NLL与Brier分数，且无需超参调优。

优化动力学视角，[Percolation Dynamics in Optimization](https://arxiv.org/abs/2609.02373) 将SGF建模为渗流过程，揭示架构对称性迫使子网络以离散块合并而非逐个合并，产生宏观有序参数的方差尖峰，类似物理相变。该机制在Adam/AdamW与重尾噪声模型下同样成立。

经验迁移方面，[Knowing When Not to Reuse](https://arxiv.org/abs/2608.26730) 在自主LLM后训练中提出BCIT方法，将观测效果绑定至源上下文、检查适用条件、否决硬冲突候选。在4B模型跨金融推理、text-to-SQL、函数调用实验中，BCIT授权更少有害更新并 attainment 更高等预算最终模型质量。

[Compile by Training](https://arxiv.org/abs/2609.04199) 将自然语言规范编译为可复用神经函数：教师模型生成任务特定示例训练小型适配器，编译后函数无需教师即可运行、版本化与组合。在FuzzyBench-Hard上达83.6%语义准确率，已部署为公开交互式服务。

分析表明，训练方法论正从"更多数据+更长训练"转向"更聪明的数据利用+算法效率优化"。OPD的单样本可行性挑战了数据规模假设，校准修复分离了置信度校正与预测稳定性的优化目标，渗流动力学为理解优化轨迹提供了物理类比框架。

## 3D重建与视觉识别

在线3D重建方面，[Scal3R](https://arxiv.org/abs/2609.04201) 针对长视频重建中pose相对于固定首帧锚点的外推漂移问题，将问题重构为多参考相对pose查询。仅约1%参数的轻量可学习token通过非对称注意力注入冻结骨干网络，配合带回环检测的在线pose图优化抑制长程漂移。在KITTI上较在线基线降低60%以上ATE，在Virtual KITTI、Sintel、TUM-Dynamic、ScanNet、7-Scenes上达SOTA，单GPU训练仅需8小时。

显微镜细胞分割上，[QCell](https://arxiv.org/abs/2608.29253) 解决重叠细胞实例的半透明弱边界问题，通过潜空间分解与重组query表示实现全局推理，配合对比query对齐目标分离重叠细胞query。在ISBI2014上达到+2.2 AP与+2.7 AJI提升，并引入Organoid新基准。

## 评估基准与用户请求理解

编码Agent评估方面，[RealSWE](https://arxiv.org/abs/2608.27831) 揭示SWE-bench等基准与真实用户请求的信息构成差异：仅含问题描述的请求占真实prompts 88%，但仅占基准问题7%；87%真实请求为口语化风格，94%基准问题为正式风格。构建的381个多变异任务族评估七款LLM发现，真实输入使解决率平均下降6.4pp，包含Desired Behavior与Motivation显著提升性能，而Environment Information与Reproduction Steps仅增加token无测量收益。

翻译评估上，[Last Translation Benchmark (LTB)](https://arxiv.org/abs/2609.04173) 针对现有基准趋近饱和、自动指标易受reward-hacking、人工评估缺乏可重复性等问题，提供人工编写与同行评审的失败案例集合，每个示例附手工验证规则描述具体失败情形，支持可靠可操作的持续评估。

个性化助手冲突检测方面，[PACE](https://arxiv.org/abs/2609.03293) 评估模型识别潜在冲突约束的能力——用户请求基于明确persona，需从自我中心知识库检索隐式事实判断请求是否冲突。提出的PaceMaker多智能体框架协调query reformulation、多跳图遍历与冲突感知过滤。

Agent行为分析方面，[AutoTraceGT](https://arxiv.org/abs/2608.30391) 将扎根理论自动化引入Agent轨迹分析，通过迭代开放编码、轴心编码与理论编码直至饱和，生成任务定制行为分类法。在六个轨迹语料库上恢复73-91%人工标注失败模式并发现额外模式，作为演绎特征空间在下游失败预测上超越零样本/少样本LLM基线。

## 其他动态

本次收集的其他论文包括音频视频生成的时间对齐研究、细胞分割的query recombination方法，以及多Agent协调的 grounded theory 自动化分析框架，均围绕提升AI系统可解释性、评估可靠性与训练效率展开。