

# 每日HFDailyPapers-2026年09月26日

## Transformer 内部机理与可解释性

两项工作分别从线性叠加与语言结构编码两个角度剖析了 Transformer 的内部表征机制。[Your Transformer Can Hold Two Thoughts at Once](https://arxiv.org/abs/2609.29845) 提出"叠加线性假设"，证明当输入来自不同文本流时，模型输出是各单独 next-token 分布的叠加；叠加线性是 Transformer 架构的内生属性，随预训练推进反而减弱，但可通过轻量微调显著恢复，并据此设计了引导解码过程实现单次前向传播同时生成两条连贯续写。[Parts-of-Speech as Emergent Categories in SAE Latent Space](https://arxiv.org/abs/2609.29362) 以词性（PoS）类别为控制测试用例，发现 SAE 潜在空间中 PoS 区分度高可恢复，但不存在单 latent 与单类别的映射关系；该可恢复性并非来自词汇记忆，开放类与封闭类 PoS 差异显著，类别由紧凑的稀疏 latent 群体支撑且跨验证数据保持稳定。

分析表明，线性叠加性质与 SAE 表征结构的研究共同指向 LLM 内部存在可解析的系统性规律，叠加线性随训练减弱则提示训练可能以非线性方式重塑表征；SAE 中语言结构的分布式编码方式为后续因果干预和可解释分析提供了新的操作接口。

## 视频生成与多模态生成

本期视频生成方向论文覆盖提示增强、联合音视频生成、少步因果视频及世界模型训练四个子主题。[WanPE](https://arxiv.org/abs/2609.30221) 提出 397B 参数提示增强模型，通过视频接地反向构建与语义一致性 GRPO（SC-GRPO）实现导演级电影规划，在 Wan3.0 上 5-15 秒段真人偏好提升 10.66-18.84 分、30 秒段提升 50.86 分。[AV-GRPO](https://arxiv.org/abs/2609.29816) 提出模态锚定扩散强化学习框架，将耦合的多模态偏好学习分解为单模分子问题，在 JavisBench 和 VABench 上超越 LTX-2.3。[ViRDM](https://arxiv.org/abs/2609.28923) 将表征分布匹配（RDM）迁移至少步因果视频生成，通过随机截断干净出口监督、轻量 VAE 解码器与分阶段向量-Jacobian 乘积消除教师-评审网络，仅用 20 次生成器更新即达 VBench 84.87 分，训练成本低至 16 A100 GPU 小时。[Training Object Permanence in World Models](https://arxiv.org/abs/2609.28654) 引入 WROP 数据集（150 个人工设计认知科学任务、150 万训练样本），训练 16B 世界模型 PWM-WROP，在延续类模型盲评中排名第一。

分析表明，视频生成正从"更大模型"转向"更高效的训练范式"，ViRDM 去掉教师-评审网络的蒸馏路径与 AV-GRPO 的模态解耦设计均体现了这一趋势；WanPE 则说明提示工程已成为视频生成质量的关键瓶颈，电影级规划能力的引入有望弥合文本描述与视频产出之间的语义鸿沟。

## AI 智能体与 AI-for-AI 框架

本期智能体方向论文数量最多，涵盖闭环开发、深度搜索、任务与运动规划及操作系统四个层面。[Qwen-Planner-Agent](https://arxiv.org/abs/2609.29892) 构建 AI-for-AI 闭环框架，通过 AI for Data、AI for Training（引入 CARE 奖励机制）和 AI drives model-harness co-evolution 三阶段驱动移动规划智能体迭代。[IterSynth](https://arxiv.org/abs/2609.29444) 提出角色解耦迭代合成范式，将规划器与综合器分离并以摘要作为持久状态，配合 RDPO 强化学习在 BrowseComp 等基准上超越此前最强 8B 智能体 4.2%。[Coding Agents for TAMP](https://arxiv.org/abs/2609.30233) 评估 Claude Code 与 Codex 在 28 个仿真环境中的代码生成能力，生成的程序在 98,000 次评估中成功率达 56%-95%，超过手工规划器并在对象数量增长时保持优势。[Agent-Editing World Model](https://arxiv.org/abs/2609.28416) 提出 AEWM 模型任务进展而非工具响应，通过 Action Judge 与 State Revision 消除任务状态污染，EditAct 在六个基准上提升 3.2-6.7 分。[AgentKernel](https://arxiv.org/abs/2609.29647) 提出信任原生智能体操作系统，将身份、感知、认知、执行四个支柱作为强制 enforcement 边界以应对提示注入、记忆中毒和工具滥用等语义层攻击。

分析表明，智能体研究正从"单点能力突破"走向"系统工程化"，Qwen-Planner-Agent 的闭环飞轮和 AgentKernel 的操作系统范式均体现了这一转向；IterSynth 的角色解耦设计与 AEWM 的状态修正机制则为长程任务中的上下文管理和决策可信度提供了可验证的解决方案。

## 机器人操作与具身智能

三项工作分别探索了 VLM 驱动的机器人操作、双臂操作的世界-动作模型及空间音频导航。[World Action Agent](https://arxiv.org/abs/2609.29964) 提出视觉动作工作空间（contact views、action rehearsal、in-view correction），通过多智能体 harness 让 VLM 直接操控机器人，在 LIBERO-Pro 上达 75.6% 成功率 SOTA；微调 Qwen3.5-9B 后域外成功率从 1.7% 提升至 43.3%。[DeltaWAM](https://arxiv.org/abs/2609.28811) 提出 Delta World Action Model，联合预测视觉差值与动作，配合 Streaming Delta Memory 减少视频专家处理，在 RoboTwin 上将成功率从 81.3% 提升至 85.4%，单步推理延迟降低 36.57%。[OmniEcho](https://arxiv.org/abs/2609.23407) 引入 FOA 空间音频编码器构建全模态空间感知模型，在 OmniEchoBench（197 个真实场景、2,972 组问答）上达空间音频视觉感知 SOTA，声音引导导航性能接近传统视觉-语言导航。

分析表明，具身智能正在从"单模态端到端策略"转向"多模态世界模型驱动"，WAA 的视觉动作工作空间和 DeltaWAM 的增量预测均显著降低了计算负担；空间音频作为导航辅助信号的有效性得到验证，但在细粒度空间定位和距离估计上仍存在明显短板。

## 强化学习与后训练方法

两项工作分别提供了 LLM 后训练配方与扩散模型 RL 训练框架的开源方案。[Rufus-Air](https://arxiv.org/abs/2609.29421) 公开基于 GLM-4.5-Air-Base（106B-A12B）的八阶段串行后训练配方（SFT→Reasoning RL→Coding RL→Instruction-Following RL→General Agent→Coding Agent→Search Agent→RLHF），强调多样化高质量 SFT、难度过滤、奖励可靠性排序及基础设施选择为关键设计原则，开源数据与奖励设计无需人工标注或内部蒸馏教师。[AV-GRPO](https://arxiv.org/abs/2609.29816)（亦属多模态生成）提出模态锚定 rollout 与轨迹锁定冻结塔优化的 RL 框架，将交叉模态奖励解耦以实现精确信用分配。

分析表明，开源后训练配方的价值不仅在于复现性能，更在于揭示阶段排序与奖励可靠性的系统性关系；Rufus-Air 的八阶段设计和 AV-GRPO 的模态解耦机制共同说明，强化学习在大型多模态模型中的应用正从"端到端联合优化"转向"分阶段、可归因"的训练架构。

## 对齐检测与安全评估

[Just Ask Jev](https://arxiv.org/abs/2609.29429) 提出通过校准决策强化学习（RLCD）训练 Jev 模型，以单一调用输出校准概率而非固定标签，构建 RLCDAlignBench 在 44 个基准和五个目标模型上检测十二种对齐失败（sycophancy、jailbreak、deception 等）。该方法通过分离问题表述与输入字段实现零样本 AUROC 0.886，成本仅为 LLM-judge 的 1/63，并能发现现有基准的标签缺陷。

分析表明，对齐检测正从"生成式评判"和"固定分类器"走向"校准概率输出"，RLCD 的单次调用多问题回答机制在保持与人类标注者一致的同时大幅降低成本；问题表述与输入字段的分离设计也为关系型对齐失败（需参考外部上下文才能定义的失败）的检测提供了新的方法论。

## 数学推理与科学探索

两项工作分别从定理发现有趣性和 AI 自主探索两个角度拓展了 AI 在科学发现中的作用边界。[Learning to Discover Interesting Mathematics](https://arxiv.org/abs/2609.28603) 将定理内在有趣性定义为证明长度与陈述长度之比，训练 27B 模型预测证明难度，优化该度量使与 Mathlib 的重叠从 91.9% 降至 30.6%，实现了自我扩展的形式化数学库。[ExplorationBench](https://arxiv.org/abs/2609.30199) 构建 AlienCode 与 AlienLogic 两个沙盒（共 55 个发现目标、140 个任务），以可执行规则与冲突常识确保答案可验证且无法通过预训练记忆解答，评估 10 个 AI 系统发现最强模型可获取并应用陌生规则，但持续探索可能出现停滞或倒退。

分析表明，数学发现与科学探索的共同挑战在于如何区分"已知知识的重组"与"真正的新发现"；有趣性度量的形式化定义和 Alien Worlds 的可验证沙盒分别为此提供了量化信号和实验环境，但探索过程中的稳定性问题仍是未解挑战。

## 视觉表征与图像质量评估

两项工作分别聚焦 RGB-D 分割基准与视频编码中的图像质量评估。[RGBD20K](https://arxiv.org/abs/2609.29028) 发布包含 20,000 对 RGB-D 图像、160 个细粒度类别的大规模数据集，纠正既有标签噪声并提出 SPF 融合方法达到 SOTA；代码已开源。[Rate-distortion optimization for FR-IQA](https://arxiv.org/abs/2609.30077) 将 MS-SSIM、LPIPS 等全参考图像质量指标近似为输入依赖二次失真（IDQD），通过 Hessian 矩阵的块对角或对角近似实现块级 RDO，在 VVC 下实现 14.2%-36.7% BD-rate 节约，编码复杂度增加 10%-30%。

分析表明，高质量开源数据集与编码效率优化是视觉系统发展的两条并行主线；RGBD20K 的大规模细粒度标注将推动更泛化的分割模型发展，而 IDQD-RDO 将感知质量指标引入编码环内则为视频压缩的视觉保真度提供了可量化的优化目标。

## 其他动态

[Neural Spectural Capacity](https://arxiv.org/abs/2609.23087) 提出基于权重矩阵奇异值谱的 NSC 标量，仅从架构规格即可计算并在全局最优动态规划下秒级搜索最佳深度-宽度分配，在 LLaMA-7B 剪枝实验中较最强无校准代理快约 5900 倍。[PUBG Ally](https://arxiv.org/abs/2609.29837) 发布语音驱动的具身游戏队友，基于近 39,000 局真实对局数据迭代训练，在 141 个国家玩家调查中推荐正评率高出负评 25.1 个百分点。