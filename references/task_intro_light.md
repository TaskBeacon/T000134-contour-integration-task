# Gabor 轮廓整合任务：知觉组织原理、神经过程与测量边界

视觉系统必须把空间上分离的局部边缘组合为连续物体边界，同时抑制来自纹理、遮挡与背景杂波的竞争信息。轮廓整合任务（Contour Integration Task）以方向可控的 Gabor 微图元构造目标路径，并将其嵌入随机取向的图元场，因此能够在不依赖物体语义的条件下量化“良好连续”原则及局部—整体知觉组织。该范式的主要方法学价值在于：局部刺激能量、图元数量与总体空间范围可以受到控制，而相邻图元的取向关系、间距、曲率和背景密度可分别操控；由此获得的正确率、敏感性和阈值反映观察者从杂波中提取跨位置方向相关性的能力（Field et al., 1993; Hess & Field, 1999）。这种可控性也使其成为连接心理物理学、认知神经科学与临床视觉研究的常用范式，但其结果不能脱离视力、空间频率、偏心度和具体任务版本解释。

## 1. 范式提出与理论背景

Field、Hayes 与 Hess（1993）提出经典 Gabor 路径检测程序，试图把格式塔心理学的“良好连续”原则转化为可参数化的空间规则。目标由一系列沿锯齿状路径排列、载波方向近似与路径切线一致的 Gabor 图元构成，背景图元的位置或方向不支持连续路径。观察者在时间二选一迫选中判断哪一幅阵列包含目标。即使相邻目标图元间距超过单个图元尺度，观察者仍可检测路径；随着相邻路径段的方向差增大、图元相对路径切线发生错位或图元由端对端排列改为侧向排列，检测表现下降。作者据此提出“关联场”（association field）：取向相近且空间关系满足共线或共圆约束的局部滤波器输出更易被联合（Field et al., 1993）。

关联场不是单一脑区或固定半径的同义词。后续研究表明，轮廓整合同时受图元间距、空间频率、视野位置和注意状态影响。外周视野的表现下降不能完全由位置不确定性解释，提示有效连接范围随偏心度与刺激尺度变化（Hess & Dakin, 1999）。以相同刺激网格比较掩蔽、拥挤与分组时，三类空间相互作用呈现不同的间距函数，说明轮廓分组不能简化为一般性的邻近刺激相互作用（Reuther et al., 2022）。近期对旁中央与近外周视野的研究进一步表明，关联场的空间范围和方向噪声耐受性具有明显视野位置依赖性（Reuther et al., 2025）。因此，范式所测构念较准确的表述是：在给定视觉尺度、偏心度与任务要求下，利用跨位置取向连续性进行知觉分组和目标—背景分离的能力。

## 2. 任务逻辑、流程与核心指标

经典试次由两个先后呈现的 Gabor 阵列组成，其中一个包含连续路径，另一个是不支持路径的随机阵列；呈现顺序随机化，观察者报告目标所在时间间隔。时间二选一迫选使单次反应的机会水平为 50%，并避免把“是否看见”与肯定反应偏向直接混合。严格匹配信号与空白阵列的图元位置、取向分布、对比度和总数，可降低局部密度、单一方向比例或总体能量成为替代线索的可能。弯折角或相邻段方向差越大，沿路径的连续性通常越弱；取向抖动则直接破坏图元载波与局部路径方向的一致性。两种操作均会降低显著性，但并非完全等价：前者改变路径几何，后者改变局部方向证据。

不同研究围绕同一逻辑发展出若干程序。固定刺激法在多个曲率或抖动水平估计正确率或信号检测敏感性；阶梯法通过改变背景图元密度、取向抖动、路径图元数或间距估计阈值；空间二选一版本要求报告轮廓的位置或朝向；短时呈现、动态揭示和被动观看版本分别用于限制搜索、研究时间整合或采集神经信号。主要因变量包括全体试次正确率、排除遗漏后的有效正确率、反应时、心理测量函数斜率与达到预定正确率的阈值。若只有目标存在与否两类单幅刺激，应同时估计敏感性与判断标准；若采用迫选，正确率仍会受遗漏处理和天花板/地板效应影响。

任务阶段对应的心理过程需要分别界定。阵列呈现早期包含局部取向与空间频率编码；连续路径相对于匹配随机阵列的差异涉及跨位置整合、目标—背景分离及注意选择；报告阶段还包括间隔记忆、决策与反应映射。曲率条件的正确率差异支持连续性对知觉分组的约束，却不能单独确定整合发生在早期水平连接、反馈回路或更高层级的前馈汇聚。反应时若从报告提示开始计时，主要反映提示后的决策与动作时间，不能作为刺激出现后整合潜伏期的直接指标。

## 3. 主要行为与神经科学证据

### 3.1 行为规律与计算解释

跨研究较稳定的行为规律是：相邻图元越接近共线或平滑共圆关系、间距越小且方向抖动越低，轮廓越易从随机背景中分离（Field et al., 1993; Hess & Field, 1999）。该规律支持自然图像边缘统计可被视觉系统利用，但不要求唯一的神经算法。Doshi 等（2025）使用与经典时间二选一相近的 12 图元路径、256 图元阵列和多级全局曲率发现，人类表现随曲率增加而下降；经过任务微调、具有逐层扩大感受野的纯前馈卷积网络也能形成相似曲率敏感性。该结果提供了前馈层级可以实现整合的计算存在性证明，不等于人类通过相同训练过程形成该能力，也不排除水平连接与反馈在生物视觉中的作用。

刺激尺度是行为解释中的关键调节因素。Reuther 等（2022）发现，分组任务的对比阈值与空间作用范围不同于掩蔽和拥挤。对达到常规 20/20 视力的观察者进一步矫正屈光误差，仍可改善高空间频率条件的轮廓整合表现（Keane et al., 2024）。因此，患者组、儿童组与对照组的差异可能同时包含图元可见性和整体分组差异；仅匹配常规视力等级不足以排除这一混杂。

### 3.2 fMRI、EEG 与因果干预证据

功能磁共振成像（functional magnetic resonance imaging, fMRI）表明，连续 Gabor 轮廓相对于随机取向阵列可增强早期视网膜拓扑区和外侧枕叶复合体（lateral occipital complex, LOC）的血氧水平依赖信号；破坏图元对齐会同时降低检测表现与相关活动，而通过双眼视差恢复分组可使两者回升（Altmann et al., 2003）。快速事件相关 fMRI 适应研究进一步区分了时空尺度：早期视觉区对局部结构的加工较短暂且受邻域限制，较高级枕颞区对整体形状的表征较持续，注意整体或局部特征会改变这种分工（Kourtzi & Huberle, 2005）。这些结果说明多个视觉阶段参与连续轮廓形成，单凭 BOLD 差异不能确定信息流方向或必要性。

事件相关电位（event-related potential, ERP）为时间进程提供补充。可检测轮廓相对于随机背景在刺激后约 150 ms 起引发后部负向增强；轮廓较难时该效应延迟，较晚的 P3 还随对齐程度变化，提示早期知觉选择与后续任务评价均影响头皮信号（Mathes et al., 2006）。同步 EEG–fMRI 研究在局部对齐不完美但整体形状存在的条件中识别出约 300 ms 的成分，并将其与 LOC 和早期视觉区之间的相互作用联系起来（Mijović et al., 2014）。fMRI 定位与 EEG 时程的联合结果支持递归加工假说，但源定位和联合分解仍是间接证据。fMRI 引导的经颅磁刺激研究显示，在不同刺激后时间窗干扰 V1/V2 与 V3B 会选择性损害轮廓检测，为较高级视觉区与早期视觉区之间的递归参与提供了因果支持（Li et al., 2019）。

## 4. 范式发展与主要应用

轮廓整合已用于研究弱视、精神分裂症谱系、视觉发展、个体差异和知觉学习。早期弱视研究提示异常眼的路径检测受损，部分差异可由位置不确定性解释；使用闭合轮廓、控制可见性与形状辨别后仍可观察到残余整合缺陷（Hess et al., 1997; Levi et al., 2007）。近期研究在接受治疗的屈光参差性弱视儿童中发现，高空间频率条件的整体轮廓加工仍受损（Jiang et al., 2023）；动态狭缝揭示程序又显示时间轮廓整合缺陷可与空间整合指标相对独立（Chen et al., 2025）。这些结果要求分别测量视力、对比敏感度、位置不确定性、空间整合与时间整合，不能以单一正确率推断统一的“整体加工障碍”。

精神分裂症研究常以取向抖动阈值或闭合轮廓定位测量知觉组织。长期证据支持患者群体平均表现下降，但效应随轮廓形状、复杂度、病程与刺激尺度变化。训练数据的再分析表明，精神分裂症组在取向抖动和所需路径图元数阈值上均劣于对照组，复杂曲线的组间差异更明显（Jayakumar et al., 2024）。采用 7 T fMRI 的跨诊断研究发现，精神病性障碍参与者的轮廓辨别受损，并伴随 LOC 反应及视觉区任务连接异常；一级亲属未呈现相同程度的行为损害（Kamath et al., 2026）。这些群体结果提示轮廓整合与精神病理及认知功能相关，尚不足以把任务作为个体诊断或病因定位工具。

大样本研究还显示，同一轮廓任务多个测量轮次之间具有较高相关，并观察到中等程度的常见单核苷酸多态性遗传度估计；单标记发现未在独立样本中稳定复制（Zhu et al., 2019）。因此，范式适合研究个体差异，但遗传关联、临床关联与具体视觉机制之间仍需独立验证。

## 5. 测量效度与解释边界

轮廓卡阶梯测验在儿童、成人及弱视样本中表现出较小的观察者差异和练习效应，重复测量误差约为一个卡片等级（Kovács et al., 1999）；大样本固定任务的三个轮次相关为 .78–.84（Zhu et al., 2019）。这些结果说明某些标准化版本具有可接受的重复性，不能直接外推到刺激数量、时序、难度范围和计分规则不同的新实现。固定项目正确率还可能因天花板、项目取样有限和熟悉效应降低个体排序信度。计划用于纵向或临床研究时，应在目标人群中估计内部一致性、重测信度、心理测量函数覆盖范围及最小可检测变化。

构念效度依赖严格的替代线索控制。信号与空白阵列应匹配图元位置、密度、对比度、总体取向分布和局部可见性；眼动、偏心度、呈现时长、屈光状态与空间频率也会改变表现。闭合性、熟悉形状和反复训练可引入更高层级预测，导致不同版本测量的过程比例不同。神经影像中的轮廓—随机差异同时包含知觉组织、显著性、注意和难度；等化行为难度、设置局部结构与整体结构对照、结合时程或扰动证据，才能缩小解释范围。群体均值差异不保证单个受试者分类准确，稳定相关也不构成因果机制证明。

## 6. TaskBeacon 中的任务实现

### 6.1 任务资源与访问入口

| 资源 | ID | 用途 | 地址 |
|---|---|---|---|
| PsychoPy 完整实验实现 | T000134 | 本地行为实验、完整参数与数据记录 | [GitHub 源码](https://github.com/TaskBeacon/T000134-contour-integration-task) |
| 浏览器行为实现 | H000134 | 与完整计划配对的网页预览源码 | [GitHub 源码](https://github.com/TaskBeacon/H000134-contour-integration-task) |
| 公共运行入口 | H000134 | 在线体验 100 试次行为流程 | [TaskBeacon Runner](https://taskbeacon.github.io/psyflow-web/?task=H000134-contour-integration-task) |

T000134 是以 PsychoPy/PsyFlow 运行的行为实验实现；H000134 保留 100 试次计划与名义时序，用于浏览器行为预览。网页呈现依赖设备、浏览器与 CSS 像素，不能视为经过物理标定的实验显示，也不替代对本地呈现时序和视觉角的验证。

### 6.2 实现流程与关键参数

TaskBeacon 当前版本采用 2 个区组、每区组 50 试次，共呈现 100 对互不重复的信号—空白材料。每种弯折条件（15°、30°、45°、60°、75°）含 20 对材料，目标在第一、第二间隔内按弯折条件平衡后随机排序。每幅 512 × 512 像素灰度阵列包含 16 × 16 个 Gabor 图元，其中信号阵列含 12 个有序路径图元；配对空白阵列保持图元位置和总体取向多重集，通过重新分配取向破坏预设路径。主要结果为弯折条件、目标间隔、选择间隔、正确性、遗漏与报告期反应时。该实现无反馈、无奖励、无自适应阶梯，因而产生多级曲率的正确率而非个体阈值。

![TaskBeacon 轮廓整合任务流程](../task_flow.png)

**图 1. TaskBeacon 轮廓整合任务流程。** 每个试次依次呈现中央注视点 500 ms、第一幅阵列 1000 ms、灰色间隔 1000 ms、第二幅阵列 1000 ms、最长 4000 ms 的报告提示和 300 ms 灰色试次间隔；一个间隔呈现含 12 图元连续路径的信号阵列，另一个呈现位置与总体取向分布匹配但路径被破坏的空白阵列。路径弯折为 15°、30°、45°、60°或 75°，并含随机方向符号及 ±10°扰动。参与者在报告提示出现后按 F 选择第一幅、按 J 选择第二幅；正确与错误均不反馈，超时记为遗漏。目标间隔在每一弯折条件内等量分配，任务不根据反应调整难度。

该实现以像素定义刺激，配置中的显示器尺寸与观察距离尚未构成实际物理标定；因此弯折角是生成几何参数，Gabor 大小和间距不能直接报告为视觉角。材料库虽控制了配对位置和总体取向分布，有限项目是否仍存在局部显著性线索需由人类预实验、眼动或项目分析检验。正式研究应校准屏幕亮度、伽马、观看距离和呈现时序，并在目标样本中确认五级难度覆盖心理测量函数的有效区间。

## 参考文献

Altmann, C. F., Bülthoff, H. H., & Kourtzi, Z. (2003). Perceptual organization of local elements into global shapes in the human visual cortex. *Current Biology, 13*(4), 342–349. https://doi.org/10.1016/S0960-9822(03)00052-6

Chen, Y.-R., Jiang, S.-Q., Liu, X.-Y., & Zhang, J.-Y. (2025). Temporal contour integration deficits in children with amblyopia. *Investigative Ophthalmology & Visual Science, 66*(4), 27. https://doi.org/10.1167/iovs.66.4.27

Doshi, F. R., Konkle, T., & Alvarez, G. A. (2025). A feedforward mechanism for human-like contour integration. *PLOS Computational Biology, 21*(8), e1013391. https://doi.org/10.1371/journal.pcbi.1013391

Field, D. J., Hayes, A., & Hess, R. F. (1993). Contour integration by the human visual system: Evidence for a local “association field.” *Vision Research, 33*(2), 173–193. https://doi.org/10.1016/0042-6989(93)90156-Q

Hess, R. F., & Dakin, S. C. (1999). Contour integration in the peripheral field. *Vision Research, 39*(5), 947–959. https://doi.org/10.1016/S0042-6989(98)00152-7

Hess, R. F., & Field, D. J. (1999). Integration of contours: New insights. *Trends in Cognitive Sciences, 3*(12), 480–486. https://doi.org/10.1016/S1364-6613(99)01410-2

Hess, R. F., McIlhagga, W., & Field, D. J. (1997). Contour integration in strabismic amblyopia: The sufficiency of an explanation based on positional uncertainty. *Vision Research, 37*(22), 3145–3161. https://doi.org/10.1016/S0042-6989(96)00281-7

Jayakumar, S., Ahmed, A. O., Butler, P. D., Silverstein, S. M., Thompson, J. L., & Seitz, A. R. (2024). Performance on a contour integration task as a function of contour shape in schizophrenia and controls. *Vision Research, 219*, 108394. https://doi.org/10.1016/j.visres.2024.108394

Jiang, S.-Q., Chen, Y.-R., Liu, X.-Y., & Zhang, J.-Y. (2023). Contour integration deficits at high spatial frequencies in children treated for anisometropic amblyopia. *Frontiers in Neuroscience, 17*, 1160853. https://doi.org/10.3389/fnins.2023.1160853

Kamath, R. S., Weldon, K. B., Moser, H. R., Montoya, S. A., Abdullahi, K. S., Burton, P. C., Sponheim, S. R., Olman, C. A., & Schallmo, M.-P. (2026). Impaired contour object perception in psychosis. *Biological Psychiatry: Cognitive Neuroscience and Neuroimaging, 11*(2), 229–241. https://doi.org/10.1016/j.bpsc.2024.12.002

Keane, B. P., Silverstein, S. M., Papathomas, T. V., & Krekelberg, B. (2024). Correcting visual acuity beyond 20/20 improves contour element detection and integration: A cautionary tale for studies of special populations. *PLOS ONE, 19*(9), e0310678. https://doi.org/10.1371/journal.pone.0310678

Kourtzi, Z., & Huberle, E. (2005). Spatiotemporal characteristics of form analysis in the human visual cortex revealed by rapid event-related fMRI adaptation. *NeuroImage, 28*(2), 440–452. https://doi.org/10.1016/j.neuroimage.2005.06.017

Kovács, I., Chandna, A., Pennefather, P. M., Polat, U., & Norcia, A. M. (1999). Contour detection threshold: Repeatability and learning with “contour cards.” *Spatial Vision, 12*(3), 257–266. https://doi.org/10.1163/156856899X00157

Levi, D. M., Yu, C., Kuai, S.-G., & Rislove, E. (2007). Global contour processing in amblyopia. *Vision Research, 47*(4), 512–524. https://doi.org/10.1016/j.visres.2006.10.014

Li, Y., Wang, Y., & Li, S. (2019). Recurrent processing of contour integration in the human visual cortex as revealed by fMRI-guided TMS. *Cerebral Cortex, 29*(1), 17–26. https://doi.org/10.1093/cercor/bhx296

Mathes, B., Trenner, D., & Fahle, M. (2006). The electrophysiological correlate of contour integration is modulated by task demands. *Brain Research, 1114*(1), 98–112. https://doi.org/10.1016/j.brainres.2006.07.068

Mijović, B., De Vos, M., Vanderperren, K., Machilsen, B., Sunaert, S., Van Huffel, S., & Wagemans, J. (2014). The dynamics of contour integration: A simultaneous EEG–fMRI study. *NeuroImage, 88*, 10–21. https://doi.org/10.1016/j.neuroimage.2013.11.032

Reuther, J., Chakravarthi, R., & Martinovic, J. (2022). Masking, crowding, and grouping: Connecting low and mid-level vision. *Journal of Vision, 22*(2), 7. https://doi.org/10.1167/jov.22.2.7

Reuther, J., Chakravarthi, R., & Martinović, J. (2025). Contour integration in the parafovea and the near periphery: Testing the association field account. *Proceedings of the Royal Society B: Biological Sciences, 292*(2055), 20251107. https://doi.org/10.1098/rspb.2025.1107

Zhu, Z., Chen, B., Na, R., Fang, W., Zhang, W., Zhou, Q., Zhou, S., Lei, H., Huang, A., Chen, T., Ni, D., Gu, Y., Liu, J., Rao, Y., & Fang, F. (2019). Heritability of human visual contour integration—An integrated genomic study. *European Journal of Human Genetics, 27*(12), 1867–1875. https://doi.org/10.1038/s41431-019-0478-2
