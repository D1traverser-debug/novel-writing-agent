# Masterwork Queue Transition Generalization — 2026-10-11

status: IMPLEMENTED_PENDING_CI_EXECUTION_OBSERVATION
scope: NOVEL_WRITING_AGENT masterwork learning queue transition
trigger: User explicitly continued after GUI_MI_ZHI_ZHU completion, activating DAO_MU_BI_JI.

## Failure model

The prior guard/test implementation correctly added a completed-current-work stop state for GUI_MI_ZHI_ZHU, but it still encoded `GUI_MI_ZHI_ZHU` and its next book as constants in the generic masterwork state machine. A valid queue transition to DAO_MU_BI_JI therefore made the persistence authority correct while deterministic validation would incorrectly reject it.

Root cause: queue-instance identity was embedded in reusable runtime/test invariants.

Classification: OWNER_LOCAL_RUNTIME_AND_TEST_DEFECT with recovery/persistence propagation impact. No Universal protocol or account/startup instruction change is required.

## Alternatives considered

1. Add a DAO_MU_BI_JI special case beside the GUI_MI_ZHI_ZHU special case — rejected because every future book would require another patch and would preserve the defect class.
2. Create a new queue-transition policy/registry — rejected because STUDY_STATE already owns current-work and queue truth; a parallel authority would increase drift.
3. Derive the current binding dynamically from `STUDY_STATE.active_work` and require queue/registry/index agreement — accepted as the smallest reusable fix.

## Implemented change

- `runtime/masterwork_distillation_guard.py` now derives the current work from `STUDY_STATE.active_work` instead of a hard-coded title.
- It requires exactly one queue ACTIVE row for an in-progress current work, validates current source/ledger bindings, requires registry active-study agreement, and checks all queue COMPLETE works are represented in completed studies.
- `runtime/recovery_guard.py` now validates project/checkpoint/index state against the dynamic current work.
- `tests/test_masterwork_distillation.py` and `tests/test_recovery_contract.py` now exercise generic queue binding plus the concrete current DAO_MU_BI_JI first-volume checkpoint.
- No new permanent authority surface or Agent was added.

## Counterexamples / held-out checks

- A stale index still naming GUI_MI_ZHI_ZHU while StudyState names DAO_MU_BI_JI must fail.
- Two queue rows marked ACTIVE must fail.
- An ACTIVE current work also listed as completed must fail.
- A prior COMPLETE book disappearing from the completed registry must fail.
- A terminal current binding may exist only with no queue ACTIVE row and must remain distinct from the next PENDING work.

## Current business safe point

- SHIRI_ZHONGYAN: COMPLETE
- GUI_MI_ZHI_ZHU: COMPLETE
- DAO_MU_BI_JI: ACTIVE
- DAO coverage: 《七星鲁王宫》CH1–CH29 complete
- next: 《怒海潜沙》第一章《蛇眉铜鱼》
- GUI_CHUI_DENG: PENDING

## Assurance boundary

Repository writes and deterministic code structure establish the intended state/validation wiring. CI execution must be observed separately; prior GitHub Actions jobs had runner-start failures (`runner_id=0`, empty steps), which must not be reported as guard/test execution.
