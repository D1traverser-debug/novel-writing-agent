# Novel Writing Agent Protocol

Version: 2.0-github
Status: ACTIVE

## 1. Ownership
This repository owns NOVEL domain business state: story Canon, chapter prose, contracts, QA/release state, project checkpoints and writing protocols.

`universal-continuity-agent` owns global task discovery/routing, compatibility and the single-writer lease. It must not duplicate novel Canon or prose.

## 2. Authority order
1. User's latest explicit external fact (for example, “第8章已发布”).
2. This repository `main`: task manifest, current checkpoint/state, Canon, FINAL prose and valid hash-bound audits.
3. Derived/binary artifacts in ChatGPT Library.
4. Historical mirrors/recovery archives.
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
`ORCHESTRATOR -> ARCHITECT + CANON -> WRITER -> independent review fan-out -> issue merge -> REFINER -> re-audit -> PROOFREADER -> artifact QA -> CANON COMMITTER -> release`

Writer may not self-approve. Any body hash change invalidates body-dependent reviews.

## 6. Drift control
Writer receives a minimum sufficient Context Pack, not the entire knowledge base. New research enters quarantine and may not rewrite project identity merely because it is newer. Every release runs project identity regression.

## 7. Release invariant
“可以传/可以发布” is permitted only after all applicable hard gates explicitly PASS on the same source hash, including final proofread, deterministic guards and artifact parity/render checks.

## 8. Checkpoint discipline
Checkpoint material stage/next-action/constraint/artifact/blocker changes. Store execution truth, not transcript summaries.

## 9. Binary artifacts
DOCX, rendered page images and recovery ZIPs are derived deliverables. They may be stored outside GitHub. The authoritative source text remains repo Markdown.

## 10. Current task
Task identity: `FQ001_MINGRI_ORDER`.
Current state is defined only by `projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json` and `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`.
