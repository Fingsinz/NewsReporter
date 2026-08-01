

# 每日HFDailyPapers-2026年08月01日

## AI4AI与递归自改进

Frontis-MA1（35B）基于开源OpenMLE全栈系统（含OpenMLE-Gym、OpenMLE-RL、OpenMLE-Evo）在机器学习中工程（MLE）领域进行递归自改进研究，将后训练与推理对齐于四种原子程序演化算子（Draft、Improve、Debug、Crossover），在MLE-Bench Lite上使Medal Average从39.39%提升至71.21%，超越GPT-5.5 + Codex并接近GPT-5.6 Sol [Link](https://arxiv.org/abs/2607.28568)。代码已开源。该研究表明将演化算子训练与长程搜索耦合可实现学习-演化的单循环，为可执行AI4AI提供了参数高效的验证路径。

## GUI与计算机使用智能体

Qwen-UI-Agent面向真实设备场景，融合移动、桌面、Web与DeepSearch环境，统一动作空间支持GUI操作与CLI执行的交错执行，采用AutoResearch数据飞轮与在线RL训练（10,000并发环境），在MobileWorld-Real上达92.2%，OSWorld-Verified上达79.5% [Link](https://arxiv.org/abs/2607.28227)。Echoverse提供12个状态感知的训练环境，通过共进化循环将9B模型从36.5%提升至67.1%，并在强化学习设置下进一步提升至68.0% [Link](https://arxiv.org/abs/2607.28074)。两者分别从模型架构与环境构建角度推动GUI智能体走向部署级能力。

## 多模态与视频理解/生成

VideoCoCo以可执行Blender代码作为过程级思维链，将物理一致性视频生成分解为代码生成与视频编辑两阶段，在PhyGenBench上提升至0.558 [Link](https://arxiv.org/abs/2607.27380)。MPIE-Bench针对多人名人接触交互编辑提出网格重建解剖学与交互性两轴评估，指出VLM-as-judge在几何错误上存在严重饱和 [Link](https://arxiv.org/abs/2607.27616)。See2Think通过1,200道视觉依赖问题与VAoT评估框架揭示模型在视觉状态渲染上的瓶颈 [Link](https://arxiv.org/abs/2607.26769)。RefCaptioner引入20,000视频与171,354参考图像构建多参考图像定位视频描述任务 [Link](https://arxiv.org/abs/2607.28509)。

## 记忆系统与长期依赖

Memory Decoder at Scale将参数化长时记忆扩展至6.9B参数并在300B token上预训练，证明独立扩展记忆比扩展基础模型更具参数效率 [Link](https://arxiv.org/abs/2607.27919)。Metis提出首个记忆基础模型原型，通过原生记忆注意力实现记忆状态的压缩与访问 [Link](https://arxiv.org/abs/2607.26760)。MemHarness将记忆从静态回放转为基于当前状态的主动重构，在ALFWorld和WebShop上显著优于静态记忆基线 [Link](https://arxiv.org/abs/2607.28272)。Σ-Mem为多智能体系统提供基于对称谱更新的在线可靠性记忆，OOD评估中优于多数投票 [Link](https://arxiv.org/abs/2607.27958)。文件系统内存研究指出组织良好的存储可减半检索成本，但当前代理在组织维持上存在不足 [Link](https://arxiv.org/abs/2607.26637)。

## 检索增强与生成范式

BM25 Wins at Scale在450倍规模层级上对比RAG范式，发现BM25在约1000万token处跨越并主导更大规模，Agent检索在小规模领先但查询开销为BM25的39倍 [Link](https://arxiv.org/abs/2607.26497)。Harness-G提出图结构检索框架，将自由文本查询转化为有限动作选择，解决检索等价坍塌现象，在六个QA基准上优于Graph-R1 [Link](https://arxiv.org/abs/2607.27652)。ReToken通过单一可学习嵌入在预填充视觉KV缓存中选择稀疏token，在Visual Haystacks上提升Qwen3VL-8B达13.4点 [Link](https://arxiv.org/abs/2607.28627)。

## 世界模型与具身智能

PhiZero提出物理语言世界模型，采用先推理后渲染范式，将世界演化表示为离散物理语言序列 [Link](https://arxiv.org/abs/2607.28624)。ShadowDancer通过影子对（相同动力学、不同外观的视频对）学习统一动力学表示，实现无动作标签的动作迁移 [Link](https://arxiv.org/abs/2607.28362)。INTACT将动作标注轨迹转换为意图到动作接口，达到无搜索部署策略 [Link](https://arxiv.org/abs/2607.26056)。ACE-Data-0构建150小时同步多模态数据，覆盖手-物操作到全身交互 [Link](https://arxiv.org/abs/2607.28625)。

## 视觉推理与工具使用

Beacon从模式适应性（Mode Adaptiveness）与工具效果（Tool Effect）两个维度重新评估智能视觉推理，提出必要性感知奖励与提示引导能力扩展机制 [Link](https://arxiv.org/abs/2607.28595)。SpatialCLI通过调用-学习-内化三阶段将专家视觉模型能力内化至VLM，在MindCube上将Qwen3-VL-8B从29.3%提升至84.6%（使用工具），内化后仍达73.8% [Link](https://arxiv.org/abs/2607.27703)。LedgerMind以结构化证据账本约束多模态代理轨迹，实现实体级与数值级溯源验证 [Link](https://arxiv.org/abs/2607.28374)。

## 模型架构与训练方法

Multi-Head Attention Residuals将注意力残差路由扩展为每子空间独立头，100M至1B参数训练验证损失持续改善 [Link](https://arxiv.org/abs/2607.27230)。Flux-OPD通过分析反向KL分解提出演化上下文蒸馏，解决开放域任务偏好难以形式化的问题 [Link](https://arxiv.org/abs/2607.28022)。β-OPSD将策略优化与自蒸馏统一，通过几何插值目标实现稳定蒸馏 [Link](https://arxiv.org/abs/2607.28582)。Chimera提出混合视觉扩散Transformer与HeteroP超参迁移方案，达到Chinchilla最优缩放 [Link](https://arxiv.org/abs/2607.28611)。OmniScope提出模态解耦token压缩，在25%保留率下实现3.53倍预填充加速 [Link](https://arxiv.org/abs/2607.23193)。

## 稀疏专家与公平性

Coherent Overlap in MoE通过专家子空间分离指数揭示稀疏MoE中专家子空间高度重叠但路由选择仍具功能价值，定义"相干重叠"概念 [Link](https://arxiv.org/abs/2607.28308)。Fairness Pruning在GLU-MLP层定位人口统计学偏差神经元，零化最多40个神经元在Llama-3.2-1B上保留99.49%推理能力 [Link](https://arxiv.org/abs/2607.28319)。

## 推理优化与可靠性

Revisiting Lossy Verification将投机解码中的有损验证分为截断式与协作式两类，指出控制草稿概率超调是防止低质量输出的关键 [Link](https://arxiv.org/abs/2607.26627)。Is Deep Research Reliable揭示Deep Research代理在长期工作中对误导性知识的脆弱性，搜索验证器在聚焦验证与工作流程级使用间存在脱节 [Link](https://arxiv.org/abs/2607.20891)。

## 其他应用与评估

AskChem将化学文献检索单元从论文转为声明，索引240万条来自14.7万篇论文的声明 [Link](https://arxiv.org/abs/2607.28618)。PALATE提出人物对齐的用户模拟评估框架用于角色扮演代理 [Link](https://arxiv.org/abs/2607.27816)。AMRD提出自适应多教师关系蒸馏用于端侧语音情感识别 [Link](https://arxiv.org/abs/2607.25289)。AI Tour Meeting构建多代理旅行规划仿真框架 [Link](https://arxiv.org/abs/2607.18806)。Pedestrian Archetypes扩展自动驾驶行人原型分类至19类 [Link](https://arxiv.org/abs/2607.16922)。PACE提出分层框架将LLM用于算法交易订单执行，在深圳交易所数据上超过TWAP和Almgren-Chriss [Link](https://arxiv.org/abs/2607.28410)。Explorative Modeling提出探索性建模作为预训练第三维度 [Link](https://arxiv.org/abs/2607.27372)。