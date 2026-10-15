# Novel Writing Agent — Active Rulebook

version: 2.5-github
status: ACTIVE
scope: NOVEL
architecture_ref: protocols/NOVEL_PRODUCT_ARCHITECTURE.md
mastery_ref: protocols/NOVEL_MASTERY_MODEL.md
masterwork_ref: protocols/MASTERWORK_DISTILLATION_PROTOCOL.md
business_authority: D1traverser-debug/novel-writing-agent@main
parent_authority: D1traverser-debug/universal-agent-os@main

## 1. Authority and non-negotiable boundaries

- UAOS owns cross-domain intent, task identity, routing, cross-chat continuation and common behavior governance.
- This repository owns Novel learning evidence, project checkpoints, story-selection evidence, Plan/Canon/prose state, release evidence and domain evolution.
- Chat/model memory is never Canon or executable state.
- Before any material Novel action, reread the exact current Novel checkpoint and relevant authority slices.
- External publish/delete/payment/sign/compliance actions remain user-controlled unless an explicit connected action is authorized.
- Google Drive fulltext/ledgers are source/history evidence; GitHub Novel authority owns executable state.
- `universal-continuity-agent`, local leases and resume epochs are retired.

Hard separations:
`LEARNING_EVIDENCE != ACTIVE_RULE`
`STORY_CANDIDATE != ACTIVE_PROJECT_IDENTITY`
`PLAN != CANON`
`CANON != PROSE_SURFACE`
`MODEL_SELF_EVALUATION != LIVE_OUTCOME`
`ROLE_SEPARATION != ATTESTED_EXECUTOR_INDEPENDENCE`

## 2. Common behavior and material deliberation

Novel adopts UAOS Common Behavior Assurance 1.2.

Before asking the user for a plausibly recoverable dependency, inspect current authority/checkpoint/Canon/artifacts/context and materially useful external evidence. Continue with bounded uncertainty when safe.

A detected repairable problem cannot legally end as recommendation-only if the current Agent has authority/capability to fix it. Valid closure is repair executed, concrete blocker, or evidence-backed no-change.

For material mutations—learning ontology, evidence rules, project identity, story selection, Rulebook, Canon schema, large outline replan—first use `runtime/deliberation_admission.py`: authority + internal evidence + external evidence/not-material reason + alternatives + counterexample + challenged assumption + risks/recovery. Do not execute the first plausible idea.

## 3. Masterwork learning campaign

Sequential fulltext study stays one book at a time. Current queue/cursor lives in `research/masterworks/STUDY_STATE.json`.

After each completed work:
1. closed-context reconstruction;
2. choose claim + narrative dimensions;
3. choose information-maximizing comparison designs;
4. assess author/series/genre/POV/market/period/translation/etc only as claim-specific shared factors;
5. compare support/contradiction/boundary and alternative explanations;
6. update observation axes;
7. transfer to new, non-copied cases;
8. adversarial review;
9. only then advance queue.

Same-author or same-series works are never automatically merged, discounted or counted as independent. They may be high-value controlled contrasts.

Current campaign bootstrap mechanisms remain REFERENCE until dependency-aware review. ACTIVE_RULE promotion waits for formal campaign synthesis unless a separate hard external event justifies an admitted exception.

## 4. Current FQ001 phase boundary

Historical project: `FQ001_MINGRI_ORDER / 《凌晨零点，我接到明天的订单》`.

During the active masterwork campaign:
- CH1–CH8 remain immutable historical evidence;
- old CH9 is non-executable;
- historical Project Profile/Story Bible/Canon/outline are diagnostic and candidate evidence, not future mandatory identity;
- no replacement prose is written;
- GUI_CHUI_DENG remains the only active study work, paused after source line 3913; resume line 3914;
- QING_YU_NIAN remains pending until GUI_CHUI_DENG completes and its D8–D11 interbook cycle passes.

User-locked constraints: `SIGNING_MODE_IMMUTABLE`, `SERIALIZATION_MODE_IMMUTABLE`.

Everything else may be rebuilt after learning: title, premise, genre mix, protagonist, POV, world, character network, relationship structure, story engine, theme, long-form architecture and old FQ001 identity.

## 5. Zero-based story reselection

After all non-excluded works complete and formal synthesis passes:
1. refresh current Fanqie first-party rules/courses/category evidence;
2. derive transferable mechanisms + failure boundaries, not surface trope mixtures;
3. generate >=3 story-product candidates and prove every pair is materially distinct on >=2 relevant axes; do not manufacture diversity through arbitrary genre/engine quotas;
4. historical FQ001 may compete but receives no incumbent privilege;
5. vector evaluation + pairwise/Pareto comparison;
6. blind-reader + adversarial evidence;
7. long-horizon 100k/300k/800k structural stress;
8. select winner + backup;
9. establish a new Active Project Identity only after selection receipt passes;
10. no new prose before pre-draft architecture admission.

Runtime: `runtime/story_reselection_admission.py` + `runtime/narrative_evaluation.py`.

## 6. Dynamic architecture

Do not write a rigid million-character chapter list.

Use `SERIES -> VOLUME -> ARC -> PACKET -> CHAPTER -> SCENE` with variable resolution:
- far horizon: flexible hypotheses tied to intended ending;
- mid horizon: bounded architecture and obligations;
- near horizon: higher resolution; freeze only when accepted/approaching execution.

A replan requires trigger evidence, >=2 alternatives, selected/rejected reasoning, complete downstream invalidation and review. A `FROZEN` structure requires hard defect/live signal to reopen; `NEAR + FLEXIBLE` structure may still improve before acceptance. Outline replan cannot silently mutate Canon.

Runtime: `runtime/dynamic_outline.py`.

## 7. Plan / Canon / dependency integrity

Existing `projects/<task>/canon/` files remain accepted factual authority for the current active project state.

`runtime/story_dependency_graph.py` coordinates dependencies among premise, events, character/relationship state, world rules, promises, foreshadow, threads and outline nodes.

Research/Plan does not become Canon because it is plausible. Candidate/Plan → Canon requires accepted prose + acceptance evidence + Canon reconciliation. Upstream changes invalidate all semantically dependent future Plan/Context evidence before reuse; edge direction is defined by relation semantics, not by one generic graph orientation.

## 8. Production organization

Minimum sufficient specialization:
- ORCHESTRATOR: recovery, freeze, decomposition, issue merge, final gate; no self-approval;
- ARCHITECT: plan slice/scene/packet architecture;
- CANON_LIBRARIAN: factual truth and dependency impact;
- WRITER: prose from frozen Context Pack; cannot edit Canon;
- CONTINUITY_AUDITOR;
- FRESH_READER;
- RETENTION_AUDITOR;
- EDITORIAL;
- ADVERSARIAL_RELEASE: default reject until no BLOCKER/HIGH;
- QUALITY_DISCOVERY: unknown-unknown search;
- REFINER;
- COPYEDITOR/PROOFREADER;
- ARTIFACT_RELEASE_ENGINEER;
- CANON_COMMITTER.

Risk-triggered specialists: domain reality, dialogue/subtext, space/action, suspense fairness, longform, world rules, theme, foreshadow/payoff, reader memory, transition, opposition/counter-agency.

Same-session roles are `CHAT_BRIDGED` unless isolated trace proves otherwise.

## 9. Execution evidence contract

For CH9+ or any replacement promotion:
- snapshot chapter/packet contract;
- freeze Context Pack with authority commit + exact refs/hashes;
- persist role execution evidence with source hash and issue ledger;
- bind Acceptance to Context Pack/evidence hashes;
- run `runtime/release_evidence_guard.py` before FINAL_ACCEPTED/PUBLISH_READY;
- any body hash change invalidates body-dependent review evidence.

Historical CH8 remains pre-v1 legacy evidence and cannot prove a replacement candidate.

## 10. Narrative evaluation

Do not authorize story selection/release with one average score.

`runtime/narrative_evaluation.py` requires evidence-bound dimensions including acquisition, reader contract, attachment, relationships, serial sustainability, engine diversity, narrative orchestration, continuity, development/richness, mystery/revelation, emotional range, voice/prose, cognitive load, originality, platform fit and production complexity/risk.

Hard gates override averages. Numeric Pareto dominance is legal only when the compared values share the same dimension rubric and calibration scope; uncertainty is explicit and conservative. Incommensurable evidence remains a qualitative/pairwise tradeoff until re-benchmarked. Model self-evaluation cannot be a hard gate or claim fake precision.

Internal vector scores are evidence, not live literary outcome.

## 11. Scene / chapter craft

Major scenes require goal, friction/uncertainty, consequential turn/choice and at least one memorable nonfunctional person/object/body detail.

Every retained scene changes at least one: goal, knowledge, relationship, risk, resource, location, world model, moral commitment.

Avoid default `ask -> exact answer`, report/memo narration, mechanical countdowns, omniscient protagonist, exposition-terminal NPCs and repeated hook shapes.

POV/focalization, psychic distance, sensory choice and sentence rhythm serve the current scene. Do not copy masterwork author voice or manufacture typos to look human.

## 12. Character / relationship / opposition

Characters need independent goals, information, costs, competencies, blind spots and actions. Supporting characters must still want/do something if protagonist disappears.

Track relationship deltas: trust, debt, power, obligation, intimacy, suspicion.

Opposition may be people, institutions, stakeholders, environment, system constraints, uncertainty or protagonist habits; no omniscient antagonist without information path.

## 13. Mystery / world / theme

Mystery manages curiosity, suspense, surprise and source credibility. Important reveals should be surprising now but reconstructable later. Maintain payoff debt; do not replace payoff with endless new unknowns.

World rules earn page cost when they change action, risk, resources, institutions or relationships.

Theme is a pressure system of competing legitimate values expressed through costly choices, not moral summary.

## 14. Narrative orchestration / pacing / memory

Track scene/chapter/packet/arc/volume/series rhythm. Rotate local engines while preserving larger promises and identity.

Control information, relationship, emotion, ordinary life, action, mystery, world expansion, payoff and rest as separate channels. Causal rigor does not substitute for narrative orchestration.

Budget names, locations, terms, promises, exact times/numbers and distinctive objects. Reactivate memory through action/sensory/relationship/consequence rather than recap lectures.

## 15. Space / reality / research

Actionable geography uses POV position, blockers/visibility, goal/threat and stable anchors. Environment should affect route, resource, choice, risk, emotion or clue.

Professional/institutional precision has truth burden and page-cost burden. Verify access/liability/workload/privacy where plot depends on it; do not give ordinary protagonists convenient protected data.

## 16. Revision hierarchy

Fix in order:
1. product/premise;
2. series/volume/arc/packet architecture;
3. character/relationship/opposition;
4. scene engine;
5. rendering/POV/emotion/dialogue/environment;
6. prose rhythm/voice;
7. sentence/copyedit.

Do not line-edit a structural failure. At a stable structural level, default max two evaluator→optimizer rounds before escalating diagnosis.

## 17. Fanqie and live outcome

A signing attempt is high-value external evidence, not a milestone to consume automatically.

Before application, refresh official current thresholds/guidance and audit opening, pacing, character setup, immersion, mainline and signing packet. A generic rejection proves the submission did not pass the quality evaluation; it does not prove AI detection, plagiarism, safety or a single editor-side cause.

Replacing already published chapters remains user-controlled.

## 18. Release gate

Before “可以发布/上传”, same FINAL hash must pass applicable:
- contract/plan/Canon checks;
- continuity;
- Fresh Reader;
- retention;
- editorial;
- adversarial release;
- title/first-screen/end appetite;
- emotion/attachment;
- prose/template scan;
- cross-chapter engine/repetition;
- length/page-cost where applicable;
- Quality Discovery;
- current platform risk;
- domain reality;
- project identity of the selected winner;
- final proofread;
- deterministic guards;
- release evidence guard;
- same-source artifact/render/text parity;
- Canon reconciliation.

BLOCKER=0 and HIGH=0. Numerical averages cannot override a hard gate.

## 19. Evolution / checkpoint

Checkpoint every material stage/next-action/constraint/artifact/blocker/authority change, every promotion and every external platform result.

A material problem record preserves symptom, impact, diagnosis, challenged assumptions, research, alternatives, failed/rejected paths, action, verification, residual unknowns and parent guidance when applicable.

Do not erase failed approaches after success.

## 20. Current assurance ceiling

This system may claim executable policy/trajectory verification after CI and production reread. It may not claim improved literary/commercial outcome until post-reselection work receives real reader/platform evidence.
