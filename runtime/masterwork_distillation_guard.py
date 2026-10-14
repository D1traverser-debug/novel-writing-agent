#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
problems: list[str] = []
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"
ACTIVE_STATUSES = {
    "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ",
    "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS",
    "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT",
}
VALID_STATUSES = ACTIVE_STATUSES | {TERMINAL}


def need(rel: str) -> Path:
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p


def load(rel: str) -> dict:
    p = need(rel)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


protocol_p = need("protocols/MASTERWORK_DISTILLATION_PROTOCOL.md")
state = load("research/masterworks/STUDY_STATE.json")
caps = load(".uaos/CAPABILITIES.json")

for rel in [
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_03_CHARACTER_ENSEMBLE.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_04_MYSTERY_WORLD_RULES.md",
    "research/masterworks/SHIRI_ZHONGYAN/FULLTEXT_CORPUS_INGEST_2026-10-11.md",
]:
    need(rel)

if protocol_p.exists():
    protocol = protocol_p.read_text(encoding="utf-8")
    if "status: ACTIVE_SYSTEM_PROTOCOL" not in protocol:
        problems.append("protocol-not-active")
    for stage in (
        "D0 RIGHTS_AND_SOURCE",
        "D3 COLD_READ_TRACE",
        "D5 MICROCRAFT_ANNOTATION",
        "D6 POSITIVE_NEGATIVE_DIFF",
        "D7 ABLATION / COUNTERFACTUAL",
        "D8 CROSS-WORK_TRIANGULATION",
        "D9 PROJECT_TRANSFER_EXPERIMENT",
        "D10 ADVERSARIAL_REVIEW",
        "D11 PROMOTION",
        "D12 STOP / DECAY",
    ):
        if stage not in protocol:
            problems.append("protocol-stage:" + stage)

if state.get("status") != "ACTIVE":
    problems.append("study-state-not-active")
if state.get("authority_role") != "SYSTEM_LEARNING_CHECKPOINT_NOT_PROSE_OR_CANON_AUTHORITY":
    problems.append("study-state-authority-role")
policy = state.get("study_policy", {})
if policy.get("mode") != "ONE_BOOK_AT_A_TIME" or policy.get("rule") != "COMPLETE_CURRENT_WORK_BEFORE_NEXT":
    problems.append("study-policy")
if policy.get("cross_work_synthesis") != "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE":
    problems.append("cross-work-policy")
if policy.get("source_scope") != "USER_PROVIDED_STANDARDIZED_TEXT_ONLY_UNLESS_USER_EXPLICITLY_EXPANDS_SCOPE":
    problems.append("source-scope-policy")
if set(state.get("user_locked_business_constraints", [])) != {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}:
    problems.append("user-locked-constraints")

active_work = state.get("active_work") or {}
work_id = active_work.get("work_id")
active_status = active_work.get("status")
next_pass = active_work.get("next_pass")
if not work_id:
    problems.append("study-state-active-work-missing")
if active_status not in VALID_STATUSES:
    problems.append("study-state-active-status")
if active_status == "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ" and next_pass != "SEQUENTIAL_FULLTEXT_FROM_BEGINNING":
    problems.append("study-state-initial-next-pass")
if active_status in {"ACTIVE__SEQUENTIAL_READ_IN_PROGRESS", "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT"}:
    if not isinstance(next_pass, str) or not next_pass.startswith("SEQUENTIAL_CONTINUE__"):
        problems.append("study-state-progress-next-pass")
    coverage = active_work.get("coverage", {})
    if not re.fullmatch(r"[0-9a-f]{64}", active_work.get("source_sha256", "")):
        problems.append("study-state-source-sha256")
    if not re.fullmatch(r"[0-9a-f]{64}", active_work.get("rolling_ledger_sha256", "")):
        problems.append("study-state-ledger-sha256")
    if not coverage.get("sequential_completed") or not coverage.get("next_location"):
        problems.append("study-state-coverage")
    if not active_work.get("rolling_ledger_file_id"):
        problems.append("study-state-rolling-ledger-id")

queue = state.get("queue", [])
queue_by_id = {w.get("work_id"): w for w in queue}
if work_id not in queue_by_id:
    problems.append("active-work-not-in-queue")
active_queue = [w for w in queue if w.get("status") == "ACTIVE"]
if active_status in ACTIVE_STATUSES and (len(active_queue) != 1 or active_queue[0].get("work_id") != work_id):
    problems.append("queue-active-binding")
if active_status == TERMINAL and (queue_by_id.get(work_id, {}).get("status") != "COMPLETE" or active_queue):
    problems.append("queue-terminal-binding")
if not any(w.get("work_id") == "NORWEGIAN_WOOD" and w.get("status") == "EXCLUDED_BY_USER" for w in queue):
    problems.append("queue-norwegian-excluded")

queue_complete_ids = {w.get("work_id") for w in queue if w.get("status") == "COMPLETE"}
state_complete_ids = {w.get("work_id") for w in state.get("completed_works", [])}
if queue_complete_ids != state_complete_ids:
    problems.append("completed-work-summary-drift")
if active_status in ACTIVE_STATUSES and work_id in state_complete_ids:
    problems.append("active-work-also-completed")
if active_status == TERMINAL and work_id not in state_complete_ids:
    problems.append("terminal-work-not-completed")

cap = next((c for c in caps.get("capabilities", []) if c.get("capability_id") == "large_corpus_distillation"), None)
if cap is None:
    problems.append("uaos-large-corpus-capability-missing")
else:
    required = set(cap.get("required", []))
    if not {"source_identity", "coverage_cursor", "rolling_ledger"}.issubset(required):
        problems.append("uaos-large-corpus-capability-contract")

if (ROOT / "continuity").exists() or (ROOT / "TASK_INDEX.json").exists() or (ROOT / "research/masterworks/INDEX.json").exists():
    problems.append("retired-learning-index-returned")

result = {
    "status": "PASS" if not problems else "FAIL",
    "protocol": "MASTERWORK_DISTILLATION_PROTOCOL@1.0",
    "active_study_binding": work_id,
    "active_status": active_status,
    "completed_studies": sorted(queue_complete_ids),
    "next_pass": next_pass,
    "assurance": "LEARNING_EVIDENCE_ONLY__PROJECT_TRANSFER_PENDING",
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
