---
name: novel-writing-agent-uaos
scope: long-form fiction production, distillation, serialization, audit and recovery
---

# Novel Writing Agent — UAOS Entry

Controller: `D1traverser-debug/universal-agent-os@main`.
Domain repository: `D1traverser-debug/novel-writing-agent@main`.

UAOS owns intent, task identity, requirements, cross-chat continuation, capability orchestration and controller action lineage. This repository owns Novel business truth: Canon, project state, research, craft rules, chapter/release artifacts and domain guards.

## Start

After UAOS resolves the exact task, load progressively:
1. `continuity/UAOS_ADAPTER.json`;
2. `continuity/UAOS_MANIFEST.json`;
3. `continuity/EXECUTION_CAPABILITIES.json`;
4. the UAOS task controller state supplied for this task;
5. the exact project business checkpoint and only the Canon/research/rule slices required by the current action.

For `FQ001_MINGRI_ORDER`, the current durable business checkpoint is `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`. The current masterwork cursor remains `GUI_CHUI_DENG` source line 3914 after verified coverage 77–3913; do not begin `QING_YU_NIAN` before the active work is complete.

Do not use chat memory, repository search results, historical continuity indexes or a second controller to reconstruct task state.

## Business authorities

Use these as distinct authorities rather than merging them into one giant prompt:
- `protocols/ACTIVE_RULEBOOK.md`: compact production/review rules;
- `protocols/NOVEL_MASTERY_MODEL.md`: competency, learning and benchmark authority;
- `projects/<task>/PROJECT_PROFILE.md`: project identity and active writing profile;
- `projects/<task>/canon/`: factual Canon ledgers;
- the active outline/architecture artifact selected by the project;
- `projects/<task>/checkpoints/CURRENT_CHECKPOINT.json`: fine-grained project business checkpoint.

Plans, hypotheses and architecture are not Canon. Research/masterwork notes are learning evidence, not automatic production rules.

## Production

Use the minimum sufficient context for each role/action. Normal production follows:
`RECOVER -> CHECK_MODE -> FREEZE_CONTEXT -> ARCHITECT+CANON -> DRAFT -> INDEPENDENT_REVIEW_FANOUT -> ISSUE_MERGE -> REVISE -> RE-AUDIT -> FINAL_PROOFREAD -> ARTIFACT_QA -> DETERMINISTIC_GUARD -> CANON_COMMIT -> RELEASE -> CHECKPOINT`.

Role separation inside one chat is not provider-attested independence. Stronger review claims require distinct execution identity/trace. A changed prose hash invalidates body-dependent review evidence.

Do not update Canon or release a candidate that has not passed the applicable contradiction, reader/retention/editorial, adversarial, proofreading, artifact and deterministic guards on the same source identity.

## Distillation and learning

Large-work distillation must preserve exact coverage/cursor/source identity, proceed sequentially where the project requires it, and produce reusable mechanism-level knowledge rather than copied wording or distinctive plot. Single-work findings remain scoped candidates until cross-work/project evidence supports promotion.

A learning source, course, web page, benchmark or model diagnosis is evidence—not authority. Promote durable craft/system changes through comparison, falsification, project benchmark and regression. Do not inflate mastery levels because documentation exists.

## External actions

Publishing/deleting/replacing platform content, signing, payment and other high-consequence external actions remain subject to the current authorization boundary. Internal reversible analysis/design/QA should proceed autonomously where allowed.

## Completion

Completion requires both UAOS task/action state and exact project business evidence. Keep historical rejected/superseded artifacts as evidence only when they are required for regression/recovery; they must not remain active execution inputs.

Do not create a parallel controller, task registry, lease system or continuation protocol inside this repository.
