# 每日HFDailyPapers-2026年07月24日

## 深度研究与智能体自主进化

摘要显示，传统深度研究面临发现与验证成本不对称的挑战。AREX ([AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461)) 提出了一种递归自我改进（RSI）架构，通过内层证据收集和外层约束审计交替运行，并引入自主上下文更新工具压缩历史状态以支持长期优化。该方法在 BrowseComp、WideSearch 等基准上显著优于同等规模基线，并展现出与更大参数模型竞争的能力。

分析表明，将“自改进”机制引入深度研究代理是应对复杂约束满足问题的有效路径。通过解决长视域强化学习中的稀疏奖励问题并优化上下文管理，AREX 展示了智能体从单纯搜索向自我修正演进的潜力，为构建更高阶的自主推理系统提供了新范式。

## 教育垂直领域与大模型基准

K12-KGraph ([K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs](https://arxiv.org/abs/2605.09635)) 针对现有教育基准忽视课程认知结构的问题，构建了涵盖 K-12 多学科教材的知识图谱及对应基准 K12-Bench。研究指出当前主流模型（如 Gemini-3-Flash）在多选题准确率上表现有限，特别是在前置依赖和邻接关系推理上。此外，基于该图谱生成的训练数据 K12-Train 显示，领域特定的监督微调能显著缩小模型差距，且文本与视觉监督具有互补性。

这揭示了通用大模型在教育垂直领域的局限性，即缺乏对课程知识逻辑结构的深层理解。通过结合结构化知识图谱进行有针对性的数据构建与微调，可以有效提升模型在复杂教育场景下的表现，强调了领域结构化数据在垂直化落地中的关键作用。

## 视频生成与视觉表征学习

在视频生成方面，SANA-Video 2.0 ([SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation](https://arxiv.org/abs/2607.21553)) 提出了一种混合线性注意力架构，结合了门控线性注意力和周期性门控 Softmax锚点，旨在保留线性注意力的长序列扩展优势同时恢复全秩交互能力。配合块级注意力残差连接，该模型在单卡 H100 上实现了高效的高分辨率视频生成，推理速度远超全 Softmax 基准。与此同时，WorldWeaver ([Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers](https://arxiv.org/abs/2607.21594)) 针对多智能体视频生成，引入了跨智能体世界状态寄存器（World State Registers），以维持共享状态的一致性，显著提升了多视角下的逻辑连贯性。

另一方面，结构化动态建模方面，SDM ([Self-Supervised Learning of Structured Dynamics from Videos](https://arxiv.org/abs/2607.21576)) 尝试从预训练图像 Transformer 的特征中提取解耦的运动表示，区分相机运动与物体运动，证明轻量级自监督信号即可捕捉结构化视频动态。此外，VCSD ([Visual Contrastive Self-Distillation](https://arxiv.org/abs/2607.21556)) 提出一种无需外部教师或特权答案的对比自蒸馏方法，通过擦除图像内容产生对比信号来强化视觉特征学习，提升了 Qwen3-VL 等模型的视觉推理性能。

这些进展表明，视频生成正朝着更高效、更具物理一致性的方向演进。混合注意力机制和显式状态寄存器的设计解决了长期生成中的信息丢失与逻辑断裂问题；而通过对比蒸馏和解耦动态学习，视觉模型的样本效率和表征鲁棒性也得到了进一步释放。

## 具身智能、空间认知与代码智能

具身与空间认知领域，Robostral Navigate ([Robostral Navigate](https://arxiv.org/abs/2607.20785)) 仅使用单目 RGB 流作为输入预测导航航点，通过 prefix-caching 训练策略大幅降低数据需求，并在 R2R-CE 等基准上刷新单模态记录。ReferTrack ([ReferTrack: Referring Then Tracking for Embodied Visual Tracking](https://arxiv.org/abs/2607.20061)) 则采用“先指认后跟踪”范式，利用边界框时序队列保持目标运动线索，在单一前向摄像头设置下实现了高精度的具身视觉跟踪。在机器人数据合成方面，TableVerse ([TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation](https://arxiv.org/abs/2607.21017)) 通过从真实网络图像重建高保真桌面场景，构建了十万级真实感抓取数据集，弥补了合成数据的物理不合理缺陷。

代码智能方面，Tencent WorkBuddy Bench ([Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction](https://arxiv.org/abs/2607.20911)) 提出一种基于反工程重构的基准构建方法，从真实 Commit/PR 逆向生成自然语言任务描述，以抵抗数据污染，覆盖了代码、Web、办公和安全四个领域。NVIDIA NOOA ([NVIDIA-labs OO Agents: Native Python Object-Oriented Agents](https://arxiv.org/abs/2607.20709)) 则提出了面向对象的智能体编程框架，将智能体视为 Python 对象，通过类型注解和文档字符串统一开发者接口与模型接口，提升了代码的可测试性和可维护性。

分析认为，具身智能的发展正从复杂的传感器依赖转向更通用的视觉交互，强调环境泛化能力与数据的高效利用；而代码智能领域则日益关注评估的公平性与开发范式的标准化，旨在解决数据泄露问题并降低工程落地门槛。

## 人类意图追踪与金融复杂推理

针对大型语言模型在动态交互中的短板，LLMs Get Lost in Evolving User Intent ([LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734)) 揭示了当前模型在用户意图随对话演变时出现表现大幅下降的现象，指出静态评估无法捕捉这一关键缺陷。在复杂行业应用方面，FinanceComplexQA ([FinanceComplexQA: Benchmarking Agentic Reasoning on Industrial-grade Financial Documents](https://arxiv.org/abs/2607.19238)) 专注于工业级金融文档的深度研究，构建了包含复杂排版和跨页信息的问答基准，评估了代理在数值计算和多跳推理上的能力。

这表明，随着 AI 代理逐渐承担协作角色，其动态意图跟踪能力成为区别于传统静态生成的核心挑战；同时，金融等高专业性场景对多模态、多跳逻辑的严谨性提出了极高要求，促使评测体系向更贴近真实业务复杂度的方向演进。

## 其他技术进展

在基础算法层面，Sample-Efficient Learning from Agent Experience ([Sample-Efficient Learning from Agent Experience](https://arxiv.org/abs/2607.21051)) 提出了“经验蒸馏”概念，通过离线重放将上下文学习收益内化到模型权重中，大幅减少了环境采样需求。Predictive Divergence Masks for LLM RL ([Predictive Divergence Masks for LLM RL](https://arxiv.org/abs/2607.10848)) 改进了强化学习中的信任区域掩码，使用闭式预测替代基于采样的重要性比率，使策略更新方向与概率散度变化更加一致。Multi-Turn On-Policy Distillation with Prefix Replay ([Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/abs/2607.04763)) 提出的 ReOPD 方法通过重用教师轨迹作为前缀，解决了多轮代理蒸馏中的分布偏移问题，显著提升了训练效率。此外，ProVisE ([Show, Don't Tell: Evaluating Spatial Cognition in Generative Pixels Rather Than LLM Text](https://arxiv.org/abs/2607.21072)) 建立了一套协议化的视觉评估框架，允许图像生成模型直接在像素空间表达空间认知，弥补了传统文本基准无法全面评估生成模型空间能力的空白。GraphVid ([GraphVid: Interactive Graph-Controllable Video Generation](https://arxiv.org/abs/2607.21580)) 利用结构化交互图实现了高可控的视频生成，证明了语义接口在精细化控制中的优势。Recurrent Sinusoidal INRs ([Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation](https://arxiv.org/abs/2607.21485)) 探索了正弦激活函数的递归机制以丰富隐式神经表示的光谱支持，在图像和 3D 表征中实现了更高保真度。Color Pass-Through via Camera-Display Coupling ([Color Pass-Through via Camera-Display Coupling](https://arxiv.org/abs/2607.12746)) 通过将相机与显示器耦合进行端到端校正，克服了分阶段校准导致的色彩失真问题，提升了真实场景的色彩还原度。