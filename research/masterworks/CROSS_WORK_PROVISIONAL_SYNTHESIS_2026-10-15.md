# Cross-work Provisional Synthesis — 2026-10-15

status: REFERENCE_ONLY__RETROACTIVE_CLAIM_CONDITIONED_REVIEW_REQUIRED
authority: LEARNING_EVIDENCE_ONLY
campaign: FQ001_POST_REJECTION_REBUILD_2026
completed source evidence: SHIRI_ZHONGYAN + GUI_MI_ZHI_ZHU + DAO_MU_BI_JI
partial challenge evidence: GUI_CHUI_DENG through source line 3913 only
promotion boundary: nothing in this file is ACTIVE_RULE or PROJECT_PROVEN

## 1. Why comparison started before the whole queue ended

The old policy deferred all cross-work synthesis until every book was complete. That reduced premature rule promotion, but created a different risk: twenty-plus books could be read through a biased observation frame before the first serious cross-work correction.

The corrected topology is:
- fulltext reading remains one work at a time;
- after each completed work, compact reconstruction and comparison occur before queue advance;
- comparison is non-promotional during the campaign;
- contradictions update future observation axes;
- formal rule promotion and zero-based story reselection remain blocked until campaign synthesis.

## 2. Important self-correction: the first comparison model was too coarse

The first candidate redesign incorrectly tried to model evidence independence with fixed `evidence_family_id` values such as same-author or same-series clusters. The user challenged this directly: the same author may change style, world, character organization, POV, temporal design, revelation architecture and other dimensions between works.

That challenge exposed a real modelling error.

The corrected rule is now:

**Evidence dependence is claim-conditioned and dimension-specific. Author, series, genre, POV, market, period, translation/edition, length and topic are potential shared factors—not automatic merge keys, weights or votes.**

Examples:
- two works by the same author can be an excellent `WITHIN_AUTHOR_CROSS_WORK` contrast when the claim concerns structural variation;
- two volumes in the same series can reveal engine or character evolution while holding much world context constant;
- same-genre works by different authors can challenge an author-specific explanation;
- different genres with the same narrative function can test whether a mechanism transfers beyond surface trope.

Therefore all mechanisms below were downgraded to `REFERENCE` pending retroactive review using `NARRATIVE_EVIDENCE_SCHEMA.json` and `runtime/learning_transfer_admission.py`.

## 3. Bootstrap mechanism hypotheses — REFERENCE only

### M001 — ANSWER_EXPANDS_MODEL
Observed candidate: a reveal can both pay an existing question and force a higher-level model of the story.
Target dimensions: story causal engine; information/revelation; serial payoff.
Boundary: endless question replacement without meaningful payoff becomes mystery debt.

### M002 — BOUNDED_EPISTEMIC_COMPETENCE
Observed candidate: compelling intelligent characters often form revisable models under limited information rather than being simply correct.
Target dimensions: POV/focalization; character agency; information architecture.
Boundary: central-genius patterns can flatten ensemble agency and suspense.

### M003 — DISTRIBUTED_OPERATIONAL_INTELLIGENCE
Observed candidate: ensembles gain story value when characters control different actionable knowledge, access, risks or judgment.
Target dimensions: character agency; relationship network; information architecture.
Boundary: distinct voices do not compensate for identical decision functions.

### M004 — WORLD_RULES_MUST_CHANGE_ACTION
Observed candidate: lore/profession/history/worldbuilding earns page cost when it changes choice, route, risk, resource, relationship or hypothesis.
Target dimensions: causal engine; world/institutions; page-cost.
Boundary: accurate explanation can still reduce momentum when it does not alter action.

### M005 — RELATIONSHIP_ADHESION_REQUIRES_COST
Observed candidate: shared risk, debt, trust revision, independent choice and reciprocal consequence may produce stronger relationship adhesion than declared closeness or banter alone.
Target dimensions: relationship arcs; reader affect.
Boundary: repeated one-way rescue can create an automatic solution device rather than mutual attachment.

### M006 — ENGINE_ROTATION_WITH_CONTINUITY
Observed candidate: long serials may sustain attention by changing local engines while preserving larger promises and character continuity.
Target dimensions: causal engine; pacing/orchestration; serial escalation/payoff.
Boundary: rotation can feel like genre reset if reader contract continuity breaks.

## 4. Negative / boundary evidence

### N001 — PROCEDURAL_RIGOR_PAGE_COST
FQ001's generic signing rejection is a real live outcome signal, but not a proven causal diagnosis. The old packet visibly emphasized causal verification, continuity safety, access realism and time/space precision; whether those features caused the rejection remains underdetermined.

### N002 — CENTRALIZATION_RISK
If one protagonist owns nearly every useful inference, secondary characters can become replaceable even when dialogue differs.

### N003 — MYSTERY_DEBT
Reframing only works if old promises are periodically paid. Continuous enlargement without payoff can create cognitive debt.

### N004 — REALISM_AS_TOOL
Institutional/spatial/technical realism has value when it changes consequence or choice. Precision can become homework when it consumes bandwidth without narrative return.

### N005 — SURFACE_IS_NOT_MECHANISM
Rule games, tombs, occult systems, secret organizations, specific powers and recognizable author voice are contexts/surfaces, not automatically transferable craft mechanisms.

## 5. Observation axes for remaining works

These are provisional axes, not a rigid checklist. Future works can add/remove axes when evidence warrants:
1. first-screen / first-20k reader contract;
2. time-to-first durable relationship engine;
3. payoff density versus mystery debt;
4. local-engine rotation versus identity continuity;
5. emotional aftershock;
6. protagonist competence versus secondary-character agency;
7. explanation density/page-cost;
8. ordinary-life texture and attachment;
9. mid-series fatigue/recovery;
10. ending pressure on middle design;
11. ablation/counterfactual loss;
12. transfer across materially different genre/surface;
13. discourse time/order and narrator/focalization;
14. world/institution consequence;
15. character-network structure;
16. reader-memory/cognitive-load management.

## 6. What remains unresolved

This bootstrap does NOT decide:
- final genre/premise;
- whether historical FQ001 survives story reselection;
- universal chapter formulas;
- universal protagonist design;
- author-style rules;
- that three completed works constitute independent proof;
- that the visible FQ001 weaknesses caused the Fanqie rejection.

Before any mechanism becomes EXPERIMENTAL, it needs a claim-conditioned comparison receipt that names target dimensions, shared factors, comparison design, support/contradiction/boundary evidence and alternative explanations, followed by a transfer probe.
