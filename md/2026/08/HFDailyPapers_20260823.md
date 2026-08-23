

# 每日HFDailyPapers-2026年08月23日

## 长上下文推理与高效计算

FlashPrefill V2 针对长上下文大语言模型在服务阶段的二次复杂度瓶颈，提出了块稀疏预填充注意力方案 [FlashPrefill V2](https://arxiv.org/abs/2608.19758)。该方法引入均值校正项抑制近似误差，重新设计了与FlashAttention-3/4对齐的稀疏注意力算子（PackGQA内存访问、warp specialization、pingpong流水线），并原生支持paged KV cache和continuous batching。在NVIDIA H20 GPU上，FP8精度下相比FlashAttention-2实现47.26倍加速，BF16精度下实现27.19倍加速。数据分析表明，该框架将稀疏注意力从算法原型推向生产部署，FP8量化支持的引入对实际推理成本优化具有直接意义。

## 机器人操作与VLA策略学习

EXIMO 提出了一种视觉-语言-动作（VLA）策略的高效微调算法，通过三阶段流程（探索-模仿-优化）提升样本效率 [EXIMO](https://arxiv.org/abs/2608.19891)。在探索阶段，VLM作为规划器将长horizon任务分解为子任务；模仿阶段利用编排数据微调VLA；优化阶段使用残差off-policy RL进一步调整。τ_0-VLA 则采用分层架构，高层策略通过执行记忆生成子任务并在必要时搜索替代方案，低层策略执行具体动作，测试时计算量可动态分配 [τ_0-VLA](https://arxiv.org/abs/2608.16885)。该方法在40,115小时异质真实数据上训练，在分布偏移场景下均表现良好。GOAG 和 CoToGrasp 分别从接触面几何匹配和接触拓扑条件生成角度推进灵巧抓取能力，两者均不依赖物体特定训练数据，在MultiDex和DexGraspNet数据集上取得state-of-the-art结果 [GOAG](https://arxiv.org/abs/2608.19759)、[CoToGrasp](https://arxiv.org/abs/2608.19776)。

## LLM Agent的自我进化与任务框架

FlowEvo 提出工作流与可执行技能的推理时协同进化框架，将成功工作流编译为可调用技能并存储于持久库，同时追踪技能下游效用以抑制负迁移 [FlowEvo](https://arxiv.org/abs/2607.21596)。在ALFWorld上达到85.6%准确率，较最强基线高出26.4个百分点，且Token消耗约为其三分之一。Hierarchical Self-Improvement (HSI) 构建了三层次进化架构（任务harness、evolver、meta-evolver），通过热交换实现harness迭代改写，在DeepSeek-V4-Flash-Preview上于BALROG基准取得稳定提升 [Hierarchical Self-Improvement](https://arxiv.org/abs/2608.08466)。Repo0 针对从零代码生成场景，维护显式架构状态（Dual-DAG），通过模块化度量引导结构演化直至收敛，在RepoCraft上较RPG基线将功能覆盖率提升20.08个百分点、通过率提升29.74个百分点 [Repo0](https://arxiv.org/abs/2608.19854)。

## Agent评估与合规控制

SWE-bench Science 建立了涵盖20个科学领域、119个任务的代码智能体基准，揭示科学软件工程的独特挑战 [SWE-bench Science](https://arxiv.org/abs/2608.19799)。即使最优模型（Claude Code with Opus-5 max）通过率仍低于50%，分析识别出四类失败机制：科学知识缺失、探索偏差、修复不完整、泛化失败。PolicyGuide 将领域策略编译为工作流图，在用户轮次边界调用主动验证器，在τ²-bench上平均Pass⁴从0.42提升至0.62，电信领域提升最显著（0.19至0.61） [PolicyGuide](https://arxiv.org/abs/2608.19861)。QuoteBench 通过精确最终状态验证和故意引入的解析器边界，揭示匹配执行分数无法区分命令生成错误与执行传输错误的问题 [QuoteBench](https://arxiv.org/abs/2608.13547)。

## 多模态视频理解与生成

4DAnyone 解决从单目视频重建4D人物的问题，识别出有界注意力上下文的两大瓶颈（参考上下文复杂度O(N)、目标组间信息隔离），提出Reference Context Packing和Target Context Routing两个设计 [4DAnyone](https://arxiv.org/abs/2608.20335)。NARU 基准测试1,481个问题覆盖155部日语长视频（共146.8小时），系统评估叙事演化与文化理解能力，测试结果显示现有模型在长期叙事整合和文化推理方面存在显著局限 [NARU](https://arxiv.org/abs/2608.13210)。ForgeWM 通过渐进因果训练将双向视频生成器转化为少数步骤世界模型，支持1/2/4步去噪预算，在Minecraft和FPS控制任务上取得最优成像质量与动作对齐准确率 [ForgeWM](https://arxiv.org/abs/2608.14022)。

## 记忆、知识内化与认知偏差

MemTrapBench 首次系统评估记忆引发的认知陷阱，包括推理固化和信念扭曲两种形式 [MemTrapBench](https://arxiv.org/abs/2608.20202)。实验显示所有评估的记忆策略均低于无记忆设置，最强方法仍下降超10%；提出的AdaptiveMem在推理时有效缓解此类陷阱。IAR（Inject-Align-Recover）框架通过三阶段后训练实现检索无关文档知识内化，在Llama/Phi/Qwen/SmolLM系列上平均提升领域QA准确率3.6个百分点、通用性能提升12.1个百分点 [IAR](https://arxiv.org/abs/2608.20281)。Thinking in a Low-Resource Language 研究揭示SFT在低资源语言中的真实效果：准确率基准无法捕捉变化（随机种子变动可产生7.7分波动），但行为维度分析显示SFT使模型在98%样本中用目标语言推理，RL进一步修复格式跳过和推理泄漏问题 [Low-Resource Language](https://arxiv.org/abs/2608.17744)。

## 代码生成与终端任务合成

FACET 框架通过重构相关智能体技能生成信息丰富的场景，确保执行环境、指令、解决方案和验证器之间的交叉一致性 [FACET](https://arxiv.org/abs/2608.18580)。分析表明，基于执行环境的构建是实现任务有效性和解决方案-验证器对齐的关键原则，多尺度微调在Terminal-Bench 2.1上持续提升性能。

## 音频表征与预测建模

NAPE 提出极简自监督框架，通过因果Transformer直接预测log-mel谱图的下一个patch嵌入，无需重建解码器、声学token化器或辅助正则化 [NAPE](https://arxiv.org/abs/2608.19863)。该方法在六个音频和语音基准测试中实现最先进微调性能，且在无显式监督下产生结构化注意力模式。TinyCast 是参数量仅146,505的零样本预测器，通过零参数频谱检测器计算主导周期，折叠上下文后用扩张卷积编码器和块自回归分位数解码器建模，在GIFT-Eval中定义尺寸-准确性前沿 [TinyCast](https://arxiv.org/abs/2608.15767)。

## Embedding与LLM的成本权衡

The Embedder's Dilemma 通过受控对比研究评估十种LLM与26种嵌入模型在37个任务上的表现 [Embedder's Dilemma](https://arxiv.org/abs/2608.12875)。结果显示两种范式总体持平（最佳LLM得分77.6 vs 最佳嵌入模型77.2），但LLM成本高达嵌入模型的1,431倍，且推理速度低2.5至736倍。分析建议按任务分工：嵌入模型用于相似度/分类/聚类，LLM仅用于推理密集型检索。

## 测试时学习与经验积累

Chain-of-Experience 研究LLM在测试时通过迭代交互积累经验实现持续改进的能力 [Chain-of-Experience](https://arxiv.org/abs/2608.18027)。在数学、编码和知识领域的8个LLM测试中，利用迭代经验持续优于无反馈基线，整体提升5.6%且API成本降低19%。组合模型反馈与正确性信号可带来额外增益，且CoE在每Token准确率上优于现有测试时策略。