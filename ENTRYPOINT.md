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
- relationship: system rules, QA, orchestration, mastery learning and evolution apply to the active project; project Canon, chapter, publication and story state remain project-scoped.

Continuation routing:
- `继承小说系统` / `继续小说系统` / `恢复小说系统` / `NOVEL_OS` / `Novel Writing Agent` route to this owner and then automatically recover the current `active_project_task_id`.
- A user should not be forced to select the active project again when exactly one authoritative active project is bound.
- Explicit project continuation still routes directly to that project.
- Bare continuation discovery exposes the resumable USER project according to Universal Continuity rules; presentation may include the system context, but it must not manufacture a second duplicate task for the same work.
- If multiple active projects exist in the future, the owner must resolve an explicit project hint or present project choices; it must never merge project state.

System evolution and project execution are therefore **logically coupled but state-layered**: system-level rules may change how subsequent project work is executed, while project chapter/Canon/publication state must not be overwritten by system-maintenance metadata.

## Authority
After cutover acceptance, this repository `main` is the sole authoritative business home for novel system rules, Canon, prose, contracts, QA state and project checkpoints.

Universal Continuity owns discovery, routing, compatibility and the single-writer `resume_epoch / active_lease`. The novel owner owns system-to-project routing semantics and project business truth.

System craft authorities are layered:
- `protocols/ACTIVE_RULEBOOK.md`: compact production/review rules;
- `protocols/NOVEL_MASTERY_MODEL.md`: competency ontology, learning-source hierarchy, L0–L4 mastery evidence and benchmark requirements.

Project architecture is not Canon. During the current FQ001 rebase, `projects/FQ001_MINGRI_ORDER/outline/SERIES_MASTER_OUTLINE.md` is the active series/volume/arc architecture authority. `outline/ARC_001.md` is superseded historical planning evidence and must never be resumed as executable chapter numbering.

Google Drive `/ChatGPT/NOVEL_OS_小说系统_交付归档` is a non-authoritative vault for derived DOCX, cover/platform evidence and historical migration ZIP snapshots only. The old ChatGPT Library novel execution tree has been removed. Notion and any legacy Google Drive novel materials are decommissioned as execution/recovery sources and must never override or reconstruct GitHub business truth.

Chat history and model memory are never execution authority.

## Recovery order
1. Resolve the system/project route from `continuity/TASK_INDEX.json` and `CONTINUITY_ADAPTER.json`. For a system alias, bind to the authoritative `active_project_task_id`.
2. Read Universal task manifest `D1traverser-debug/universal-continuity-agent@main/tasks/FQ001_MINGRI_ORDER/TASK_MANIFEST.json`.
3. Verify this chat owns the current `active_lease` and `resume_epoch` before any material project-state write.
4. Read `AUTHORITY_STATUS.json`.
5. Read `PROTOCOL.md`, `SKILL.md`, `CONTINUITY_ADAPTER.json`, `continuity/UNIVERSAL_PROTOCOL_ADAPTER.json` and `continuity/EXECUTION_CAPABILITIES.json`.
6. Read `protocols/NOVEL_MASTERY_MODEL.md` for architecture/rebase/system-evolution work; for ordinary prose execution load only relevant distilled competency slices rather than the whole file.
7. Read `projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json`.
8. Read `projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md`.
9. Read `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`.
10. Read `projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md`.
11. If `production_mode=FULL_FRONT_ARC_REBASE`, read `projects/FQ001_MINGRI_ORDER/outline/SERIES_MASTER_OUTLINE.md`, `audits/NOVEL_MASTERY_EVOLUTION_2026-10-11.md`, `audits/FULL_REBASE_LEARNING_EVIDENCE_2026-10-11.md` and `audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md` before prose work. Treat `outline/ARC_001.md` and `audits/FRONT_ARC_SIGNING_REPAIR_MATRIX_2026-10-11.md` as superseded history only.
12. Read `projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md`; if it is superseded/held, do not execute it as the next chapter.
13. Load only relevant Canon ledgers and the old FINAL/scenes explicitly selected by the active architecture. Do not preload all historical prose/research simply because it exists.
14. Run `runtime/recovery_guard.py`.
15. Continue the exact project `current_stage / next_action`; never silently fall back to old CH9, old ARC_001 numbering or the superseded targeted-patch plan.

## Current execution truth
- Project status: ACTIVE.
- Production mode: `FULL_FRONT_ARC_REBASE`.
- Current architecture authority: `outline/SERIES_MASTER_OUTLINE.md`.
- Competency/mastery authority: `protocols/NOVEL_MASTERY_MODEL.md`.
- CH1–CH7: historically user-confirmed published on Fanqie; internal rebase does not infer withdrawal/replacement.
- CH8: historical FINAL_ACCEPTED / PUBLISH_READY; external publication remains NOT_CONFIRMED.
- CH1–CH8 old FINALs/hashes: `IMMUTABLE_HISTORICAL_BASELINE`; preserved as business evidence/source material, not binding active chapter architecture.
- Old CH9 contract: `SUPERSEDED_BY_FULL_FRONT_ARC_REBASE`; do not write it next. Its strongest Xu Zhiwei verification-relationship design is migration source for the new front arc.
- Old `outline/ARC_001.md`: `SUPERSEDED_BY_SERIES_MASTER_OUTLINE_FOR_ACTIVE_REBASE`; historical planning evidence only.
- First Fanqie signing attempt: rejected for generic signing-quality insufficiency; do not infer a hidden AI/safety/plagiarism cause.
- Second signing attempt: blocked until the replacement packet passes `SIGNING_READINESS_AUDIT`.
- Current work must demonstrate project-level mastery evidence for the architecture-critical competencies before architecture freeze; a file/CI PASS is not equivalent to L3/L4 craft mastery.
