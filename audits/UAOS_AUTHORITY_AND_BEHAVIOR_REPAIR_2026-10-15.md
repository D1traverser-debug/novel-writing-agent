# UAOS authority and behavior repair — 2026-10-15

Status: PROMOTED__PRODUCTION_CI_VERIFIED__LIVE_BEHAVIOR_OBSERVATION_OPEN
Owner: DOMAIN:novel
Problem ref: N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR

## Trigger
A UAOS total-controller audit of the Novel domain found that current domain binding files and README identify `D1traverser-debug/universal-agent-os@main` as the only control plane, while `protocols/ACTIVE_RULEBOOK.md` still named the retired `universal-continuity-agent@main` and required `active_lease + resume_epoch` before material writes.

The same audit observed that production main `e84a99ce3643ffd29df40884a9924a7e8f548778` had a failed historical push validation (#275 / run 38539165735), while the newest successful main validation visible at the time was run #175 on commit `f0e7357b4eb95ef7b754c7b7bd7f7584734f7172`.

## CI reproduction correction
A fresh PR baseline was created directly from that same current main, with only this diagnostic audit added. PR run #276 / `38675471138` passed the existing recovery guard, release-evidence guard, masterwork-distillation guard and owner contract tests.

Therefore #275 is preserved as a historical failed/stale production validation event, but it is **not** evidence that the current code tree still failed the old validation suite. The repair did not misclassify a non-reproducible historical red run as a current runtime defect.

## Micro diagnosis
The reproducible defect was authority drift: the UAOS migration updated the manifest/adapter/skill/README/runtime control model but did not mechanically forbid retired-controller execution semantics inside the active business rulebook. Existing recovery tests verified retired files were absent, but did not verify that active authority-bearing prose was free of retired controller/lease requirements.

A second gap was behavioral adoption: the Novel capability profile declared UAOS common capability inheritance but predated Common Behavior Assurance 1.2, with no owner-native executable admission for recover-before-user-escalation / problem-to-action closure and no minimal canonical evolution-evidence entrypoint.

## Macro alignment
Novel remains domain-owned for checkpoint, Canon, research, release and learning evidence. UAOS remains the sole parent control plane. The repair uses Novel-native checkpoint/guard/audit evidence rather than copying Financial's article lifecycle or creating a second controller.

## Governing assumptions challenged
1. Removing retired controller files and updating the adapter is sufficient to prove control-plane cutover. It is not: an active rulebook can still instruct execution through the retired topology unless runtime/tests reject those semantics.
2. Declaring UAOS common-capability inheritance is sufficient operational proof. It is not: owner-native behavior evidence is required for an operational claim.
3. A historical red CI run proves the current tree is broken. It does not when a fresh exact-base reproduction passes; current conclusions must follow reproducible evidence.

## External method evidence
Declarative configuration is reliable only when intended configuration and live behavior are reconciled; authoritative state should be mechanically checked rather than inferred from one declaration surface. This repair uses that principle only as a control-method analogy, not as a claim that Novel is Kubernetes.

## Implemented repair
- `protocols/ACTIVE_RULEBOOK.md` moved parent authority to UAOS, quarantined the retired controller/lease/resume-epoch model, and added Novel-native Common Behavior 1.2 semantics.
- `.uaos/CAPABILITIES.json` advanced to profile 4, declared Common Behavior Assurance 1.2 minimum, the canonical evolution entrypoint, and executable owner-native capability refs.
- `.uaos/MANIFEST.json` exposed the common behavior, evolution and behavior-admission entrypoints.
- `UAOS_SKILL.md` exposed the same authority/evidence path progressively.
- `runtime/owner_behavior_admission.py` mechanically denies avoidable user escalation without a recovery receipt and denies recommendation-only closure when an authorized repair is available.
- `runtime/authority_behavior_guard.py` rejects the old active authority requirements while allowing explicit historical-quarantine text.
- `tests/test_owner_behavior_admission.py` exercises recovery/escalation and repair-or-block trajectories.
- `tests/test_authority_behavior_contract.py` locks current authority, behavior adoption and evolution discoverability.
- `.github/workflows/validate.yml` executes the authority/behavior guard in every PR/main validation.
- `audits/EVOLUTION_INDEX.json` provides a minimal Novel-owned canonical evidence entrypoint instead of a Financial-shaped journal.

## Verification and promotion evidence
- Fresh pre-repair reproduction: PR run #276 / `38675471138` PASS on the old guards/tests, proving historical #275 was not reproducible as a current-tree defect.
- Final candidate head `9b90b6146816cb062954ed3f2a819ec6ebcd1762`: PR run #288 / `38675978812` PASS. Recovery guard, authority/behavior guard, release-evidence guard, masterwork-distillation guard and 31 owner contract/trajectory tests all passed.
- PR #1 squash-promoted the mechanism as production commit `7cc56fbdca5139c2b61d0a16823d963693e9094c`.
- Production push CI #289 / `38676046948` PASS with the same guard/test chain.
- FQ001 business state was not advanced by this maintenance: `GUI_CHUI_DENG` remains paused after source line 3913 with next cursor line 3914, and `QING_YU_NIAN` remains pending.

## Result
The old controller wording can no longer silently coexist with current UAOS authority: it is explicitly quarantined and mechanically rejected if reintroduced as an active execution requirement. Common Behavior 1.2 is no longer declaration-only in Novel; recover-before-user-escalation and problem-to-action closure have executable Novel-owner admission and trajectory evidence.

## Assurance boundary and observation
Assurance is `EXECUTABLE_POLICY_AND_TRAJECTORY_VERIFIED`. This does not prove physical interception of every natural-language host response, and it does not prove improved live literary/business outcomes. Future real Novel work should observe whether recoverable dependencies are actually resolved without avoidable user homework and whether repairable defects cross into action rather than recommendation-only output; regress if the mechanism causes unsupported inference or inappropriate persistence.
