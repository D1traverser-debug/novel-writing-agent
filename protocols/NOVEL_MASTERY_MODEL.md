# Novel Writing Agent — Competency & Mastery Model

version: 1.0
status: ACTIVE_SYSTEM_PROTOCOL
scope: NOVEL_OS system-level capability map, learning targets, audit coverage, mastery evidence
business_authority: D1traverser-debug/novel-writing-agent@main

## 0. Purpose

This protocol answers four questions that the production Rulebook alone cannot answer:

1. **What must the Novel Writing Agent know how to do?**
2. **Where should each capability be learned from?**
3. **How deep must the capability be learned before it is trusted in production?**
4. **What evidence proves competence, and what evidence is still missing?**

`protocols/ACTIVE_RULEBOOK.md` remains the compact production-rule authority. This file is the capability ontology and mastery/evaluation authority. Raw research notes never override either file.

## 1. Evidence hierarchy for learning

Use the strongest evidence available for the specific decision:

1. **LIVE_PROJECT_OUTCOME** — real reader retention/follow-read/comment clusters, platform signing/recommendation result, editor feedback, actual publication constraints.
2. **CURRENT_PLATFORM_FIRST_PARTY** — current Fanqie rules, creator academy, creator help center, current platform programs and official examples.
3. **PRIMARY_CRAFT_METHOD** — reproducible methods from experienced professional writers/editors/teachers; prefer original source over summaries.
4. **MASTERWORK_DECONSTRUCTION** — direct analysis of successful works in the same or adjacent genre, especially the same acquisition/word-count window.
5. **BLIND_READER_EVIDENCE** — fresh-reader, target-reader, character-first, fair-play and mobile-reader observations.
6. **COMMUNITY_HEURISTIC** — forums, creator anecdotes and trend discussion; discovery signal only until corroborated.
7. **MODEL_SELF_EVALUATION** — lowest evidence class; useful for hypothesis generation, never sufficient for mastery or release.

A technique may be useful without becoming a universal rule. Source authority and scope must be recorded separately.

## 2. Mastery levels

### L0 — UNMAPPED
The capability is absent or only vaguely named. No stable rubric, benchmark or failure signature exists.

### L1 — CONCEPTUAL
Can explain the concepts and identify obvious examples, but cannot be trusted to design or diagnose a difficult production case.

Required evidence: source notes + terminology map.

### L2 — OPERATIONAL_WITH_SCAFFOLD
Can apply the capability with an explicit checklist/template and can catch common failures.

Required evidence: at least one project-specific artifact/exercise + failure analysis.

### L3 — PROJECT_READY
Can design, execute, audit and revise the capability in a real project without relying on the user to name the missing step; can compare alternatives and explain tradeoffs.

Required evidence:
- project artifact or body of prose using the capability;
- adversarial/alternative challenge;
- issue ledger or audit result;
- no unresolved BLOCKER/HIGH in that capability for the active production scope.

### L4 — TRANSFER_VERIFIED
Capability transfers across materially different projects/genres and is supported by repeated external outcome evidence. A single successful chapter/book or internal CI cannot establish L4.

Required evidence: multiple projects or phases + real reader/editor/platform outcomes + regression showing the rule does not overfit one work.

**Policy:** reading a course can move knowledge toward L1; it cannot by itself establish L2/L3/L4.

## 3. Core competency map

All core competencies target **L3 before they become the unreviewed driver of a high-impact production decision**. L4 is a long-term system-learning target, not a default claim.

### C01 — Premise / market / reader contract
Mastery means: identify the distinctive story promise, target reader, genre expectations, novelty source and commercial acquisition problem without blindly chasing trends.

Must be able to:
- state one-sentence premise and reader promise;
- distinguish premise novelty from surface trope novelty;
- define why the intended reader continues after the first screen / first chapter / first unit;
- compare at least 2–3 positioning candidates when the premise is underperforming.

Failure signatures: generic premise, trend-copying, mismatched target reader, strong lore but weak immediate story question.

Primary sources: current Fanqie category/creator guidance, same-category successful works, Story Grid genre expectations as a diagnostic lens.

### C02 — Series architecture / master outline
Mastery means: design the story from ending and global transformation backward through series → volume → arc/unit → chapter → scene, while preserving controlled flexibility.

Must be able to track:
- external mainline;
- protagonist internal arc;
- relationship arcs;
- world/rule expansion;
- opposition escalation;
- mystery/reveal ladder;
- promise/payoff debt;
- commercial/retention rhythm;
- ending constraints.

Failure signatures: only a chapter list, endless unit repetition, no volume-level turning points, no ending pressure on the middle, local improvements that preserve a weak macro trajectory.

Primary sources: Fanqie outline/volume-outline/multi-line guidance; Writing Excuses outlining/pre-writing; structure methods used as tools, not formulas.

### C03 — Worldbuilding / system design
Mastery means: world rules generate conflict, cost, choice and social consequences rather than encyclopedia exposition.

For speculative systems, audit:
- reader-understood capabilities vs mystery;
- limitations/costs/side effects;
- exploit surface;
- social/institutional/economic consequences;
- escalation path;
- contradictions and second-order effects;
- what remains unknown to characters/readers.

Failure signatures: new power added to escape a scene, rules without consequences, lore that never changes behavior, world only exists around protagonist, unexplained institutional convenience.

Primary sources: Fanqie story-setting/worldbuilding guidance; Sanderson Laws as a non-binding design heuristic (limitations, reader understanding, expand-before-add); Writing Excuses worldbuilding consequence/ripple methods.

### C04 — Character design / character arc
Mastery means: build a character with desire, fear, wound/history, coping strategy, contradiction, competence, blind spot, values and change pressure; external plot choices must enact the internal arc.

Track:
- Want / Need;
- limited belief / emerging truth;
- short-term objective and long-term identity pressure;
- cost of staying unchanged;
- decisive choices at major structural turns;
- behavior/voice consistency without making characters static.

Failure signatures: character exists only to move plot, emotion labels replace behavior, competence without vulnerability, late-stage personality imported into opening, arc explained but not dramatized.

Primary sources: current Fanqie character courses; K.M. Weiland character-arc/Truth-Lie tools as optional diagnostics; direct masterwork character-decision analysis.

### C05 — Relationship / ensemble dynamics
Mastery means: every durable relationship has its own goal conflict, leverage, debt, trust, power, intimacy/suspicion delta and independent reason to continue existing.

Failure signatures: supporting characters are search engines, cheerleaders, exposition terminals, or disappear after function is served.

Audit: if protagonist vanished for one chapter, what would this person still want/do?

### C06 — Theme / moral argument
Mastery means: theme emerges from competing legitimate values and costly choices; antagonist/supporting characters embody workable counterarguments.

Failure signatures: moral summary, strawman opponent, theme detached from climax, “correct” answer has no cost.

Primary sources: character-arc/theme methods; thematic-square/counterargument methods; project-specific ethical research.

### C07 — Opposition / stakes / conflict escalation
Mastery means: opposition has agency, information limits, capabilities, costs and tactic changes; stakes widen/deepen/transform rather than merely increase numerically.

Failure signatures: protagonist wins because others become stupid; every obstacle is solved by more information; danger increases but choice does not become harder.

### C08 — Mystery / suspense / information architecture
Mastery means: start from the intended truth/reveal, work backward through fair clues, alternate hypotheses, misdirection and staged reinterpretation; manage curiosity, suspense and surprise separately.

Must track:
- reader question;
- current candidate answers;
- evidence known to reader vs protagonist;
- clue visibility;
- red-herring legitimacy;
- reveal timing;
- how each answer creates the next larger question.

Failure signatures: answer withheld arbitrarily, deus-ex clue, mystery debris, protagonist asks endless questions, reader cannot retrospectively reconstruct the reveal.

Primary sources: Writing Excuses mystery/fair-play/reveal methods; Fanqie hook/nested-suspense guidance; direct mystery deconstruction.

### C09 — Scene architecture
Mastery means: each major scene has a goal, meaningful friction, turning choice and value/state change; reaction/processing is included at the amount the story needs.

Useful diagnostics: Goal→Conflict→Outcome and Reaction→Dilemma→Decision; Story Grid value shift/crisis-choice. These are diagnostics, not mandatory templates.

Failure signatures: ask→exact answer, travel-only scene, scene can be deleted with no state change, conflict without consequence.

### C10 — Chapter architecture / hooks
Mastery means: a chapter has a specific job, visible progress/payoff, emotional contour and a state-changing ending; first screen earns attention and the ending earns the next click.

Failure signatures: chapter is only setup, hook is a new noun with no consequence, every chapter ends with same phone call/system prompt, “总结中心思想” ending.

### C11 — Pacing / long-serial rhythm
Mastery means: control local reading speed and macro event cadence; place escalation, relief, emotional landing, payoff and renewal across a long serial without mechanical fixed-number formulas.

Track at multiple scales:
- sentence/paragraph velocity;
- scene density;
- chapter payoff/progress;
- 3–10 chapter unit rhythm;
- volume rise/fall;
- series escalation.

Failure signatures: constant high pressure, prolonged procedural plateau, repetitive engine, padding to hit word count.

Primary sources: current Fanqie pacing/outline/long-form courses + real retention/follow-read curves.

### C12 — Dialogue / subtext / voice
Mastery means: dialogue participants pursue different goals; text, context and subtext can diverge; voice remains character-specific under pressure.

Failure signatures: Q&A interview, every line is maximally clever, everyone has same syntax, explicit explanation of feelings/intent that could be inferred.

Primary sources: Writing Excuses dialogue/subtext methods; direct transcript-style deconstruction of strong scenes.

### C13 — POV / prose / immersion
Mastery means: psychic distance, sensory selection, syntax and paragraph rhythm serve the current emotion/action; prose remains readable, specific and non-template.

Failure signatures: camera-only narration, report/memo texture, repetitive rhetorical forms, every sentence “golden line”, overprecision that increases cognitive homework.

### C14 — Emotion / attachment / reader empathy
Mastery means: attachment is created by specific vulnerability, competence, desire, cost, ordinary life and relationship consequence—not by demanding that the reader care.

Failure signatures: protagonist in danger but socially/emotionally weightless, no aftershock, “克制” used as absence of feeling.

### C15 — Foreshadow / payoff / reader memory
Mastery means: Seed→Echo/Transform→Payoff/Reframe; major promises have owner, horizon, progress and payoff state; cognitive load is budgeted.

Failure signatures: mystery debris, forgotten setups, payoff requires recap lecture, too many names/times/rules at once.

### C16 — Domain reality / research
Mastery means: know when factual precision improves story and when it only creates truth burden; research access, institutional behavior and professional mechanisms before they determine plot.

Failure signatures: ordinary protagonist gets protected data, institutions behave as exposition services, pseudo-technical detail masks implausibility.

### C17 — Revision / editorial diagnosis
Mastery means: diagnose the **level** of the defect before editing: premise → architecture → character/relationship → scene engine → prose → sentence → copyedit.

Failure signatures: line-editing a structural failure, endless revision loops, changing old chapters without dependency analysis, revision that fixes one chapter but breaks the arc.

Primary sources: current Fanqie revision/self-check courses + hash-bound project evidence + blind readers.

### C18 — Platform / acquisition / serial business fit
Mastery means: understand current platform rules, signing/recommendation opportunities, target-audience acquisition, title/intro/first-screen behavior and long-form retention—without turning platform heuristics into universal art laws.

Failure signatures: chasing word-count thresholds, treating one platform campaign as eternal taste, confusing safety review with quality/signing review.

### C19 — Canon / continuity / longform state
Mastery means: factual truth, planned outline and prose surface remain separated; knowledge state, timeline, location, causal dependency and retcon impact stay coherent across long serialization.

### C20 — Meta-learning / benchmark discipline
Mastery means: identify capability gap without waiting for the user to name it, find the right evidence source, compare methods, benchmark on project material, promote only proven scope-fit rules and retire superseded mechanisms.

Failure signatures: research hoarding, “learned” means “read”, user has to repeatedly remind the agent of an entire quality dimension, or rules accumulate without tests/removal.

## 4. Audit architecture

### Gate A — Concept / series design
Required for new project, major rebase, new volume or major premise shift.

Audit: C01–C08 + C18–C20.

Questions:
- What is the primary reader promise and what pays it off?
- What changes permanently by the end of this unit/volume/series?
- Which character belief/relationship/world rule is under pressure?
- What is the opposition doing independently?
- Which mystery answers now, which enlarges, which stays latent?
- What would make this outline repetitive at 100k/300k/800k?

### Gate B — Arc / packet architecture
Audit: C02, C04–C11, C14–C15, C19.

Required outputs: arc objective, protagonist choice arc, relationship deltas, reveal ladder, promise/payoff map, engine-diversity map, emotional rhythm, end-state.

### Gate C — Chapter / scene production
Audit: C09–C16 + current contract/Canon.

### Gate D — Revision
Audit: C17 first. Defect level determines which upstream gate reopens. Never default to sentence polish.

### Gate E — Release / platform
Audit: current release hard gates + C18. Real platform outcome can reopen earlier gates.

## 5. Benchmark library requirements

A competency is not promoted to L3 merely because its rule exists. The owner maintains project-grounded benchmark evidence.

Minimum benchmark types:
- **Architecture benchmark:** produce competing outlines, falsify the first attractive option, show ending-to-opening causal chain.
- **Worldbuilding benchmark:** implication tree + limitation/exploit test + social consequence test.
- **Character benchmark:** decisive-choice map + voice/behavior consistency + independent-agency test.
- **Mystery benchmark:** solution-first clue ladder + fair-play audit + alternate-hypothesis/red-herring test.
- **Scene benchmark:** remove/reorder scene test; every kept scene must change state.
- **Dialogue benchmark:** subtext rewrite where meaning survives after literal explanation is removed.
- **Prose benchmark:** cold-read clarity/texture comparison; detect template repetition and report texture.
- **Pacing benchmark:** same-word-window comparison against project goals and comparable successful works; no fixed formula promotion.
- **Revision benchmark:** seeded structural/prose defects; reviewer must diagnose defect level before editing.

## 6. Current project learning target — FQ001

Before candidate CH1–CH8 prose is promoted, the active project must demonstrate L3 project-ready evidence for at least:

- C01 Premise / reader contract
- C02 Series architecture / master outline
- C03 World/system design
- C04 Character arc
- C05 Relationship dynamics
- C06 Theme
- C08 Mystery / information architecture
- C09–C11 Scene/chapter/pacing
- C14–C15 attachment + foreshadow/payoff
- C17 Revision
- C18 Platform/acquisition fit
- C19 Canon/continuity
- C20 Meta-learning

C12/C13/C16 are mandatory at prose execution/release time and may remain benchmark-pending during architecture freeze if their unresolved state cannot change architecture.

## 7. Learning source map — current baseline

### Fanqie current first-party
Use Creator Academy / Help Center as the first platform-specific source. Current curriculum explicitly covers:
- topic selection;
- outline/mainline/multi-line/volume outline;
- story/world/character/timeline setting;
- opening, plot, hooks, immersion, characters;
- revision/self-check;
- stable long-form serialization;
- acquisition/IP/creator programs.

Current 2026 long-form guidance is especially relevant for complex protagonist design, distinctive/deep worldbuilding, nested suspense, tension/relief rhythm and long-range foreshadow closure.

### General craft originals / high-signal methods
Use as diagnostic tools, not universal formulas:
- Sanderson: reader-understanding vs conflict-solving, limitations > powers, expand-before-add;
- Writing Excuses: pre-writing/outlining, worldbuilding ripples, mystery solution-first clue design, fair play, tension/unanswered questions, dialogue subtext;
- Scene/Sequel and value-shift methods for scene causality;
- character-arc/theme tools for aligning internal change with external plot.

### Masterwork deconstruction
Prefer same-channel/current-category works and compare at equivalent word-count windows. Extract functions, not sentences/tropes:
- what promise is made;
- what changes by 3k/10k/20k/50k;
- when durable relationships enter;
- how the world expands;
- how mystery answers generate larger questions;
- where emotional breathing and memorable human details land.

No prose imitation, phrase borrowing or plot cloning.

## 8. Learning trigger / stop rule

Open learning when one of these occurs:
- real platform/reader/editor failure;
- unresolved BLOCKER/HIGH with no current capability;
- new genre/story phase exposes an unmapped skill;
- repeated same-class defect across chapters;
- current method cannot distinguish competing solutions.

Stop research when:
- the missing capability is mapped;
- at least two viable methods were compared when the decision is material;
- a benchmark demonstrates project-level use;
- active rules/audit surface has been updated;
- further reading no longer changes the decision.

Then return to production. The system is not rewarded for accumulating courses.