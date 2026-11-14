# CAOS Governance Migration — Novel Writing Agent

Date: 2026-11-15
Status: CANDIDATE — CI and independent review pending
Domain: `DOMAIN:novel`
CAOS source repository: `D1traverser-debug/cognition-agent-os`
CAOS source revision inspected: `9686cedeb3fd8171ecf70eab33aaea641217b04a`
Candidate branch: `migration/caos-governance-20261115`

## Root cause

Novel's business state was already stored in the Novel repository, but the active control surface still required the retired UAOS parent: `.uaos/MANIFEST.json`, `.uaos/ADAPTER.json`, `.uaos/CAPABILITIES.json`, `UAOS_SKILL.md`, parent controller/task references in the FQ001 manifest/checkpoint, and runtime guards that loaded those paths. The active Rulebook, product architecture and artifact governance also named UAOS as the current parent.

This created a split authority model: Novel owned the checkpoint, learning cursor, Canon and prose, while a retired external controller remained a mandatory startup and recovery dependency. Simply deleting the old files would have broken the Novel recovery and learning guards.

## Alternatives compared

1. Retain UAOS as parent and add CAOS alongside it — rejected: preserves two competing governance authorities.
2. Copy CAOS code or cognition kernel into Novel — rejected: duplicates the controller and forks the parent implementation.
3. Move Novel task identity, checkpoint, Canon, corpus cursor or prose state into CAOS — rejected: violates domain business ownership and creates a second state store.
4. Use CAOS as external ChatGPT-session cognition/governance while Novel owns all business identity/state and keeps narrow owner-native execution gates — selected.

## Selected governance model

- CAOS: complete-goal recovery, cross-layer/root-cause investigation, method research, competing alternatives, counterexample testing, decision rechallenge, execution governance, independent acceptance and cross-domain learning.
- Novel: task identity, task manifest/checkpoint, study queue/cursor, corpus and narrative evidence, story reselection, Plan, Canon, prose, release evidence, domain execution gates and evolution.
- Integration mode: `CHAT_GOVERNED_EXTERNAL`.
- CAOS runtime/API dependency: none.
- Parent task identity, business-state mirror, runtime upcall and CAOS permission grant: explicitly forbidden.
- CAOS source repository/code/branches/PRs/configuration: read-only and unchanged.

Novel's `runtime/owner_behavior_admission.py` and `runtime/deliberation_admission.py` remain narrow Novel-specific execution admission. They are not a second CAOS cognition controller.

## Changes in this candidate

- Added `CAOS_NOVEL_ENTRY.md`, `config/CAOS_GOVERNANCE.json` and `config/DOMAIN_CAPABILITIES.json`.
- Removed active `.uaos/` manifests/adapters/capability profile and `UAOS_SKILL.md`.
- Rebound README, Rulebook, product architecture, artifact governance and domain capability references to CAOS external governance.
- Replaced parent controller/task fields in FQ001 task manifest/checkpoint with CAOS governance metadata; Novel remains the task identity and business-state owner.
- Updated recovery, authority, learning-to-planning and masterwork-distillation guards to consume the CAOS governance contract and Novel-owned capability profile.
- Renamed active parent-control-plane hypothesis/review semantics to CAOS governance review; no automatic upcall was introduced.
- Replaced stale UAOS-bound tests with CAOS boundary and domain-state-preservation tests.
- Preserved historical UAOS audit records and Git history as non-executable provenance only.

## Preserved business invariants

The migration is governance-only. It must not mutate:
- FQ001 task identity `FQ001_MINGRI_ORDER`, status or current stage;
- `GUI_CHUI_DENG` study cursor, source/ledger identity or coverage;
- next sequential source location: line 3914 in 《鬼吹灯I-1之精绝古城》第二十六章《天砖秘道》;
- D8–D11 claim-conditioned interbook learning gate before `QING_YU_NIAN`;
- historical CH1–CH8 final hashes, Canon, accepted prose or release evidence;
- user-locked `SIGNING_MODE_IMMUTABLE` and `SERIALIZATION_MODE_IMMUTABLE`;
- CH8 publication uncertainty or user-controlled external publication state.

## Verification

Candidate CI must pass all workflow guards and pytest:
- recovery guard;
- authority/behavior guard;
- release evidence guard;
- masterwork distillation guard;
- learning-to-planning system guard;
- complete Novel owner contract tests.

Independent full code and security reviews must confirm:
- no active UAOS binding or runtime dependency remains;
- no CAOS code or permission path was introduced into Novel;
- no business-state, task identity, Canon, cursor, publication or external authorization was moved or changed;
- owner-native admission and all existing learning/Plan/Canon/release gates remain intact.

After clean candidate CI/review, merge this migration PR, verify mainline CI, then close any stale UAOS-only PRs as superseded. Do not report production takeover before mainline verification.
