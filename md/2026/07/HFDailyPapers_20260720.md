# 每日HFDailyPapers-2026年07月20日

## 强化学习与推理机制优化

近期研究深入探讨了预训练与后训练强化学习（RL）之间的接口关系，以及多种先进的RL策略在提升大模型推理能力中的作用。研究表明，预训练阶段的损失和token数量能有效预测RL后的性能表现，且RL在不同难度的任务上分别起到放大已有正确偏好和挖掘潜在正确路径的作用 [Understanding Reasoning from Pretraining to Post-Training](https://arxiv.org/abs/2607.16097)。在具体的RL算法优化方面，对比策略优化（CPO）通过引入基于token级对比分歧的正确性感知优势塑形，解决了传统熵正则化无法区分有用不确定性与有害混淆的问题，显著优于基于熵的方法 [Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization](https://arxiv.org/abs/2607.14614)。此外，On-Policy Delta Distillation (OPD²) 提出使用教师模型与基础模型在推理能力上的差异信号进行蒸馏，比直接模仿输出分布更有效，能在较短的后训练周期内实现强推理性能 [On-Policy Delta Distillation](https://arxiv.org/abs/2607.15161)。针对智能体RL中的优化器选择，实验发现Muon优化器在特定设置下（如结合Group-in-Group Policy Optimization）能显著提升稀疏奖励环境下的成功率，优于传统的AdamW [When Does Muon Help Agentic Reinforcement Learning?](https://arxiv.org/abs/2607.16169)。最后，Agon框架通过让两个竞争模型互为评估者，隐式地对推理过程进行评分，无需过程标签即可在复杂数学和编程任务上取得远超单一模型RL的效果 [Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning](https://arxiv.org/abs/2607.07690)。

## 架构创新与高效训练扩展

Transformer架构及其变体的扩展性研究取得了新进展，重点在于如何突破现有参数规模或计算效率的瓶颈。Loopie系列提出了循环Transformer（Looped Transformer）的新范式，通过混合专家（MoE）结构和新颖的后训练流水线，在相同计算预算下显著超越了传统的参数扩展方案，并在奥数和国际物理奥赛中达到金牌水平 [Loop the Loopies!](https://arxiv.org/abs/2607.16051)。在残差流扩展方面，xHC（Expanded Hyper-Connections）解决了传统超连接方法在N>4时收益递减和成本激增的问题，通过时间特征增强和稀疏残差流架构，实现了更大规模的并行流扩展，同时引入了xHC-Flash以减少内存流量 [xHC: Expanded Hyper-Connections](https://arxiv.org/abs/2607.14530)。此外，为了提升视频生成的语义一致性，VideoRAE利用冻结的视频基础模型的多尺度分层特征，通过轻量级投影器和局部-全局表示对齐目标，构建了既支持连续潜在变量又支持离散标记的高效自编码器，加速了扩散和自回归模型的收敛 [VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](https://arxiv.org/abs/2607.14088)。

## 多模态与大模型应用落地

多模态模型在推荐系统、科学计算、音频视觉理解及机器人领域的应用不断深化，强调状态保持、统一表征和真实世界数据的利用。RecGPT-V3作为淘宝部署的推荐系统模型，引入了状态记忆枢纽和混合模态基础模型，通过联合推理自然语言标签和语义ID，大幅降低了计算开销并提升了点击率和GMV [RecGPT-V3 Technical Report](https://arxiv.org/abs/2607.15591)。在科学AI领域，S1-Omni构建了一个统一的 multimodal reasoning 模型，将自然语言指令与CIF、SMILES等多种科学对象映射到共享空间，支持属性预测和分子生成等200多种科学任务，性能超越多个前沿专有模型 [S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation](https://arxiv.org/abs/2607.15686)。Audio-Visual Flamingo (AV-Flamingo) 专注于长复杂视频的音频-视觉联合理解，通过大规模真实世界视频数据集和时序交叉思维链推理框架，在多项基准测试中展现出强大的泛化能力 [Audio-Visual Flaminging: Open Audio-Visual Intelligence for Long and Complex Videos](https://arxiv.org/abs/2607.16107)。医疗领域方面，Cura 1T 通过人类门控的自我进化循环训练，整合了患者咨询、临床推理和电子健康记录工具使用能力，在医疗基准测试中名列前茅 [Cura 1T: Specialized Model for Agentic Healthcare](https://arxiv.org/abs/2607.15314)。

## 智能体技能获取与工作流优化

智能体在执行复杂任务时的技能复用和工作流效率成为研究热点，重点在于如何将多模态资源转化为可执行技能以及如何优化推理过程。RESOURCE2SKILL 框架将从教程视频、代码库等多模态资源中提取的技能组织为分层的多模态“技能维基”，使智能体能够检索和组合这些技能，显著提升了在多个编写领域的表现 [RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources](https://arxiv.org/abs/2606.29538)。在数据科学领域，DSWorld 提出了数据科学世界模型的概念，通过预测环境状态转换来减少昂贵的实时执行，结合强化学习优化策略，加速了智能体的训练和推理过程 [DSWorld: A Data Science World Model for Efficient Autonomous Agents](https://arxiv.org/abs/2607.15901)。对于代码审查工作流，实证研究显示，虽然AI代理参与的协作模式能加快审查速度，但并不一定能提高审查质量，人机协作模式是影响效率和质量的关键因素 [From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality](https://arxiv.org/abs/2607.13196)。此外，递归Harness自我改进（RHI）通过迭代优化提示级别的Harness规范，提升了智能体在执行轨迹中的上下文管理能力，降低了推理成本 [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524)。

## 机器人学与具身智能

具身智能模型正朝着更大规模真实世界数据训练和更精准的空间表征方向发展。Xiaomi-Robotics-1 是一个基础的视觉-语言-动作（VLA）模型，通过在超过10万小时的真实世界操作轨迹上进行预训练，并开发可扩展的自动标注流水线，实现了在未见环境中出色的开箱即用能力和高效的微调适应性，在RoboCasa和RoboDojo等基准上刷新了纪录 [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330)。为解决VLA模型中相机视角与机器人动作坐标系不匹配的问题，See like a Robot 提出了以机器人为中心的点图（Pointmaps），将场景点的3D坐标编码为图像像素，从而在保持2D VLA架构兼容性的同时，显著提升了跨视角泛化能力和真实机器人实验的成功率 [See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models](https://arxiv.org/abs/2607.11498)。

## 音乐生成与检索增强技术

在特定领域的生成模型和知识检索方面，Qwen-Music 和 RAGU 分别代表了音乐生成和图检索增强生成的最新进展。Qwen-Music 是一个强大的音乐生成模型，支持文本到音乐和翻唱生成，其核心创新包括25Hz的音乐语义Token压缩、基于旋律Token的思维链（Melody-CoT）规划机制以及高保真立体声渲染模块，在多语言音乐数据上预训练后取得了优异的音乐性和音质指标 [Qwen-Music Technical Report](https://arxiv.org/abs/2607.11699)。RAGU 是一个开源的模块化GraphRAG引擎，通过分离实体提取和整合步骤（包括去重、总结和社区检测），并结合专为语言技能优化的紧凑型Meno-Lite-0.1模型，提高了知识图谱构建的质量和检索的完整性，同时在单GPU上即可运行 [RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM](https://arxiv.org/abs/2607.11683)。