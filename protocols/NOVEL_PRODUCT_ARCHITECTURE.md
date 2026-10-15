# Novel Writing Agent — Evidence-to-Outcome Product Architecture

version: 1.0
status: CANDIDATE_SYSTEM_ARCHITECTURE
scope: learning -> story selection -> planning -> canon -> production -> evaluation -> outcome -> evolution
business_authority: D1traverser-debug/novel-writing-agent@main
parent_control: D1traverser-debug/universal-agent-os@main

## 0. Product objective

目标不是“写出一篇看起来像小说的文本”，也不是“把规则越堆越多”。目标是建立一个能够长期产出、诊断、学习和重规划的小说产品系统：

1. 从真实读者/平台结果、当前平台权威、用户合法语料、创作方法与反例中学习；
2. 把学习压缩为可检索、可比较、可迁移的机制证据，而不是模仿库；
3. 在学习 campaign 完成后从零比较故事产品，而不是默认修旧项目；
4. 用动态分层规划和结构化依赖控制长篇漂移，但不把文学创作降成数据库填表；
5. 把 Plan、Canon、Prose、Review、Outcome 分开，任何一层都不能伪装成另一层的证据；
6. 每次 material 决策先研究、比较、反例挑战，再执行；
7. 用真实平台/读者结果反向更新规划和系统规则。

## 1. Eight-layer authority model

### L1 — LEARNING EVIDENCE
Authority:
- `protocols/MASTERWORK_DISTILLATION_PROTOCOL.md`
- `research/masterworks/STUDY_STATE.json`
- `research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json`
- `research/masterworks/CORPUS_MAP.json`
- `research/masterworks/CROSS_WORK_LEARNING_STATE.json`
- `research/masterworks/MECHANISM_REGISTRY.json`

Function: sequential full-text study, closed-context reconstruction, claim-conditioned comparison, transfer probes, boundary/negative evidence.

Hard boundary: LEARNING does not directly change Rulebook, Canon or prose.

### L2 — STORY PRODUCT CANDIDATES
Authority: a future reselection packet admitted through `runtime/story_reselection_admission.py`.

Each candidate must define premise, story engine, target reader, reader contract, acquisition hypothesis, character attachment engine, serial sustainability, differentiation and risks.

Hard boundary: historical FQ001 has no incumbent privilege.

### L3 — DYNAMIC PLAN
Runtime: `runtime/dynamic_outline.py`.

Hierarchy: `SERIES -> VOLUME -> ARC -> PACKET -> CHAPTER -> SCENE`.

Near horizon may freeze for execution; mid/far horizon remains revisable. Replan requires evidence, alternatives, downstream invalidation and review. Plan is expectation, not truth.

### L4 — STORY/CANON DEPENDENCY GRAPH
Runtime: `runtime/story_dependency_graph.py`.

Coordinates premise, events, character/relationship state, world rules, promises, foreshadowing, threads and outline dependencies. Existing project Canon files remain the accepted factual authority.

Hard boundary: research or plan alone cannot become Canon. Canon promotion requires accepted prose + acceptance evidence + reconciliation.

### L5 — EXECUTION / CONTEXT PACK
Authority: project chapter/packet contract, frozen Context Pack and `runtime/release_evidence_guard.py`.

Writer receives minimum sufficient project identity, current plan slice, relevant Canon and bounded rule slices. No research dump into Writer context.

### L6 — MULTI-DIMENSIONAL EVALUATION
Runtime: `runtime/narrative_evaluation.py` plus owner review roles.

Candidate/prose evaluation is a vector, not a scalar. Required dimensions include acquisition, reader contract, character attachment, relationship dynamics, serial sustainability, engine diversity, narrative orchestration, continuity, development/richness, mystery/revelation, emotional range, voice/prose, cognitive load, originality, platform fit and production-complexity risk.

Hard gates override averages. Pareto/pairwise evidence preserves tradeoffs instead of hiding them in one weighted score.

### L7 — LIVE OUTCOME
Strongest evidence:
- actual platform signing/recommendation result;
- real reader retention/follow-read/comment clusters when available;
- explicit editor feedback;
- publication constraints confirmed by user/platform.

Hard boundary: CI, self-review, simulated readers or internal scores are not live literary outcome.

### L8 — EVOLUTION
Authority: `audits/EVOLUTION_INDEX.json` + causal audit records.

A real defect triggers diagnosis, external research where material, alternatives, counterexamples, repair-or-block action, regression and outcome observation. Failed approaches and rejected alternatives remain visible.

## 2. Core data separation

`LEARNING_EVIDENCE != ACTIVE_RULE`

`STORY_CANDIDATE != ACTIVE_PROJECT_IDENTITY`

`PLAN != CANON`

`CANON != PROSE_SURFACE`

`MODEL_SELF_EVALUATION != BLIND_READER`

`INTERNAL_CI != PLATFORM_OUTCOME`

`ROLE_SEPARATION != INDEPENDENT_EXECUTOR_IDENTITY`

`PUBLISHED_STATE != INFERRED_FROM_INTERNAL_ARTIFACT`

Any mechanism that collapses these boundaries is a system defect.

## 3. Learning architecture

Reading remains one work at a time and in source order. Comparison happens only after a work completes so full-text contexts do not contaminate the active sequential pass.

Cross-work comparison does not use a fixed book/author independence score. It is claim-conditioned:
- choose target narrative dimensions;
- choose comparison design;
- assess shared factors such as author/series/genre/POV/market/period/translation;
- find support, contradiction and boundary evidence;
- test alternative explanations;
- run transfer probes.

Same-author and same-series works are often unusually valuable controlled contrasts, not duplicates.

## 4. Post-study zero-based product selection

When all non-excluded corpus works complete:
1. formal synthesis of mechanisms and contradictions;
2. refresh current Fanqie first-party rules/courses/category signals;
3. generate >=3 materially different engine candidates;
4. include historical FQ001 only if it remains competitive, without bonus weight;
5. vector evaluation + pairwise/Pareto analysis;
6. blind-reader and adversarial review;
7. long-horizon stress at approximately 100k/300k/800k structural horizons;
8. select winner + backup;
9. create dynamic series/volume/arc/opening-packet architecture;
10. freeze first acquisition/signing packet before new prose starts.

## 5. Long-form planning principle

Do not prewrite a rigid 1.2-million-character chapter list. Plan the intended ending and irreversible transformations, then maintain variable-resolution hierarchy:
- SERIES: end state, central transformation, final value conflict;
- VOLUME: major state transitions and promise/payoff obligations;
- ARC: engine, character/relationship changes, reveal/payoff ladder;
- PACKET: near-horizon reading experience and acquisition/retention function;
- CHAPTER/SCENE: frozen only near execution.

New evidence may replan future nodes, but accepted prose and Canon require explicit reconciliation.

## 6. Evaluation principle

No single weighted quality score can authorize release or story selection.

Use:
- hard gates for identity, continuity, safety/platform constraints, source/evidence integrity and unresolved HIGH/BLOCKER defects;
- vector scores only as bounded evidence;
- Pareto front to expose non-dominated alternatives;
- pairwise tradeoff reasoning for product selection;
- live outcomes to recalibrate dimensions after publication.

## 7. Current FQ001 transition

During the active masterwork campaign:
- historical CH1–CH8 remain immutable evidence;
- old CH9 remains non-executable;
- old FQ001 profile/outline/Canon remain historical project evidence and may be used for diagnosis/benchmarks;
- no replacement prose is drafted;
- the only active content-learning cursor is GUI_CHUI_DENG source line 3914.

After campaign synthesis:
- only `SIGNING_MODE_IMMUTABLE` and `SERIALIZATION_MODE_IMMUTABLE` remain user-locked;
- title, premise, genre mix, protagonist, POV, world, character network, story engine, theme, outline and old FQ001 identity may all lose the candidate tournament;
- if historical FQ001 wins, its identity becomes active again through an explicit selection receipt; otherwise it remains historical.

## 8. Research-before-mutation rule

Material mutations—learning ontology, capability model, story selection, Rulebook promotion, Canon schema, major outline replan—require `runtime/deliberation_admission.py` evidence:
- current authority;
- internal evidence;
- external evidence when material or explicit not-material reason;
- >=2 alternatives;
- counterexample;
- challenged assumption;
- selection/rejection reasoning;
- risks and rollback/recovery.

This is the mechanical interpretation of “先学习、归类、比较、自我挑刺，再执行”。

## 9. Assurance ceiling

The system can prove:
- authority and state consistency;
- executable admission behavior;
- trajectory/regression behavior;
- source/cursor integrity;
- comparison/evaluation mechanics;
- release evidence integrity.

It cannot prove a future novel is commercially successful before live reader/platform outcomes exist. Until post-reselection prose is written and tested, the maximum claim is `SYSTEM_AND_TRAJECTORY_VERIFIED__LIVE_POST_RESELECTION_LITERARY_OUTCOME_OPEN`.
