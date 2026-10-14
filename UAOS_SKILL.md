---
name: novel-writing-agent-uaos-entry
version: 2.4.0-uaos-cutover
scope: 独立长篇网络小说生产、连载、审计、恢复
---

# Novel Writing Agent — UAOS Entry

Current cross-domain controller: `D1traverser-debug/universal-agent-os@main`.
Domain/business repository: `D1traverser-debug/novel-writing-agent@main`.
Adapter: `continuity/UAOS_ADAPTER.json`.

## 1. Current authority boundary

UAOS owns intent classification, task identity, cross-chat continuation, requirement scope, capability orchestration and controller checkpoints. This repository owns Novel business rules, Canon, research, project artifacts, release evidence and domain guards.

For NEW_TASK or CONTINUE, resolve through UAOS first. `FQ001_MINGRI_ORDER` is a legacy resumable task seed; on its first UAOS continuation, read `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json` once, preserve the exact GUI_CHUI_DENG cursor at source line 3914, import the durable task meaning to UAOS, then stop writing old v3.7 cross-chat controller fields.

Do not create/refresh `active_lease`, `resume_epoch` or Universal v3.7 progress receipts. ChatGPT/GitHub host controller writes use UAOS observed-HEAD CAS; Local host uses the UAOS SQLite authority. Domain project files continue to use their own business integrity/hash guards.

## 2. Business-rule source

After UAOS has resolved the exact task, use `SKILL.md` as the detailed Novel business/craft/QA rulebook **except for the legacy controller semantics superseded below**.

The following legacy statements in `SKILL.md` are RETIRED and must not execute:
- `D1traverser-debug/universal-continuity-agent` as global routing/single-writer lease authority;
- rereading a Universal task manifest to verify `active_lease.lease_id + resume_epoch`;
- pipeline step `VERIFY_LEASE` as a v3.7 lease operation;
- any requirement to emit/update a Universal v3.7 progress receipt.

Their UAOS replacements are:
- route/recover from UAOS `ENTRYPOINT.md` + `CURRENT_SYSTEM.json` + `state/TASK_INDEX.json`;
- resolve exact task identity and migration disposition before loading project state;
- verify current UAOS task authority + current Novel project checkpoint/hash evidence;
- use UAOS task/action checkpoint semantics and host-specific CAS, not old lease epochs.

Conceptually, the serialization pipeline is therefore:
`RECOVER_UAOS_TASK -> VERIFY_TASK_AUTHORITY -> CHECK_MODE -> FREEZE_CONTEXT -> ARCHITECT+CANON -> DRAFT -> INDEPENDENT_REVIEW_FANOUT -> ISSUE_MERGE -> REVISE -> RE-AUDIT -> FINAL_PROOFREAD -> ARTIFACT_QA -> DETERMINISTIC_GUARD -> CANON_COMMIT -> RELEASE -> CHECKPOINT`.

All Canon, execution-evidence, rebase, mastery, quality, signing, artifact and release gates in `SKILL.md` remain active unless explicitly superseded by a newer Novel-domain rule.

## 3. Continuation invariant for current project

For `FQ001_MINGRI_ORDER` preserve at minimum:
- current stage: `MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING`;
- active study: `GUI_CHUI_DENG`;
- verified coverage: source lines 77–3913;
- next source location: line 3914, 《鬼吹灯I-1之精绝古城》第二十六章《天砖秘道》;
- do not start `QING_YU_NIAN` before GUI_CHUI_DENG is complete;
- existing Canon/project artifacts stay in this repository and are not duplicated into UAOS as a second Canon authority.

If this source checkpoint later changes before first import, reread the latest authoritative checkpoint rather than trusting this summary.
