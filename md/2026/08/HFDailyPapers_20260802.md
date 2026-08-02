

# 每日HFDailyPapers-2026年08月02日

## 世界模型与视频生成

多份研究聚焦于物理世界建模与视频生成的一致性。[PhiZero](https://arxiv.org/abs/2607.28624) 提出基于物理语言的先推理后渲染范式，从自然视频中自监督学习离散化的状态转移表示，显式建模物理世界演化；[ShadowDancer](https://arxiv.org/abs/2607.28362) 通过影子对（相同动态不同外观的视频对）学习统一的动力学表征，实现跨场景的动作迁移，在多个动力学家族中达到86%的盲评胜率；[VideoCoCo](https://arxiv.org/abs/2607.27380) 使用可执行Blender代码作为中间推理链，将物理仿真与视频生成分离，在PhyGenBench上将OmniWeaving基线从0.475提升至0.558。[Chimera](https://arxiv.org/abs/2607.28611) 设计混合视觉扩散Transformer，结合Kimi Delta Attention与稀疏MoE，11B参数（2B激活）在预训练扩散损失上较全注意力Wan-2.1基线提升1.7倍计算效率，并支持零样本从5秒外推到30秒视频。分析表明，视频生成正从隐式动力学学习向显式可执行中间表示演进，代码级过程建模与物理语言抽象有望缓解现有模型在时态一致性上的瓶颈。

## 代理记忆与知识管理

记忆机制在多个代理系统中得到独立探索。[Memory Decoder at Scale](https://arxiv.org/abs/2607.27919) 将参数化长期记忆扩展至6.9B参数和300B tokens，证明独立扩展记忆模块优于扩展基础模型本身，Pythia-410M配对后超越Pythia-12B且参数减少39%；[MemHarness](https://arxiv.org/abs/2607.28272) 提出记忆重构而非重放，通过统一策略模型在当前状态下批判性重建检索经验，在ALFWorld和WebShop上显著优于静态记忆基线；[Σ-Mem](https://arxiv.org/abs/2607.27958) 针对多智能体系统设计在线可靠性记忆，记录个体能力证据与关系证据，基于Weyl不等式保证谱更新稳定性，OOD泛化优于多数投票；[Metis](https://arxiv.org/abs/2607.26760) 首次提出记忆基础模型概念，将持久记忆状态内嵌于骨干网络并通过记忆注意力访问，在线维护无需梯度；[Filesystem-Based Memory](https://arxiv.org/abs/2607.26637) 系统研究基于文件系统的代理记忆，发现结构化存储可减半检索成本，但仅最强管理代理能维持组织形态。分析表明，参数化记忆与外部存储两条路径并行发展，前者追求端到端可微，后者强调可解释与可持续组织。

## 检索增强与推理验证

检索范式与多模态推理验证得到深入对比。[BM25 Wins at Scale](https://arxiv.org/abs/2607.26497) 在28个严格嵌套语料层级上对比Lexical、Dense、图基RAG与代理搜索，发现BM25在约1000万token处实现跨尺度反超，Lexical检索成为可扩展默认方案；[AskChem](https://arxiv.org/abs/2607.28618) 将化学文献检索单位从论文转为可溯源声明，索引240万声明/14.7万论文，GPT-5.5在AskChem-Bench上DOI解析率达100%；[Harness-G](https://arxiv.org/abs/2607.27652) 将自由形式查询生成重构为有限动作选择，缓解检索等价坍塌现象，在1.5B和3B模型上较Graph-R1分别提升10.74和3.98 F1点；[LedgerMind](https://arxiv.org/abs/2607.28374) 通过结构化证据账本约束多模态代理轨迹，防止无来源内容引入，同时改善答案准确率与轨迹忠实度；[Beacon](https://arxiv.org/abs/2607.28595) 提出Mode Adaptiveness与Tool Effect两维度评估视觉推理，通过必要性感知奖励与提示引导能力扩展强化RL训练。分析表明，传统检索范式在大规模下仍具竞争力，而声明级结构化与轨迹验证正成为提升RAG可靠性的关键方向。

## 多模态与具身智能

多模态感知与具身数据成为独立研究主线。[ACE-Data-0](https://arxiv.org/abs/2607.28625) 通过人体中心环境捕捉引擎构建150小时/1700万帧多模态数据集，涵盖从手部操作到全屋运动的完整感知-行动环路；[MPIE-Bench](https://arxiv.org/abs/2607.27616) 引入基于多人体网格重建的解剖学与交互性双轴评估，揭示VLM-as-judge对几何错误的高估问题，现有编辑模型在两项指标上均未超过0.72；[SpatialCLI](https://arxiv.org/abs/2607.27703) 通过三阶段框架（暴露-学习-内化）教授VLM使用空间工具，MindCube上Qwen3-VL-8B从29.3%提升至84.6%，内化后仍保持73.8%；[ReToken](https://arxiv.org/abs/2607.28627) 通过单一可学习嵌入从视觉KV缓存中选择稀疏相关token，在Visual Haystacks上Qwen3VL-8B提升13.4点；[See2Think](https://arxiv.org/abs/2607.26769) 系统评估多模型是否真正依赖中间视觉状态，发现忠实渲染仍是主要瓶颈。分析表明，具身智能正从单一模态评估转向多模态同步数据构建，而空间推理能力可通过工具内化实现零工具推理。

## GUI与计算机使用代理

跨平台GUI代理能力成为竞争焦点。[Qwen-UI-Agent](https://arxiv.org/abs/2607.28227) 统一移动、桌面、网页与DeepSearch环境，支持GUI与CLI动作交织执行，在MobileWorld达82.1%、MobileWorld-Real达92.2%、AndroidDaily达97.5%，领先于Opus 4.8、Gemini 3.1 Pro与GPT-5.6 Sol；[Echoverse](https://arxiv.org/abs/2607.28074) 提供具有行为深度、交互针对性与共进化能力的状态化训练环境，9B模型从36.5%提升至67.1%，距教学其的前沿模型仅差14点；[Palate](https://arxiv.org/abs/2607.27816) 通过用户模拟器进行个性化角色扮演评估，发现固定历史对话无法反映真实多轮体验，个性化评估标准与人类判断一致性高于通用标准。分析表明，GUI代理正从单一平台向跨平台统一执行演进，而评估方法论亦从固定打分转向用户对齐的个性化度量。

## 模型训练与效率优化

训练范式与架构效率持续迭代。[Flux-OPD](https://arxiv.org/abs/2607.28022) 提出 evolving contexts 在线蒸馏，通过反向KL分解揭示几何平均与冲突项机制；[β-OPSD](https://arxiv.org/abs/2607.28582) 将自蒸馏统一为策略优化家族成员，β参数化参考策略约束强度，在数学推理基准上稳定超越 vanilla OPSD；[Explorative Modeling](https://arxiv.org/abs/2607.27372) 引入探索作为预训练第三轴，在连续与离散域均单调提升性能，计算效率提升4.1倍；[Multi-Head Attention Residuals](https://arxiv.org/abs/2607.27230) 将残差流路由拆分为每子空间头部，1B模型验证损失提升0.140，8B中训练后GSM8K提升3.2点；[OmniScope](https://arxiv.org/abs/2607.23193) 实现模态解耦Token压缩，25%压缩率下获得3.53倍预填充加速与15%+显存降低；[Intact](https://arxiv.org/abs/2607.26056) 提出意图到动作的同构世界模型，四任务成功率达85.78%-100%，直接推理仅需2.9-5.5ms；[ReToken](https://arxiv.org/abs/2607.28627) 轻量设计支持单H100长视频推理。分析表明，训练效率优化正从单一参数扩展转向探索-蒸馏-架构设计的协同改进。

## 公平性、可靠性与测试安全

模型可靠性和安全性评估受到系统关注。[Fairness Pruning](https://arxiv.org/abs/2607.28319) 在GLU-MLP层定位人口统计偏差神经元，零化最多40个神经元（Llama-3.2-1B不足0.031%宽度）实现99.49%推理能力保持，但引发双向偏差失稳；[MisKnow-Agent](https://arxiv.org/abs/2607.20891) 构建5933个误导性知识实例，揭示Deep Research代理即使在有限接触下仍会采纳错误结论，聚焦验证与工作流程级证据使用存在脱节；[Pedestrian Archetypes Extension](https://arxiv.org/abs/2607.16922) 新增7类行人原型扩展自动驾驶安全测试集。分析表明，从静态偏见检测向动态工作流可靠性验证转变，安全评估正从单一维度测试转向全链路证据链追踪。

## 其他动态

[AMRD](https://arxiv.org/abs/2607.25289) 提出自适应多教师关系蒸馏用于端侧语音情感识别，在IEMOCAP和CREMA-D上超越单教师基线；[Lossy Verification in SD](https://arxiv.org/abs/2607.26627) 分析投机解码中损耗验证的分布失真机制，将方法归类为截断式与协作式两类；[AI Tour Meeting](https://arxiv.org/abs/2607.18806) 提供多LLM代理协作行程规划框架及仿真分析接口。