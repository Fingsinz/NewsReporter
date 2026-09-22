

# 每日HFDailyPapers-2026年09月22日

## Agent Harness 优化与自我改进

多篇研究聚焦于智能体（Agent） Harness 的构建、优化与知识蒸馏。[RRSI](https://arxiv.org/abs/2609.24972) 针对现有 Harness 递归自我改进方法容易过拟合训练任务的问题，提出了正则化递归自我改进方法，通过引入时间退化的预算限制编辑数量，并结合审查器与剪枝器筛选有价值的修改，在代码、工程等多个基准上验证了其在分布外基准上的泛化能力以及降低策略 Token 消耗的效果。[Harness-Zero](https://arxiv.org/abs/2609.24974) 则从另一个角度出发，研究 Harness 蒸馏，通过引入 Harnessing Agent 将特定领域 Harness 的行为指导转移至模型权重，使得在部署时去除专用 Harness 后仍能保留其行为增益，实验显示基座模型的任务成功率可显著提升。此外，[EDGEGEN](https://arxiv.org/abs/2609.24115) 关注工具调用 Agent 的边界情况生成，通过提取合规规则生成违反规则的数据库接地边缘案例任务，结合微调与 Harness 优化形成闭环系统，提升了 Agent 在航空领域的任务表现。

上述研究表明，Agent Harness 的优化正从单一的任务调优向正则化防过拟合、知识蒸馏以及边界案例强化等方向演进，通过约束演化过程或转移 Harness 行为，旨在提升 Agent 的泛化能力与部署效率，减少对外部复杂 Harness 的依赖。

## 视频生成与编辑的改进

在视频生成领域，多项工作致力于提升物理一致性、编辑能力与生成效率。[WorldCrafter](https://arxiv.org/abs/2609.24984) 提出了一种具有隐式 3D 感知记忆的视频世界模型，通过相机查询的记忆编码器将历史观测压缩到视频生成器的 Token 预算中，实现了长 horizon 的时序一致性和相机控制准确性。[Why Do Video Diffusion Models Violate Physics?](https://arxiv.org/abs/2609.23658) 深入分析了视频扩散模型违反物理规律的根本原因，发现 Rotary Position Embedding (RoPE) 导致过度的空间注意力衰减，并提出通过缩放不同去噪步骤的 RoPE 频率来缓解这一问题。[Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788) 提出了 SVEET 框架，通过解耦训练方案使双向视频扩散模型支持自回归方式的流式视频编辑，在单张 H100 GPU 上达到 15 FPS 的实时性能。[UltraTex](https://arxiv.org/abs/2609.23169) 则专注于高分辨率（2K）多视角扩散用于 3D 纹理生成，通过背景 Token 丢弃和块稀疏注意力等机制解决计算瓶颈，实现了大幅的训练与推理加速。

这些工作显示视频生成研究正从单纯追求视觉保真度，转向解决长程一致性、物理合理性、实时编辑以及高分辨率效率等核心挑战，并通过解耦不同模块、优化注意力机制和引入高效计算策略来推动技术进步。

## 机器人与视觉 - 语言 - 动作（VLA）模型

针对机器人控制，特别是 VLA 模型的研究，集中在提升策略的鲁棒性、安全性以及利用人类数据。[CARE](https://arxiv.org/abs/2609.24118) 提出了一种经验引导的原子纠正执行框架，通过收集失败轨迹并合成纠正示范来提升 VLA 策略在执行偏离后的恢复能力。[Think Like a World Model, Act Like a VLA](https://arxiv.org/abs/2609.24682) 展示了如何将世界模型的表征知识蒸馏到紧凑的机器人策略中，仅通过特征对齐训练即可提升性能，而无需在部署时增加额外计算开销。[Grounded Action Model](https://arxiv.org/abs/2609.23863) 提出以 3D 接地为基础构建机器人基础模型，能够接受语言、点或框提示，实现更准确的物体定位与操作。[Transferring the Intelligence of VLMs to Robotic Control](https://arxiv.org/abs/2609.22966) 通过 RoboDawn 界面将 VLM 的智能转移到机器人控制，利用少量演示的上下文学习实现了零样本和少样本下的优异性能。[HuRo](https://arxiv.org/abs/2609.10706) 系统性地验证了将人类视频机器人化作为 VLA 预训练数据的可行性与可扩展性，展示了增加此类数据对提升模型泛化能力的效果。[ShieldVLA](https://arxiv.org/abs/2609.13231) 则专注于 VLA 模型的安全性对齐，基于哈密顿 - 雅可比（HJ）可达性理论学习安全区域估计，有效降低了累积安全成本。

这表明机器人 VLA 模型的研究正综合借鉴世界模型表征、3D 几何信息、人类视频数据以及安全性约束，通过蒸馏、机器人化数据增强和专门的安全对齐机制，推动机器人策略在复杂动态环境中实现更鲁棒、安全和通用的操作。

## 大模型评估、标注与对齐技术

在促进大模型评估与训练效率方面，多项工作提出了新的方法与工具。[A Lie Detector Test for Language Models](https://arxiv.org/abs/2609.21996) 借鉴测谎技术中的隐蔽信息测试，提出了 PIR 方法，通过分析模型内部状态来识别模型是否知道但不愿透露的答案，可用于审查模型的隐藏知识与不学习验证。[onPanda](https://arxiv.org/abs/2609.24983) 介绍了一种基于 Token 级纠正的高效交互式标注工具，大幅减少了标注时间并保留了模型的采样分布，适用于构建对策 SFT 和偏好数据。[1% of Tokens Can Be Enough](https://arxiv.org/abs/2609.24432) 研究了稀疏对策蒸馏中的梯度估计问题，提出了基于信息效率比率（IER）的 Token 选择方法，在小 Token 预算下提升了蒸馏效果。[Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation](https://arxiv.org/abs/2609.20758) 针对 AI 系统的分域评估，提出了预测驱动平滑估计方法，通过借用跨领域信息提高了小样本领域的评估精度。[Measuring the Checker](https://arxiv.org/abs/2609.22220) 引入了变异分析作为 GPU 内核基准测试判官的充分性度量，揭示了现有测试协议对特定类型错误的检测盲区。

这些研究反映出大模型社区正日益关注评估的准确性与细粒度、训练数据的标注效率与质量，以及蒸馏等优化过程中的统计可靠性，旨在构建更严谨的模型评估体系与更高效的训练流程。

## 3D 生成与视频游戏 AI 评测

在 3D 内容与游戏 AI 评测领域，两项工作提供了新的数据集与框架。[Mira-Scene](https://arxiv.org/abs/2609.23796) 提出了一种基于像素对齐布局的生成式 3D 场景重建框架，通过规范坐标图（CCM）实现密集的对象 - 场景对应，从而在有限数据下显著提升 3D 场景布局的生成精度。[GameHorizon Suite](https://arxiv.org/abs/2609.25001) 构建了一个统一的游戏玩法数据与评测套件，包含自动化标注管道、大规模 AAA 游戏数据集以及可复现的离线与在线基准，用于评估不同模型家庭在多时间 horizon 下的游戏能力，揭示了模型能力差距与任务难度层次。

这两项工作表明，3D 生成正致力于解决对象布局的精细控制问题，而游戏 AI 评测则向着标准化、多 horizon 和多模型可比的方向发展，为相关领域的研究提供了重要的数据资源与评估基准。

## 其他动态

其余研究涉及语言模型基础架构与特定领域应用。[Complex KDA](https://arxiv.org/abs/2609.24797) 扩展了 Kimi Delta 注意力的参数范围，使其能够实现 2D 旋转，提升了线性 RNN 的表达能力和长度外推表现。[The Functionalizer](https://arxiv.org/abs/2609.15991) 提出了一种无损子词分词预处理框架，通过功能分解减少词汇表需求并改善代码与文本生成效果。[Realtime-Venus](https://arxiv.org/abs/2609.13814) 是一个全双工交互系统，整合了音视频理解与生成，支持异步委托与实时对话中断。[Deep Persona](https://arxiv.org/abs/2609.22255) 构建了一个基于心理学原理的角色扮演智能体架构与无参考评估框架。[TAPe+ML](https://arxiv.org/abs/2609.20869) 提出了一种紧凑的多任务计算机视觉系统。[One to More, More to One](https://arxiv.org/abs/2609.23377) 提出了类别感知的软件工程 Agent 专家训练方法。[OmniEdu](https://arxiv.org/abs/2609.23088) 构建了面向 K-12 教育的开放基础模型系列。这些工作分别在模型基础组件效率、实时交互、角色模拟、专业领域应用等方面进行了探索。