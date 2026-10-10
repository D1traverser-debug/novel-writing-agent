# Novel Writing Agent — Entry Point

Status: ACTIVE
Domain owner: `D1traverser-debug/novel-writing-agent@main`
Domain: `NOVEL`
Continuity contract: Universal Continuity v3.3
Active task: `FQ001_MINGRI_ORDER`

## Authority
After cutover acceptance, this repository `main` is the authoritative business home for novel Canon, prose, contracts, QA state and checkpoints.

Universal Continuity owns only discovery, routing, compatibility and the single-writer `resume_epoch / active_lease`.

ChatGPT Library is a backup / derived-artifact store after cutover. DOCX, render images and ZIP snapshots may remain there, but never override repo Markdown/JSON.

Chat history and model memory are never execution authority.

## Recovery order
1. Read Universal task manifest `D1traverser-debug/universal-continuity-agent@main/tasks/FQ001_MINGRI_ORDER/TASK_MANIFEST.json`.
2. Verify this chat owns the current `active_lease` and `resume_epoch`.
3. Read `AUTHORITY_STATUS.json`.
4. Read `PROTOCOL.md`, `SKILL.md`, `CONTINUITY_ADAPTER.json`.
5. Read `projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json`.
6. Read `projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md`.
7. Read `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`.
8. Read `projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md`.
9. Read `projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md`.
10. Load only relevant ledgers under `projects/FQ001_MINGRI_ORDER/canon/`, recent FINAL chapters and valid reviews.
11. Run `runtime/recovery_guard.py`.
12. Continue exact `current_stage / next_action`; never replay completed chapter work.

## Current execution truth
- CH1–CH7: user-confirmed published on Fanqie.
- CH8: FINAL_ACCEPTED / PUBLISH_READY; external publication NOT_CONFIRMED.
- CH9: READY.
- Current task status: WAITING for the user's external publication confirmation of CH8.
