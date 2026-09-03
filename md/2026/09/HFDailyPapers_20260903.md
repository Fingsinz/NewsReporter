

# 每日HFDailyPapers-2026年09月03日

## 自主代理与操作知识蒸馏

自主代理正在发展端到端的机器学习研究能力，但现有的代理架构将领域专业知识排除在外。[Repo-To-Skill](https://arxiv.org/abs/2609.02749) 提出 DisCo，一种技能驱动的研究代理，通过在任务无关和任务导向两个维度上从 GitHub 仓库蒸馏操作知识。该方法构建了包含 5,000+ 经过验证技能的 AREX-Skill Library，从 1,000 个广泛使用的 ML 仓库中提炼，覆盖 20 个领域和 178 个能力家族。在固定 GPT-5.5 骨干和研究框架的前提下，配备技能的代理在 MLE-bench 上得分提高 134.3%，在 PaperBench 上提高 34.4%。[EarlyEval](https://arxiv.org/abs/2609.02783) 针对代理评估成本过高的问题，提出通过早期结果预测来减少每任务执行步骤。该方法训练 LightGBM 分类器，在 SWE-bench Verified、TerminalBench 和 Toolathlon 三个基准上消除 13%-26% 的代理步骤，输入 token 减少达 44.1%，预测准确率达 89%-97%。[HarnessDev](https://arxiv.org/abs/2609.01437) 评估 LLM 创建和执行自身代理 harness 的能力，在六个创造模型、四个领域的 2,207 个实例上测试，发现生成的 harness 在代码和搜索研究领域仍大幅落后于人类工程师参考，但在写作和 ML 实验领域可达到或超过参考。

分析表明，操作知识的显式蒸馏正成为提升代理研究能力的关键路径，技能库的可复用性显著减少了重复发现成本。代理评估的效率优化（如 EarlyEval 的早期终止策略）显示了从"减少任务数"向"减少每任务成本"的范式转变趋势。然而，HarnessDev 的结果揭示了当前模型在自主构建执行基础设施方面仍存在能力鸿沟，尤其是跨领域迁移性的局限。

## 视频世界模型与视觉表示学习

[SolarWM](https://arxiv.org/abs/2609.02886) 提出构建交互式视频世界模型的开放基础，通过将 10 个数据集中的 143 万个规范片段转换为统一的帧对齐格式，解决了异构数据源的耦合问题。该方法基于 Wan2.2、LTX-2.5 和 MiniMax-H3 实例化了 5B-33B 参数模型，在仅训练 5 秒序列后，因果模型可实现分钟至小时的实时交互回放。[Pixel Linguist II](https://arxiv.org/abs/2609.01147) 研究像素级文本表示学习的根本设计原则，通过系统消融识别出四个关键组件：可变图像分辨率、自然图像-文本对、布局感知渲染和多语言课程。该编码器在 2.8 亿训练样本上训练，在英语、跨语言和多层 Visual STS 及 ViDoRe 上达到新 SOTA，且在 80% 视觉 token 压缩下仍保持鲁棒性。[SimLoss](https://arxiv.org/abs/2609.00591) 提出一种无参考的嵌入空间目标，用于单次-pass 细粒度图像描述生成。该方法通过 InfoNCE 对比损失在文本解码前提供密集视觉监督，SimLoss FFT 变体在保持单次-pass 推理的同时，比多阶段流水线快约 20 倍。[SnapBench](https://arxiv.org/abs/2609.02783) 构建了首个针对移动场景中 snap-and-ask 多模态检索的配对基准，涵盖 1,145 个查询、9,085 个图库项和 53 种受控污染条件，评估发现图像污染显著降低检索性能，而文本污染对联合检索影响有限。

分析表明，视频世界模型的训练基础设施正朝着开放化和标准化方向演进，SolarWM 的解耦设计为复现和比较提供了可操作的路径。视觉表示学习中，像素级处理和自然图像对的引入有效缓解了文本-only 坍塌问题，为文档理解场景提供了高效的压缩方案。

## 长上下文推理与注意力优化

[Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737) 提出声明式注意力（Declarative Attention, DA），让模型在思维链中声明需要关注的上下文区域，从而跳过大部分 KV cache 读取。该方法在 Gemma-4-31B 和 Qwen-3.6-27B 上实现了 52.0% 和 31.1% 的总注意力 token 减少，准确率下降分别仅为 1.27pp 和 2.75pp。[CRISP](https://arxiv.org/abs/2609.01925) 针对动态稀疏注意力中的结构挑战，提出基于结构质量的代理 C_struct，替代 Jensen-Shannon Divergence 路由，消除了池化矩阵乘法和 KL 散度开销。在 InfiniteBench、RULER 和 LongBench 上，CRISP 在检索密集型任务上比基线恢复高达 28.0 个百分点，在 512k token 时实现 5.30x 注意力加速。

分析表明，长上下文推理的优化正从静态稀疏模式转向输入自适应的动态方法。DA 的"内在"方法与现有"外在"评分方法形成互补路径，而 CRISP 的结构质量代理证明了路由决策可直接从注意力图结构读出，无需额外的计算开销。

## 代码智能与编程能力

[Post-Training Language Models for Gold-Medal Performance in Coding Competitions](https://arxiv.org/abs/2609.02849) 提出针对编程竞赛的端到端专业化流程，结合问题整理、合成推理轨迹、SFT 和 RL。Nemotron-3-Nano-CC (30B-A3B) 在 IOI 2025 上从 130 分提升至 468 分，超过金牌阈值 438.3；Nemotron-3-Ultra-CC (550B-A55B) 在 IOI 2026 上获得 535.4 分，超越人类最高分 498.27。[PaperCompiler](https://arxiv.org/abs/2609.02272) 解决论文到代码生成的忠实性问题，将论文证据编译为显式的仓库级实现规范，在 Paper2CodeBench 上实现 13.8% 的相对提升，高分严重性评估减少从 13.2% 降至 6.1%。[ExecRetrieval](https://arxiv.org/abs/2609.01865) 提出代码嵌入检索的功能正确性基准，包含 939 个 Python 任务和执行验证的 buggy 变体，测试发现领先系统在 exec@1 上仅达 0.331，排名首位的失败中 91.5-99.4% 为配对 buggy 变体。[Debias-SparseGPT](https://arxiv.org/abs/2609.02496) 解决模型压缩中的偏差放大问题，在 25%、50% 和结构化 2:4 稀疏度下，该方法在保持模型困惑度和 zero-shot 准确性的同时一致减少剪枝诱导的偏差。

分析表明，编程能力的提升已从通用预训练转向竞赛专用的后训练流程，GenCorrect 的反馈驱动测试时计算策略展示了迭代优化的潜力。代码检索研究揭示了嵌入模型在功能正确性判别上的显著局限，这为代码 agent 的可靠性评估提供了更严格的测试标准。

## 多模态检索与信息检索

[NeoMME](https://arxiv.org/abs/2609.01657) 提出 260M 和 800M 参数的多模态多语言双向编码器，从 scratch 预训练，支持 16,384 token 上下文。NeoMME-Retriever 260M 在 ViDoRe v3 上达到 0.523 nDCG@10，在 2048x2048 输入下编码速度是 ColModernVBERT 的 2 倍，分层 token 池化和非对称量化压缩 Embedding 达 255 倍。[MULTI3IR](https://arxiv.org/abs/2608.30949) 构建包含 104.9K Stack Exchange 查询的多视角多领域多模态检索基准，提出 SPIN 方法通过学习噪声向量引导嵌入向多样化语义方向。实验显示现有模型存在单视角偏差，SPIN 显著改善了 Multi³IR 上的视角覆盖率。[KBMR](https://arxiv.org/abs/2608.21450) 针对基于知识的视觉问答，提出首个 MLLM 嵌入检索器，通过 MLLM 语义判别器生成连续实体一致性权重，在 Recall@1 上提升 14.7%，端到端 VQA 准确率提升 9.4%。

分析表明，检索任务正从纯文本或纯视觉向多模态融合演进，NeoMME 的单一编码器架构证明了高效多模态表示的可行性。MULTI3IR 揭示了现有模型在开放查询多视角覆盖上的系统性不足，SPIN 的参数高效方法为多样性检索提供了新方向。

## 模型压缩与知识蒸馏

[Influence-Directed Distillation](https://arxiv.org/abs/2608.29846) 分析采样 token 策略蒸馏中的多样性瓶颈，提出一阶局部熵影响度量，将每次更新的熵效应解耦为教师-学生 log-probability 差和学生局部概率结构。IDA-OPD 方法保留熵扩张更新，替换熵收缩更新为发散自适应优势收缩，在推理导向的蒸馏中显著改善 pass@k。[Cliff](https://arxiv.org/abs/2609.02817) 提出 RLVR 中的奖励塑形策略，利用现成 LLM 识别 rollout 中的第一个错误，将过程分解为正确前缀和错误后缀，赋予正负 token 级优势。在 12 个场景中，Cliff 比 on-policy 蒸馏提升 15%，比标准 GRPO 提升 7%。[VibeVoice-ASR-Streaming](https://arxiv.org/abs/2609.02812) 提出首个基于 LLM 的流式说话人归属 ASR 方法，7B 模型在五个评估集上达到最低平均 WER/CER，在 12/13 评估设置中达到最佳或并列最佳说话人归属性能。

分析表明，模型压缩和蒸馏正从追求单一指标优化转向多样性保持和细粒度监督。Cliff 利用"第一个错误"信号提供了比传统过程奖励更高效的训练信号，而 Influence-Directed 方法揭示了蒸馏中熵收缩的系统性机制。

## 动物运动生成与3D表示

[Kirin](https://arxiv.org/abs/2609.01823) 提出从野生视频中重建动物运动的框架，构建 AiM3D 数据集，这是首个提供四足动物对齐视频-文本-运动三元组的大规模数据集。该方法结合文本和图像条件生成多样化物种的真实运动，并通过图像到 3D 模型自动生成 rig 和动画。[ZipTok3D](https://arxiv.org/abs/2609.01740) 提出面向极高保真重建的紧凑 3D tokenization 方法，通过嵌套 dropout 随机截断编码后的潜在序列，要求每个保留前缀重建完整对象。该方法在 ShapeNet 上仅需 1 个 token 达到 32-token COD-VAE 基准的质量，在 TRELLIS 上仅需 4 个 token。

分析表明，动物运动生成的瓶颈正从数据采集转向表示学习，Kirin 的野外视频利用策略显著扩展了数据规模。3D tokenization 中，前缀优先策略证明了极短序列重建的可行性，为 3D 生成效率提供了新路径。

## 模型自我进化与评估基准

[Aspire](https://arxiv.org/abs/2608.31111) 提出模糊目标驱动的自进化基准，仅提供自然语言能力目标而隐藏下游评估任务。实验显示，当前代理能够完成训练循环，但权重级提升稀疏且不稳定，最强进化 harness 仍低于手工设计的 Qwen-Agent 参考。[S³Gym](https://arxiv.org/abs/2608.31100) 评估 LLM 通过自我测试、自我评判和自我改进实现自我提升的能力，在七个文本游戏中测试直接历史 ICL、分数条件摘要记忆和参数训练三种路径。结果显示自我提升既非自动也非均匀，最有效的路径强烈依赖任务结构。[Ignorance or Incompetence?](https://arxiv.org/abs/2608.30322) 提出知识门控任务构建协议，将任务指令与包含私有约定的紧凑工件分离，验证了某前沿代理在 68.0% 通过率与 0% 的极端差异。

分析表明，模型的自我进化研究揭示了从"任务优化"到"目标解释"的范式转变挑战。S³Gym 的发现表明，经验积累并不自动转化为能力提升，策略选择需要与任务结构匹配。知识门控协议为区分模型的知识缺口与能力不足提供了可操作的评估框架。

## 空间推理与领域特定应用

[Autoregressive Mosaics](https://arxiv.org/abs/2608.30751) 构建 AM-Bench 基准分离 2D 空间推理的翻译与布局能力，测试八种仅文本和代码的开放权重模型。结果发现，所有模型可靠地翻译指定几何为代码，但开放布局性能差异显著，且输出媒介（代码 vs SVG）显著影响得分。[FoldingAgent](https://arxiv.org/abs/2609.00377) 提出从折纸演示视频中推断显式参数化折叠程序的代理框架，结合 VLM 推理、几何模拟、物理合理性验证和视觉内容检索工具。[LLAMIA-Bench](https://arxiv.org/abs/2609.00474) 研究语言与非语言代理（如国际象棋引擎）的协作，引入潜状态内部化方法将子代理的连续表示直接投影到 LLM token 流中，14B 模型 LLAMIA 通过该方法匹配或超越带工具访问的 GPT-5.1。[Institutional Newspapers Pipeline](https://arxiv.org/abs/2608.18972) 与波士顿公共图书馆合作构建历史报纸处理流程，从 1,473,635 份 1795-1930 年公共领域报纸扫描中提取 163 亿 token，输出 8310 万独立裁剪。

分析表明，空间推理研究显示代码生成能力不足以解释 2D 布局理解，输出介质的选择对性能有系统性影响。LLAMIA 的潜状态内部化方法证明了绕过"语言化瓶颈"的可行性，为多代理协作提供了新的集成范式。历史报纸管道的可扩展设计为大规模非结构化文档的数字化处理提供了参考框架。

## 其他动态

[CoGR](https://arxiv.org/abs/2609.00638) 提出协同进化检索框架，训练 LLM 直接在查询和物品两侧构建检索表示，通过 GRPO 交替优化两侧生成器，在内部 APP 市场和 WANDS 基准上分别将 F₁ 提升 10.9% 和 36.1%。[Portfolio Risk Bounds](https://arxiv.org/abs/2608.29692) 和 [Wasserstein-Barycentric Interaction Fields](https://arxiv.org/abs/2608.29669) 探索语言模型表示在投资组合风险评估中的应用，利用 firm-level 分布特征替代跨资产收益协方差构建风险上界，在 52 公司面板上验证了基于 Qwen3-Embedding 的分配策略。