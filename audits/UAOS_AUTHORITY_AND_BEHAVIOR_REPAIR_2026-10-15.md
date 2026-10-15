# UAOS authority and behavior repair — 2026-10-15

Status: CANDIDATE_DIAGNOSIS
Owner: DOMAIN:novel

## Trigger
A UAOS total-controller audit of the Novel domain found that current domain binding files and README identify `D1traverser-debug/universal-agent-os@main` as the only control plane, while `protocols/ACTIVE_RULEBOOK.md` still names the retired `universal-continuity-agent@main` and requires `active_lease + resume_epoch` before material writes.

The same audit found that current production main `e84a99ce3643ffd29df40884a9924a7e8f548778` has failing `validate-novel-owner` CI (#275 / run 38539165735), while the newest successful main validation observed was run #175 on commit `f0e7357b4eb95ef7b754c7b7bd7f7584734f7172`.

## Micro diagnosis
The UAOS migration updated the manifest/adapter/skill/README/runtime control model but did not mechanically forbid retired-controller semantics inside the active business rulebook. Existing recovery tests verify retired files are absent, but they do not verify that active authority-bearing prose is free of retired controller/lease requirements.

The Novel capability profile also predates UAOS Common Behavior Assurance 1.2 and therefore declares common capability inheritance without an owner-native discoverable evolution entrypoint or explicit behavior-adoption evidence for recover-before-user-escalation / problem-to-action closure.

## Macro alignment
Novel should remain domain-owned for checkpoint, Canon, research, release and learning evidence. UAOS should remain the sole parent control plane. The repair must use Novel-native checkpoint/guard/audit evidence rather than copy Financial's article lifecycle or create a second controller.

## Governing assumption challenged
Removing retired controller files and updating the adapter is sufficient to prove control-plane cutover. It is not: an active rulebook can still instruct execution through the retired topology unless the runtime/tests reject those semantics.

## External method evidence
Declarative configuration is reliable only when intended configuration and live behavior are reconciled; authoritative state should be mechanically checked rather than inferred from one declaration surface. This repair uses that principle only as a control-method analogy, not as a claim that Novel is Kubernetes.

## Selected repair direction
1. Reproduce the current CI failure on a fresh candidate run and preserve the actual failure output.
2. Remove retired controller/lease semantics from `ACTIVE_RULEBOOK.md` and bind material writes to UAOS task state + current Novel checkpoint.
3. Extend Novel recovery admission to reject retired authority semantics in current control/rule surfaces.
4. Adopt UAOS Common Behavior Assurance 1.2 in the Novel capability profile using Novel-native evidence.
5. Add a minimal canonical `audits/EVOLUTION_INDEX.json` rather than a Financial-shaped journal.
6. Add regression/trajectory coverage for authority cutover and repair-or-block behavior; do not claim host-level physical interception.
7. Promote only after exact candidate CI passes, then re-read production main and CI.

## Assurance boundary
Current diagnosis is evidence-backed but not yet promoted. Production remains unhealthy until candidate repair passes and production main is revalidated.
