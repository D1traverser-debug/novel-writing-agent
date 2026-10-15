# UAOS authority and behavior repair — 2026-10-15

Status: CANDIDATE_REPAIR
Owner: DOMAIN:novel
Problem ref: N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR

## Trigger
A UAOS total-controller audit of the Novel domain found that current domain binding files and README identify `D1traverser-debug/universal-agent-os@main` as the only control plane, while `protocols/ACTIVE_RULEBOOK.md` still named the retired `universal-continuity-agent@main` and required `active_lease + resume_epoch` before material writes.

The same audit observed that production main `e84a99ce3643ffd29df40884a9924a7e8f548778` had a failed historical push validation (#275 / run 38539165735), while the newest successful main validation visible at the time was run #175 on commit `f0e7357b4eb95ef7b754c7b7bd7f7584734f7172`.

## CI reproduction correction
A fresh PR baseline was then created directly from that same current main, with only this diagnostic audit added. PR run #276 / `38675471138` passed the existing recovery guard, release-evidence guard, masterwork-distillation guard and owner contract tests.

Therefore #275 is preserved as a historical failed/stale production validation event, but it is **not** evidence that the current code tree still fails the old validation suite. The repair must not misclassify a non-reproducible historical red run as a current runtime defect.

## Micro diagnosis
The real reproducible defect is authority drift: the UAOS migration updated the manifest/adapter/skill/README/runtime control model but did not mechanically forbid retired-controller execution semantics inside the active business rulebook. Existing recovery tests verify retired files are absent, but they did not verify that active authority-bearing prose is free of retired controller/lease requirements.

A second gap is behavioral adoption: the Novel capability profile declared UAOS common capability inheritance but predated Common Behavior Assurance 1.2, with no owner-native executable admission for recover-before-user-escalation / problem-to-action closure and no minimal canonical evolution-evidence entrypoint.

## Macro alignment
Novel remains domain-owned for checkpoint, Canon, research, release and learning evidence. UAOS remains the sole parent control plane. The repair uses Novel-native checkpoint/guard/audit evidence rather than copying Financial's article lifecycle or creating a second controller.

## Governing assumptions challenged
1. Removing retired controller files and updating the adapter is sufficient to prove control-plane cutover. It is not: an active rulebook can still instruct execution through the retired topology unless runtime/tests reject those semantics.
2. Declaring UAOS common-capability inheritance is sufficient operational proof. It is not: owner-native behavior evidence is required for an operational claim.
3. A historical red CI run proves the current tree is broken. It does not when a fresh exact-base reproduction passes; current conclusions must follow reproducible evidence.

## External method evidence
Declarative configuration is reliable only when intended configuration and live behavior are reconciled; authoritative state should be mechanically checked rather than inferred from one declaration surface. This repair uses that principle only as a control-method analogy, not as a claim that Novel is Kubernetes.

## Implemented candidate repair
- `protocols/ACTIVE_RULEBOOK.md` moves parent authority to UAOS, quarantines the retired controller/lease/resume-epoch model, and adds Novel-native Common Behavior 1.2 semantics.
- `.uaos/CAPABILITIES.json` advances to profile 4, declares Common Behavior Assurance 1.2 minimum, the canonical evolution entrypoint, and executable owner-native capability refs.
- `.uaos/MANIFEST.json` exposes the common behavior, evolution and behavior-admission entrypoints.
- `UAOS_SKILL.md` exposes the same authority/evidence path progressively.
- `runtime/owner_behavior_admission.py` mechanically denies avoidable user escalation without a recovery receipt and denies recommendation-only closure when an authorized repair is available.
- `runtime/authority_behavior_guard.py` rejects the old active authority requirements while allowing explicit historical-quarantine text.
- `tests/test_owner_behavior_admission.py` exercises recovery/escalation and repair-or-block trajectories.
- `tests/test_authority_behavior_contract.py` locks current authority, behavior adoption and evolution discoverability.
- `.github/workflows/validate.yml` executes the authority/behavior guard in every PR/main validation.
- `audits/EVOLUTION_INDEX.json` provides a minimal Novel-owned canonical evidence entrypoint instead of a Financial-shaped journal.

## Assurance boundary
The candidate can prove executable admission, trajectory behavior, authority consistency and CI enforcement. It cannot prove physical interception of every natural-language host response or improved live literary/business outcomes. Those remain observation claims, not release claims.
