

# 每日HFDailyPapers-2026年10月07日

## AI代理安全与鲁棒性

本周研究聚焦于Web代理、工具使用代理及GUI代理的安全性与鲁棒性提升。[AdvSim2Real](https://arxiv.org/abs/2610.08773) 提出协同进化框架，在冻结的Web世界模型中同时演化任务课程、注入 adversaries 和Agent，训练后的4B代理在面对未见过的前沿模型adversary时，在150个Web任务上完成率提升33.6%。[From Evidence to Action](https://arxiv.org/abs/2610.07753) 引入SafeActBench基准，包含656个案例，揭示工具使用代理的证据到行动链条在交互执行阶段易断裂，单动作执行可靠但多动作工作流暴露未解决的先决条件问题。[GUI-HARVEST](https://arxiv.org/abs/2610.00948) 提出自动Harness优化方法，通过将模型输出与前后截图对齐、将重复任务运行作为联合证据单元，使Qwen3-VL-32B-Instruct在OSWorld-Verified上提升12.33分。[DAEDALUS](https://arxiv.org/abs/2610.08048) 通过探索者与求解者的双Agent协作从自生成任务中引导可复用记忆，在AppWorld等基准上将成功率提升最高15.9分。分析表明，代理安全研究正从静态防御转向动态对抗训练与可验证证据链，多阶段工作流的安全性仍是开放挑战。

## 强化学习训练方法优化

多篇研究探索RL训练的效率与稳定性。[TRACE](https://arxiv.org/abs/2610.07767) 针对MoE语言模型的FP4 RL训练，通过rollout引导的量化感知训练直接减少训练与rollout路径间的量化差异，实现最高5.4倍rollout加速且性能接近BF16。[NeMo-DCR](https://arxiv.org/abs/2610.08430) 提出位精确的Delta压缩Refit机制，在3%变化率下将1T模型跨集群refit时间从87.5分钟降至150秒。[MEND](https://arxiv.org/abs/2610.05954) 引入近端速度匹配方法，在100次更新内超越Flow-GRPO的4000次更新效果。[HuatuoGPT-3](https://arxiv.org/abs/2610.05966) 针对纯在线RL的冷启动问题，提出OnePO框架，在医学领域适应中HealthBench总分达70.1，超越GPT-6 Astra。[RGPO](https://arxiv.org/abs/2610.07342) 通过自适应推理脚手架缓解奖励稀疏问题，在语言和视觉语言推理中均优于RLVR基线。[DiffGate](https://arxiv.org/abs/2610.04596) 将GRPO与选择性教师指导结合，仅对失败轨迹应用教师监督。[OPD Before RL](https://arxiv.org/abs/2610.02781) 利用评分标准作为特权教师上下文进行密集token级蒸馏，再应用于RL阶段。数据表明，RL训练正从单一目标优化转向多阶段协同、低精度高效训练与自适应指导的融合方向。

## 具身AI与机器人控制

具身智能研究覆盖数据生成、策略学习与验证机制。[EmbodiedSmith](https://arxiv.org/abs/2610.07969) 通过递归自改进飞轮统一资产、场景与任务生成，支持移动操作臂、人形机器人和灵巧手，显著提升数据多样性与泛化能力。[VeriFine](https://arxiv.org/abs/2610.08761) 提出策略-课程-评估器协同进化框架，在驾驶与机器人导航任务中实现持续自我改进。[Attacca](https://arxiv.org/abs/2610.07785) 通过上下文解耦目标采样与行为阶段 conditioning，在Minecraft长时程任务上实现最高7倍性能提升。[A Safe Action Is Not Enough](https://arxiv.org/abs/2610.05166) 指出安全动作不一定是可行动作，提出VICS-G重排序器，在Safety-CHORES上将累积安全成本降低1.9%-57.5%。[SLA](https://arxiv.org/abs/2610.08244) 构建涵盖11.6万个体、79种传感器模态的统一传感器-语言-动作模型。[K-MF](https://arxiv.org/abs/2610.00864) 实现一步动作生成，使GR00T-N1.6的推理延迟降低67.5%-74.4%。[WING](https://arxiv.org/abs/2610.03607) 通过光谱域交互中心引导从第一人称视频迁移知识，在LIBERO达99.2%成功率。[Magic-W0](https://arxiv.org/abs/2609.39870) 联合建模结构化物理状态演化与连续动作，在RoboDojo-Sim取得最高平均分27.10。[Taming VLAs](https://arxiv.org/abs/2609.37334) 提出部署时自补偿方法，在两种物理机械臂上提升任务成功率超30个百分点。[DiVeR](https://arxiv.org/abs/2610.04933) 通过动作表示分散度估计决策关键性，重新加权验证器学习。分析显示，具身AI正从孤立任务测试转向长时程连续执行与物理一致性验证，执行误差补偿成为实际部署的关键。

## 视频生成与世界模型

视频生成研究关注物理一致性与效率优化。[World Models' Last Exam in Physics](https://arxiv.org/abs/2610.08791) 构建涵盖力学、光学、流体等6个物理领域的40项基准测试，发现最佳模型仅获57.76/100分，揭示视频世界模型的物理不一致性。[ALIVE](https://arxiv.org/abs/2610.08779) 通过35,800个编辑对训练VLM预测交互引导，使插入对象能与源视频内容协调交互，在ALIVE-interaction基准提升0.95分。[CtrlCache](https://arxiv.org/abs/2610.08777) 利用控制序列预测chunk状态，实现1.21-1.41倍DiT骨干加速。[S2PD](https://arxiv.org/abs/2610.06847) 在低噪声阶段切换至并行扩散，兼顾物理规则遵循与采样效率。[DuoMatching](https://arxiv.org/abs/2610.03543) 通过联合边际统一 formulation 提升视觉质量与语义对齐，人类偏好率达80%以上。[DistScene](https://arxiv.org/abs/2610.06960) 联合建模环境与对象组件，提升室内外场景的空间一致性。[Learning Discriminative Geometry](https://arxiv.org/abs/2610.04703) 通过持久表示学习改善漂移模型的判别几何，FID降低82%-95%。数据表明，视频生成研究正从视觉逼真性转向物理合理性与控制响应性的统一。

## 检索增强与记忆管理

RAG与记忆机制研究探索上下文高效利用。[UNREAL](https://arxiv.org/abs/2610.08463) 通过模型内部表征统一检索与长上下文，在21M chunk的Wikipedia索引上HotpotQA召回率从49.1%提升至73.2%，128K上下文下NoLiMa准确率从1.0%提升至24.83%。[Towards In-Parameter Memory](https://arxiv.org/abs/2610.08630) 综述参数内记忆方法，按参数放置位置（Embedding、Attention、FFN）与获取时间（在线/离线）组织分类。[AGO AI Quality Gate](https://arxiv.org/abs/2610.01218) 在工业RAG评估中引入四层决策模型，在回归场景下将不安全发布率从29.3%-41.8%降至22.2%-35.1%。[Harness-Aware Distillation](https://arxiv.org/abs/2610.02858) 针对小语言模型代理，通过对比 Harness 信息的动作偏好实现蒸馏，减少无效循环并提高错误恢复能力。[Personal-Agent Mediated Recommendation](https://arxiv.org/abs/2610.07588) 提出PAMO方法平衡平台排名与跨平台历史，在MediateRec基准上实现更好的 rescue-harm 平衡。分析表明，RAG系统正从单纯检索增强转向模型内部证据选择与跨平台个人代理协同。

## 语言模型效率优化

模型效率研究聚焦于架构创新与压缩技术。[Stepped MoE](https://arxiv.org/abs/2610.07348) 结合弹性结构与稀疏门控架构，单模型可灵活使用12-40亿参数，知识密集型基准准确率提升2-5%。[HLA](https://arxiv.org/abs/2610.05842) 引入查询依赖的chunk级注意力机制，在Qwen3.5系列上LongBench-V2最高提升5.57分，RULER从4K扩展到32K。[LSP](https://arxiv.org/abs/2609.40127) 通过可学习子空间投影实现端到端压缩，在-70%压缩率下Llama-2-7B的WikiText-2困惑度从13.3降至10.9。[Fixed Token Codes](https://arxiv.org/abs/2610.04002) 验证固定最小Token编码（1.7B参数）在HellaSwag等任务上仍可获得实质性语言能力。[Cross-Lingual Alignment](https://arxiv.org/abs/2610.01921) 通过MoE路由器输出对齐实现跨语言对比学习，提升多语言性能。[Multilinguality in Hybrid Attention](https://arxiv.org/abs/2609.35378) 发现混合注意力模型的跨语言表征在第一层全注意力处出现对齐峰值，替代层排序训练速度提升最高2.5倍。数据表明，效率优化正从单纯参数压缩转向动态路由、子空间学习与架构设计的多维协同。

## 语音与多模态交互

语音交互研究关注延迟优化与全双工对话。[Hiding Tool Latency](https://arxiv.org/abs/2610.07641) 通过投机执行预测工具调用，在Android语音助手上将中位数首次音频时间从5.79秒降至4.60秒。[HiPLEX](https://arxiv.org/abs/2610.07727) 将全双工策略分解为时序控制与条件内容生成两部分，在Full-Duplex-Bench上降低接管率并缩短中断后响应延迟。[Accent Analogy Guidance](https://arxiv.org/abs/2609.29123) 提出免训练的语音克隆方法，在OmniVoice等模型上 speaker similarity 提升0.11-0.27。分析显示，语音代理正从串行处理转向预测性执行与层次化策略分解，跨语言语音克隆通过频谱引导实现身份与口音解耦。

## 评估基准与方法

多篇研究提出新型评估基准与可解释性方法。[CheckerBench](https://arxiv.org/abs/2610.07557) 构建300个静态分析检查器合成任务，最优模型Pass@1仅45.33%，揭示可靠检查器开发仍具挑战。[CoT Interpretability](https://arxiv.org/abs/2609.38972) 提出CIA指标衡量CoT与内部计算的对齐度，发现LLMs在44.8%-75.9%范围内存在有限对齐。[Source Identification](https://arxiv.org/abs/2610.00417) 证明源识别（98.7%准确率）与训练数据选择是分离问题，改写后归因准确率降至29.0%。[WildMatch](https://arxiv.org/abs/2610.07384) 提出弱监督图像匹配器适应方法，在野生动物重识别中优于现成匹配器。[Selection-Based Structured Reasoning](https://arxiv.org/abs/2610.01892) 将推理重构为选择任务，使2B/4B模型每步推理延迟降低超90%。[EVISKILL](https://arxiv.org/abs/2610.05030) 通过可重放证据卡组织执行观察，在三个交互式基准上验证有效性。[AutoSciBench](https://arxiv.org/abs/2610.05140) 构建自动化科学代理基准生成框架，在计算生物学与材料科学中将求解器准确率降低22.4和25.5个百分点。数据表明，评估研究正从静态准确率测量转向动态证据追踪、自适应基准与可解释性验证。