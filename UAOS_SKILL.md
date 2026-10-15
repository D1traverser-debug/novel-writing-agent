---
name: novel-writing-agent-uaos
scope: long-form fiction learning, story selection, planning, production, serialization, audit and recovery
---

# Novel Writing Agent — Current UAOS Entry

Controller: `D1traverser-debug/universal-agent-os@main`.
Domain repository: `D1traverser-debug/novel-writing-agent@main`.

UAOS owns intent, task identity, requirements, cross-chat continuation, common behavior governance, capability orchestration and controller action lineage. This repository owns Novel learning evidence, story-selection evidence, project checkpoint, Plan/Canon boundaries, prose/release evidence, craft rules and domain evolution.

## Start
After UAOS resolves the exact task, load progressively:
1. `.uaos/ADAPTER.json`;
2. `.uaos/MANIFEST.json`;
3. `.uaos/CAPABILITIES.json`;
4. UAOS task controller state;
5. the exact project checkpoint;
6. only the learning/Canon/plan/rule slices required for the current action.

For `FQ001_MINGRI_ORDER`, business checkpoint authority remains `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`. The active masterwork is still `GUI_CHUI_DENG`; verified sequential coverage stops at source line 3913 and the only prose-learning resume point is line 3914 in 《鬼吹灯I-1之精绝古城》第二十六章《天砖秘道》. Do not start `QING_YU_NIAN` until GUI_CHUI_DENG completes and its mandatory D8–D11 claim-conditioned interbook learning cycle passes.

Do not reconstruct task state from chat memory, broad repository search, retired task indexes or another controller.

## Business authorities
- `protocols/ACTIVE_RULEBOOK.md`: active production/review rules;
- `protocols/NOVEL_PRODUCT_ARCHITECTURE.md`: learning-to-outcome system architecture;
- `protocols/NOVEL_MASTERY_MODEL.md`: competency/benchmark authority;
- `protocols/MASTERWORK_DISTILLATION_PROTOCOL.md`: masterwork learning/transfer protocol;
- `research/masterworks/STUDY_STATE.json`: exact corpus queue/cursor;
- `research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json`: multidimensional comparison ontology;
- `research/masterworks/CROSS_WORK_LEARNING_STATE.json`: campaign comparison/promotion gates;
- `research/masterworks/MECHANISM_REGISTRY.json`: compact learning index, never Rulebook authority;
- `config/ARTIFACT_CONTEXT_GOVERNANCE.json`: artifact/context governance;
- `audits/EVOLUTION_INDEX.json`: canonical domain-evolution entrypoint;
- `runtime/owner_behavior_admission.py`: recovery, root-scope cognition, typed evolution and problem closure;
- `runtime/deliberation_admission.py`: research/compare/challenge admission for material mutations;
- `runtime/learning_transfer_admission.py`: closed-context reconstruction, claim-conditioned comparison, transfer and promotion admission;
- `runtime/story_reselection_admission.py`: post-campaign zero-based story-selection and pre-draft admission;
- `runtime/dynamic_outline.py`: evidence-driven hierarchical replan contract;
- `runtime/story_dependency_graph.py`: Plan/Canon dependency and invalidation contract;
- `runtime/narrative_evaluation.py`: calibrated uncertainty-bounded vector/Pareto quality evaluation;
- `projects/<task>/canon/`: accepted factual Canon;
- `projects/<task>/checkpoints/CURRENT_CHECKPOINT.json`: fine-grained business checkpoint.

## Hard separations
`LEARNING_EVIDENCE != ACTIVE_RULE`

`STORY_CANDIDATE != ACTIVE_PROJECT_IDENTITY`

`PLAN != CANON`

`CANON != PROSE_SURFACE`

`MODEL_SELF_EVALUATION != LIVE_READER_OR_PLATFORM_OUTCOME`

`ROLE_SEPARATION != PROVIDER_ATTESTED_INDEPENDENCE`

Any current execution that silently collapses these layers is a system defect.

## Common behavior / material decision discipline
Novel adopts UAOS Common Behavior Assurance 1.3 owner-natively. Before externalizing a plausibly recoverable dependency, inspect lawful authority/state/artifacts/context and materially useful external evidence. If safe bounded progress remains, continue provisionally instead of blocking.

A detected problem does not become repairable merely because a plausible edit exists. User framing, external methods and the first repairable symptom are evidence rather than root-cause authority. Before repair or evidence-backed no-change, `runtime/owner_behavior_admission.py` must produce a root-scope receipt and typed evolution disposition. A small one-off local defect may use a single-layer receipt; material, repeated, cross-subsystem, architecture-gap, complexity-growth or scope-expansion signals must compare multiple causal layers, test an architecture/upstream hypothesis and preserve a rejected alternative.

For those material/systemic problems, root-scope admission reuses the existing `MaterialDecisionReceipt` from `runtime/deliberation_admission.py`; it does not create a second deliberation system. That receipt supplies current authority, internal evidence, relevant external research (or a justified not-material reason), >=2 alternatives, counterexample, challenged assumption, rejection reasoning, risks and rollback/recovery. Root-scope then answers the distinct causal question: which Novel layer actually owns the failure?

Material/evolution-relevant problems require durable causal evidence in `audits/EVOLUTION_INDEX.json` or a linked owner-native record. A genuine user-controlled fact/authorization/publication choice may be surfaced as a blocker without fabricating a root-cause claim. An admitted, owner-authorized repair cannot terminate at recommendation-only; it must be attempted and verified or converted to a real blocker.

The problem transaction is:
`DETECT -> RECOVER WHEN APPLICABLE -> MATERIAL DELIBERATION WHEN REQUIRED -> ROOT_SCOPE_ADMISSION -> TYPED_EVOLUTION_DISPOSITION -> REPAIR / NO_CHANGE / BLOCK -> VERIFY`.

## Masterwork learning
Sequential full-text reading remains one work at a time. Cross-work comparison occurs only after a work completes, but no longer waits until the entire corpus is finished.

Evidence dependence is claim-conditioned and dimension-specific. Same author, series, genre, POV, market or period can be a confound or a useful controlled contrast depending on the claim. Never collapse same-author/same-series works into a fixed evidence vote.

Current campaign keeps interim mechanisms at REFERENCE until retroactive dependency-aware comparison verifies them; ACTIVE_RULE promotion remains blocked by the campaign/formal-synthesis gate.

## Post-study story selection
After all non-excluded works complete and formal synthesis passes, refresh current Fanqie evidence and run a zero-based story tournament. Historical FQ001 may compete only as one candidate/evidence source and receives no incumbent privilege. Candidate diversity must be proved on relevant story/product axes; broad genre/engine labels are not quotas. Only signing mode and serialization mode remain user-locked.

No new replacement prose before reselection + pre-draft architecture admission.

## Production
After a winner exists, use minimum sufficient context:
`RECOVER -> PLAN_SLICE/FREEZE -> CONTEXT_PACK -> DRAFT -> REVIEW_FANOUT -> ISSUE_MERGE -> REVISE -> RE-AUDIT -> FINAL_PROOFREAD -> ARTIFACT_QA -> RELEASE_EVIDENCE_GUARD -> CANON_RECONCILIATION/COMMIT -> RELEASE -> CHECKPOINT`.

A prose hash change invalidates body-dependent review evidence. Research cannot directly promote Canon. Plan changes require impact-scoped replanning. `NEAR + FLEXIBLE` material may improve before acceptance; only accepted/`FROZEN` structure requires hard-defect/live-signal evidence to reopen. Numeric candidate comparison requires shared rubric/calibration scope and explicit uncertainty; otherwise use qualitative/pairwise tradeoff evidence.

## Completion
System completion is not a literary-success claim. Internal tests may verify authority, admissions, state/cursor, dependency invalidation, evaluation mechanics and release evidence. Commercial/literary outcome stays open until actual post-reselection prose receives real reader/platform evidence.

Do not create a parallel controller, local task registry, lease, resume epoch or cross-chat continuation protocol in this repository.
