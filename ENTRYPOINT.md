# Novel Writing Agent — Entry Point

Status: ACTIVE
System identity: `NOVEL_OS`
System display name: `小说系统`
Domain owner: `D1traverser-debug/novel-writing-agent@main`
Domain: `NOVEL`
Continuity contract: Universal Continuity v3.7
Active project task: `FQ001_MINGRI_ORDER`

## System / project topology

`NOVEL_OS` is the durable novel-production system and `NOVEL_WRITING_AGENT` is its domain owner. Concrete novels are project tasks owned by this system; they are not parallel substitutes for the system.

Current topology:

- system: `NOVEL_OS` / 小说系统
- active project: `FQ001_MINGRI_ORDER` / 《凌晨零点，我接到明天的订单》
- relationship: system rules, QA, orchestration and evolution apply to the active project; project Canon, chapter, publication and story state remain project-scoped.

Continuation routing:

- `继承小说系统` / `继续小说系统` / `恢复小说系统` / `NOVEL_OS` / `Novel Writing Agent` route to this owner and then automatically recover the current `active_project_task_id`.
- A user should not be forced to select the active project again when exactly one authoritative active project is bound.
- Explicit project continuation still routes directly to that project.
- Bare continuation discovery exposes the resumable USER project according to Universal Continuity rules; presentation may include the system context, but it must not manufacture a second duplicate task for the same work.
- If multiple active projects exist in the future, the owner must resolve an explicit project hint or present project choices; it must never merge project state.

System evolution and project execution are therefore **logically coupled but state-layered**: system-level rules may change how subsequent project work is executed, while project chapter/Canon/publication state must not be overwritten by system-maintenance metadata.

## Authority
After cutover acceptance, this repository `main` is the authoritative business home for novel system rules, Canon, prose, contracts, QA state and project checkpoints.

Universal Continuity owns discovery, routing, compatibility and the single-writer `resume_epoch / active_lease`. The novel owner owns system-to-project routing semantics and project business truth.

ChatGPT Library is a backup / derived-artifact store after cutover. DOCX, render images and ZIP snapshots may remain there, but never override repo Markdown/JSON.

Chat history and model memory are never execution authority.

## Recovery order
1. Resolve the system/project route from `continuity/TASK_INDEX.json` and `CONTINUITY_ADAPTER.json`. For a system alias, bind to the authoritative `active_project_task_id`.
2. Read Universal task manifest `D1traverser-debug/universal-continuity-agent@main/tasks/FQ001_MINGRI_ORDER/TASK_MANIFEST.json`.
3. Verify this chat owns the current `active_lease` and `resume_epoch` before any material project-state write.
4. Read `AUTHORITY_STATUS.json`.
5. Read `PROTOCOL.md`, `SKILL.md`, `CONTINUITY_ADAPTER.json` and `continuity/EXECUTION_CAPABILITIES.json`.
6. Read `projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json`.
7. Read `projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md`.
8. Read `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`.
9. Read `projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md`.
10. Read `projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md`.
11. Load only relevant ledgers under `projects/FQ001_MINGRI_ORDER/canon/`, recent FINAL chapters and valid reviews.
12. Run `runtime/recovery_guard.py`.
13. Continue exact project `current_stage / next_action`; never replay completed chapter work.

## Current execution truth
- CH1–CH7: user-confirmed published on Fanqie.
- CH8: FINAL_ACCEPTED / PUBLISH_READY; external publication NOT_CONFIRMED.
- CH9: READY.
- Current project status: WAITING for the user's external publication confirmation of CH8.
