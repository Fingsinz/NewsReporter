

# 每日HFDailyPapers-2026年08月13日

## Agent系统与安全评估

本周安全研究方向呈现系统化趋势，多项工作聚焦LLM Agent在开放环境中的鲁棒性。ToolHazard提出可扩展的对立环境合成框架，通过环境模拟器、攻击者Agent和用户模拟器自动生成状态化环境、注入点和载荷，构建了ToolHazard-Bench用于压力测试，实验发现注入时机和位置显著影响攻击效果，且合成对齐数据可在保持良性任务效用前提下提升Agent安全性 [ToolHazard](https://arxiv.org/abs/2608.11878)；OpenART则提供超过10,000个验证过的状态化场景和50万工具池，通过进化式马尔可夫超图攻击（EMHA）实现黑盒反馈驱动的环境演化，在75种Agent配置上达到85%的综合攻击成功率，并指出运行时实现是安全差异的重要解释因素 [OpenART](https://arxiv.org/abs/2608.00677)。在理论层面，一项工作明确提出Agent安全应被视为"运行时契约"而非训练时属性，主张通过沙箱、权限门控、轨迹监控等预防性机制与测试运行、日志捕获、文件差异等证据性机制相结合来保障安全，并揭示了2023-2025年顶会论文中训练时安全研究与部署时安全研究存在8-12倍的数量失衡 [Agent Safety Should Be a Runtime Contract](https://arxiv.org/abs/2608.11274)。此外，对视觉工具使用的因果审计揭示了"视觉工具使用幻觉"现象：多模态模型在使用裁剪-缩放等操作时，大量返回的视觉证据对答案无因果影响，表现为"不观察就调用"和"有信息但无规划"两种失败模式 [The Illusion of Visual Tool-Use](https://arxiv.org/abs/2608.06270)。

## 研究自动化与自主演化

AI辅助科学研究正在从单一任务向端到端工作流演进。Spark-to-Paper在编程助手内实现了由13个可组合技能构成的端到端研究论文生成系统，通过分离模型判断与确定性操作、实验规划与报告、结合确定性完整性检查与自我批判机制，在8个受控研究主题上实现99.5%的引用有效性和96.4%的图形可编辑性，单次生成成本仅8.1美元 [Spark-to-Paper](https://arxiv.org/abs/2608.11924)。Mechanist则专注于机制发现自动化，构建了包含约13,000篇可解释性论文和4,300万篇多学科论文的知识图谱，以及32种机制分析方法库，实现了从发现模型行为到解释和控制AI模型的演进，包括跨模态不安全特征转移的安全风险发现和信念机制理论的开发 [Mechanist](https://arxiv.org/abs/2608.12036)。在软件演化方面，Genesis提出以持久递归世界组织长期软件开发，而非依赖持久Agent，使用DeepSeek V4 Flash在超过120小时内构建出通过完整c-testsuite的Rust C编译器，耗资仅44美元，并实现了13个MESA模块从Fortran到Rust的重实现 [Persistent Recursive Worlds](https://arxiv.org/abs/2608.10450)。AutoWorldModel-Bench为世界模型研究提供了闭环基准，让前沿编码Agent在固定计算预算下自主改进世界模型初始代码，实验显示Codex-5.4和Claude Opus 4.6在91%的会话中产生了非平凡的研究式修改 [AutoWorldModel-Bench](https://arxiv.org/abs/2608.11216)。

## 视觉表示与视频生成

视频理解与生成领域在表示学习和状态建模方面取得进展。AVA-Encoder提出代理原生视频表示学习框架，将视频转换为知识图谱表示，通过分层状态节点存储结构化文本，链接资产层保存生成图像、音频和视频，并引入文本梯度优化框架，在策略设置下比人工调优策略减少74.3%的系统提示token [AVA-Encoder](https://arxiv.org/abs/2608.12313)。StateFlow针对预可视化场景提出以状态为中心的方法，将世界表示为持久的结构化3D状态而非一次性视频生成，通过状态构建、演化和访问三阶段支持场景编辑和迭代改进 [StateFlow](https://arxiv.org/abs/2608.12314)。视频去反射方面，S2R框架统一了物理 grounding 的反射模拟、基于扩散的视频去反射和基准评估，通过S2R-Synthesis流水线生成配对反射/无反射视频数据，提出了首个扩散基视频去反射模型S2R-Removal，实现单步去噪恢复 [From Synthesis to Removal](https://arxiv.org/abs/2608.11562)。

## 具身智能与机器人

具身Agent的长期任务和感知遗忘问题得到关注。SHAPER提出免训练的自演化框架，通过进化可重用技能和上下文代码 harness 而非更新模型参数来实现具身适应，在VLABench和ESI-Bench上验证了该方法在模型训练昂贵或不可用场景下的实用性 [Self-Evolving Embodied Agents](https://arxiv.org/abs/2608.11350)。AtlasVLA则针对部分可观测和长horizon任务中的感知遗忘问题，提出持久的世界-自我状态建模框架，通过4D持久世界状态记忆和ego工作记忆的组合，仅使用腕部摄像头即在LIBERO-Long上获得9.4%的绝对成功率提升，在多视角基线中实现显著超越 [AtlasVLA](https://arxiv.org/abs/2608.06729)。

## 模型训练与优化方法

扩散模型和训练策略方面出现多项创新。Simplax为离散扩散模型引入精确的Dirichlet-categorical增强，通过耦合辅助单纯形变量保留原始均匀扩散过程，在OpenWebText无条件生成和Sudoku任务上改善了生成质量-熵权衡 [Simplex Relaxation for Discrete Diffusion](https://arxiv.org/abs/2608.10615)。NeuPAT从神经元可塑性异质性视角解决多模态扩展中的语言能力退化问题，通过小规模探测阶段估计神经元适应模式，选择性保护语言敏感神经元，在11个语言基准上恢复94.5%的能力退化 [NeuPAT](https://arxiv.org/abs/2608.08107)。Self-Geometry针对视觉基础模型的多视图几何不一致问题，提出即插即用的测试时自适应流水线，通过显式多视图几何约束直接施加2D像素对应伪标签，在6个VFM和4个基准上实现姿态和几何估计的一致改进 [Self-Geometry](https://arxiv.org/abs/2608.10708)。在强化学习探索方面，3PO方法探索参数空间而非动作空间的探索策略，通过采样不同策略生成rollout，在数学推理和代码生成任务上相比标准GRPO保持一致成本下的性能提升 [Parameter Exploration for RLVR](https://arxiv.org/abs/2608.09805)。

## Agent效率与能力迁移

Agent系统的可扩展性和效率优化受到重视。SkillZip提出执行感知的过程抽象框架，在节级图上进行契约保持压缩，将重复动机重写为可逆端口宏，在200至100K技能规模的库上实现3.46倍压缩率和98.7%的验证器可达性 [SkillZip](https://arxiv.org/abs/2608.05604)。AI4AI at Test-Time研究了测试时强到弱能力迁移，使用5%数据作为验证集迭代精炼harness，将目标模型性能从0.49提升至0.91，表明将不稳定推理卸载到确定性代码和严格格式执行是 gains 的主要来源 [AI4AI at Test-Time](https://arxiv.org/abs/2608.12307)。Ready Cohorts从系统角度形式化了LLM Agent控制的GPU执行边界，通过精确打包恢复81.83%的机会损失，并证明设备驻留GPU决策路径在所有36种配置下均更快 [Ready Cohorts](https://arxiv.org/abs/2608.12123)。Poor Man's Agentic Modeling则通过低参数模型拟合替代LLM Agent进行大规模社会模拟，在EconAgent等8个模拟中验证了误差趋势预测的有效性 [Poor Man's Agentic Modeling](https://arxiv.org/abs/2608.11215)。

## 基准与评估数据集

多领域基准的构建推动了评测标准化。MBA-Bench提出首个多模态商业创意基准，包含30K样本跨越6个领域，通过GPT-4o生成参考创意并结合LoRA微调与组相对策略优化，在盲注和已知准则设置下分别超越多模态基线25.6%和35.8% [MBA](https://arxiv.org/abs/2608.11616)。NCP-Bench针对交互式叙事的长期一致性挑战，构建100个电影情节衍生环境，发现即使最强模型GPT-5.2在20轮后存活率仅42%，事实冲突率40-68% [Can LLM Agents Stick to the Script?](https://arxiv.org/abs/2608.08160)。Hand Visibility Detector首次系统研究逐关键点手部可见性估计作为独立任务，利用大规模预训练HPE模型骨干网络获得高性能，并在多视角三角测量3D手部姿态标注中验证了有效性，代码已开源 [Hand Visibility Detector](https://arxiv.org/abs/2608.11574)。