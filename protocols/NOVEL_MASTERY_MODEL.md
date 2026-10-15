# Novel Writing Agent — Competency & Mastery Model

version: 2.0
status: ACTIVE_SYSTEM_PROTOCOL
scope: learning, story product design, long-form planning, writing, evaluation, serialization and system evolution
business_authority: D1traverser-debug/novel-writing-agent@main
architecture_ref: protocols/NOVEL_PRODUCT_ARCHITECTURE.md

## 0. Purpose

本模型回答五个问题：
1. 小说系统到底必须会什么；
2. 这些能力从什么证据学习；
3. 如何证明不是“读过/总结过”而是真能迁移；
4. 何时可以进入生产，何时只能保持假说；
5. 如何让真实平台/读者结果反向校准系统，而不是自评闭环。

`ACTIVE_RULEBOOK.md` 是生产约束；本文件是能力/评测权威；`MASTERWORK_DISTILLATION_PROTOCOL.md` 是训练执行层。研究笔记不能直接覆盖三者。

## 1. Evidence hierarchy

针对具体决策使用最强适用证据：
1. `LIVE_PROJECT_OUTCOME`：真实签约/推荐/留存/追读/评论簇/编辑反馈；
2. `CURRENT_PLATFORM_FIRST_PARTY`：当前番茄官方规则、帮助、课程、活动；
3. `PROJECT_BENCHMARK`：可复现的盲读、A/B、结构/正文 benchmark；
4. `PRIMARY_CRAFT_OR_RESEARCH`：原始创作方法、叙事学、学习科学、长篇生成研究；
5. `MASTERWORK_DIRECT_EVIDENCE`：用户提供语料的直接拆解与反例；
6. `COMMUNITY_HEURISTIC`：发现信号，不能单独晋级；
7. `MODEL_SELF_EVALUATION`：最低，只用于假说生成。

同一来源可以在不同 claim 上具有不同相关性。作品“成功”不证明其中每个特征都是成功原因。

## 2. Mastery levels

### L0 UNMAPPED
没有稳定问题定义、benchmark 或 failure signature。

### L1 CONCEPTUAL
能解释概念、区分例子和反例，但不能依赖它做重大生产决策。

### L2 OPERATIONAL_WITH_SCAFFOLD
能按明确 contract/benchmark 应用、发现常见失败并留下证据。

### L3 PROJECT_READY
能在真实项目中自主设计、比较替代方案、执行、审计、修复，不依赖用户指出漏掉的一级维度；无当前 scope 的 unresolved HIGH/BLOCKER。

### L4 TRANSFER_VERIFIED
在 materially different 项目/类型/阶段中迁移，并有真实 reader/editor/platform outcome。单一作品、单一项目或内部 CI 绝不能证明 L4。

## 3. Competency system

### C01 — Product premise / target reader / reader contract
必须能比较多个故事产品，区分题材表面新鲜与可持续 reader promise；知道为什么第一屏、第一章、前2万字、第一卷值得继续。
Failure: generic premise、只追热点、强设定弱故事、旧项目 incumbent bias。

### C02 — Dynamic long-form architecture
从 intended ending / transformation 反推 series → volume → arc → packet → chapter → scene，但分辨率随时间变化。近端可冻结，远端保持可重规划。
Failure: 120万字静态章节表、没有终局压力、局部改动不做下游失效分析、研究文章一来就重写冻结结构。
Runtime: `runtime/dynamic_outline.py`。

### C03 — World / system / institutional consequence
世界规则必须制造限制、成本、选择、社会/制度/经济后果；不以百科解释代替故事。

### C04 — Character construction / agency / arc
跟踪 want/need、belief、fear、competence、blind spot、coping strategy、values、choice、change pressure；人物弧必须由重大选择显现。

### C05 — Relationship network / ensemble
关系有独立的 trust/debt/power/obligation/intimacy/suspicion 变化；配角有脱离主角也会采取的行动。网络结构和双人关系都要可追踪。

### C06 — Theme / value conflict
主题由可成立的价值冲突与有代价的选择构成，不用旁白宣言或稻草人反方。

### C07 — Opposition / counter-agency / stakes
对手、人、机构、环境、制度和主角习惯都可能是 opposing force；必须有信息边界、资源、成本、独立策略和 tactic change。

### C08 — Mystery / revelation / information architecture
从真相/终局模型反推 clue、hypothesis、misdirection、source credibility、reframing、payoff debt。答案既要偿还承诺，也可以扩大模型。

### C09 — Scene architecture
每个保留场景至少改变 goal/knowledge/relationship/risk/resource/location/world-model/moral-commitment 之一；有目标、摩擦、turn/consequence。

### C10 — Chapter / packet architecture & acquisition
章节/packet 有具体功能、可见推进、情绪轮廓和 state-changing ending。前约2万字作为独立 acquisition/signing 产品评测，不套固定“黄金三章”公式。

### C11 — Narrative orchestration / pacing / long-serial rhythm
不仅是“快慢”。同时协调 event density、reveal、relationship、emotion、breather、engine rotation、ordinary life、payoff、reader memory 和 volume/series escalation。
Failure: 持续高压、程序化平台、只优化因果一致性、同一发动机循环。

### C12 — Dialogue / subtext / character voice
人物说话服务不同目标，允许拒绝、误解、回避、打断、隐瞒；文本、subtext、context 可分离。

### C13 — POV / focalization / prose / stylometry awareness
控制叙述者、视角、psychic distance、感官选择、句法和段落节奏。作者/译者/题材/时期都可能影响表面风格；不能把 stylometry 当成全部叙事结构。

### C14 — Emotion / tension / attachment
情绪与 tension 分开跟踪；形成 cause → pressure → behavior → consequence → aftershock。Attachment 来自具体欲望、脆弱、能力、普通生活、共同成本与关系后果。

### C15 — Foreshadow / payoff / reader memory
Seed → Echo/Transform → Payoff/Reframe；承诺有 owner/horizon/status。控制名字、规则、地点、时间数字和谜团债务的 cognitive load。

### C16 — Space / environment / action / domain reality
空间/环境作为 orientation、constraint、resource clock、clue、threat、action surface；专业现实只有改变选择/后果时才值得 page cost。

### C17 — Editorial diagnosis / revision / dependency impact
先判断 defect level：product/premise → architecture → character/relationship → sequence/scene → prose → sentence/copyedit。结构改动必须做 dependency invalidation。

### C18 — Platform / commercialization / serialization fit
理解当前番茄签约/推荐/治理/读者获取机制，但平台 heuristic 不能冒充普遍艺术规律。真实平台结果高于内部自评。

### C19 — Canon / story-state / dependency integrity
Plan 与 Canon 分离；accepted factual truth、timeline、knowledge state、relationship state、promises、threads、foreshadow、retcon impact 可追踪。
Runtime: `runtime/story_dependency_graph.py` + project Canon。

### C20 — Meta-learning / evidence design / system evolution
发现能力缺口 → 研究 → 多维分类 → claim-conditioned comparison → confound challenge → transfer probe → benchmark → bounded promotion → decay/rollback。
必须能够识别自己设计的错误抽象并撤回，而不是为了保持“已经写了”而继续固化。
Runtimes: `runtime/deliberation_admission.py`, `runtime/learning_transfer_admission.py`。

### C21 — Story candidate tournament / zero-based reselection
学习完成后能从零生成 materially different story engines，旧项目不享 incumbent privilege；使用向量、pairwise/Pareto、blind-reader、red-team、long-horizon stress 选 winner + backup。
Runtime: `runtime/story_reselection_admission.py`, `runtime/narrative_evaluation.py`。

## 4. Narrative evidence dimensions

跨作品学习和生产评测不得只用“文笔/节奏/逻辑”三个大词。至少参考 `NARRATIVE_EVIDENCE_SCHEMA` 的16维：story causality、discourse time、POV/focalization、character agency、relationship network、world/institutions、information/revelation、emotion/tension、pacing/page-cost、dialogue/voice、prose surface、serial escalation/payoff、acquisition/platform、theme、space/action、reader-memory load。

作者、系列、类型、POV、市场、时代、翻译、篇幅、题材是 claim-specific dependency factors，不是固定权重。

## 5. Learning-to-mastery gate

读完一本书最多证明获得 REFERENCE evidence。跨书重复出现也不能自动证明机制。

从 REFERENCE 到 EXPERIMENTAL：
- target dimensions 明确；
- comparison design 明确；
- shared factors/confounds 被评估；
- support + contradiction/boundary + alternative explanations；
- transfer probe。

到 PROJECT_PROVEN：真实项目 benchmark。

到 ACTIVE_RULE：formal campaign synthesis + 多种 comparison design + material confounds 已挑战 + boundary evidence + transfer + project/platform/live outcome。

到 L4：跨 materially different 项目与真实外部结果。

## 6. Planning / Canon / prose gate

Story candidate 先于 Active Project Identity。

Plan 是未来假设；Canon 是已接受事实；Prose 是读者看见的实现。三者不可互相偷换。

Plan→Canon 只能通过 accepted prose + acceptance + Canon reconciliation；研究结论不能直接写进 Canon。

## 7. Evaluation architecture

`runtime/narrative_evaluation.py` 使用向量评测和 hard gates。候选至少评估：
- acquisition;
- reader contract;
- character attachment;
- relationship dynamics;
- serial sustainability;
- engine diversity;
- narrative orchestration;
- continuity;
- development/richness;
- mystery/revelation;
- emotional range;
- voice/prose;
- cognitive load;
- originality;
- platform fit;
- production complexity/risk。

平均分不能覆盖 hard gate。故事选择使用 pairwise/Pareto 保留真实 tradeoff。

## 8. Audit gates

### Gate A — Learning evidence
source identity、coverage、closed-context reconstruction、claim/dimension、comparison design、shared factors、negative evidence、transfer。

### Gate B — Story product selection
current platform evidence、>=3 materially distinct candidates、vector/Pareto、blind-reader、red-team、long-horizon stress、winner+backup。

### Gate C — Series / volume architecture
ending constraint、dynamic hierarchy、character/relationship arcs、opposition、world/rules、reveal/payoff ladder、engine diversity、theme/value conflict。

### Gate D — Opening / packet
first-screen acquisition、first-payoff、attachment engine、reader promise、cognitive load、platform fit、packet-level continuity/signing readiness。

### Gate E — Chapter / scene production
frozen context/contract、scene state change、POV/emotion/dialogue/environment、continuity、reader appetite。

### Gate F — Release
same FINAL hash review evidence、proofread、artifact QA、deterministic guard、Canon reconciliation。

### Gate G — Outcome / replan
reader/platform evidence, causal uncertainty, replan alternatives, downstream invalidation, Rulebook/system evolution when warranted。

## 9. Current campaign assurance

Current FQ001 masterwork campaign is a learning intervention after a real generic Fanqie quality rejection. Exact editor-side cause remains unknown.

Current maximum claims:
- source/cursor and distillation mechanics can be verified;
- learning comparison/transfer/reselection mechanics can be trajectory tested;
- old FQ001 is historical evidence only during the campaign;
- no claim that the future winner will be commercially successful before live outcome exists.

System target after this redesign: `EXECUTABLE_LEARNING_TO_PLANNING_OS_VERIFIED__LIVE_POST_RESELECTION_LITERARY_OUTCOME_OPEN`.
