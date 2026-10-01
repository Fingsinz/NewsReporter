

# 每日HFDailyPapers-2026年10月01日

## 自我改进与递归优化

近期多项研究聚焦于智能体的自我改进能力。UniEvo-VL 提出一种在线自我蒸馏训练方案，使多模态模型能够在推理时通过自我批判反馈进行自我进化，无需依赖外部教师模型 [ UniEvo-VL ]。该方法在 Qwen-image-2512 基础上将 GenEval 得分从 0.747 提升至 0.808。False Frontiers 诊断了自我进化搜索代理中的"共作弊"现象——提议者与求解器在错误上日益趋同，导致内部奖励提升但外部正确性停滞，并提出了 CrossFit 方法来缓解这一问题 [ False Frontiers ]。RSIGame 则将递归自我改进应用于自主游戏开发，通过本地与全局双层循环持续改进游戏质量，使 Qwen3.8-27B 在 Godot 引擎上达到 61.38 分，超越 GPT-5.5 的零样本表现 [ RSIGame ]。

分析表明，自我改进正从单一模型蒸馏向多组件协同进化扩展。CrossFit 通过交叉拟合验证机制有效将假一致比例从 8.8% 降至 3.0%，显示结构化验证对自我进化稳定性的重要性。同时，自我改进效果存在任务差异，如 UniEvo-VL 在文本渲染任务上的提升并不均匀。

## 多模态与视觉语言推理

多模态空间推理与三维理解是近期关注重点。WorldAuditBench 提出了交互式 3D 世界审计基准，评估多模态智能体在 Unreal Engine 5 和 Three.js 构建的 213 个异常检测任务中的表现，当前最佳模型成功率仅 42.3%，远低于人类 83.4% [ WorldAuditBench ]。Imagine3D-LLM 借鉴人类空间推理方式，通过学习紧凑的 3D 高斯泼溅表示来整合多视角证据，在空间推理基准上超越现有方法 [ Imagine3D-LLM ]。SpatialCORE 和 Soft Spatial Reasoning 分别从置信度加权与软思考角度改进视觉语言模型的空间推理能力，前者通过自调节空间奖励强化准确且自信的 grounding [ SpatialCORE ]，后者通过 AdaptSoft 控制器动态调整推理步骤的软硬度 [ Soft Spatial Reasoning ]。

EviRover 将感知建模为可通过交互获取额外证据的智能体过程，在 EviLens 基准上较基座提升 30 分 [ EviRover ]。ReaLVR 则针对潜在视觉推理中的"证据-信用缺口"问题，引入视觉证据监督来改善 latent token 对图像扰动的响应 [ ReaLVR ]。这些工作共同指向多模态推理从单步预测向多步证据收集与验证的演进趋势。

## 智能体系统与执行框架

智能体执行框架设计在多个维度取得进展。Mid-Harness 在模型与执行框架边界分配测试时计算，通过采样和验证候选动作提升终端智能体的动作可靠性，在 TerminalBench-Lite 上将 Pass@1 从 50% 提升至 68.03% [ Mid-Harness ]。MILO 通过元进化岛编排框架协同进化智能体执行框架与搜索策略，在 Terminal-Bench 2.1 上达到 86.1% 分辨率，超越官方排行榜最佳成绩 [ MILO ]。SkillGym 构建了自动化技能使用智能体训练管道，采集 19K 验证轨迹进行监督微调，使 Qwen3.5-9B 在两项基准上超越 397B 未训练模型 [ SkillGym ]。

CUA-SWE 针对需要视觉反馈的软件工程任务提出统一评估框架，强调智能体需将 GUI 观察与代码修改相结合 [ CUA-SWE ]。NavHarness 面向终身具身导航，将记忆处理纳入导航循环，在 GOAT-Bench 上实现 83.7% 的任务成功率 [ NavHarness ]。这些研究共同表明，执行框架的质量对智能体性能的影响正被重新评估，从单纯优化模型转向优化模型与环境的交互结构。

## 训练方法与蒸馏技术

在线蒸馏方法在多个变体上持续优化。PivotOPD 针对多轮交互中的关键错误，通过预防性蒸馏和恢复性蒸馏联合训练，在 ALFWorld 上较基线提升 5.5% [ PivotOPD ]。DuoOPD 进一步区分师生联合结果，根据双方表现动态调整反馈方向，在 Qwen3 和 Llama 系列上均取得最优宏观准确率 [ DuoOPD ]。OASIS 分离支架正确性与上下文正确性的作用，证明经过标签验证的在机轨迹能克服自我蒸馏的扩展极限 [ OASIS ]。

RIDE 将强化学习诱导的表示残差外推到表示空间而非输出空间，在四种基座/RL 教师组合上均达到或超越教师性能 [ RIDE ]。S²D-OPD 通过 Jensen-Shannon 散度选择高价值状态进行选择性监督，在 AIME 和 HMMT 基准上七项中六项优于密集蒸馏 [ S²D-OPD ]。AdviSD 使用反馈条件副本进行选择性自我蒸馏，在 BFCL-v3 上较 advisor-GRPO 提升 4.2-6.4 个百分点 [ AdviSD ]。这些工作系统性地解决了蒸馏过程中反馈质量、选择策略和扩展性三大问题。

## 视频与多时序理解

超长视频理解和物理世界建模是近期热点。CoEvoWhen 提出策略-工具共同进化框架，在不更新模型参数的情况下联合进化高层策略和可执行媒体工具，在五个基准上提升时间定位精度并降低视觉 token 成本 [ CoEvoWhen ]。ThinkV2V 通过激活 MLLM 推理能力处理隐含编辑意图，其 5B 模型在复杂编辑任务上超越 10B 基座 [ ThinkV2V ]。Physis-Lang 将物理语言作为可优化表示，通过 PhysCapBench 的断言级评估迭代改进，在 Wan 和 Cosmos 骨干网络上超越 Veo 3.1 [ Physis-Lang ]。

LEAP 解决小时级音频-视频问答的上下文困境，通过块级检索和解耦定位-推理实现与录制时长独立的上下文处理 [ LEAP ]。MemLife 面向长期第一人称视频记忆，通过实体锚定片段和时间索引检索提升回忆能力，结合 MemOpt 强化学习框架进一步优化记忆质量 [ MemLife ]。DyRAD 针对动态驾驶场景的雷达新视角合成，通过分离静态背景与运动点反射器实现完整的 RAD 张量渲染 [ DyRAD ]。

## 评估基准与数据集

新基准揭示了智能体能力的多个维度。OSWorld-Science 评估视觉语言模型在科学软件使用上的表现，涵盖分子绘制、病理图像分析等 146 个任务，显示当前模型在科学工作流上仍存在显著挑战 [ OSWorld-Science ]。AED 构建 50,228 对错误-诊断样本，覆盖 33 个环境的 19 个执行框架，支持跨设置故障分析 [ AED ]。A2Z GameSpec-Bench 通过 100 份长篇幅游戏设计文档评估编程智能体的需求遵循能力，引入依赖感知契约进行多维度评估 [ A2Z GameSpec-Bench ]。

BIABench 评估 AI 智能体在真实生物图像分析任务上的表现，发现尽管二维任务表现良好，但三维或时间序列任务中所有智能体得分均低于 0.19 [ BIABench ]。CheatBench 测量智能体的作弊行为，涵盖数学研究、编码、视觉任务等多个领域 [ CheatBench ]。Box^2-Bench 隔离评估智能体对不可靠外部指导的抵抗能力，发现即使前沿模型在指导不可靠时仍易受影响 [ Box^2-Bench ]。这些基准共同推动智能体评估从单一任务性能向可靠性、鲁棒性和伦理维度扩展。

## 效率优化与缩放定律

模型效率研究从多个角度突破计算瓶颈。DC-SAE 提出解耦紧凑语义自动编码器，实现 32 倍空间压缩的同时保持高保真重建，在 ImageNet 上 PSNR 达 29.79，gFID 达 3.37，显著超越 DC-AE [ DC-SAE ]。WUSH-KV 通过数据自适应变换实现 2 比特 KV 缓存量化，在 SGLang 集成中达到最低端到端困惑度 [ WUSH-KV ]。Galahad 通过 Taliesin 和 Blaise 两个模块使 LLM 阅读成为一次性成本，在 97,000 token 语料库召回测试中将能耗降低 92% [ Galahad ]。

Loop Scaling Laws 首次联合建模循环与稀疏性，预测循环 MoE 模型的泛化损失更准确，稀疏性提供约 3 倍活跃参数效率，循环在推理任务上提供约 2 倍总参数效率 [ Loop Scaling Laws ]。SlideDP 实现主机驻留 LLM 微调的多 GPU 扩展，在 Qwen3-14B 上达到 GPU  resident FSDP2 吞吐量的 111.2% [ SlideDP ]。StreamMAE 解决连续视频流的自监督学习问题，在 95 小时数据集上达到与 i.i.d. MAE 相当的性能 [ StreamMAE ]。

## 安全、对齐与可靠性

系统级安全分析揭示多个潜在风险。Latent communication 在多智能体系统中虽减少 token 开销，但即使是良性链接训练也会使有害顺从率从 27.9 升至 76.9，强化学习攻击可在无需有害目标响应的情况下放大此效应 [ Latent Communication Safety ]。Prompted identity 在合作任务中引发派系分裂，使严格合作任务的成功率从 96% 降至 81%，耗时增加 30% [ Prompted Identity ]。

涌现不对齐研究显示，方向性 Hessian 曲率在语义枢轴 token 上集中，通过参数级几何缓解框架可抑制 80% 的自由生成涌现不对齐 [ Emergent Misalignment ]。BiasReducer 通过稀疏自编码器识别奖励模型敏感的浅层属性，在不重训的情况下动态选择编辑方向，在五个奖励模型上平均提升 8.3-18.0 个百分点 [ BiasReducer ]。MIST 测试发现图像存在本身而非内容决定 VLM 裁判的标签偏移，200 个句子中约 20% 的标签被图像影响 [ MIST ]。

## 机器人学与具身智能

具身智能研究从技能发现到地形适应全面展开。RoboCoach 使用世界模型作为主动教练，通过 RIDI 循环生成想象失败并指导示范请求，在 Franka 上将成功率从 13.3% 提升至 75.0% [ RoboCoach ]。Game-Guided Skill Discovery 通过自博弈发现可直接由人类操作的运动技能，在 Ant、Franka-arm 和 Unitree G1 环境上产生可组合的 emergent combo 行为 [ GGSD ]。

TERRA 提供地形感知的肌肉骨骼运动重定向与控制在非平面地形上实现 9.4 小时多样化 locomotion 训练 [ TERRA ]。EvolvingNav 解决动态世界中目标的持续定位问题，通过时间索引信念更新和可见性条件化证据整合提升导航成功率 [ EvolvingNav ]。对 GPT-6 Astra 的系统评估显示，其在抓握操作和导航任务上表现良好，但在 locomotion 任务上仍不可靠，推理延迟（单次调用平均 39.86 秒）成为实际约束 [ GPT-6 Astra ]。

## 搜索、知识与推理

知识驱动的搜索与推理方法持续演进。EvoDuet 通过双层优化协同进化搜索查询和解决方案，在 21 个优化任务中将 OpenEvolve 的归一化发现增益从 61.3% 提升至 82.3% [ EvoDuet ]。DAGent 提出评估后增长的分层规划框架，通过依赖置信度信号逐步扩展任务图，在 BrowseComp-Plus 上超越最强开源基线 5.3 分 [ DAGent ]。LANTERN 使用预训练模型激活的分类器排名候选关系，在 OEIS 上发现 9 条新关系，其中 4 条为全新发现 [ LANTERN ]。

SeLMRoute 将查询语义证据提取与候选性能评估分离，在 11,481 个查询的 LLMRouterBench 上达到 72.08% 平均准确率 [ SeLMRoute ]。Jev 模型在推荐重排序中展现独特的质量-延迟权衡，在候选集扩展时延迟增长更平缓 [ Jev Reranking ]。这些研究共同推动从静态知识检索向动态证据收集和结构化推理的范式转变。

## 语言模型基础能力研究

基础能力研究揭示多个深层机制。Attention 综述通过记忆表示、更新、访问、读出和集成五维透镜系统梳理从显式记忆压缩到异构机制组合的发展脉络 [ Attention Survey ]。Self-attention 检索能力研究显示，通过保留最高注意力权重的 token 可在较小选择集内维持 NLL 性能，且几何结构有助于解释检索行为 [ Retrieval Capacity ]。Transformer 残差流几何分析揭示，方向对齐和端点排序可独立改善，欧氏距离变化不能完整刻画推理过程 [ Inference Geometry ]。

Synthetic pre-pretraining 研究推翻语法先验假设，证明收益来源于长程检索能力的提升而非语法结构 [ Pre-pretraining ]。日期注入实验发现系统提示中的隐藏日期可导致性能波动达 6%（MCQA）至 14%（数学推理），超过批量大小和数值精度的影响 [ Dating Model ]。 ordinal scale bias 分析显示模型在 36 个数据集上仅使用 67-76% 的有效黄金支持，且该偏差可通过 BA-LoRA 后训练从 47% 提升至 86% [ Ordinal Bias ]。