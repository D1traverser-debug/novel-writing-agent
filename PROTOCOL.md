# Novel Writing Agent Protocol

Version: 2.1-github
Status: ACTIVE

## 1. Ownership
This repository owns NOVEL domain business state: story Canon, chapter prose, contracts, QA/release state, project checkpoints and writing protocols.

`universal-continuity-agent` owns global task discovery/routing, compatibility and the single-writer lease. It must not duplicate novel Canon or prose.

## 2. Authority order
1. User's latest explicit external fact (for example, “第8章已发布”).
2. This repository `main`: task manifest, current checkpoint/state, Canon, FINAL prose and valid hash-bound audits.
3. Google Drive `/ChatGPT/NOVEL_OS_小说系统_交付归档` only for explicitly needed derived/binary artifacts or historical migration evidence.
4. Decommissioned Notion / ChatGPT Library / legacy Google Drive novel materials, if encountered, as non-authoritative historical clues only.
5. Chat/model memory.

If authority is unknown or inconsistent: fail closed; do not reconstruct executable state by guess.

## 3. Single writer
Before any material business checkpoint write:
- re-read the Universal task manifest;
- require matching `active_lease.lease_id` and `resume_epoch`;
- stale writers must stop and re-inherit.

A new chat takeover increments the Universal `resume_epoch`; the old chat is retired for this task.

## 4. Autonomous scope
Internal reversible work is delegated to the ORCHESTRATOR: research, architecture, writing, review, refinement, Canon bookkeeping, tests, guard updates and artifact preparation.

External/irreversible boundaries remain user-controlled: final platform publication/deletion/replacement, payment, signing, legal/compliance declaration and other high-consequence account actions.

The user is not the QA manager and does not maintain the checklist.

## 5. Production topology
`ORCHESTRATOR -> ARCHITECT + CANON -> WRITER -> role-separated blind-first-pass review fan-out -> issue merge -> REFINER -> re-audit -> PROOFREADER -> artifact QA -> CANON COMMITTER -> release`

Writer may not self-approve. Any body hash change invalidates body-dependent reviews.

Normal same-session role separation is `CHAT_BRIDGED`; it must not be represented as `ATTESTED_ISOLATED`. A higher isolation claim requires a distinct execution identity and trace evidence.

## 6. Drift control
Writer receives a minimum sufficient Context Pack, not the entire knowledge base. New research enters quarantine and may not rewrite project identity merely because it is newer. Every release runs project identity regression.

From CH9 onward, Context Pack freeze is durable evidence, not a chat-only event: the immutable chapter contract snapshot plus `CHxxxx_CONTEXT_PACK.json` must bind the exact owner commit and selected input refs/hashes used for writing and review.

## 7. Release invariant
“可以传/可以发布” is permitted only after all applicable hard gates explicitly PASS on the same source hash, including final proofread, deterministic guards, release-evidence validation and artifact parity/render checks.

From CH9 onward, aggregate PASS prose is insufficient. A valid release must hash-bind:
- immutable chapter contract snapshot;
- frozen Context Pack receipt;
- role-level execution/review receipts;
- issue ledger with unresolved BLOCKER/HIGH = 0;
- FINAL body hash;
- Acceptance record.

`runtime/release_evidence_guard.py` is the deterministic enforcement point for this evidence contract. CH8 remains a preserved pre-v1 legacy acceptance and must not be replayed merely to manufacture receipts that never existed.

## 8. Checkpoint discipline
Checkpoint material stage/next-action/constraint/artifact/blocker changes. Store execution truth, not transcript summaries.

## 9. Binary artifacts
DOCX, rendered page images, cover/platform evidence and recovery ZIPs are derived or historical artifacts. The designated external vault is Google Drive `/ChatGPT/NOVEL_OS_小说系统_交付归档`. These artifacts never become business authority; the authoritative source text and execution state remain repo Markdown/JSON. ChatGPT Library is not a novel execution or recovery store after the 2026-10-10 cleanup.

## 10. Canon authority
Current Canon is the set of authoritative ledgers under `projects/<task>/canon/` plus accepted project state. Do not create or infer a parallel `CANON_SNAPSHOT.json` authority unless a future explicit contract introduces one with a unique non-duplicating role.

## 11. Current task
Task identity: `FQ001_MINGRI_ORDER`.
Current state is defined only by `projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json` and `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`.
