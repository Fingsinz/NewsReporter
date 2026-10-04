

# 每日HFDailyPapers-2026年10月04日

## Agent Harness 优化与自动化课程学习

ActiveSaddler 将 harness 优化中的训练场景选择形式化为自动化课程学习问题，通过非平稳 bandit 建模动态优化的失败模式，自适应平衡已知弱点修复与新场景探索，在 GAIA2 和 Terminal-Bench 2.0 上分别提升 4.4 和 7.5 个百分点 [ActiveSaddler](https://arxiv.org/abs/2610.00906)。RPTune 针对小型商户目录搜索，通过编码器策展器排序裁剪产品，并结合 LLM 后训练提升搜索精度 [RPTune](https://arxiv.org/abs/2610.00964)。Prompt2Skill 从自然语言任务描述出发，在闭环反思编辑中自动构建技能，跨越问答、阅读理解和数学推理等四个领域实现平均 10.8 点的提升 [Prompt2Skill](https://arxiv.org/abs/2609.38593)。RASO 利用外部技能语料库作为先验知识，通过 Cross-Harness Adaptation 适配目标和 harness 差异 [Retrieval-Augmented Skill Optimization](https://arxiv.org/abs/2609.38024)。

分析表明，Agent harness 优化正从单一参数更新向课程学习、技能检索与后训练协同的复合维度演进。动态课程学习解决了固定训练场景随 harness 演化而失效的问题，而检索增强方法降低了从零开始优化的成本。这些趋势反映智能体系统对可复用知识和自适应训练策略的依赖加深。

## 流式与持久视频交互

OneStreamer 通过共享的主动生成过程联合学习无查询的证据记录和任务响应，其 PHCM 生成时间锚定的局部细节描述和事件摘要，PSTL 减少重复等待状态的主导性 [OneStreamer](https://arxiv.org/abs/2610.01762)。World Observer 解耦观察与行动，通过全景观察者持续记录离开 actor 视野的物体状态 [World Observer](https://arxiv.org/abs/2610.02162)。LOCI 采用混合空间记忆架构，在 Transformer 块中分别使用 KV 缓存和受相机几何条件化的循环线性注意力 [LOCI](https://arxiv.org/abs/2609.40222)。Honeycomb 使用 HexMemory 低秩表示在六个空间面中存储场景特征，保持恒定内存 [Honeycomb](https://arxiv.org/abs/2609.37690)。Memorizon 打破长跨度监督与注意力成本的耦合，通过基于相机可见性的 latent 检索维持重访一致性 [Memorizon](https://arxiv.org/abs/2610.00544)。SemanTok 通过 DINO 特征注入和轻量级头实现每 token 前缀的语义重建 [SemanTok](https://arxiv.org/abs/2610.00686)。

分析显示，流式视频交互正从单通道处理转向感知-记忆-响应的统一架构。主动生成与显式记忆的引入解决了历史证据复用与实时感知之间的权衡问题，而空间记忆的低秩表示和检索机制在长跨度一致性和内存效率之间取得平衡。

## 视频世界建模与评估基准

4Director 以 4D 场景表示为条件，每帧对物体施加单一刚性变换，通过 Motion Adapter 将几何支架转换为视频 [4Director](https://arxiv.org/abs/2610.02160)。Ego2Act 提供 2,640 个第一视角操作视频的多步骤物理推理基准 [Ego2Act](https://arxiv.org/abs/2610.01092)。VTR-Bench 评估视频生成模型的视觉文本渲染能力，引入 Keyframe-Guided Agentic Framework 指导迭代优化 [VTR-Bench](https://arxiv.org/abs/2610.01499)。PROWBench 通过程序化构建的场景评估视频模型对细粒度规则的执行保真度 [ROWBench](https://arxiv.org/abs/2610.02205)。EgoTools 提供 100 小时工具中心第一视角数据，覆盖工具使用理解从感知几何到程序因果推理的四个轨道 [EgoTools](https://arxiv.org/abs/2609.39378)。PhysVista 通过感知-推理-评估闭环评估 VLM 的物理智能 [PhysVista](https://arxiv.org/abs/2610.00559)。

分析表明，视频世界模型的研究重心从生成质量向物理一致性和工具交互能力延伸。基准设计趋向于提供程序化可验证的 ground truth 和细粒度评估维度，以弥补现有基准仅关注美学和物理合理性而忽视任务正确性的不足。

## 多模态与具身推理

OmniSeek 将 Omni-LLM 转化为主动多轮推理代理，通过迭代协议动态获取音频和视觉证据 [OmniSeek](https://arxiv.org/abs/2610.02181)。InterEvolve 结合 FB 行为基础模型和 LLM 驱动的奖励程序优化，实现测试时类人 locomotion 技能的再利用和演化 [InterEvolve](https://arxiv.org/abs/2610.02196)。BeyondSCe 利用事件历史和当前场景几何选择相机视角，实现事件指涉抓取 [Beyond the Current Scene](https://arxiv.org/abs/2609.39375)。ARgo-Bench 构建包含 8100 万订单和 235 张表的 ERP 仓库，评估数据代理在复杂企业工作流中的能力 [Argo-Bench](https://arxiv.org/abs/2610.02122)。KaliBench 提供 8,504 条自然语言到 CLI 翻译查询对，覆盖 1,642 个安全工具 [KaliBench](https://arxiv.org/abs/2610.02206)。

分析显示，多模态推理正从单步感知向多轮证据获取和物理交互演化。具身智能中的工具使用和场景理解需要跨模态对齐和长跨度规划能力，而企业级基准则揭示了代理在真实复杂工作流中的显著性能瓶颈。

## 语言模型训练与解码优化

Sharpening Tax 量化后训练对 LLM 测试时可扩展性的损失，提出 PTGS 自适应采样温度 [Sharpening Tax](https://arxiv.org/abs/2610.01509)。LoopCD 利用循环 Transformer 的中间状态进行对比解码，在零额外输出开销下实现性能提升 [Decoding Looped Transformers](https://arxiv.org/abs/2610.02185)。DARA 通过逆平方根密度校正平衡多奖励强化学习中的信号差异 [Make Sparse Rewards Count](https://arxiv.org/abs/2610.00574)。CorrGRPO 将成对协方差归一化为 Pearson 相关系数，避免大尺度奖励主导归一化 [CorrGRPO](https://arxiv.org/abs/2609.36820)。N-OPSD 通过局部参数扰动的专家池提供补充监督 [Better Supervision Is Nearby](https://arxiv.org/abs/2609.39687)。Small Models Better Rejects 证明小冻结模型生成的拒绝样本比自生成拒绝更有效 [Smaller Models, Better Rejects](https://arxiv.org/abs/2609.38987)。

分析表明，训练与解码优化正从固定策略向自适应机制转变。后训练的 sharpening 效应虽然提升单次精度但损害采样覆盖，而基于密度的奖励校准和对比解码方法在保持效率的同时恢复模型能力。

## 长上下文与个性化记忆

PoS 构建并维护显式信念状态作为代理决策上下文，通过一致性和任务进度验证检测信念陷阱 [Beyond Memory](https://arxiv.org/abs/2610.01415)。MemFold 将查询条件化的文本记忆压缩为 K 个连续向量，通过组相对奖励和置信门控蒸馏进行 on-policy 优化 [MemFold](https://arxiv.org/abs/2609.36435)。Personalized Image Generation 将用户历史作为个性化条件，通过 reason-reflect 循环生成符合用户审美的图像 [Personalized Image Generation](https://arxiv.org/abs/2610.00737)。IntentFlux 定义意图漂移为已废弃意图影响最终输出的失败模式，StateForge 显式维护活动需求以缓解该问题 [When Users Change Their Minds](https://arxiv.org/abs/2609.32520)。

分析显示，长上下文处理正从历史压缩转向显式状态维护。信念状态和软记忆的引入解决了传统方法在上下文增长时的一致性和可解释性退化问题，而个性化生成则强调对用户历史语义的深层对齐而非仅外观匹配。

## 模型路由与效率优化

AgSpec 为编码代理管道提供会话、工作区和全局语料库检索，通过离线配置文件和在线验证反馈动态调整草稿长度，生成吞吐量最高提升 4.76 倍 [AgSpec](https://arxiv.org/abs/2610.01108)。PyRUA-Lean 结合反馈驱动的原语组合和选择性观察，减少 65% 输入 token 的同时将成功率从 63.1% 提升至 71.7% [Fewer Tokens, Better Action](https://arxiv.org/abs/2610.01939)。RouteFM 从行为上下文中学习模型表征，实现跨任务、跨候选模型和部署条件的迁移 [Pretrain Once, Route Anywhere](https://arxiv.org/abs/2609.37362)。FlexRouter 使用行列式点过程建模模型互补性，最大化答案覆盖度 [FlexRouter](https://arxiv.org/abs/2609.38585)。HeteroFold 实现跨模型家族的无预填充 KV 缓存转移，在 32K 上下文下比原生预填充快 10.7 倍 [Prefill-Free Cross-Family](https://arxiv.org/abs/2609.32259)。

分析表明，推理效率优化正从单一模型加速向系统级协同设计发展。代理管道的动态草稿调整和选择性观察减少了不必要的计算，而模型路由的基础模型化方法降低了多模型部署的适配成本。

## 3D 生成与纹理合成

SILSA 使用滑动窗口切片潜在表示形状，引入切片级拓扑监督匹配持久性图和对齐 Betti 转换，生成 token 减少 98% 以上 [SILSA](https://arxiv.org/abs/2610.02201)。Tex-Zero 证明高质量 2D 图像可转换为 3D 纹理训练样本，无需真实 3D 资产 [Does Native 3D Texture](https://arxiv.org/abs/2609.34621)。

分析显示，3D 生成在保持拓扑结构的同时大幅降低计算成本。切片表示和显式拓扑约束解决了体素方法在薄结构和长程连接性上的缺陷，而 2D 到 3D 的转换范式为训练数据稀缺问题提供了可行路径。

## 多模态嵌入与表征学习

Omni-Embed-Mini 通过密集蒸馏将文本、语音、音频、图像、视频和文档映射到共享余弦空间，0.9B 参数版本保持文本权重比特级不变 [Omni-Embed-Mini](https://arxiv.org/abs/2610.02148)。Multimodal Flow 引入统一连续架构，通过 Flow Matching 学习单一向量场 [Multimodal Flow](https://arxiv.org/abs/2609.40362)。Latent-Foresight 联合学习潜在标记器和流式生成动力学模型，塑造支持时序可预测性的表征 [Latent-Foresight](https://arxiv.org/abs/2610.01942)。Where-OPD 提供文本空间化指导给教师模型，实现合成到真实的泛化 [Where-OPD](https://arxiv.org/abs/2610.02117)。

分析表明，多模态嵌入正从离散 token 建模向连续流形学习演进。共享空间和连续生成过程避免了视觉量化瓶颈和模态依赖目标的权衡，而端到端的时序可预测性学习改进了两阶段方法的解耦缺陷。

## 其他动态

ScholarCatalyst 构建包含 184 位作者的检索基准，评估从初始研究问题到相关文献的检索能力，Agentic 搜索仅达到 0.42 Recall@20 [ScholarCatalyst](https://arxiv.org/abs/2610.02202)。SAGO 框架从生成一致性、内部激活、置信度和响应镜像等多个维度测量 LLM 泛化稳定性 [Generalization Is Stability](https://arxiv.org/abs/2610.01428)。AutoGUIWorld 结合图像生成器和规划器合成 GUI 交互轨迹，提升 Qwen3.5-35B-A3B 在 OSWorld 上的任务得分 [AutoGUIWorld](https://arxiv.org/abs/2610.01215)。GraphForge 基于证据图构建真实文件工作区，在 Qwen3.6-27B 上显著提升工作空间任务性能 [GraphForge](https://arxiv.org/abs/2609.38923)。Architect-Ant 通过 GRPO 优化布局规则分数实现可编辑的建筑平面图布置 [Architect-Ant](https://arxiv.org/abs/2606.10953)。JevSpawn 连接自然语言任务规范与有限域概率探索，实现组合策略代理推理 [JevSpawn](https://arxiv.org/abs/2610.00437)。DataMagic 通过声明式多代理编排从原始表格数据生成数据视频 [DataMagic](https://arxiv.org/abs/2609.33403)。AutoDataBench 隔离数据智能评估维度，验证轨迹可复用性 [AutoDataBench](https://arxiv.org/abs/2609.40097)。ATR 建立帧级唇部表征与候选行语音单元的单调对齐，改进多语言口型同步判断 [Align Then Reason](https://arxiv.org/abs/2610.00825)。HIDE 基准评估部分可观察环境中的操作记忆，SEEEK 框架结合三种互补记忆机制 [Benchmarking and Enhancing Skill-Level Memory](https://arxiv.org/abs/2609.38886)。