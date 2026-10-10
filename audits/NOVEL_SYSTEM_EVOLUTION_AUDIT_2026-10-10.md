# NOVEL_OS / Novel Writing Agent — System Evolution Audit

Date: 2026-10-10
Scope: owner-local operational hygiene + evolution audit
Universal methodology profiles applied: `operational_hygiene@1.0`, `evolution@1.0`, with existing `artifact_io@1.0` authority preserved
Business task: `FQ001_MINGRI_ORDER`
Business stage changed by this audit: **NO**
Writer lease changed by this audit: **NO**

## 1. Trigger

The user explicitly requested that the novel system inspect itself using the Universal Continuity challenge / distillation / learning / evolution method.

This audit therefore treated existing novel architecture, user-suggested expectations, and the assistant's first repair ideas as candidates rather than authority. The goal was to find a concrete reliability gap, challenge plausible fixes, apply the smallest owner-local repair, and leave deterministic evidence.

## 2. Observed problems

### P1 — Process claims were stronger than execution evidence

`SKILL.md` and `protocols/ACTIVE_RULEBOOK.md` defined a strong pipeline:

`FREEZE_CONTEXT -> ARCHITECT+CANON -> WRITER -> review fan-out -> issue merge -> revise -> re-audit -> proofread -> artifact QA -> Canon commit -> release`

`continuity/EXECUTION_CAPABILITIES.json` already required frozen input refs, role-specific receipts, source hashes and an issue ledger.

But the migrated active repository did not have a mechanical release contract enforcing those receipts. `CH0008_ACCEPTANCE.md` contained aggregate gate lines such as `Fresh Reader Blind: PASS`, `Editorial: PASS`, etc., while no per-role invocation receipts or durable frozen Context Pack existed in GitHub.

Failure mode: an aggregate Acceptance file could claim every role passed without durable evidence that the role pass happened on the stated inputs/body hash.

### P2 — Context freeze was declared but not durable

The Writer was instructed to use a frozen minimum Context Pack, but there was no required per-chapter Context Pack receipt. The system therefore could not later prove exactly which owner commit, contract, Canon refs, recent chapters or rule slices were supplied.

Failure mode: long-running serialization can drift while still claiming the Context Pack was frozen.

### P3 — Chapter contract provenance was not immutable

Only the mutable `NEXT_CHAPTER_CONTRACT.md` existed. Once a later chapter becomes next, the exact contract that governed a finished chapter could be lost unless separately snapshotted.

Failure mode: Acceptance can say “contract gate PASS” without a durable immutable contract artifact for that chapter.

### P4 — Dangling Canon authority reference

`SKILL.md` pointed readers to `CANON_SNAPSHOT.json`, but the current GitHub owner has no such authoritative file. Canon truth is held in the project ledgers under `projects/<task>/canon/`.

Failure mode: a future executor could search for or recreate a duplicate snapshot authority and split Canon truth.

### P5 — Stale post-cutover provenance wording

`protocols/ACTIVE_RULEBOOK.md` still said historical protocol/research files remained in Library backup evidence even after the old Library execution tree was removed and the artifact vault moved to Google Drive.

Failure mode: stale lower-authority storage can be reintroduced into recovery reasoning.

## 3. Root cause

The GitHub cutover correctly prioritized recoverable business truth: current task state, Canon ledgers, FINAL prose, acceptance, next contract, owner routing and lease safety.

During that compaction, **process semantics migrated more completely than process-execution evidence**. The repository could describe the intended editorial organization and release gates, but it did not yet make role execution receipts and Context Pack provenance a mechanical precondition for future releases.

This is a declaration-to-enforcement gap, not a need for more permanent agents.

## 4. Candidate challenge

### Candidate A — Add more permanent reviewer Agents
**Rejected.**

Reason: current runtime does not have distinct attested execution identities for those permanent roles. More named agents would increase architecture surface without solving the evidence problem and could encourage false independence claims.

### Candidate B — Require ATTESTED_ISOLATED review for every release now
**Rejected.**

Reason: `strict_attested_isolated_reviewer` is currently `DECLARED_ONLY`. Making it mandatory would either block all serialization or pressure the system to fake isolation. Normal review remains `CHAT_BRIDGED` role-separated, with explicit assurance limits.

### Candidate C — Keep the aggregate Acceptance format and add stronger prose reminders
**Rejected.**

Reason: this repeats the failure class. A reminder cannot prove execution and is not a deterministic guard.

### Candidate D — Replay CH8 and manufacture missing historical role receipts
**Rejected.**

Reason: completed work must not be replayed solely to fabricate provenance that did not exist at the time. CH8 remains valid business history but is explicitly labeled `LEGACY_AGGREGATE_MIGRATED` with unavailable role receipts and no isolation claim.

### Candidate E — Create a new `CANON_SNAPSHOT.json` to satisfy the dangling reference
**Rejected.**

Reason: existing Canon ledgers already own the facts. Creating a new snapshot authority would duplicate/split the invariant. The reference was corrected instead.

### Candidate F — Add a new top-level release policy / giant governance document
**Rejected.**

Reason: existing authority surfaces can own the rule. The missing control is executable, so it belongs in the current Skill/Protocol/Rulebook plus runtime guard/tests rather than a parallel policy.

### Candidate G — Add one compact per-chapter execution-evidence contract with deterministic enforcement
**Accepted.**

Why it wins: smallest surface that directly closes the failure; auditable; hash-bound; compatible with current CHAT_BRIDGED execution; does not fabricate isolated assurance; testable in CI; preserves owner/business boundaries.

## 5. Accepted changes

From CH9 onward, release evidence contract v1 requires:

1. immutable chapter contract snapshot: `projects/<task>/contracts/CHxxxx_CONTRACT.md`;
2. frozen Context Pack receipt: `projects/<task>/execution/CHxxxx_CONTEXT_PACK.json` with owner commit and selected input refs/hashes;
3. `projects/<task>/reviews/CHxxxx_EXECUTION_EVIDENCE.json` containing role receipts, peer-review visibility, source hash and issue ledger;
4. Acceptance hash bindings to Context Pack and execution-evidence artifacts;
5. deterministic `runtime/release_evidence_guard.py` PASS before `FINAL_ACCEPTED / PUBLISH_READY`;
6. CI runs both recovery and release-evidence guards and the full owner test suite.

Role-separated same-session review is explicitly recorded as `ROLE_SEPARATED_NOT_ATTESTED_ISOLATED`. An `ATTESTED_ISOLATED` claim requires an actual `ISOLATED_EXTERNAL` execution identity and trace.

## 6. Regression / validation evidence

Behavioral validation head: `738625da998ad530a3af1d04e22b39cf3c1b5d16`

GitHub Actions:
- workflow: `validate-novel-owner`
- run id: `38064234066`
- job id: `114248515612`
- result: **SUCCESS**

Validated steps:
- Recovery Guard: PASS
- Release Evidence Guard: PASS
- Full owner contract tests: PASS

Synthetic negative tests prove at least these fail-closed cases:
- CH9 Acceptance without execution evidence is rejected;
- false `ATTESTED_ISOLATED` claim on a CHAT_BRIDGED receipt is rejected;
- a correctly bound frozen Context Pack + role receipt fixture passes.

## 7. Behavioral effect

Before: the repository could preserve a strong release checklist while aggregate PASS text remained sufficient evidence in practice.

After: CH9+ release promotion requires machine-checkable, source-hash-bound execution evidence. A future assistant cannot truthfully claim the required roles executed merely by writing their names into Acceptance.

The change strengthens evidence; it does **not** create genuinely independent reviewer identities. That capability remains unavailable until an external executor can produce a distinct identity/trace.

## 8. Business-state preservation

Unchanged:
- CH1–CH7 publication facts;
- CH8 FINAL body/hash;
- CH8 `FINAL_ACCEPTED / PUBLISH_READY` business status;
- CH8 external publication remains NOT_CONFIRMED;
- Canon v12;
- CH9 READY contract content;
- Universal `resume_epoch=2` and active lease.

No chapter was replayed and no Canon fact was rewritten by this system audit.

## 9. Remaining risks / future evidence boundary

1. **No true isolated reviewer executor yet.** The new receipt contract prevents false claims but does not manufacture independence.
2. **CH8 remains legacy aggregate evidence.** This is disclosed and grandfathered; the stronger standard begins at CH9.
3. **The Universal rebuildable owner-conformance registry currently caches an older novel regression head.** It is not business authority. Updating that global cache belongs to the valid Universal maintenance writer; this owner audit does not steal that lease.
4. **The new contract is not operationally proven on a real CH9 production run yet.** CI proves enforcement mechanics and negative cases. The first CH9 execution must generate real Context Pack and role receipts; only that can prove action-level operational conformance.

## 10. Stop rule

Do not add more agents, policies or review layers merely because this audit found a gap. The current reliability defect has a bounded executable repair. Resume normal serialization when the external CH8 publication boundary is cleared, and judge this evolution on actual CH9 evidence and later reader/platform outcomes.

## 11. Universal follow-up challenge — evidence-strength overclaim

The Universal maintenance writer independently re-read the release guard after the first repair and found a second-order weakness: the first repair could still be described too strongly.

The v1 guard initially proved that a receipt object existed and that reviewer FINAL rows matched the FINAL source hash, but it did **not** fully validate every local Context Pack ref/hash, did not require every CHAT_BRIDGED receipt to bind the frozen Context Pack, did not require non-empty role result summaries, and did not bind final-body pipeline roles such as proofread/artifact/canon commit to the FINAL source hash.

More importantly, one aggregate `CHxxxx_EXECUTION_EVIDENCE.json` written by the same CHAT_BRIDGED session can still be authored post hoc. More receipt files, timestamps or role names would not create independent execution provenance. Therefore the assurance claim must stay below attestation.

### Follow-up candidates

- **Force more files / one file per role:** rejected. The same session could still generate them together; file count is not independence.
- **Force ATTESTED_ISOLATED now:** rejected. The capability remains unavailable and would create either deadlock or fake assurance.
- **Strengthen what can be deterministically verified and explicitly downgrade what cannot:** accepted.

### Follow-up accepted changes

Compatible hardening of release evidence contract v1 before its first real CH9 production use:

- all local `PROJECT_PROFILE`, Canon and recent-FINAL Context Pack refs must exist and match their recorded SHA-256;
- every receipt requires a unique `receipt_id`, frozen Context Pack binding for CHAT_BRIDGED mode, and a non-empty role `result_summary`;
- final-body pipeline roles (`COPYEDITOR_PROOFREADER`, `ARTIFACT_RELEASE_ENGINEER`, `CANON_COMMITTER`) must bind the FINAL source hash;
- blinded reviewer evidence must itself carry a valid source hash and the frozen Context Pack binding;
- deterministic output now labels evidence strength as `STRUCTURED_SELF_ATTESTED_CHAT_BRIDGED_UNLESS_EXTERNAL_TRACE_PRESENT`;
- `SKILL.md` and `continuity/EXECUTION_CAPABILITIES.json` explicitly prohibit describing CHAT_BRIDGED receipts as independent proof of cognition or chronology.

New negative tests cover wrong Canon hash, missing/wrong CHAT_BRIDGED context binding, missing role result summary, and wrong final-source binding for final pipeline roles.

First hardened CI attempt (`38065104562`) failed only because an older recovery-contract test asserted the exact pre-hardening evidence-contract string. Recovery Guard and Release Evidence Guard themselves passed. The stale assertion was updated rather than bypassed.

Hardened validation head: `ced06cec1a2201135d32c7f9d8c8c32c43b83507`

GitHub Actions:
- workflow: `validate-novel-owner`
- run id: `38065144178`
- job id: `114251164978`
- result: **SUCCESS**
- Recovery Guard: PASS
- Release Evidence Guard: PASS
- Full owner contract tests: PASS

## 12. Refined evidence boundary

The correct claim after hardening is:

> CH9+ cannot reach release merely from aggregate PASS prose. It must carry deterministically verifiable, input/body-bound, role-specific structured receipts. In normal CHAT_BRIDGED mode those receipts remain self-attested execution records, not independent attestation of model cognition or non-post-hoc chronology.

True independent execution proof remains contingent on a distinct execution identity/provider trace. This is an external capability boundary, not something to simulate by adding files or role labels.
