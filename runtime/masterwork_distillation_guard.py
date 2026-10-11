#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
problems = []
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"
ACTIVE_STATUSES = {"ACTIVE__PENDING_FIRST_SEQUENTIAL_READ", "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS"}
VALID_STATUSES = ACTIVE_STATUSES | {TERMINAL}


def need(rel):
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p


def load(rel):
    p = need(rel)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


protocol_p = need("protocols/MASTERWORK_DISTILLATION_PROTOCOL.md")
registry = load("research/masterworks/INDEX.json")
state = load("research/masterworks/STUDY_STATE.json")
canonical = load("continuity/TASK_INDEX.json")
alias = load("TASK_INDEX.json")
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
    for stage in ("D0 RIGHTS_AND_SOURCE", "D3 COLD_READ_TRACE", "D6 POSITIVE_NEGATIVE_DIFF", "D8 CROSS-WORK_TRIANGULATION", "D9 PROJECT_TRANSFER_EXPERIMENT", "D11 PROMOTION", "D12 STOP / DECAY"):
        if stage not in protocol:
            problems.append("protocol-stage:" + stage)

if registry.get("status") != "ACTIVE":
    problems.append("registry-not-active")
if registry.get("study_state_ref") != "research/masterworks/STUDY_STATE.json":
    problems.append("registry-study-state-ref")
if registry.get("authority_role") != "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY":
    problems.append("registry-authority-role")
cp = registry.get("copyright_policy", {})
if cp.get("pirated_fulltext_allowed") is not False or cp.get("store_substitute_for_original_work") is not False:
    problems.append("copyright-policy")
if "USER_LAWFULLY_PROVIDED_TEXT" not in set(cp.get("allowed_sources", [])):
    problems.append("user-provided-source-not-allowed")

if state.get("status") != "ACTIVE":
    problems.append("study-state-not-active")
policy = state.get("study_policy", {})
if policy.get("mode") != "ONE_BOOK_AT_A_TIME" or policy.get("rule") != "COMPLETE_CURRENT_WORK_BEFORE_NEXT":
    problems.append("study-policy")
if policy.get("cross_work_synthesis") != "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE":
    problems.append("cross-work-policy")
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
if active_status == "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS" and (not isinstance(next_pass, str) or not next_pass.startswith("SEQUENTIAL_CONTINUE__")):
    problems.append("study-state-progress-next-pass")
if active_status == TERMINAL and active_work.get("binding_role") != "CURRENT_FOCUS_BINDING_AFTER_COMPLETION__NOT_IN_PROGRESS":
    problems.append("study-state-terminal-binding-role")

if active_status in {"ACTIVE__SEQUENTIAL_READ_IN_PROGRESS", TERMINAL}:
    cov = active_work.get("coverage", {})
    if not re.fullmatch(r"[0-9a-f]{64}", active_work.get("source_sha256", "")):
        problems.append("study-state-source-sha256")
    if not re.fullmatch(r"[0-9a-f]{64}", active_work.get("rolling_ledger_sha256", "")):
        problems.append("study-state-ledger-sha256")
    if not cov.get("sequential_completed"):
        problems.append("study-state-coverage:sequential_completed")
    if not cov.get("next_location"):
        problems.append("study-state-coverage:next_location")
    if not active_work.get("rolling_ledger") or not active_work.get("rolling_ledger_file_id"):
        problems.append("study-state-rolling-ledger")

queue = state.get("queue", [])
queue_by_id = {w.get("work_id"): w for w in queue}
if work_id and work_id not in queue_by_id:
    problems.append("active-work-not-in-queue")
active_queue = [w for w in queue if w.get("status") == "ACTIVE"]
if active_status in ACTIVE_STATUSES:
    if len(active_queue) != 1 or active_queue[0].get("work_id") != work_id:
        problems.append("queue-active-binding")
elif active_status == TERMINAL:
    if queue_by_id.get(work_id, {}).get("status") != "COMPLETE":
        problems.append("queue-terminal-binding")
    if active_queue:
        problems.append("queue-terminal-has-active-work")
if not any(w.get("work_id") == "NORWEGIAN_WOOD" and w.get("status") == "EXCLUDED_BY_USER" for w in queue):
    problems.append("queue-norwegian-excluded")

active_studies = registry.get("active_studies", [])
if len(active_studies) != 1 or active_studies[0].get("work_id") != work_id:
    problems.append("registry-active-study-binding")
else:
    reg = active_studies[0]
    if reg.get("execution_authority") is not False:
        problems.append("active-study-authority-inflation")
    if reg.get("current_status") != active_status:
        problems.append("active-study-status-drift")
    if reg.get("next_pass") != next_pass:
        problems.append("active-study-next-pass-drift")
    for field in ("source_file_id", "source_sha256", "rolling_ledger_file_id", "rolling_ledger_sha256"):
        if active_work.get(field) and reg.get(field) != active_work.get(field):
            problems.append("active-study-binding-drift:" + field)

completed = {s.get("work_id"): s for s in registry.get("completed_studies", [])}
queue_complete_ids = {w.get("work_id") for w in queue if w.get("status") == "COMPLETE"}
missing_completed = sorted(w for w in queue_complete_ids if w not in completed)
if missing_completed:
    problems.append("registry-missing-completed:" + ",".join(missing_completed))
if active_status in ACTIVE_STATUSES and work_id in completed:
    problems.append("active-work-also-completed")
if active_status == TERMINAL and work_id not in completed:
    problems.append("terminal-work-not-completed")

for label, idx in (("canonical", canonical), ("alias", alias)):
    learning = idx.get("system", {}).get("masterwork_learning", {})
    if learning.get("registry_ref") != "research/masterworks/INDEX.json":
        problems.append(label + "-registry-ref")
    if learning.get("study_state_ref") != "research/masterworks/STUDY_STATE.json":
        problems.append(label + "-study-state-ref")
    if learning.get("active_study") != work_id:
        problems.append(label + "-active-study-binding")
    if set(learning.get("completed_studies", [])) != queue_complete_ids:
        problems.append(label + "-completed-studies-drift")
if alias.get("system", {}).get("masterwork_learning", {}).get("active_study_ref") != canonical.get("system", {}).get("masterwork_learning", {}).get("active_study_ref"):
    problems.append("compat-index-masterwork-drift")

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
