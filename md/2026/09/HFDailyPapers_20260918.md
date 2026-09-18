

# 每日HFDailyPapers-2026年09月18日

## 长上下文模型与计算效率优化

DeepSeek-AI 发布了 DeepSeek-V4.1-Flash，这是一种支持百万token上下文的552B参数多模态MoE模型，通过因果编码器-解码器架构实现prefill阶段激活8B参数、decode阶段激活16B参数，并结合CSA2跨层KV cache复用与FP4缓存技术，将全局KV cache占用降至每token 890字节，约为前代的四分之一；同时通过SWA Bounded Replay优化将持久化KV cache降至前代的约八分之一 [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969)。针对视频生成场景，Video DeltaNet提出了一种结合局部Softmax注意力与双向线性记忆的混合注意力机制，在MiniMax H3上实现14.5倍加速，将14.3秒768p视频的DiT去噪时间压缩至6.70秒（八卡B200） [Video DeltaNet](https://arxiv.org/abs/2609.20744)。在推理效率方面，When2Think提出了一种实例级难度感知控制机制，通过预计算参考统计数据动态分配计算资源，使模型能在简单问题上采用直接回答（System 1），在困难问题上保留扩展推理（System 2），在AIME24上Pass@3提升10.0%的同时token使用量减少27.9% [When2Think](https://arxiv.org/abs/2609.19671)。

分析表明，长上下文部署的成本瓶颈正从单一的计算或存储维度转向 KV cache 的综合优化，DeepSeek-V4.1-Flash 与 Video DeltaNet 分别从模型架构设计与注意力机制改进两个方向推进这一目标。When2Think 则揭示了推理效率优化的新路径——从统一长度约束转向实例自适应的计算分配，这可能与 Agent 工作负载的输入重型特征相呼应。

## 编码与GUI智能体系统设计

SoL-Pi 提出了一种递归扩展自动研究循环的方法，在 Action execution、context compaction、observation handling 和 delegated reading 四个机制上实现 token 效率优化，在 EdgeBench 51任务上达成与 Pi 相当的性能，同时将 token 流量降低 44.7-49.0%，API 成本降低约三分之一 [SoL-Pi](https://arxiv.org/abs/2609.20519)。针对编码智能体的组件级分析显示，上下文管理在窗口预算收紧时价值显著提升，主要是预防上下文溢出；在较弱模型上规划是准确性脚手架，在较强模型上则转为成本节省工具；预定义工具对 bash 能力较弱的模型有益，而具备 bash 能力的模型使用纯 bash 界面可实现更低的成本 [An Empirical Study of Harness Design](https://arxiv.org/abs/2609.20804)。对于 GUI 智能体，EvoSkill-GUI 提出训练无关的技能演化框架，通过 reflect-revise-reuse 循环在部署时从执行反馈中即时修订技能，在 MobileWorld、AndroidWorld 和 OSWorld 上分别实现最高 +16.2%、+6.0% 和 +10.5% 的提升 [Reflect, Revise, Reuse](https://arxiv.org/abs/2609.17653)。此外，ActObs 方法通过在 SFT 阶段同时对观察 token 进行监督，使策略保留环境预测能力，在 Terminal-Bench 2.0 和跨领域代码编辑任务上均优于仅监督动作的基线 [Don't Mask the Environment](https://arxiv.org/abs/2609.20715)。

编码与 GUI 智能体的研究正从单一模型能力提升转向系统级优化，包括 token 效率、组件模块化设计和部署时技能演化。ActObs 的发现——动作与观察梯度在 SFT 阶段迅速正交化——提示了当前训练范式的结构性缺陷，而 EvoSkill-GUI 的零训练演化机制则为动态界面适应性提供了一种轻量级解决方案。

## 在策略蒸馏与强化学习优化

多项研究聚焦于在策略蒸馏（OPD/OPSD）的关键问题。EOS token 不匹配分析发现，Qwen3、Llama 和 Gemma 等不同模型即使在声明相同的停止集合时，也可能将终止概率分布在不同 EOS token 上，导致学生模型的长度膨胀；将功能等价的 EOS token 视为共享语义停止动作可显著缓解此问题 [When EOS Tokens Disagree](https://arxiv.org/abs/2609.20511)。RetireOPD 提出自适应退休机制，让学生模型在自身成功率达到教师目标比例且差异停止缩小时自动放弃教师监督，在 Qwen2.5 1.5B-7B 模型上将 ALFWorld 成功率提升 14.1%-18.8%、WebShop 准确率提升 11.8%-19.0% [RetireOPD](https://arxiv.org/abs/2609.20784)。关于特权信息的价值研究使用 AMPLE-Math 数据集发现，参考-free 蒸馏已解释了 Qwen3-1.7B 大部分改进，特权参考仅在 polished solution 场景下贡献显著，且这些收益取决于学生模型是否经过训练 [What Does Privileged Information Add](https://arxiv.org/abs/2609.20612)。测试时扩展方面，Sample Count Is Not Enough 指出仅报告候选数量不足以描述系统成本，固定 N=8 时八次串行调用比单次批量调用能耗高 4.64-4.86 倍、P95 延迟高 5.77-6.12 倍 [Sample Count Is Not Enough](https://arxiv.org/abs/2609.19499)。

OPD 相关研究揭示了多个未被充分重视的技术细节：EOS token 语义对齐、教师监督的阶段性价值、特权信息的边际贡献边界。这些发现共同指向一个趋势——在策略蒸馏的效率优化正从架构设计转向训练动态与超参数策略的精细化控制。

## 多模态世界建模与具身智能

JEPA-Anything 提出了一种领域无关的预测因子分解框架，在视觉、生物、临床轨迹、控制、分子动力学、物理场和天气七个领域均优于匹配的 JEPA 基线，在干预预测任务上将 Interventional Pong 的单次干预预测误差降低 34.8%，并在分子动力学中实现最低的一步和百步预测误差 [JEPA-Anything](https://arxiv.org/abs/2609.20800)。VABench 评估了通用 MLLM 在具身空间智能中的 observe-reason-act-revise 循环，发现主动相机控制使任务成功率从 27.86% 提升至 57.50%，但 Held-out 几何迁移可导致成功率下降超 30 个百分点，且无一模型完成严格的长视程片段 [VABench](https://arxiv.org/abs/2609.19554)。MiniMax-H3 的物理世界推理评估覆盖隐式提示、音频-图像、前缀视频和音频-视频四种多模态输入场景，整体成功率 41.97%，其中基于视频的决策推理表现最佳（56.00%），基于音频的消歧推理最弱（27.40%）[Can MiniMax-H3 Reason](https://arxiv.org/abs/2609.18323)。在 MLLM 感知优化方面，Vision-RL2 通过区域级强化学习优化提议网络，用约四倍更少的视觉 token 达到了最大预算模型的精度 [Region-Level Policy Optimization](https://arxiv.org/abs/2609.19745)。

世界建模与具身智能的研究正从单一领域验证转向跨域通用性探索。JEPA-Anything 的跨七领域验证与 VABench 发现的 active perception 价值，共同提示多模态统一表征在物理推理中的潜力；MiniMax-H3 评估中音频模态的相对薄弱则揭示了当前多模态对齐的不均衡性。

## 评估基准与测试框架

多项研究提出了面向特定领域的评估基准。WeVisDoc 采用两阶段数据中心方法，在 OmniDocBench v1.6 上达到 95.38 的总分，在 PureDocBench 三个赛道均获第一，第二阶段通过保留探测数据集诊断残差错误并指导针对性数据构建 [WeVisDoc](https://arxiv.org/abs/2609.20423)。UFO 提出原子化评估单元链范式，将多模态对齐评估分解为细粒度单元，与人工评估相关性平均提升 15.25% [UFO](https://arxiv.org/abs/2609.12397)。RiskChainBench 针对平台滥用campaign，配对 3,600 条合成消息恢复输入与 600 个本地化 Web 调查环境，发现执行失败占 Web 运行的 31.9%，稳定探索与风险判断是主要瓶颈 [RiskChainBench](https://arxiv.org/abs/2609.16900)。PACT 基准在 12 个企业监管领域、48 个场景中测试 AI 助手的合规性，发现即使最强助手也有 6-10% 的项目误用规则，普通用户压力使违规率平均上升 65% [PACT](https://arxiv.org/abs/2609.18605)。VākQA 提供了 2,001 对泰卢固语事实型问答，发现语音输入引入的音素混淆和级联 ASR-MT 误差会累积影响答案正确性 [VākQA](https://arxiv.org/abs/2609.19879)。

评估基准的设计趋势正从单一任务指标转向多维度、对抗性场景和跨模态一致性检验。PACT 的压力测试框架和 RiskChainBench 的链式评估协议，反映了对 AI 系统鲁棒性和安全性的更高要求；WeVisDoc 和 UFO 则分别针对文档解析和多模态生成提出了数据驱动与链式分解的评估方法论。

## 3D视觉与多语言生成

FAMOS 提出了一种前馈式 3D 铰接物体建模方法，通过多状态铰接 Transformer 聚合稀疏观测中的运动证据，并引入观测铰接跨度目标函数，在 PartNet-Mobility、ACD 和 ArtiCraft-10K 上均优于现有基线 [FAMOS](https://arxiv.org/abs/2609.20817)。Srijika 系统针对九种婆罗米系文字（天城文、泰米尔文、孟加拉文等）提出 OpenType 布局复用字体重构方法，通过保留模板字体的 cmap、GSUB 和 GPOS 数据，生成 66 个完整 TTF 字体，所有输出均通过 OpenType Sanitizer 验证 [Srijika](https://arxiv.org/abs/2609.05661)。

3D 视觉与多语言字体生成的研究展示了从单一任务优化向结构约束保持方向的演进。FAMOS 的多元观测聚合策略突破了单视图 priors 的局限，而 Srijika 的布局复用方法则为 Indic 文字的复杂连字系统提供了一种兼顾风格多样性和 OpenType 兼容性的可行路径。