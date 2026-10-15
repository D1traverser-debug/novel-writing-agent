# Novel Learning-to-Planning OS Redesign — Causal Audit

problem_ref: N-20261015-02-LEARNING_TO_PLANNING_OS_REDESIGN
status: CANDIDATE_EVALUATION
owner: DOMAIN:novel
parent: D1traverser-debug/universal-agent-os@main
updated_at: 2026-10-15T16:11:53+08:00

## 1. Trigger

User clarified the original recovery plan after Fanqie rejection:
- keep the real rejection as a hard external signal;
- learn the user-provided 20+ works one by one and in full source order;
- after learning, plan the novel again from the beginning;
- the system itself may be rebuilt if a better architecture exists;
- every material step should first learn broadly, classify, compare, challenge itself and only then execute.

The audit was therefore not scoped to incremental craft-rule repair. It reopened the learning architecture, post-learning story-selection architecture and long-form production architecture.

## 2. Baseline facts preserved

Production baseline before this candidate:
- Novel main: `fc0108383d6a8f5c8318ce6c4440c9115680ee60`;
- previous owner CI #291 PASS;
- three works complete: SHIRI_ZHONGYAN, GUI_MI_ZHI_ZHU, DAO_MU_BI_JI;
- GUI_CHUI_DENG active but explicitly paused after source line 3913;
- only valid resume location: source line 3914, Jingjue Gucheng CH26;
- QING_YU_NIAN pending;
- NORWEGIAN_WOOD excluded by user;
- FQ001 old prose/CH9 held;
- user-locked business constraints remain only SIGNING_MODE_IMMUTABLE and SERIALIZATION_MODE_IMMUTABLE.

No content cursor was advanced during this system redesign.

## 3. Initial diagnosis

The existing system already had strong pieces:
- exact source/cursor binding;
- substantive per-work ledgers with positive/negative evidence and counterfactuals;
- release evidence guards and historical hash preservation;
- explicit generic-signing-rejection inference boundary;
- owner-native problem/recovery admission from UAOS Common Behavior 1.2.

The main product-level gaps were:
1. all cross-work synthesis was deferred until the whole corpus ended, producing excessively late learning feedback;
2. reading evidence was stronger than transfer evidence: a good ledger did not prove a mechanism could be reconstructed or applied later;
3. old FQ001 identity was still strongly present in Rulebook/Profile despite a stated future story-reselection intention;
4. long-form architecture remained more static than an evidence-driven variable-resolution plan should be;
5. quality evaluation could still collapse too much into checklists/implicit aggregate judgment rather than explicit multi-dimensional tradeoffs;
6. Plan, Canon, learning and outcome boundaries were present in pieces but not one unified product architecture;
7. the user's required research/compare/challenge-before-mutation discipline was not itself mechanically represented for material Novel decisions.

## 4. External method research used

Research was not treated as direct Novel authority; it informed alternatives and counterexamples.

### Fanqie first-party/current platform evidence
Reviewed current official material covering:
- signing evaluation opportunities around the 20k/50k/80k stages;
- opening/acquisition, character, worldbuilding, outline/pacing and self-check guidance;
- platform governance against low-quality/mass-produced AI content.

Conclusion: platform fit must be refreshed at the time of actual reselection/signing; current official guidance is evidence for acquisition/product constraints, not a universal literary formula.

### Long-form AI / narrative systems
Reviewed recent work including:
- DOME: dynamic hierarchical outlines + structured temporal memory;
- IS-CoT: dynamic Plan-Write-Reflect;
- CritiCS: collective critic/iterative revision;
- WSE-bench: consistency, coverage and richness are distinct and can form non-convex tradeoffs;
- LitVISTA: current LLM evaluation often overweights local causal coherence and undercaptures global narrative orchestration;
- NarraBench and structured/graph memory work.

Conclusion: use dynamic hierarchy, structured state/dependency memory, multi-dimensional evaluation and bounded critique; do not assume more rigid planning or more consistency automatically means better fiction.

### Learning science
Reviewed retrieval-practice, interim retrieval and transfer/interleaving research.

Conclusion: full sequential reading should be preserved, but each completed work should be followed by compressed reconstruction, comparison and transfer instead of waiting until the final corpus item to discover a biased learning frame.

### Narratology / stylometry / correlated evidence
Reviewed narratology distinctions among story/discourse/narration, computational character/relationship work, authorship/stylometry confounds, and statistical handling of non-independent observations.

Conclusion: author, series and genre cannot be universal fixed evidence weights. Dependence is claim- and dimension-specific.

## 5. Alternatives considered

### A — Keep existing protocol and only finish all books
Rejected as insufficient. Preserves clean sequential reading but delays corrective comparison and transfer testing until the end.

### B — Mix multiple full books during active reading for constant interleaving
Rejected. It increases context contamination and makes exact per-work cold-read/coverage evidence harder to preserve. Interbook learning belongs after a work completes, not inside the active fulltext pass.

### C — Finish each book, then compare, but promote rules immediately
Rejected. Early completed books would dominate before genre/structure diversity and negative evidence accumulate.

### D — Fixed evidence families by author/series/genre
**Implemented briefly in this candidate, then rejected after user challenge.** It was an over-compression error. Same-author works can differ materially in structure, POV, world, character network, revelation, pacing and prose; same-series stages can also be valuable controlled contrasts. A fixed family key loses these distinctions and confuses correlation with equivalence.

### E — Claim-conditioned multidimensional dependency graph
Selected. For each mechanism claim, identify target narrative dimensions, observations, comparison design, shared factors/confounds, support/contradiction/boundary evidence, alternative explanations and transfer probes. Author/series/genre/etc can be either confounds or useful controls depending on the claim.

### F — Keep historical FQ001 as mandatory identity and only rewrite opening
Rejected. It violates the user's intent to learn first and then re-plan from zero, and creates incumbent bias.

### G — Throw away all old FQ001 material
Rejected. Published/final text, generic platform rejection, Canon and prior design are valuable historical evidence and benchmarks. They should lose execution privilege, not evidentiary value.

### H — Static full-series outline before drafting
Rejected. Useful end-state constraints are retained, but million-character chapter-level rigidity creates false confidence and expensive downstream invalidation.

### I — Dynamic hierarchical outline with evidence-driven replan
Selected: series/volume/arc/packet/chapter/scene, variable resolution by horizon, hard evidence to reopen near/frozen structure, impact-scoped invalidation.

### J — One scalar quality score
Rejected. It hides tradeoffs among acquisition, attachment, consistency, richness, pacing/orchestration, originality and production risk. A hard-gate failure cannot be averaged away.

### K — Vector + Pareto/pairwise evaluation
Selected. Hard gates remain authoritative; vector evidence exposes tradeoffs; live outcomes later recalibrate the system.

## 6. Candidate architecture implemented

Product chain:
`LEARNING EVIDENCE -> ZERO-BASED STORY TOURNAMENT -> DYNAMIC PLAN -> STORY/CANON DEPENDENCY GRAPH -> CONTEXT+PROSE -> VECTOR/MULTI-ROLE REVIEW -> RELEASE/CANON RECONCILIATION -> LIVE OUTCOME -> EVENT-DRIVEN REPLAN/EVOLUTION`

New/changed executable surfaces include:
- `runtime/deliberation_admission.py`
- `runtime/learning_transfer_admission.py`
- `runtime/story_reselection_admission.py`
- `runtime/dynamic_outline.py`
- `runtime/story_dependency_graph.py`
- `runtime/narrative_evaluation.py`
- `runtime/learning_planning_system_guard.py`

New evidence/state surfaces include:
- `protocols/NOVEL_PRODUCT_ARCHITECTURE.md`
- `protocols/MASTERWORK_DISTILLATION_PROTOCOL.md` 2.1
- `protocols/NOVEL_MASTERY_MODEL.md` 2.0
- `protocols/ACTIVE_RULEBOOK.md` 2.5
- `research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json`
- `research/masterworks/CORPUS_MAP.json` 2.0
- `research/masterworks/CROSS_WORK_LEARNING_STATE.json` 1.1
- `research/masterworks/MECHANISM_REGISTRY.json` 2.0

Novel capability profile candidate moves from Profile 4 to Profile 5.

## 7. Important failed path preserved

### FIXED_EVIDENCE_FAMILY_OVERCOMPRESSION
Sequence:
1. first redesign correctly noticed that raw book count is not automatically independent evidence;
2. implementation then overcorrected by creating fixed `evidence_family_id` values for same-series/same-author clusters;
3. user challenged the assumption: same author does not imply identical style/world/character arrangement/structure;
4. material mutation paused;
5. external narratology/stylometry/correlated-data research was expanded;
6. fixed families were removed from CORPUS_MAP, runtime comparison and mechanism registry;
7. all bootstrap mechanisms were downgraded from EXPERIMENTAL back to REFERENCE pending retroactive dependency-aware review;
8. regression tests were rewritten to explicitly prove that within-author and within-series contrasts can be valid evidence designs.

This failure remains part of the causal record and must not be rewritten as if the selected architecture existed from the beginning.

## 8. Tool/maintenance issue preserved

`TOOL_FRESHNESS_409_NO_SIDE_EFFECT`:
- an update to `tests/test_learning_transfer_admission.py` initially used a stale blob SHA;
- GitHub rejected the write with 409;
- no repository state was overwritten;
- the candidate file was reread and updated against the current SHA.

This is an operational freshness event, not a Novel architecture failure.

## 9. Invariants after redesign

- fulltext reading remains one work at a time;
- exact GUI_CHUI_DENG cursor remains line 3914;
- next work cannot activate before the completed-work D8–D11 cycle;
- author/series/genre/etc are never fixed independence labels;
- interim learning cannot silently become ACTIVE_RULE;
- historical FQ001 has no incumbent privilege;
- no replacement prose before corpus synthesis + story reselection + pre-draft architecture gate;
- Plan cannot silently become Canon;
- scalar quality cannot override hard gates;
- internal CI cannot be claimed as live literary/commercial outcome.

## 10. Remaining candidate verification

Before promotion:
- run recovery guard;
- authority/common-behavior guard;
- release evidence guard;
- masterwork distillation guard;
- learning-to-planning system guard;
- full pytest including deliberate rejection trajectories;
- inspect PR diff for stale fixed-family and incumbent-identity language;
- merge only after candidate CI passes;
- run production main CI;
- close this evolution with event-scoped production evidence;
- refresh UAOS parent Novel observation if it caches the old Profile 4 assurance.

## 11. Assurance boundary

Successful CI can prove executable architecture/trajectory/state contracts. It cannot prove the future selected novel will sign, retain readers or earn revenue. The live literary outcome remains open until post-reselection material reaches real reader/platform evaluation.
