

# 每日HFDailyPapers-2026年09月24日

## 记忆机制：从视频生成到多模态代理

多份研究聚焦于如何让 AI 系统保持对历史信息的持久访问能力。针对自回归视频生成，[《The Past Frames the Future》](https://arxiv.org/abs/2609.28466) 系统梳理了记忆操作的五个维度（形式、功能、操作、学习与评估），指出随着生成序列延长，实体身份、动态状态等关键信息会在到达相关时间前脱离上下文窗口。在 LLM 代理场景中，[《Just-in-Time Memory》](https://arjav.org/abs/2609.27334) 提出了延迟策展思路：与其在写入时固化记忆，不如保留原始轨迹并在读取时根据当前任务生成自适应内容，在 ALFWorld、WebShop 和 τ²-bench 上分别超越最强基线 16.2、16.3 和 3.9 个百分点。针对具身智能，[《MemBodied》](https://arxiv.org/abs/2609.28256) 设计了固定大小的情节记忆模块（关联状态 + 情节锚点），在 RMBench 记忆任务上达到无记忆策略的 7.81 倍成功率，同时仅增加 10 倍参数。此外，[《SpeakerMem-R1》](https://arxiv.org/abs/2609.26780) 解决多角色对话中的归属与关系理解瓶颈，采用双轨记忆（原始消息 + 派生状态）结合人员级/群体级视图，在 GroupMemBench 和 EverMemBench 上达到 62.33% 的最新最高分。分析表明，记忆机制正从"写入时固化"向"读取时适配"演进，资源受限与任务依赖的权衡构成当前核心挑战。

## 世界模型与具身智能

物理世界模型是具身 AI 的核心基础设施。[《InternW0》](https://arxiv.org/abs/2609.27656) 提出异步多频处理架构，视频专家与动作专家以不同时间尺度运行，通过层级 K/V 复用和观测条件路由避免逐动作重生成未来，基于约 7,200 小时异质机器人数据训练，在 MOF 合成和灵巧操作任务上展现潜力。[《Uranus》](https://arxiv.org/abs/2609.24815) 则构建数据驱动的机器人模拟器，采用联合轨迹条件自回归扩散模型，实现 24 FPS 的低延迟生成与开放式 rollout，支持多机载配置同步生成。针对世界模型评估，[《HappyWorld-Bench》](https://arxiv.org/abs/2609.24308) 提出六层能力框架（W1-W6），覆盖视频、空间与具身三个赛道共 1,692 个测试用例，发现当前模型在长时交互下状态一致性显著下降。在空间推理方面，[《Spatial-Interactor》](https://arxiv.org/abs/2609.23038) 通过三级课程（被动状态转换→主动自我状态转换→长轨迹集成）训练 VLM 建模物理世界状态变化，结合 LSI-108K 数据集实现持续性能提升。规划层面，[《X-Planner》](https://arxiv.org/abs/2609.25187) 提出事件结构化计划接口，通过楼梯解码（Staircase Decoding）在离散接口与潜变量接口间切换，在真实机器人实验中超越基线。这些工作表明，具身智能正从静态预测转向动态交互中的可执行推理。

## 视频生成与多模态对齐

视频生成研究聚焦于跨模态对齐与奖励建模。[《Closing the Cross-Attention Gap in Joint Video Generation》](https://arxiv.org/abs/2609.27901) 揭示联合扩散 Transformer 存在"视频更平等"的不对称性：视频对其他模态的对应关系强，但反向约束关系弱，由此提出 RecCAR（互惠跨注意力正则化），将人体解剖得分从 0.69 提升至 0.75，音视频不同步从 0.804 降至 0.752。在奖励建模方面，[《RewardVerse》](https://arxiv.org/abs/2609.22947) 针对视频生成 RL 中标量漂移问题，引入动态评价量规作为中间表示，结合 RGPO 两阶段训练算法，在 16 维 EvalVerse 基准上实现点级与对级评估的 SOTA 性能。分析表明，多模态联合生成正从"质量优先"转向"一致性优先"，跨模态不对等性成为关键瓶颈。

## 大语言模型训练与推理优化

LLM 训练方法呈现多条技术路线并进态势。[《Hunyuan-A13B》](https://arxiv.org/abs/2609.27284) 发布 80B 总参数/13B 激活参数的 MoE 开源模型，引入双模式思维链（快思考/慢思考）适配不同任务复杂度，在数学、编程与代理任务上接近更大模型性能。[《PACT》](https://arxiv.org/abs/2609.26355) 从数学角度定义 token 级信用并证明其唯一性，提出 Actor-then-Critic 更新顺序，在数学推理基准上平均准确率达 72.87%，超越 GRPO 8.80 个百分点。在推理层面，[《FLEET》](https://arxiv.org/abs/2609.27657) 将记忆机制引入文本生成，通过稀疏轨迹与熵阈值推断 token 效用分数调整 logits，在 LiveCodeBench 上以相同预算实现 3 倍加速且 Pass@32 从 59.9% 提升至 66.2%。模型压缩方面，[《GeoPair》](https://arxiv.org/abs/2609.25963) 提出训练无关的跨层权重因式分解框架，通过收敛优化管道替代启发式分组，在多种架构与模态上取得 SOTA 压缩效果。分析表明，LLM 训练正从"更大参数"转向"更高效学习"，信用分配、推理压缩与架构适配成为并行方向。

## 评估基准与数据泄漏问题

研究社区对评估可靠性日益关注。[《WhatWorkedBench》](https://arxiv.org/abs/2609.27490) 提出实验理解基准，通过 36 个任务、1,248 条配置记录评估代理对组件变化的预测准确性，高斯过程拟合将效应恢复精度从 0.632 提升至 0.698。[《StudentBench》](https://arxiv.org/abs/2609.28470) 收集 17.5 万条学生-AI 消息，发现 AI 辅导在 GRE 学习增益上与人类专家相当（p=0.015），且成本仅为人类的 1/918。在代码评估领域，[《Schrödinger's Code Repository》](https://arxiv.org/abs/2609.27891) 揭示 SWE-bench 等基准存在数据泄漏风险：通过四种动态变换（问题陈述重构、命名空间重映射、文件内布局重排、功能保持改写）消除熟悉线索后，代理性能显著下降，交互成本大幅上升，表明当前模型部分依赖记忆而非真正推理。分析指出，评估基准正从"静态分数"转向"动态验证"，泄漏检测与鲁棒性测试成为必要环节。

## 其他动态

[《On the Diffusibility of High-Dimensional Latents》](https://arxiv.org/abs/2609.28473) 发现对强重建编码器微调会降低表征有效维度，导致高维空间优化低效，建议用 x₀ 预测替代速度预测。[《Six Layers Less》](https://arxiv.org/abs/2609.27980) 提出 Whisper 编码器剪枝方法，移除 WER 影响最小的 6 层（占 18.5%），结合无标签蒸馏恢复性能，代码已开源。[《The Linear Representation Hypothesis Needs a Group Action》](https://arxiv.org/abs/2609.27158) 用群作用形式化表征等价性，澄清可解释性分析中的假设变化。[《Knowledge Pull Requests》](https://arxiv.org/abs/2609.26634) 将文档更新建模为可解释的知识拉取请求，生成变更日志区分知识变化与文本变化。[《Capable yet Parsimonious》](https://arxiv.org/abs/2609.26637) 通过 API 工具诱导闭源模型输出隐藏思维链，发现 Astra 展示令牌高效定向推理。[《Self-Organizing Agent Teams》](https://arxiv.org/abs/2609.22682) 研究 AI 代理团队的自组织能力，团队从经验中学习协作策略，在数学基准上达 66.7% 准确率，超过最强成员 17.9 个百分点。[《Verifiable Hidden Dynamics Play》](https://arxiv.org/abs/2609.27321) 提出逆向生成流程：先采样求解数学模型再生成具身环境，低成本生产 3,300 个多样化训练环境。[《MemoryAthena》](https://arxiv.org/abs/2609.25853) 探索生成式记忆的补充价值，通过轻量路由头学习何时干预检索路径。[《EmbodiedSWE》](https://arxiv.org/abs/2609.27308) 用代码代理解决长视距机器人任务并生成训练轨迹，在 LIBERO-Long 达 90.6%。[《PackLab》](https://arxiv.org/abs/2609.23784) 提供机器人装箱的 MLLM 训练与评估框架，物理仿真平台支持闭环决策。