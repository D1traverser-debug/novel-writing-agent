# Masterwork Progress Persistence Repair — 2026-10-11

status: REPAIRED_PENDING_FINAL_HEAD_REGRESSION_CONFIRMATION
owner: NOVEL_WRITING_AGENT
task_id: FQ001_MINGRI_ORDER
scope: masterwork sequential-study recovery and persistence only

## Observed failure

A real recovery found contradictory durable evidence:

- Google Drive rolling learning ledger for `GUI_MI_ZHI_ZHU` recorded 第一部《小丑》 CH1–CH213 + volume summary complete and the next location as 第二部《无面人》 CH1.
- GitHub `research/masterworks/STUDY_STATE.json` still reported `ACTIVE__PENDING_FIRST_SEQUENTIAL_READ`.

The source-bound Drive evidence was cross-checked against the user-provided standardized source and the study queue before it was used to repair GitHub state.

## Root cause

`runtime/masterwork_distillation_guard.py` and its direct tests hard-coded the only valid active state to the initial state:

- `ACTIVE__PENDING_FIRST_SEQUENTIAL_READ`
- `SEQUENTIAL_FULLTEXT_FROM_BEGINNING`

That made legitimate progressive checkpoints fail the guard, encouraging the durable GitHub checkpoint to remain frozen at the initial state while the rolling learning ledger advanced.

A secondary drift source existed in `AUTHORITY_STATUS.json`, which duplicated dynamic `current_stage/next_action` even though project manifest/checkpoint were the declared project-state authority.

A third governance gap existed because the Drive masterwork research library was actively used as explicit user source / learning evidence but was not classified in owner artifact governance.

## Accepted repair

1. Make the masterwork guard validate progression invariants rather than one frozen initial state.
2. Make recovery/masterwork tests accept only the initial state or a properly bound sequential in-progress state.
3. Bind in-progress state to source SHA, rolling-ledger identity/hash, coverage and exact next location.
4. Classify `/Google Drive/ChatGPT/NOVEL_OS_名作蒸馏研究库` as explicit source/learning evidence only; it remains non-authoritative for task state, Canon and rules.
5. Remove duplicated dynamic task state from `AUTHORITY_STATUS.json`; project manifest/checkpoint remain the single business-state source.
6. Preserve one-book-at-a-time study, copyright/source boundaries, prose hold, signing/serialization locks and all historical FQ001 publication/Canon evidence.

## Counterexamples / second-order challenge

- A progress state without source hash, coverage, next location or rolling-ledger reference must still fail.
- A Drive ledger by itself must never override GitHub task state without explicit owner provenance and reconciliation.
- A successful deterministic guard or CI run does not prove semantic reading quality.
- A self-attested execution receipt does not become independent verification merely because it is structured.
- Stage observations from one book must not become cross-work rules before the configured queue and triangulation gates complete.
- Removing the duplicate dynamic fields must not remove the stable authority declaration itself.

## Current recovered and advanced state

Source:
- Drive file id: `1iXkVcu9gCCVKZweYVMrN8vH8jNIhbfEC`
- SHA-256: `25d76c8752e97255d8653205e44e0c12348fd50d9c68a657b3fc970d77112489`

Rolling ledger:
- Drive file id: `1Ixa5xE8iWyrGQjuJDgwBSTAQxO81hcXo`
- verified SHA-256 after current action: `4da3cdf81fb55a3bad06abce492b84f9893b661db5a142e83099b06eaf31dac8`

Coverage now:
- 第一部《小丑》 CH1–CH213 + volume summary
- 第二部《无面人》 CH1–CH60
- next: 第二部《无面人》 CH61

Exact action evidence:
- `research/masterworks/GUI_MI_ZHI_ZHU/EXECUTION_RECEIPT_2026-10-11_V2_CH31_CH60.json`

## Assurance boundary

The strongest current claims are:

- persistence/recovery wiring: deterministic/regression-verifiable;
- CH31–CH60 action record: action-level self-attested and exact-input-bound;
- stage mechanisms: single-work learning evidence only.

Not proven:

- independent semantic verification of the reading/distillation action;
- cross-work transfer validity;
- L4 mastery;
- replacement-prose quality improvement;
- Fanqie signing or reader outcome improvement.

Final closure requires the owner validation workflow to pass on the resulting `main` HEAD. No higher assurance may be inferred from that CI result.
