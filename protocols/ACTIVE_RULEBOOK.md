# Novel Writing Agent — Active Rulebook

version: 2.2-github
status: ACTIVE
scope: NOVEL
source: distilled from NOVEL_OS 1.9.0 active protocols plus accepted GitHub-owner evolution; legacy protocol/research snapshots are archived in the Google Drive artifact vault as non-authoritative historical evidence.

## 1. Non-negotiable authority
- Business authority: `D1traverser-debug/novel-writing-agent@main`.
- Global discovery/routing/single-writer lease: `D1traverser-debug/universal-continuity-agent@main`.
- Chat/model memory is never Canon or executable state.
- Before any material checkpoint write, re-read Universal task manifest and verify this chat owns `active_lease + resume_epoch`.
- External publication/delete/payment/sign/compliance declarations remain user-controlled. Never infer publication.
- User is not QA manager. QA may not depend on user prompting.
- Google Drive is derived-artifact/history vault only; retired Notion/Library/legacy Drive material cannot regain execution authority by presence.

## 2. Production organization
Use minimum sufficient specialization, not “one micro-check = one permanent agent”.
Core roles:
- ORCHESTRATOR: state recovery, context freeze, task decomposition, issue merge, conflict arbitration, final gate collection. Must not self-approve its own prose.
- ARCHITECT: chapter function, scene engine, promises, escalation, alternatives.
- CANON_LIBRARIAN: facts, timeline, characters, threads, foreshadow, promises.
- WRITER: writes only from frozen Context Pack + contract; cannot edit Canon.
- CONTINUITY_AUDITOR: facts/contract only.
- FRESH_READER: reader-visible text only; finds confusion/drop points.
- RETENTION_AUDITOR: promises, attachment, tension, follow-read, hook, cross-chapter repetition.
- EDITORIAL: scene life, dialogue, voice, prose, pacing, AI/template roughness.
- ADVERSARIAL_RELEASE: default REJECT until no BLOCKER/HIGH.
- QUALITY_DISCOVERY: searches for missing quality dimensions/unknown unknowns.
- REFINER: fixes registered issues; any text hash change invalidates body-dependent audits.
- COPYEDITOR/PROOFREADER: final typo/grammar/punctuation/numerical/read-aloud pass after literary changes stop.
- ARTIFACT_RELEASE_ENGINEER: same-source DOCX/render/hash/guard/recovery artifact.
- CANON_COMMITTER: commits only after release gates pass.
Risk-triggered specialists: domain reality, dialogue/subtext, spatial staging, suspense fairness, longform, world rules, theme, foreshadow/payoff, reader memory, transition bridge, opposition/counter-agency.

Independent first judgments mean input-level separation from peer conclusions. Normal same-session role separation is `CHAT_BRIDGED` and must be labeled `ROLE_SEPARATED_NOT_ATTESTED_ISOLATED`; do not claim distinct independent executor identity unless an external/isolated trace proves it. No open-ended group debate and no majority vote overriding hard facts. Two+ role-separated reviewers finding the same defect escalates severity but does not magically increase assurance level.

### 2.1 Execution evidence contract（CH9+）
A release pipeline is not proven by a checklist saying every role PASS. From CH9 onward:
- snapshot the chapter contract to `projects/<task>/contracts/CHxxxx_CONTRACT.md` before execution;
- freeze `projects/<task>/execution/CHxxxx_CONTEXT_PACK.json` with owner commit and exact input refs/hashes;
- persist `projects/<task>/reviews/CHxxxx_EXECUTION_EVIDENCE.json` with role receipts, source hash, peer-visibility and issue ledger;
- bind Acceptance to the Context Pack and execution-evidence hashes;
- run `runtime/release_evidence_guard.py` before `FINAL_ACCEPTED / PUBLISH_READY`.

CH8 is a pre-v1 legacy aggregate acceptance. Preserve its accepted business state, disclose the missing receipt assurance, and never replay completed work merely to manufacture historical evidence.

## 3. Revision hierarchy
Fix in this order:
1. concept/chapter function;
2. structure/scene engine;
3. character/relationship/choice;
4. scene rendering and reality friction;
5. prose rhythm/voice;
6. sentence/word;
7. copyedit.
Default maximum two full evaluator→optimizer rounds. If HIGH/BLOCKER remains, escalate to architecture/specialist diagnosis instead of infinite polishing.

## 4. Project identity regression
FQ001 must remain:
- 都市脑洞 × 悬疑单元剧 × 城市群像;
- realistic modern city occupation/institution friction;
- supernatural opens one narrow aperture;
- third-person limited Chen Du;
- Chen Du is route/city/logistics smart, not omniscient detective;
- restrained suspense with human texture, not report/memo narration;
- future information is useful but incomplete; modifying future migrates risk;
- Mingrida does not provide the “correct answer” or convenient new powers.

Reject drift toward pure detective fiction, rule-horror, mindless system power fantasy, universal conspiracy explanation, omniscient protagonist, or procedural report.

## 5. Context budget / drift control
Writer receives:
- ACTIVE project identity/profile;
- frozen current chapter contract snapshot;
- minimum relevant Canon;
- recent 3 FINAL chapters;
- at most 2–4 relevant specialist rule slices.
Do not load all research/history into Writer.
New learning enters REFERENCE/EXPERIMENTAL quarantine first. Promote only if repeated defects, new story phase, platform change, or evidence shows meaningful gain. Context Pack freezes when a chapter starts; new craft tips do not rewrite the current chapter unless they reveal a hard fact/compliance/blocker issue.
Profile structural upgrade: at most every 10 chapters absent a hard failure.

The frozen Context Pack must be durable from CH9 onward; chat-only recollection is not evidence of what the Writer or reviewers actually received.

## 6. Scene engine
A major scene must have:
- concrete goal;
- conflict/friction/uncertainty;
- consequential choice/turn;
- at least one memorable nonfunctional person/object/body detail.
Use Goal→Conflict→Disaster and Reaction→Dilemma→Decision as diagnostic models, not templates.
If a scene is only “ask → exact answer”, restructure.
Professional information survives only if it changes choice, risk, character, foreshadow/payoff, or real-world friction.
Temporary characters have local priorities: workload, liability, convenience, fear, money, fatigue, misunderstanding, curiosity.

## 7. Voice / psychic distance
Narration is not Chen Du’s spreadsheet.
His rationality is shown primarily through:
1. choices;
2. consequences;
3. missed/misjudged factors;
4. only then concise conclusions.
Psychic distance may move closer under pressure.
Perception should be character-specific, not generic camera prose.
Short sentences are impact tools, not default formatting.
Avoid repeated formulae such as “不是X，是Y”, “没有X，只Y”, symmetric triads, checklist-thinking and conclusion slogans.
Do not intentionally add typos or awkwardness to appear human.

## 8. Dialogue / relationship
Dialogue has text + subtext + context. Participants pursue different goals and may refuse, misunderstand, withhold, redirect, or care about something else.
Avoid interview/Q&A pipelines.
Track relationship deltas: trust, debt, power, obligation, intimacy, suspicion.
Supporting characters need independent agendas and actions they would take even without protagonist.

## 9. Opposition / counter-agency
Opposition includes people, institutions, stakeholders, system constraints, logistics, evidence uncertainty and protagonist habits.
For each meaningful opposing force know:
- current goal;
- believed truth;
- missing information;
- capabilities;
- unaffordable costs;
- trigger for tactic change;
- what it would do without protagonist.
No omniscient antagonists without information paths. No protagonist wins merely because everyone else becomes careless/stupid. Mingrida is not automatically antagonist.

## 10. Suspense / information architecture
Use a mix of:
- curiosity: what happened/how does it work;
- suspense: what bad outcome may happen next;
- surprise: new fact forces reinterpretation;
- dramatic irony where useful.
Maintain nested promises across scene/chapter/unit/volume.
Fair-play: important reversals should be surprising now but explainable in retrospect.
Rule reveal progression: OBSERVED → HYPOTHESIS → REPEATED → OPERATIONAL → CONFIRMED → BROKEN/REFRAMED.
Never write hypothesis as confirmed.
A rule reveal should clarify an old contradiction and create new consequence/choice/limitation/cost.
Avoid mystery debris.

## 11. Longform escalation
Track Scene / Chapter / Unit (3–10 chapters) / Volume / Series.
Rotate escalation dimensions:
information depth, relationship/personal cost, moral ambiguity, time pressure, public scale, rule complexity, opponent sophistication, irreversible consequence.
Adjacent units cannot rely on the same primary engine + dominant cost + reveal shape.
Reject endless “new order → investigate → solve → new order”.
Every 10 chapters: longform/world-rule/foreshadow review.
Every 50 chapters: full Canon reconciliation.

## 12. Theme / moral argument
Theme is a pressure system of competing legitimate values, not speeches.
FQ001 territory:
- knowing future vs controlling future;
- whether information creates responsibility;
- who has authority to decide another person’s future;
- prediction vs consent;
- harm reduction vs agency.
Recurring characters should embody workable competing answers. No strawman/cost-free morality.

## 13. Foreshadow / payoff
Important elements follow Seed → Echo/Transform → Payoff/Reframe.
Track who knows, visibility, payoff horizon, echoes, payoff type, staleness risk.
Do not accumulate mystery debris. Payoffs should be retrospectively legible.

## 14. Emotion / tension
Track tension and emotion separately: entering emotion → disturbance → escalation → peak/turn → aftershock → exit appetite.
Avoid same emotional color across five chapters.
Breather scenes must still accomplish at least two of relationship/consequence/ordinary-life/seed conflict/change decision/world texture.
Emotion through body, behavior, relationship, choice—not explanatory labels.

## 15. Reader memory / cognitive load
Per 3–5 chapter window track new names, locations, mechanism terms, high-priority promises, distinctive objects and exact times/numbers.
Classify details:
- MUST_REMEMBER
- RECOGNIZE_ON_RETURN
- ATMOSPHERE_ONLY
After absence, reactivate through action/sensory/relationship/consequence, not naked recap.
Avoid name collisions, timestamp homework and simultaneous spikes in multiple categories.

## 16. Spatial staging / action clarity
Render actionable geography only:
- POV position;
- blockers/visibility;
- goal/threat;
- 1–2 stable anchors.
Update position through action/consequence, not coordinates.
Physical action order: intent/perception → movement → contact/change → consequence → reaction.
Exact geography belongs in Canon when it does not affect reader action comprehension.
No teleporting or silent POV reorientation.

## 17. Transition / bridge
A transition must do at least two:
- aftermath/process cost/emotional residue/relationship change;
- reorientation/new goal/rule/place/phase;
- attachment/ordinary life/humor/intimacy/obligation/social texture;
- load future conflict/resource/misunderstanding/choice.
It ends with a changed state: decision, relationship delta, resource, commitment, belief, concrete next action.
Compress pure transport/info; do not skip consequences.

## 18. Domain reality
Precision increases truth burden.
Before using professional/institutional mechanisms ask:
- Can this character realistically know/access it?
- Would staff disclose it?
- What privacy/liability/workload friction exists?
- Does the mechanism actually work this way?
Real-world professional mechanism changing plot outcome is a hard gate.
Do not give ordinary protagonist confidential backends/medical/police/vehicle data without legitimate access.

## 19. Chapter title / first screen / hook
Every release explicitly audits:
- title click value without fake spoilers;
- first-screen actionable problem/novelty;
- chapter promise;
- end hook that changes story state.
Do not end with abstract moral/theme summary.
Avoid consecutive chapters using the same hook shape.

## 20. Chapter length
Use actual Fanqie backend count when available; otherwise authoritative FINAL non-whitespace character count.
Regular target roughly 2400–3000; major payoff/climax 2600–3300, but story need outranks arbitrary quota.
Compare against recent four chapters:
- >30% deviation → mandatory special review;
- >45% deviation → default release block unless structurally justified.
Never bloat to chase update incentives.
Every five chapters inspect length × read-through/follow-read when data exists.

## 21. Beta reader panel
Fixed personas:
- target male suspense/brain-hole reader;
- casual mobile reader;
- mystery fair-play reader;
- character-first reader;
- skim reader.
If 2+ role-separated personas identify the same defect, escalate severity. If target + casual both DROP, default HIGH. Persona simulation remains `CHAT_BRIDGED` unless a distinct external execution identity proves otherwise.

## 22. Final proofread hard gate
After literary edits stop, run:
A. Mechanical pass: typos, missing/extra/repeated characters, quotation/bracket/punctuation, times, numbers, plates, names, measure-word order.
B. Semantic copyedit: grammar, collocation, reference ambiguity, logic, unnatural spoken phrasing.
C. Read-aloud pass: awkward rhythm, repetitions, unnatural pauses.
D. deterministic proofread guard.
Any body change invalidates old hash-bound audits. Re-run required gates on new hash.

## 23. Autonomous release checklist
Before saying “可以传/可以发布”, ORCHESTRATOR must verify on the same FINAL hash:
1. contract/architecture;
2. scene internal QA;
3. continuity;
4. Fresh Reader Blind;
5. Reader Retention;
6. Editorial;
7. Adversarial Release = RELEASE;
8. title;
9. first screen;
10. emotion/attachment/theme embodiment;
11. prose texture/template scan;
12. cross-chapter engine/repetition;
13. length variance;
14. Quality Discovery;
15. current platform risk;
16. Domain Reality when applicable;
17. Project Identity Regression;
18. Final Proofread;
19. deterministic guards;
20. CH9+ release evidence guard + hash-bound role receipts;
21. same-source DOCX;
22. render every page visually;
23. text parity.
BLOCKER=0 and HIGH=0. Numerical average scores never override a hard gate. Aggregate PASS prose cannot substitute for the evidence contract.

If user finds a responsibility defect only after “可以发布”, immediately revoke release, mark REMINDER_DEPENDENCY_INCIDENT, fix, invalidate stale audits, diagnose gate miss, upgrade guard/reviewer/rubric, and only re-release after full applicable gates pass.

## 24. Data / evidence hierarchy
1. actual reader/platform data;
2. current Fanqie official rules/courses/governance;
3. reproducible craft/editorial methods;
4. authoritative domain/public research;
5. blind readers;
6. community heuristics;
7. model self-evaluation.
Research does not count as evolution unless it changes a rule/process/benchmark/reviewer/script/data field and passes the relevant regression/evidence gate.

### 24.1 Fanqie signing-readiness
A signing attempt is a high-value external evaluation event, not a word-count milestone to consume automatically.

Before each application:
- refresh current official Fanqie signing thresholds and evaluation guidance;
- run a signing-readiness audit on at least opening, pacing, character setup, immersion and mainline;
- treat real platform rejection as stronger evidence than model self-score;
- never infer AI detection, safety failure, plagiarism or another hidden reason from a generic quality rejection unless the platform explicitly says so;
- after a rejection, do not simply continue unchanged to the next threshold; first diagnose the visible front arc and create a bounded repair plan;
- a previously frozen baseline may be reopened when the rejection is a genuine external hard-quality signal, but changes must remain traceable and dependency-audited;
- replacing already-published platform chapters remains user-controlled even when internal candidate revisions are prepared;
- the next signing attempt is blocked until its project-specific readiness gate passes.

## 25. Checkpoint cadence
- every material stage/next_action/constraint/artifact/blocker/authority change: checkpoint;
- every chapter: immutable FINAL + immutable chapter contract snapshot + frozen Context Pack + role execution evidence + acceptance + derived delivery artifact;
- every 5 chapters: lightweight checkpoint + cross-chapter texture scan;
- every 10 chapters: full project snapshot + independent longform review;
- every 50 chapters: global Canon reconciliation;
- major rebase/structural change: pre/post snapshot;
- every signing evaluation result: persist exact platform fact, inference boundary, next threshold/gate and any resulting front-arc repair state.
Store execution truth, not chat transcript.
