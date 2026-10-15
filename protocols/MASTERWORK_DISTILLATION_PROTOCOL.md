# NOVEL_OS — Masterwork Distillation & Transfer Protocol

version: 2.1
status: ACTIVE_SYSTEM_PROTOCOL
scope: lawful masterwork study -> compact learning evidence -> claim-conditioned comparison -> transfer benchmark -> bounded promotion -> zero-based story reselection
business_authority: D1traverser-debug/novel-writing-agent@main

## 0. Purpose

优秀作品不是“模仿库”，逐字读完也不等于学会。本协议把用户提供的20+本语料变成一个可验证训练系统，同时防止：

- 把成功作品的一切误当成功因；
- 把“同作者”“同系列”“同类型”粗暴当成相同作品或固定权重；
- 把作品数量误当独立证据数量；
- 只总结“节奏好、人物立体、伏笔多”；
- 复制措辞、桥段、设定、人物关系或独特表达；
- 全部读完才第一次比较，导致观察框架偏差到最后才暴露；
- 学习库存不断增加，却没有压缩、检索、反证、迁移和淘汰；
- 只会保持因果一致，却不会组织节奏、关系、情绪、视角、揭示和读者体验；
- 直接把旧FQ001设计当默认答案，错过真正从零重选题材/故事的机会。

本协议是 `protocols/NOVEL_MASTERY_MODEL.md` 的学习执行层。任何 Masterwork evidence 默认只是 `LEARNING_EVIDENCE`，不能直接覆盖 `ACTIVE_RULEBOOK`、项目 Canon 或正文。

## 1. Source / copyright boundary

允许研究输入：
1. 用户合法提供或系统合法可访问的文本；
2. 官方/作者授权的免费阅读、试读、公开章节；
3. 作者访谈、创作谈、官方课程；
4. 合法书评、学术/媒体评论、读者反馈。

禁止主动抓取盗版/破解资源。仓库只保存结构标签、位置引用、摘要、机制结论、极短必要引文与证据关系，不保存可替代原作阅读的大段正文。

用户全文语料的文件身份、hash、游标和覆盖由 `research/masterworks/STUDY_STATE.json` 持有；完整原文留在用户提供的 Drive 语料库。

## 2. Narrative evidence ontology

`research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json` 是跨作品比较的维度权威，至少区分：
- story/fabula 与 causal engine；
- discourse/temporal order；
- narrator/POV/focalization；
- character construction/agency；
- relationship network/arcs；
- world/setting/institutions；
- information/mystery/revelation；
- emotion/tension/reader affect；
- pacing/rhythm/page-cost；
- dialogue/voice/subtext；
- prose/stylometry/surface；
- serial engine/escalation/payoff；
- acquisition/product/platform；
- theme/value conflict；
- space/environment/action；
- reader memory/cognitive load。

核心原则：**证据依赖不是某本书的固定属性，而是“针对某个 claim、在某些维度上的条件相关性”。**

作者、系列、类型、时代、语言/翻译、市场、POV、篇幅、题材等只是 `potential dependency factors`：
- 同作者异作品可以“控制作者、观察结构/题材/叙述差异”；
- 同系列跨卷可以“控制世界/角色背景、观察发动机/人物/节奏变化”；
- 同类型异作者可以测试作者因素；
- 异类型但同功能可以测试机制是否脱离表面题材仍成立。

任何字段都不得自动把两本书合并成“一票”，也不得自动判定“独立”。

`research/masterworks/CORPUS_MAP.json` 只保存队列、关系提示和预研元数据状态。未读作品的类型/风格/结构标签必须在 D1 预检后才能作为正式证据使用。

## 3. Distillation unit

### A. Macro — series / volume / arc
reader contract、主线/终局压力、volume turns、world-rule expansion、mystery/reveal ladder、character/relationship arcs、payoff debt、escalation/rest、ending convergence。

### B. Meso — packet / sequence
sequence objective、question opened/answered/replaced、state change、engine diversity、relationship delta、emotional contour、information asymmetry、next-packet handoff。

### C. Micro — chapter / scene / paragraph
first-screen acquisition、goal/friction/turn/consequence、causality、心理、情绪、环境/空间、动作、对白/subtext/voice、POV/psychic distance、world-rule delivery、clue/reveal、relationship power shift、transition/compression、humor/relief、motif、句段节奏、chapter-end reading reason、mobile cognitive load。

用户指出一个遗漏的一级维度时，视为 C20 meta-learning incident：先扩 ontology/benchmark，再继续。

## 4. Required learning pipeline — D0–D14

### D0 RIGHTS_AND_SOURCE
确认来源、source identity、hash、范围、版本/重复边界和缺口。

### D1 SELECTION_RATIONALE_AND_METADATA_PREFLIGHT
说明本书可训练哪些 C01–C20 能力、哪些不能向它学习。外部核对作者/系列/出版形态/市场等会影响比较设计的元数据；未核对字段保持 UNKNOWN/PREFLIGHT_HINT，不能直接进入推断。

### D2 PHASE_MAP
按真实结构分阶段，不平均抽样。最低覆盖 opening/acquisition、first payoff、early relationship/world expansion、mid escalation、late convergence、ending/payoff、显著强段/弱段。

### D3 COLD_READ_TRACE
先记录此刻读者想知道、担心、相信、误解什么以及为何继续读，禁止理论先行替代读者体验。

### D4 STRUCTURAL_ANNOTATION
记录 state change、causal chain、question-answer/reveal ladder、relationship delta、world-rule delta、event anchors 与关键结构位置。

### D5 MICROCRAFT_ANNOTATION
分析心理、环境、对白、动作、POV、信息释放、句段节奏等微观技术，并回答“这个描写改变了什么”。

### D6 POSITIVE_NEGATIVE_DIFF
同一作品同时记录有效机制、失败/高代价机制、作者自我复盘、高信号读者分歧。成功作品不享有“全自动正确”。

### D7 ABLATION / COUNTERFACTUAL
至少一个反事实：删掉、延后、反转或低成本替代某机制，会损失什么？若几乎无损，它可能只是表面风格。

### D8 CLOSED_CONTEXT_RECONSTRUCTION
单书完成后关闭全文和滚动总账，只允许读取压缩学习索引，重建核心 reader contract、关键机制、边界/负证据、最容易误学的表面特征；再重新打开总账核对遗漏/失真并修正压缩层。

目的不是假装模型形成永久人类记忆，而是验证压缩后的可加载知识是否足够支撑后续决策。Retrieval-like reconstruction 失败本身就是学习系统缺陷。

### D9 CLAIM-CONDITIONED CROSS-WORK TRIANGULATION
每完成一本立即进行非晋级式比较，不等全部队列结束。

每次比较必须：
1. 明确 `claim_id` 与目标 narrative dimensions；
2. 选择最有信息量的 comparison design，而不是固定书对；
3. 明确 support / contradict / boundary / mixed observations；
4. 对作者、系列、类型、市场、时期、POV、翻译/版本等共享因素逐项判断与当前 claim 的相关性；
5. 记录替代解释与未解决 confounds；
6. 用 matched contrasts 挑战主要混杂因素；
7. 更新下一本应该重点观察的维度。

允许且鼓励：`WITHIN_AUTHOR_CROSS_WORK / WITHIN_SERIES_CROSS_STAGE / CROSS_AUTHOR_SAME_OR_ADJACENT_GENRE / CROSS_GENRE_SAME_FUNCTION / CROSS_FORMAT_OR_MARKET / WITHIN_WORK_CROSS_ARC / MATCHED_SURFACE_DIFFERENT_FUNCTION / MATCHED_FUNCTION_DIFFERENT_SURFACE`。

当前 campaign 中，bootstrap hypotheses 先保持 REFERENCE；完成新的 claim-conditioned dependency review 后才允许变成 EXPERIMENTAL。

### D10 PROJECT_TRANSFER_EXPERIMENT
把机制迁移到全新、非复制案例；优先使用合成 benchmark、历史FQ001诊断片段或新候选设计小样，而不是直接重写当前正文。至少两个替代方案，明确 target dimensions、预期收益、副作用、失败条件。

### D11 ADVERSARIAL_REVIEW
主动寻找：过拟合、幸存者偏差、作者/题材混杂、翻译/版本影响、复杂度崇拜、认知负荷、低成本替代方案、反例、不同读者/平台边界。

### D12 PROMOTION
等级：`REFERENCE -> EXPERIMENTAL -> PROJECT_PROVEN -> ACTIVE_RULE -> CROSS_PROJECT_VERIFIED`。

当前20+本 campaign：
- 单书观察：REFERENCE；
- 完成 dependency-aware comparison + transfer probe：可到 EXPERIMENTAL；
- PROJECT_PROVEN：必须有项目 benchmark；
- ACTIVE_RULE：默认等 formal campaign synthesis；
- 正常 ACTIVE_RULE promotion 不按“独立作者数”或“作品票数”决定，而要求：重复支持、至少两种不同 comparison design、明确 boundary/contradiction、高相关 shared factors 已被对照挑战或继续作为 blocker、transfer probe、项目/平台/live outcome evidence。

### D13 STOP / DECAY
达到当前决策所需证据就停止扩资料。平台、类型、项目变化后旧规则可降级，不把研究库存当永恒真理。

### D14 CAMPAIGN_SYNTHESIS_AND_STORY_RESELECTION
全部非排除语料完成后做正式综合：
- claim-conditioned mechanism graph；
- multidimensional competency evidence matrix；
- failure/boundary library；
- comparison-design coverage map；
- transfer benchmark results；
- 当前番茄官方规则/课程/市场证据刷新；
- zero-based story candidate tournament。

旧《凌晨零点，我接到明天的订单》只作为历史候选/外部结果证据之一，没有 incumbent privilege。新正文在 reselection + pre-draft architecture admission 前保持 HOLD。

## 5. Continual comparison cycle

`research/masterworks/CROSS_WORK_LEARNING_STATE.json` 持有 campaign 跨书状态。

强制循环：
`COMPLETE WORK -> D8 RECONSTRUCTION -> SELECT CLAIM/DIMENSIONS -> SELECT COMPARISON DESIGN -> ASSESS SHARED FACTORS -> SUPPORT/CONTRADICT/BOUNDARY ANALYSIS -> UPDATE OBSERVATION AXES -> D10 TRANSFER -> D11 RED TEAM -> QUEUE ADVANCE`。

因此“一次只逐字读一本”与“持续比较学习”同时成立：全文上下文不混书，学习反馈不延迟。

## 6. Compact mechanism registry

`research/masterworks/MECHANISM_REGISTRY.json` 只是压缩学习索引，不是 Rulebook。
每个机制至少记录：mechanism id、target dimensions、support works、comparison maturity、boundary、negative evidence、promotion status、active_rule flag。

禁止保存 `evidence_family_id` 这类固定独立性标签；依赖关系存在 comparison receipt 中。

## 7. Microcraft benchmark definitions

### 7.1 Psychological portrayal
控制 attention、interpretation、desire/fear collision、bodily leakage、suppression、causally relevant memory、decision/aftershock、thought/speech/action subtext。删去显式情绪标签后仍能读出主要情绪。

### 7.2 Environment / atmosphere
环境至少承担 `ORIENTATION / CONSTRAINT / CLUE / THREAT / CHARACTER_LENS / EMOTION / WORLD / FORESHADOW / ACTION_SURFACE` 之一。删除后若方向、情绪、选择、信息、世界均无变化，则 page-cost 需要重证。

### 7.3 Plot progression
每个保留场景至少改变 `GOAL / KNOWLEDGE / RELATIONSHIP / RISK / RESOURCE / LOCATION / WORLD_MODEL / MORAL_COMMITMENT` 一项。

### 7.4 Dialogue
检查目的冲突、权力变化、隐藏意图、声纹、打断/回避/错答、行动穿插；长期 Q&A 信息采访默认失败。

### 7.5 Emotion
情绪链至少具有 `cause -> pressure -> behavior -> consequence -> aftershock`。

### 7.6 Quality audit
从高到低：`reader contract -> architecture -> character/relationship -> mystery/world -> sequence -> scene -> POV/emotion/dialogue/environment -> prose rhythm -> sentence/copyedit -> artifact/platform`。禁止先润色结构失败。

## 8. Anti-overfit / confound questions

每次至少回答：
1. 这是功能机制、作者特色、题材惯例、市场约束，还是几者混合？
2. 同一作者在另一作品是否使用不同结构/声纹/人物组织？
3. 同一系列跨阶段是否改变发动机或叙事方式？
4. 同类型异作者能否复现该功能？
5. 异类型是否存在不同表面、同功能的实现？
6. 该机制在哪里失效、付代价或被作品自己放弃？
7. 是否存在更低复杂度实现？
8. 翻译、版本、时代、篇幅、POV、平台是否影响这个具体 claim？
9. 有没有 live project / platform / blind reader / opposite-case evidence 支持或反驳？

## 9. Zero-based story reselection

正式重规划不是“把旧故事修得更像名作”。必须：
1. 刷新当时最新番茄官方规则、课程和市场/品类信号；
2. 从训练结果提取机制、能力边界和失败条件，不拼装名作表面元素；
3. 生成至少3个 materially distinct story-engine candidates；
4. 旧FQ001若保留，也只能作为候选之一；
5. 用向量比较，不用单一总分；至少看 acquisition、reader contract、character attachment、serial sustainability、engine diversity、world/mystery capacity、emotional range、originality、platform fit、production complexity、long-horizon consistency risk；
6. 做 pairwise/Pareto comparison、blind-reader、adversarial、100k/300k/800k stress test；
7. 选 winner + backup；
8. 用动态分层大纲（series -> volume -> arc -> opening packet）+ 结构化 Canon/Story Graph，允许基于真实结果事件驱动重规划；
9. 第一约2万字作为 acquisition/signing packet 单独通过 benchmark 后才写正文。

机械 admission：`runtime/story_reselection_admission.py`。

## 10. Material decision discipline

学习协议、能力模型、story selection、Rulebook promotion、Canon/schema 重构等 material mutation，先经过 `runtime/deliberation_admission.py`：当前权威 + 内部证据 + 外部证据/不适用理由 + 至少2方案 + 反例 + 假设挑战 + 风险/回退。不能“想到就写”。

这不要求每次改标点都上网；它要求每个**会改变系统行为、学习框架、故事产品方向或证据标准的决策**都先研究、比较和自我攻击。

## 11. Current campaign boundary

FQ001 当前：
- 已完成：`SHIRI_ZHONGYAN / GUI_MI_ZHI_ZHU / DAO_MU_BI_JI`；
- 当前：`GUI_CHUI_DENG`，暂停于 source line 3913，唯一恢复点 line 3914；
- `QING_YU_NIAN` 仍 PENDING；
- `NORWEGIAN_WOOD` 按用户要求 EXCLUDED；
- 旧正文/旧CH9继续 HOLD；
- `SIGNING_MODE_IMMUTABLE`、`SERIALIZATION_MODE_IMMUTABLE` 保持用户锁定；
- 其余题材、书名、世界观、主角、人物关系、叙事结构、总纲、卷纲和旧FQ001候选设计在最终学习后均可从零竞争。
