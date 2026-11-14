# CAOS Governance Migration — Novel Writing Agent

Date: 2026-11-14  
Status: CANDIDATE_IMPLEMENTED__CI_AND_INDEPENDENT_REVIEW_PENDING  
Repository: `D1traverser-debug/novel-writing-agent`  
CAOS source: `D1traverser-debug/cognition-agent-os@main` (read-only)

## Root cause

The Novel domain still declared UAOS as its active controller in `.uaos/MANIFEST.json`, `.uaos/ADAPTER.json`, `.uaos/CAPABILITIES.json` and `UAOS_SKILL.md`. The same binding was embedded in the active Rulebook, artifact-context governance, runtime guards and the FQ001 task manifest/checkpoint. Deleting only the visible directory would have left stale task identity, recovery and audit assumptions.

The current Novel mainline already contains owner-native recovery, material-decision, root-scope, evolution, learning-transfer and zero-based story-reselection mechanisms. These are retained as Novel-owned domain gates; the migration does not copy a second cognition controller.

## Selected architecture

CAOS governs cross-project reasoning in the active ChatGPT session through the installed `cognition-parent-chatgpt-intake` Skill when available. The Novel repository remains the sole authority for Novel task identity, checkpoints, masterwork study cursor, Canon, story selection, prose/release evidence and domain evolution.

CAOS integration mode: `CHAT_GOVERNED_EXTERNAL`.

- No CAOS runtime/API dependency.
- No parent task ID, mirrored business state, lease, local daemon or automatic runtime upcall.
- CAOS does not grant write permission or replace Novel-native action/release gates.
- CAOS source repository, files, code, branches, PRs and installed Skill assets are read-only and unchanged.

## Migration changes

- Added `CAOS_NOVEL_ENTRY.md`, `config/CAOS_GOVERNANCE.json`, `config/DOMAIN_MANIFEST.json` and `config/DOMAIN_CAPABILITIES.json`.
- Removed the active `.uaos/` binding and root `UAOS_SKILL.md` from the candidate branch.
- Repointed README, Rulebook, product architecture, artifact-context governance and runtime guards to CAOS external governance and Novel-owned domain authority.
- Migrated FQ001 task manifest and checkpoint to `3.2-domain-owned`, replacing parent controller/task references with Novel-owned task identity and CAOS governance metadata.
- Preserved the owner-native Novel recovery, material-decision, root-scope, evolution, masterwork, learning-transfer and story-reselection mechanisms.
- Strengthened root-scope evidence integrity: all compared hypotheses (including rejected alternatives) are retained in the receipt; blank evidence references are rejected; manually forged or inconsistent receipts are rejected at construction and revalidated before closure.
- Historical UAOS audits, dated records and Git history remain immutable provenance, not active authority.

## Preserved business state

No changes are intended to:
- FQ001 task identity, user-locked business constraints, historical chapter hashes, Canon version or publication history;
- current stage `MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__CLAIM_CONDITIONED_LEARNING__ZERO_BASED_STORY_RESELECTION_PENDING`;
- current masterwork `GUI_CHUI_DENG`, sequential coverage through source line 3913 and resume point at source line 3914;
- the D8–D11 claim-conditioned interbook learning gate before `QING_YU_NIAN`;
- the story-reselection block and historical FQ001 no-incumbent-privilege rule.

The task manifest and checkpoint retain the same business fields; only governance/identity binding metadata and schema versions change.

## Acceptance gates

Pending:
1. Full repository CI and system/recovery/learning guards on the exact candidate head.
2. Full independent code review and security review of the migration diff.
3. Exact readback of all changed files and confirmation that active UAOS artifacts/bindings are absent.
4. Mainline CI after merge.

A green unit suite alone does not certify literary quality, live reader/platform outcomes, a new story selection or permission to write replacement prose.

## Governance

This migration changes Novel domain integration only. It does not modify CAOS source or any other domain repository. Historical UAOS records are preserved as provenance and must not be reactivated as startup instructions or execution authorities.
