#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
problems = []


def need(rel):
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p


protocol_p = need("protocols/MASTERWORK_DISTILLATION_PROTOCOL.md")
registry_p = need("research/masterworks/INDEX.json")
study_state_p = need("research/masterworks/STUDY_STATE.json")
canonical_idx_p = need("continuity/TASK_INDEX.json")
alias_idx_p = need("TASK_INDEX.json")
for rel in [
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_03_CHARACTER_ENSEMBLE.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_04_MYSTERY_WORLD_RULES.md",
    "research/masterworks/SHIRI_ZHONGYAN/FULLTEXT_CORPUS_INGEST_2026-10-11.md",
]:
    need(rel)

TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"
STOP_PASS = "STOP_AFTER_CURRENT_WORK__NEXT_BOOK_NOT_STARTED"

if not problems:
    protocol = protocol_p.read_text(encoding="utf-8")
    registry = json.loads(registry_p.read_text(encoding="utf-8"))
    state = json.loads(study_state_p.read_text(encoding="utf-8"))
    canonical = json.loads(canonical_idx_p.read_text(encoding="utf-8"))
    alias = json.loads(alias_idx_p.read_text(encoding="utf-8"))

    if "status: ACTIVE_SYSTEM_PROTOCOL" not in protocol:
        problems.append("protocol-not-active")
    for stage in ("D0 RIGHTS_AND_SOURCE","D3 COLD_READ_TRACE","D6 POSITIVE_NEGATIVE_DIFF","D8 CROSS-WORK_TRIANGULATION","D9 PROJECT_TRANSFER_EXPERIMENT","D11 PROMOTION","D12 STOP / DECAY"):
        if stage not in protocol:
            problems.append("protocol-stage:" + stage)
    for concept in ("Psychological portrayal","Environment / atmosphere","Plot progression","Dialogue","Emotion","Quality audit"):
        if concept not in protocol:
            problems.append("microcraft-gap:" + concept)

    if registry.get("status") != "ACTIVE":
        problems.append("registry-not-active")
    if registry.get("study_state_ref") != "research/masterworks/STUDY_STATE.json":
        problems.append("registry-study-state-ref")
    if registry.get("authority_role") != "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY":
        problems.append("registry-authority-role")
    copyright_policy = registry.get("copyright_policy", {})
    if copyright_policy.get("pirated_fulltext_allowed") is not False:
        problems.append("pirated-fulltext-not-denied")
    if copyright_policy.get("store_substitute_for_original_work") is not False:
        problems.append("copyright-substitute-risk")
    if "USER_LAWFULLY_PROVIDED_TEXT" not in set(copyright_policy.get("allowed_sources", [])):
        problems.append("user-provided-source-not-allowed")

    if state.get("status") != "ACTIVE":
        problems.append("study-state-not-active")
    policy = state.get("study_policy", {})
    if policy.get("mode") != "ONE_BOOK_AT_A_TIME" or policy.get("rule") != "COMPLETE_CURRENT_WORK_BEFORE_NEXT":
        problems.append("study-policy")
    if policy.get("cross_work_synthesis") != "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE":
        problems.append("cross-work-policy")
    if set(state.get("user_locked_business_constraints", [])) != {"SIGNING_MODE_IMMUTABLE","SERIALIZATION_MODE_IMMUTABLE"}:
        problems.append("user-locked-constraints")

    active_work = state.get("active_work") or {}
    active_status = active_work.get("status")
    active_next_pass = active_work.get("next_pass")
    valid_statuses = {"ACTIVE__PENDING_FIRST_SEQUENTIAL_READ", "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS", TERMINAL}
    if active_work.get("work_id") != "GUI_MI_ZHI_ZHU":
        problems.append("study-state-active-work")
    if active_status not in valid_statuses:
        problems.append("study-state-active-status")
    if active_status == "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ":
        if active_next_pass != "SEQUENTIAL_FULLTEXT_FROM_BEGINNING":
            problems.append("study-state-initial-next-pass")
    elif active_status == "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS":
        if not isinstance(active_next_pass, str) or not active_next_pass.startswith("SEQUENTIAL_CONTINUE__"):
            problems.append("study-state-progress-next-pass")
    elif active_status == TERMINAL:
        if active_next_pass != STOP_PASS:
            problems.append("study-state-terminal-next-pass")
        if active_work.get("next_pending_work") != "DAO_MU_BI_JI":
            problems.append("study-state-terminal-next-work")
        if active_work.get("binding_role") != "CURRENT_FOCUS_BINDING_AFTER_COMPLETION__NOT_IN_PROGRESS":
            problems.append("study-state-terminal-binding-role")

    if active_status in {"ACTIVE__SEQUENTIAL_READ_IN_PROGRESS", TERMINAL}:
        coverage = active_work.get("coverage", {})
        sha = active_work.get("source_sha256", "")
        ledger_sha = active_work.get("rolling_ledger_sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            problems.append("study-state-source-sha256")
        if not re.fullmatch(r"[0-9a-f]{64}", ledger_sha):
            problems.append("study-state-ledger-sha256")
        if not coverage.get("sequential_completed"):
            problems.append("study-state-coverage:sequential_completed")
        if not coverage.get("next_location"):
            problems.append("study-state-coverage:next_location")
        if not active_work.get("rolling_ledger"):
            problems.append("study-state-rolling-ledger")
        if active_status == TERMINAL:
            if coverage.get("full_book_end_verified") is not True:
                problems.append("study-state-full-book-end")
            if coverage.get("chapter_heading_count") != 1394:
                problems.append("study-state-chapter-count")
            if coverage.get("source_total_lines") != 117803:
                problems.append("study-state-source-line-count")
            if coverage.get("next_location") != "STOP_AFTER_GUI_MI_COMPLETION__DO_NOT_BEGIN_NEXT_BOOK":
                problems.append("study-state-terminal-location")

    active = registry.get("active_studies", [])
    if len(active) != 1 or active[0].get("work_id") != "GUI_MI_ZHI_ZHU":
        problems.append("active-study-binding")
    else:
        guimi = active[0]
        if guimi.get("execution_authority") is not False:
            problems.append("active-study-authority-inflation")
        if guimi.get("current_status") != active_status:
            problems.append("guimi-status-drift")
        if guimi.get("next_pass") != active_next_pass:
            problems.append("guimi-next-pass-drift")
        if active_status == TERMINAL and guimi.get("binding_role") != "CURRENT_FOCUS_BINDING_AFTER_COMPLETION__NOT_IN_PROGRESS":
            problems.append("guimi-terminal-binding-role")

    completed = {s.get("work_id"): s for s in registry.get("completed_studies", [])}
    shiri = completed.get("SHIRI_ZHONGYAN", {})
    if not shiri:
        problems.append("shiri-completed-study-missing")
    else:
        if shiri.get("current_status") != TERMINAL:
            problems.append("shiri-completion-state")
        if shiri.get("next_pass") != "NEXT_BOOK__GUI_MI_ZHI_ZHU":
            problems.append("shiri-next-work")
        cov = shiri.get("fulltext_coverage", {})
        expected = {
            "user_source_numbered_mainline_through": 1359,
            "user_source_chapter_heading_occurrences": 1360,
            "source_numbering_anomaly": "two distinct headings labelled CH1357",
            "sequential_study_completed": "SOURCE_ORDER_1-1360",
            "body_numbering": "CH1-CH1359",
            "study_scope": "USER_PROVIDED_TEXT_ONLY_PER_USER_DIRECTION",
            "official_supplement_status": "OUT_OF_SCOPE_FOR_THIS_STUDY",
        }
        for key, value in expected.items():
            if cov.get(key) != value:
                problems.append("shiri-coverage-drift:" + key)
        for rejected in ("MORE_COMPLEXITY_IS_ALWAYS_BETTER","MANDATORY_AUTOBIOGRAPHY_CHAPTERS","DEATH_GAME_TEMPLATE","HYPERINTELLIGENT_PROTAGONIST_TEMPLATE"):
            if rejected not in shiri.get("explicitly_not_promoted", []):
                problems.append("anti-overfit-missing:" + rejected)

    if active_status == TERMINAL:
        guimi_done = completed.get("GUI_MI_ZHI_ZHU", {})
        if guimi_done.get("current_status") != TERMINAL:
            problems.append("guimi-completed-study-missing")
        else:
            cov = guimi_done.get("fulltext_coverage", {})
            expected = {
                "user_source_sha256": "25d76c8752e97255d8653205e44e0c12348fd50d9c68a657b3fc970d77112489",
                "source_total_lines": 117803,
                "chapter_heading_count": 1394,
                "sequential_study_completed": "ALL_8_VOLUMES__THROUGH_FULL_BOOK_END",
                "full_book_end_verified": True,
                "study_scope": "USER_PROVIDED_STANDARDIZED_TEXT_ONLY_PER_USER_DIRECTION",
            }
            for key, value in expected.items():
                if cov.get(key) != value:
                    problems.append("guimi-coverage-drift:" + key)
            if guimi_done.get("next_pass") != STOP_PASS:
                problems.append("guimi-completion-next-pass")

    queue = state.get("queue", [])
    if not any(w.get("work_id") == "SHIRI_ZHONGYAN" and w.get("status") == "COMPLETE" for w in queue):
        problems.append("queue-shiri-complete")
    expected_guimi_queue_status = "COMPLETE" if active_status == TERMINAL else "ACTIVE"
    if not any(w.get("work_id") == "GUI_MI_ZHI_ZHU" and w.get("status") == expected_guimi_queue_status for w in queue):
        problems.append("queue-guimi-status")
    if active_status == TERMINAL and not any(w.get("work_id") == "DAO_MU_BI_JI" and w.get("status") == "PENDING" for w in queue):
        problems.append("queue-next-book-started-or-missing")
    if not any(w.get("work_id") == "NORWEGIAN_WOOD" and w.get("status") == "EXCLUDED_BY_USER" for w in queue):
        problems.append("queue-norwegian-excluded")

    c_learning = canonical.get("system", {}).get("masterwork_learning", {})
    a_learning = alias.get("system", {}).get("masterwork_learning", {})
    for label, learning in (("canonical", c_learning), ("alias", a_learning)):
        if learning.get("registry_ref") != "research/masterworks/INDEX.json":
            problems.append(label + "-registry-ref")
        if learning.get("study_state_ref") != "research/masterworks/STUDY_STATE.json":
            problems.append(label + "-study-state-ref")
        if learning.get("active_study") != "GUI_MI_ZHI_ZHU":
            problems.append(label + "-active-study-binding")
        if active_status == TERMINAL:
            if "GUI_MI_ZHI_ZHU" not in learning.get("completed_studies", []):
                problems.append(label + "-guimi-not-listed-complete")
            if learning.get("next_pending_study") != "DAO_MU_BI_JI":
                problems.append(label + "-next-pending-study")
            if learning.get("stop_after_current_work") is not True:
                problems.append(label + "-stop-boundary")
    if a_learning.get("active_study_ref") != c_learning.get("active_study_ref"):
        problems.append("compat-index-masterwork-drift")

result = {
    "status": "PASS" if not problems else "FAIL",
    "protocol": "MASTERWORK_DISTILLATION_PROTOCOL@1.0",
    "active_study_binding": "GUI_MI_ZHI_ZHU",
    "active_status": state.get("active_work", {}).get("status") if 'state' in locals() else None,
    "study_policy": "ONE_BOOK_AT_A_TIME",
    "next_pass": state.get("active_work", {}).get("next_pass") if 'state' in locals() else None,
    "assurance": "LEARNING_EVIDENCE_ONLY__PROJECT_TRANSFER_PENDING",
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
