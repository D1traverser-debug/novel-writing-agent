# Novel Writing Agent Protocol

Version: 2.3-github
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
Internal reversible work is delegated to the ORCHESTRATOR: research, learning-evidence classification, candidate comparison, architecture, writing, review, refinement, Canon bookkeeping, tests, guard updates and artifact preparation.

External/irreversible boundaries remain user-controlled: final platform publication/deletion/replacement, payment, signing, legal/compliance declaration and other high-consequence account actions.

The user is not the QA manager and does not maintain the checklist.

## 5. Production topology
Normal serialization:
`ORCHESTRATOR -> ARCHITECT + CANON -> WRITER -> role-separated blind-first-pass review fan-out -> issue merge -> REFINER -> re-audit -> PROOFREADER -> artifact QA -> CANON COMMITTER -> release`

Full-unit rebase when durably activated:
`FREEZE_OLD_BASELINE -> CLASSIFY_SIGNAL -> EVIDENCE_SCOUT -> COMPARE/FALSIFY -> ARCHITECTURE_PROTOTYPE -> RED_TEAM -> FREEZE_REBASE_ARCHITECTURE -> WRITE_CANDIDATE_PACKET -> PACKET_QA -> ACCEPT_OR_REJECT -> PROMOTE_WITH_DEPENDENCY_INVALIDATION -> CLEAN_SUPERSEDED_ACTIVE_PATHS`

Writer may not self-approve. Any body hash change invalidates body-dependent reviews.

Normal same-session role separation is `CHAT_BRIDGED`; it must not be represented as `ATTESTED_ISOLATED`. A higher isolation claim requires a distinct execution identity and trace evidence.

## 6. Drift control / learning authority
Writer receives a minimum sufficient Context Pack, not the entire knowledge base. New research enters quarantine/`LEARNING_EVIDENCE` and may not rewrite project identity merely because it is newer. External courses, community patterns and model suggestions are candidates, not execution authority.

A hard external failure may reopen a frozen baseline, but the owner must first separate the user goal from the proposed mechanism, compare alternatives, record accepted/rejected learning evidence, and explicitly supersede the old active path.

Context Pack freeze is durable evidence when the current evidence contract applies: immutable contract/architecture snapshot plus Context Pack receipt must bind the exact owner commit and selected input refs/hashes used for writing and review.

## 7. Release / replacement invariant
“可以传/可以发布/可以替换” is permitted only after all applicable hard gates explicitly PASS on the same source hash, including final proofread, deterministic guards, release-evidence validation and artifact parity/render checks.

For current evidence-contract prose, aggregate PASS text is insufficient. A valid promotion must bind the applicable:
- immutable chapter contract / rebase architecture snapshot;
- frozen Context Pack receipt;
- role-level execution/review receipts;
- issue ledger with unresolved BLOCKER/HIGH = 0;
- FINAL body hash;
- Acceptance record.

For a multi-chapter front-arc replacement, individual chapter PASS is necessary but insufficient. The coherent packet must additionally pass cross-chapter continuity, engine diversity/pacing, character attachment, promise/progress/payoff, identity regression and signing-readiness before any authoritative replacement transaction.

`runtime/release_evidence_guard.py` is the deterministic enforcement point for the current evidence contract. Historical CH8 remains a preserved pre-v1 legacy acceptance; it cannot be replayed as evidence for a replacement candidate.

CI/regression proves recovery/enforcement wiring only. It does not prove improved literary quality, reader retention or signing outcome.

## 8. Checkpoint discipline
Checkpoint material stage/next-action/constraint/artifact/blocker changes. Store execution truth, not transcript summaries.

During `FULL_FRONT_ARC_REBASE`, checkpoint architecture freeze, candidate packet readiness and accept/reject/promotion decisions. Old FINAL/hashes remain immutable historical evidence until an explicit promotion supersedes them.

## 9. Binary artifacts
DOCX, rendered page images, cover/platform evidence and recovery ZIPs are derived or historical artifacts. The designated external vault is Google Drive `/ChatGPT/NOVEL_OS_小说系统_交付归档`. These artifacts never become business authority; the authoritative source text and execution state remain repo Markdown/JSON. ChatGPT Library is not a novel execution or recovery store after the 2026-10-10 cleanup.

## 10. Canon authority
Current Canon is the set of authoritative ledgers under `projects/<task>/canon/` plus accepted project state. Chapter boundaries/scene order are prose architecture, not Canon. Factual changes to character knowledge, event outcomes, system rules or timeline require explicit Retcon/Canon reconciliation.

Do not create or infer a parallel `CANON_SNAPSHOT.json` authority unless a future explicit contract introduces one with a unique non-duplicating role.

## 11. Current task
Task identity: `FQ001_MINGRI_ORDER`.
Current state is defined only by `projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json` and `projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json`.

At the current checkpoint, the active mode is `FULL_FRONT_ARC_REBASE`; old CH9 is superseded/held and must not be executed until the replacement front arc is accepted and a new next-chapter contract is issued.
