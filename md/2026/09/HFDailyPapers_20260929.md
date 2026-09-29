

# 每日HFDailyPapers-2026年09月29日

## 多教师蒸馏与在线策略优化

多篇研究聚焦于多教师蒸馏（MOPD）与在线策略自蒸馏（OPSD）的技术改进。[Beyond Teacher Assignment](https://arxiv.org/abs/2609.35347) 指出标准MOPD中反馈不平衡问题：指令遵循反馈比数学反馈分散程度更高，导致学生模型难以获得数学专家的优势。研究者提出域归一化MOPD（DN-MOPD），通过重缩放各域反馈分布改善性能，在六项公开基准上平均得分提升。[An RL View of OPD](https://arxiv.org/abs/2609.35505) 从强化学习视角分析OPD，提出最小二乘策略蒸馏（LSPD），引入乐观探索与离线数据复用机制，在数学推理基准上平均提升1.59分。[Decision-Aligned On-Policy Distillation](https://arxiv.org/abs/2609.33391) 识别决策-时间戳不匹配问题，提出AlignOPSD框架，在ALFWorld和WebShop上较GRPO提升5.5-8.7%。

分析表明，蒸馏领域正从单一"谁教学"转向"教学强度"的精细化控制，域归一化与决策对齐是提升多教师融合效果的关键方向。在线策略蒸馏与强化学习的理论融合（LSPD与OPD的KL正则化联系）为样本效率提升提供了新路径。

## 多模态视觉语言模型架构与效率

[Encoder-Free MLLMs](https://arxiv.org/abs/2609.35457) 系统比较有无视觉编码器的多模态模型缩放规律，发现去除编码器将计算最优分配转向更大模型，且在约10²² FLOPs处可追赶有编码器架构。[Just MLPs](https://arxiv.org/abs/2609.34972) 提出δ-Vision，用轻量级低秩适配器替代视觉标记的重复Transformer演化，在图像与视频基准上实现更高精度同时保留全部视觉标记。[SpatialSpeak](https://arxiv.org/abs/2609.33616) 通过QA原生重建预训练连接局部几何与全局场景上下文，在ReVSI上达62.8分，超越最强基线8.7分。[AnswerMap](https://arxiv.org/abs/2609.35247) 构建黑盒可解释方法，通过输出头生成空间解释图，定位准确率达AUC 0.85。[SCOPD](https://arxiv.org/abs/2609.34044) 针对视觉Token剪枝后的表示-利用差距，提出稀疏上下文在线策略自蒸馏，10%视觉Token保留率下性能恢复至92.43%。

分析表明，视觉编码器正在从多模态模型的必要组件转向可选模块，缩放定律显示其优势随计算规模增长而递减。视觉Token效率优化从剪枝转向保留与利用并重，蒸馏与适配器技术成为关键手段。

## 推理增强与测试时计算

[Knowing When Thinking Is Not Enough](https://arxiv.org/abs/2609.34327) 揭示小推理模型（sRMs）的自我精炼主要巩固现有概率质量而非创造新解，区分执行瓶颈与知识瓶颈，提出FlyBy框架在知识瓶颈时查询更强模型，FlyBy-4B以2.7倍更低成本超越Qwen3-14B。[Improving Test-Time Scaling](https://arxiv.org/abs/2609.35748) 提出TaH2，通过前瞻深度监督实现自适应迭代，在AIME基准上精度-计算斜率提升53%。[Why Deterministic PRM Guidance Underperforms](https://arxiv.org/abs/2609.35472) 证明离散扩散语言模型中确定性PRM引导弱于独立采样加ORM重排序，指出PRM在早期去噪阶段信号衰减严重。[Diffusion Reward Models](https://arxiv.org/abs/2609.33803) 将奖励建模重构为条件密度估计，保留奖励分布的多模态结构，下游RLHF实验验证其实际收益。

分析表明，测试时计算扩展正从"更多思考"转向"更智能的思考"，区分瓶颈类型与自适应迭代深度成为提升推理效率的关键。PRM引导的有效性受限于去噪阶段信号质量，混合策略（独立采样+ORM重排）优于单一确定性引导。

## 长上下文与高效推理

[MassAlloc Attention](https://arxiv.org/abs/2609.32712) 提出MALA，按归一化注意力贡献分配后续计算，在128K token基准上训练前向延迟降低2.2倍。[CoWindow Attention](https://arxiv.org/abs/2609.32704) 证明全因果覆盖可为头集合的集体属性，通过互补长程窗口实现稀疏注意力，128K token下训练延迟降低7.4倍。[DepthBench](https://arxiv.org/abs/2609.32534) 系统评估残差连接设计对计算深度的贡献，发现HC和Full AttnRes在极深架构下持续提升性能。[WaveFront Decoding](https://arxiv.org/abs/2609.23033) 提出环形语言模型的波前解码框架，Huginn-3.5B上实现3.54倍加速。[TokenCast](https://arxiv.org/abs/2609.35760) 学习可组合成本表示预测Agent执行token消耗，平均预测误差降低14.5%。[KVCMAS](https://arxiv.org/abs/2609.34060) 和[PReCache](https://arxiv.org/abs/2609.34054) 分别针对多Agent系统提出低秩KV缓存修正与共享框架，前者TTFT加速2.0倍，后者峰值内存降低3.7倍。

分析表明，长上下文推理的效率优化正从架构创新（稀疏注意力、环形解码）转向计算分配优化（MALA的贡献感知、CoWA的集合覆盖）。多Agent场景下的缓存共享已成为独立研究方向，低秩近似是实现高效修正的核心技术。

## 多智能体与具身智能

[Self-Evolving Coding Agents](https://arxiv.org/abs/2609.35432) 提出Physical Coding框架，将任务状态与执行表示为代码，HexaAnything在RoboCasa365上超越XR-1 VLA，并实现数据、模型、工具自进化。[Recursive Harness Distillation](https://arxiv.org/abs/2609.33378) 通过递归蒸馏将强Agent经验转化为可复用指导，真实操作成功率从37.3%提升至64.0%。[CompoWorld](https://arxiv.org/abs/2609.33665) 通过组合服务库扩展任务空间，Qwen3.6-35B-A3B在八个基准上平均提升9.17分。[WideSWE](https://arxiv.org/abs/2609.33382) 评估跨仓库代码Agent，发现独立执行难以纠正已尝试但未成功的实现，联合执行可利用相关仓库信息。[RoboFoundry](https://arxiv.org/abs/2609.32862) 提出系统即策略进化框架，在EmbodiedBench上GPT-5.5提升27.8%。[Rolling-WAM](https://arxiv.org/abs/2609.30247) 将联合去噪分布到连续重规划周期，实现4.5倍稳态加速。

分析表明，多智能体正从单次任务执行转向跨任务经验积累与系统级进化。具身智能的关键突破在于将执行轨迹转化为可复用代码/协议，而非仅优化单一策略。跨仓库协调与长程规划仍是当前Agent的主要瓶颈。

## 检索增强与文档处理

[RenderRank](https://arxiv.org/abs/2609.35069) 证明压缩视觉文档表示可支持准确的相关性评分，16.5-35.5%更少输入Token下NDCG@10达55.96，吞吐量提升1.7倍。[ColNanoVDR](https://arxiv.org/abs/2609.34899) 将无文档蒸馏扩展至多向量视觉检索，149M参数学生保留教师95% NDCG@5且查询编码速度提升26倍。[AdaTutoRank](https://arxiv.org/abs/2609.32472) 提出自适应辅导优化，按 rollout 质量动态选择提示形式，在十个基准上实现最佳整体性能。[SolveEdiT](https://arxiv.org/abs/2609.35504) 构建视觉问题解决基准，指出当前最强模型仅达57%得分，提出两阶段规划器提升9.1分。

分析表明，文档检索正从纯文本转向视觉压缩表示，Token效率与评分精度可同时提升。多向量检索的蒸馏瓶颈通过最优传输对齐得到突破，无文档训练避免了TB级页面Token缓存。

## 安全、对齐与可解释性

[Imprint Reader](https://arxiv.org/abs/2609.35261) 训练模型描述冻结权重更新，通过MetaEdit干预提升有害提示拒绝率（57.9%→64.1%）与数学推理回溯频率。[When Do Model Internals Help?](https://arxiv.org/abs/2609.34771) 比较表征工程与行为对齐方法，发现DPO提供最强整体控制，表征探测在低数据场景更具竞争力。[AdaGuard](https://arxiv.org/abs/2609.34241) 提出自适应守卫模型，支持推理时用户提供策略，4B模型在AdaptiveSafety达89.3%准确率。[Distillation Defenses Break After RL](https://arxiv.org/abs/2609.35699) 揭示蒸馏防御在后续强化学习后易被突破，简单攻击即可窃取推理能力。[Safe Error Correction](https://arxiv.org/abs/2609.16145) 验证冻结基座+逻辑层修正可保留53.3%错误修正同时不降级能力。[How Reproducible Are Evaluation Conclusions?](https://arxiv.org/abs/2609.30074) 自我审计显示LLM推断提示结构排名的顶部两个模型仅68%稳定性，结论可靠性受限。

分析表明，模型安全正从静态防御转向动态适应（AdaGuard的运行时策略），但蒸馏防御的RL脆弱性揭示了评估威胁模型的局限性。可解释性研究从文本解释转向权重更新描述，为模型自我反思提供新路径。

## 生成模型与视觉合成

[WorldPlay2](https://arxiv.org/abs/2609.35560) 提出因子化混合控制接口与稳定蒸馏，实现实时交互式世界模型。[EditWorld](https://arxiv.org/abs/2609.34470) 支持流式编辑指令与参考图像，WBench-Editing得分73.8。[Structural Residual Connectivity](https://arxiv.org/abs/2609.33203) 重新设计DiT残差连接为主动检索机制，REPA-XL/2模型FID从5.9降至4.34。[VGGT-Diff](https://arxiv.org/abs/2609.33253) 通过视觉几何路由器将3D点关联引入视频扩散模型。[YuE2](https://arxiv.org/abs/2609.33757) 统一符号与音频音乐生成，专家偏好率49.3%，WildSongBench得分6.73。[In-Flight KV Cache](https://arxiv.org/abs/2609.32540) 复用飞行中KV缓存加速自回归视频扩散，20秒视频生成速度提升1.42-2.92倍。

分析表明，世界模型正从导航扩展至精确编辑，控制接口与内存压缩是关键技术创新。视觉生成架构通过结构化残差连接与几何路由实现质量突破，音乐生成通过符号规划统一了两个原本分离的范式。

## 语音、音频与多模态任务

[InfiniHand](https://arxiv.org/abs/2609.35743) 提出端到端流式框架联合估计手部几何与相机轨迹，ARCTIC PA-p降低21.4%且达11.19 FPS。[Pruned CTC](https://arxiv.org/abs/2609.33645) 将CTC训练限制于目标Token子集，180K词汇下内存降低5.1倍。[Rethinking Voice Similarity](https://arxiv.org/abs/2609.33999) 揭示感知对齐由嵌入几何而非EER决定，维度瓶颈可提升对齐度从0.08至0.74。[REALM](https://arxiv.org/abs/2609.33095) 提出粗到细的响应式听模型，在ViCo和L2L基准上提升多项运动质量指标。[Duplex-MPE](https://arxiv.org/abs/2609.31948) 构建全双工对话基准，评估助手在多人对话中的响应时机决策。

分析表明，语音与音频任务正从独立模块转向联合估计（手部+相机、音频+动作），CTC训练的效率突破为LLM原生词汇ASR奠定基础。语音相似性评估从准确率指标转向嵌入几何分析，揭示模型训练目标对感知对齐的决定性影响。

## 其他动态

[Hard Vision, Easy Vision](https://arxiv.org/abs/2609.35718) 评估GPT-6 Astra在34项能力、55个基准的表现，发现语义推理与结构化预测已接近专用模型，但度量几何精度、时序一致密集预测仍存在较大差距。[How Does "English (US)" Become the Default?](https://arxiv.org/abs/2604.04204) 系统审计AmE偏好，发现其在所有预训练语料与 tokenizer 中占主导，British English提示仅部分改变偏好。[Who Gets a Token, and What Does It Carry?](https://arxiv.org/abs/2609.34065) 揭示不同姓名在词汇层获得的不平等支持 persisted 至任务相关内部表示，NameTrace框架测量概念可访问性差异。[Post-Training Leaves Behavioral Shadows](https://arxiv.org/abs/2609.29233) 发现仅用教师单个词即可实现能力迁移，5,664样本在HumanEval+提升5.34个百分点。[NanoForecast v0.5](https://arxiv.org/abs/2609.31669) 通过训练管道优化使6.5M参数模型在时间序列预测上超越200M参数TimesFM。[Playing to Par](https://arxiv.org/abs/2609.32146) 训练RL智能体构建四边形网格分解，在96个测试域中90%达证明最优。[Not All Objectives Are Born Equal](https://arxiv.org/abs/2606.29521) 提出优先级约束下降（PCD）处理层次化多目标优化。[Routing Drift Alone Does Not Diagnose Failure](https://arxiv.org/abs/2609.32821) 证明MoE合并后的路由漂移不足以诊断路由失败，需通过任务干预验证。[Residual Transferability in Neural Image Watermarking](https://arxiv.org/abs/2609.32241) 揭示架构设计决定水印残差可移植性，提出CoverLock即插即用增强方案。[EvolvingAvatar](https://arxiv.org/abs/2609.35616) 通过测试时训练适应对话模式，最困难分布减少11.1%表达失配。[GeoVerse](https://arxiv.org/abs/2609.35734) 在几何潜空间中合成世界一致新视角，DL3DV上PSNR提升2.23dB。[FactorEngram](https://arxiv.org/abs/2609.35578) 提出因子化n-gram记忆，相关模式可复用公共成分。[SentZero](https://arxiv.org/abs/2609.34479) 增强句子级VL预训练用于零样本胸部X光分析。[FlowTool](https://arxiv.org/abs/2609.35673) 将工具参数建模为流匹配问题，推理延迟降低50倍。[Program-Verified Self-Evolution](https://arxiv.org/abs/2609.33855) 通过程序验证替代多数投票实现自进化，人类评估正确率达94%。[TT-VidT](https://arxiv.org/abs/2609.33419) 解耦时间轴进行运动中心视频预训练，编码器FLOPs降低48-55%。[DroneWAM](https://arxiv.org/abs/2609.33148) 提出无人机世界动作模型，自适应 rollout 将预测深度从8降至4.58。[Controlling LLM Post-Training](https://arxiv.org/abs/2609.34645) 提出成本感知运行时Nereus，8B PPO吞吐量提升2.14-7.27倍。[BaRe-Mem](https://arxiv.org/abs/2609.35551) 贝叶斯可靠记忆提升多Agent咨询鲁棒性。[G^2PTQ](https://arxiv.org/abs/2609.31009) 统一一阶与二阶信息实现全局监督PTQ。[Groupwise Agentic Grading](https://arxiv.org/abs/2609.32577) 通过群体级Agent评分改进代码Agent RL。[Adaptive Consistency Graph](https://arxiv.org/abs/2609.32754) 为长程Agent提供结构化上下文视图，GPT-5.6-luna平均成功率从44.5%提升至50.2%。[Limitations of On-Policy Self-Distillation](https://arxiv.org/abs/2609.32353) 极端视觉Token缩减下LT-OPD在5%预算下性能恢复至82.3%。[RL View of OPD](https://arxiv.org/abs/2609.35505) 理论分析LSPD达到O(log K) regret界。[Surprising Success, Repeated Failure](https://arxiv.org/abs/2609.33781) 熵引导信用分配强化意外成功、纠正重复失败。[Learning to Learn from Context](https://arxiv.org/abs/2609.33642) 扰动公开文档生成10K样本，Qwen3.6-35B-A3B在CL-bench达24.6%。[Skill2Env](https://arxiv.org/abs/2609.33772) 从技能合成可执行环境，1.5K轨迹支持SFT训练。[QCQ-DRE](https://arxiv.org/abs/2609.32400) 双阶段红队进化框架，平均攻击成功率45.28%。[TraceDance](https://arxiv.org/abs/2609.33295) 从部署轨迹构建行为基准，95.3%构建目标满足率。[MM-Reflection](https://arxiv.org/abs/2609.35767) 统一模型反射轨迹RL，BAGEL上GenEval提升12.05分。[KernelZero](https://arxiv.org/abs/2609.33074) 共同进化Proposer与Coder，CUDA pass@1达75.8%。[VisionHOPE](https://arxiv.org/abs/2609.33325) 自修改学习系统视觉主干，在ImageNet/COCO/ADE20K达竞争力结果。[What Masking Geometry Works Best](https://arxiv.org/abs/2609.33487) 系统评估58个EEG模型，识别JEPA特有失败模式。[When Privacy Moves ML](https://arxiv.org/abs/2609.33312) 分析隐私保护拍卖信息错位，50 tick后超支1,669%。[Reinforcing Agentic Creativity](https://arxiv.org/abs/2609.35706) Night Science框架扩展研究路径27.8%、原创性提升66.2分。[EmbdodiedMemory-Bench](https://arxiv.org/abs/2609.28236) 评估2,554交互 episode，EMem-8B表现最佳。[PLDR-LLMs Dynamics](https://arxiv.org/abs/2609.34130) 统一训练与推理动力学分析。[On-Policy Self-Distillation for Image Editing](https://arxiv.org/abs/2609.35611) MT-OPSD改善多轮编辑长期鲁棒性。