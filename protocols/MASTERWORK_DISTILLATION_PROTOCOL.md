# NOVEL_OS — Masterwork Distillation & Transfer Protocol

version: 2.0
status: ACTIVE_SYSTEM_PROTOCOL
scope: lawful masterwork study -> compact learning evidence -> cross-work comparison -> transfer benchmark -> bounded rule promotion -> zero-based story reselection
business_authority: D1traverser-debug/novel-writing-agent@main

## 0. Purpose

优秀作品不是“模仿库”，逐字读完也不等于学会。本协议把用户提供的20+本语料变成一个可验证训练系统，同时防止：

- 把成功作品的一切都误当成功因；
- 幸存者偏差；
- 只会总结“节奏好、人物立体、伏笔多”；
- 复制措辞、桥段、设定、人物关系或独特表达；
- 把同一作者/系列的多本书重复计成多份独立证据；
- 读完很多书但不会把机制迁移到新问题；
- 全部读完才第一次比较，导致学习方向错误到最后才暴露；
- 学习库存越积越大，却没有压缩、检索、反证、迁移和淘汰；
- 直接把旧FQ001设计当默认答案，错过真正从零重选题材/故事的机会。

该协议是 `protocols/NOVEL_MASTERY_MODEL.md` 的学习执行层。Masterwork evidence 默认只是 `LEARNING_EVIDENCE`，不能直接覆盖 `ACTIVE_RULEBOOK`、项目 Canon 或正文。

## 1. Source / copyright boundary

允许的研究输入：
1. 用户合法提供或系统合法可访问的文本；
2. 官方/作者授权的免费阅读、试读、公开章节；
3. 作者访谈、创作谈、官方课程；
4. 合法书评、学术/媒体评论、读者反馈。

禁止把来路不明或破解资源主动抓取为训练源。仓库只保存结构标签、位置引用、摘要、机制结论、极短必要引文与证据关系；不保存可替代原作阅读的大段正文。

用户当前标准化全文语料的文件身份、hash、游标和覆盖由 `research/masterworks/STUDY_STATE.json` 持有；完整原文留在用户提供的Drive语料库。

## 2. Corpus taxonomy / evidence independence

`research/masterworks/CORPUS_MAP.json` 是当前训练语料分类权威。

规则：
- 一本文件不自动等于一份独立证据；
- 同一系列的多卷不得作为多个独立 corroboration vote；
- 同一作者的多部作品可以提供差异/边界证据，但在“跨作者普适性”判断中属于同一 evidence family；
- 至少区分 `genre_cluster`、`evidence_family_id`、`learning_roles`；
- 跨作品晋级必须报告证据族数量，而不仅是作品数量；
- 题材、角色名、独特设定、具体桥段永远不是可直接迁移机制。

## 3. Distillation unit

每部作品同时按三个尺度研究，禁止只做宏观剧情梗概。

### A. Macro — series / volume / arc
- reader contract / premise；
- mainline and terminal pressure；
- volume/unit turns；
- world-rule expansion；
- mystery/reveal ladder；
- character/relationship arcs；
- payoff debt / foreshadow horizon；
- escalation and rest rhythm；
- ending convergence。

### B. Meso — 3–10 chapter packet / sequence
- sequence objective；
- question opened / answered / replaced；
- irreversible state changes；
- engine diversity；
- relationship delta；
- emotional contour；
- information asymmetry；
- next-packet handoff。

### C. Micro — chapter / scene / paragraph function
主动扫描：first-screen acquisition、scene goal/friction/turn/consequence、causality、心理、情绪、环境/空间、感官、动作、对白/subtext/voice、POV/psychic distance、world-rule delivery、clue/red-herring/reveal、人物行为、关系权力变化、transition/compression、humor/relief、motif、句段节奏、chapter-end reading reason、mobile readability/cognitive load。

如果用户指出一个这里没有覆盖的一级维度，视为 C20 meta-learning incident：先扩 competency lattice，再继续研究。

## 4. Required learning pipeline — D0–D14

### D0 RIGHTS_AND_SOURCE
确认来源、source identity、hash、范围、版本/重复边界和缺口。

### D1 SELECTION_RATIONALE
说明这部作品训练哪些 C01–C20 能力、哪些能力不该向它学习，并绑定 `CORPUS_MAP` 分类。

### D2 PHASE_MAP
按真实结构分阶段，而不是平均抽样。至少标记 opening/acquisition、first major payoff、early relationship/world expansion、mid-series escalation、late convergence、ending/payoff、明显强段/弱段。

### D3 COLD_READ_TRACE
第一遍记录“此刻想知道什么、担心什么、相信什么、误解什么、为何继续读”，禁止先用理论替读者体验。

### D4 STRUCTURAL_ANNOTATION
记录 state change、causal chain、question-answer ladder、reveal ladder、relationship delta、world-rule delta。

### D5 MICROCRAFT_ANNOTATION
分析心理、环境、对白、动作、POV、信息释放、句段节奏等微观技术，并回答“这个描写改变了什么”。

### D6 POSITIVE_NEGATIVE_DIFF
同一作品同时记录有效机制、失败/代价高机制、作者自我复盘、高信号读者分歧。成功作品不享有“全自动正确”。

### D7 ABLATION / COUNTERFACTUAL
至少做一个反事实：删掉、延后、反转或低成本替代某机制后，会失去什么？如果几乎无损，它可能是表面风格而非核心机制。

### D8 CLOSED_CONTEXT_RECONSTRUCTION
单书完成后，先关闭全文和滚动总账，只允许读取该书的压缩学习索引/机制卡，重建：核心 reader contract、3–8个关键机制、3个负证据/边界、1个最可能被误学的表面特征。再重新打开总账核对遗漏/失真并修正压缩层。

目的不是假装模型像人类一样形成永久记忆，而是验证：**压缩后的可加载知识是否保留了足以用于后续决策的结构**。

### D9 CROSS-WORK_TRIANGULATION
每完成一本立即进行非晋级式跨书比较，不再等全部队列完成才第一次比较：
- 与至少一个既有 completed work 比较；
- 区分相同机制、冲突机制、边界条件和负证据；
- 按 `evidence_family_id` 去重；
- 更新下一本的 observation axes；
- 当前训练 campaign 未结束前，比较结果最高保持 `REFERENCE / EXPERIMENTAL`，不得直接升为 ACTIVE_RULE。

### D10 PROJECT_TRANSFER_EXPERIMENT
把机制迁移到**全新、非复制**的案例。优先使用合成 benchmark、历史FQ001诊断片段或新候选设计小样，而不是直接重写当前正文。至少做两个替代方案，预测收益和副作用。

### D11 ADVERSARIAL_REVIEW
主动挑刺：是否过拟合原作？是否只是题材/作者声纹？是否与项目身份冲突？是否把复杂度当质量？是否增加认知负荷？是否存在更低成本机制？反例是否更能解释效果？

### D12 PROMOTION
等级：`REFERENCE -> EXPERIMENTAL -> PROJECT_PROVEN -> ACTIVE_RULE -> CROSS_PROJECT_VERIFIED`。

当前20+本训练 campaign 内：
- 单书观察可到 REFERENCE；
- 跨书比较/迁移假说可到 EXPERIMENTAL；
- PROJECT_PROVEN 需要项目 benchmark；
- ACTIVE_RULE 默认被训练 campaign completion gate 阻断，除非出现新的强外部硬结果且另行走 material decision admission；
- ACTIVE_RULE 正常晋级要求至少3个独立 evidence family、至少2个 genre cluster、负证据/边界、transfer probe、项目或外部结果证据。

### D13 STOP / DECAY
达到当前学习决策所需证据即停止继续扩资料。规则会因平台、类型、项目变化而降级；旧结论没有永恒地位。

### D14 CAMPAIGN_SYNTHESIS_AND_STORY_RESELECTION
全部非排除语料完成后，才做正式 campaign synthesis：
- mechanism graph（support / contradict / boundary）；
- competency evidence matrix；
- failure library；
- transfer benchmark results；
- 当前平台官方证据刷新；
- 从零 story candidate tournament。

历史《凌晨零点，我接到明天的订单》只作为候选/历史结果证据之一，**没有 incumbent privilege**。新正文在 story reselection + pre-draft architecture admission 通过前保持 HOLD。

## 5. Continual comparison cycle

`research/masterworks/CROSS_WORK_LEARNING_STATE.json` 持有训练 campaign 的跨书状态。

每本完成后的强制循环：
`COMPLETE WORK -> D8 CLOSED-CONTEXT RECONSTRUCTION -> D9 EVIDENCE-FAMILY COMPARISON -> UPDATE OBSERVATION AXES -> D10 TRANSFER PROBE -> D11 ADVERSARIAL REVIEW -> QUEUE ADVANCE`。

因此“一次只读一本”与“持续跨书学习”同时成立：阅读上下文不混书，但学习反馈不延迟到最后。

## 6. Compact mechanism registry

`research/masterworks/MECHANISM_REGISTRY.json` 是压缩学习索引，不是 Rulebook。

每个机制至少记录：
- mechanism id；
- support work ids；
- support evidence family ids；
- genre clusters；
- boundary condition；
- negative evidence；
- current promotion status；
- 是否为 active rule。

禁止以“出现次数”替代机制证据质量。

## 7. Microcraft benchmark definitions

### 7.1 Psychological portrayal
控制 attention、interpretation、desire/fear collision、bodily leakage、suppression、causally relevant memory、decision/aftershock、thought/speech/action subtext。删掉显式情绪标签后，读者仍应能读出主要情绪。

### 7.2 Environment / atmosphere
环境至少承担 `ORIENTATION / CONSTRAINT / CLUE / THREAT / CHARACTER_LENS / EMOTION / WORLD / FORESHADOW / ACTION_SURFACE` 之一。删除后若方向、情绪、选择、信息、世界均无变化，则 page-cost 需要重证。

### 7.3 Plot progression
每个保留场景至少改变 `GOAL / KNOWLEDGE / RELATIONSHIP / RISK / RESOURCE / LOCATION / WORLD_MODEL / MORAL_COMMITMENT` 一项。

### 7.4 Dialogue
检查目的冲突、权力变化、隐藏意图、声纹、打断/回避/错答、行动穿插；长期 Q&A 信息采访默认失败。

### 7.5 Emotion
情绪链至少具有 `cause -> pressure -> behavior -> consequence -> aftershock`。

### 7.6 Quality audit
顺序固定从高到低：`reader contract -> architecture -> character/relationship -> mystery/world -> sequence -> scene -> POV/emotion/dialogue/environment -> prose rhythm -> sentence/copyedit -> artifact/platform`。禁止先润色结构失败。

## 8. Anti-overfit questions

每次至少回答：
1. 这是必要机制、作者特色，还是二者混合？
2. 同样机制在哪里失效、付代价或被作品自己放弃？
3. 如果移植到不同类型，会保留功能还是只剩形式？
4. 是否依赖作者既有读者、题材、超长篇幅或系列积累？
5. 能否用更低复杂度实现同样读者效果？
6. 有没有 live project / platform / blind reader / opposite-case evidence 支持或反驳？
7. 同一作者/系列是否正在被重复计票？

## 9. Zero-based story reselection after learning

正式重规划不是“把现在故事修得更像名作”。必须：
1. 重新抓取当时最新番茄官方规则/课程/品类信息；
2. 从训练结果中导出能力约束和失败边界，而不是拼装名作表面元素；
3. 生成至少3个 materially distinct story-engine candidates；
4. 旧FQ001若保留，也只能作为其中一个候选；
5. 使用向量比较而非单一总分，至少看 acquisition、reader contract、character attachment、serial sustainability、engine diversity、world/mystery capacity、emotional range、originality、platform fit、production complexity、long-horizon consistency risk；
6. 做 pairwise / Pareto comparison、blind-reader、adversarial、100k/300k/800k stress test；
7. 选出 winner + backup；
8. 用动态分层大纲（series -> volume -> arc -> opening packet）和结构化 Canon/Story Graph规划，允许后续基于真实结果事件驱动重规划；
9. 第一约2万字作为独立 acquisition/signing packet 先通过 benchmark，再开始正文生产。

机械 admission：`runtime/story_reselection_admission.py`。

## 10. Material decision discipline

学习协议、能力模型、story selection、Rulebook promotion、Canon/schema重构等 material mutation，先经过 `runtime/deliberation_admission.py`：当前权威 + 内部证据 + 外部证据/不适用理由 + 至少2方案 + 反例 + 假设挑战 + 风险/回退。不能“想到就写”。

## 11. Current campaign boundary

FQ001 当前：
- 已完成：`SHIRI_ZHONGYAN / GUI_MI_ZHI_ZHU / DAO_MU_BI_JI`；
- 当前：`GUI_CHUI_DENG`，用户暂停于 source line 3913，唯一恢复点 line 3914；
- `QING_YU_NIAN` 仍 PENDING；
- `NORWEGIAN_WOOD` 按用户要求 EXCLUDED；
- 当前正文/旧CH9继续 HOLD；
- `SIGNING_MODE_IMMUTABLE`、`SERIALIZATION_MODE_IMMUTABLE` 保持用户锁定；
- 其余题材、书名、世界观、主角、人物关系、总纲、卷纲和旧FQ001候选设计在最终学习后均可从零竞争。
