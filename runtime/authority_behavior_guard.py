#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
problems: list[str] = []


def load_json(rel: str) -> dict:
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


manifest = load_json(".uaos/MANIFEST.json")
adapter = load_json(".uaos/ADAPTER.json")
caps = load_json(".uaos/CAPABILITIES.json")
evolution = load_json("audits/EVOLUTION_INDEX.json")
rulebook_p = ROOT / "protocols/ACTIVE_RULEBOOK.md"
if not rulebook_p.exists():
    problems.append("missing:protocols/ACTIVE_RULEBOOK.md")
    rulebook = ""
else:
    rulebook = rulebook_p.read_text(encoding="utf-8")

if manifest.get("controller") != "D1traverser-debug/universal-agent-os@main":
    problems.append("manifest-controller")
if adapter.get("task_identity_authority") != "UAOS" or adapter.get("cross_chat_continuity_authority") != "UAOS":
    problems.append("adapter-uaos-authority")

# Historical names may appear only to state that they are retired. Reject the old
# executable requirements themselves, not every textual mention of their names.
for retired_active_pattern in (
    "Global discovery/routing/single-writer lease: `D1traverser-debug/universal-continuity-agent@main`",
    "verify this chat owns `active_lease + resume_epoch`",
    "Before any material checkpoint write, re-read Universal task manifest",
):
    if retired_active_pattern in rulebook:
        problems.append("retired-active-authority-semantics:" + retired_active_pattern)
if "`universal-continuity-agent`, `active_lease`, `resume_epoch` and retired Novel controller surfaces are historical only" not in rulebook:
    problems.append("retired-authority-quarantine-marker-missing")
if "D1traverser-debug/universal-agent-os@main" not in rulebook:
    problems.append("rulebook-current-parent-missing")
if "runtime/owner_behavior_admission.py" not in rulebook:
    problems.append("rulebook-owner-admission-ref-missing")
if "audits/EVOLUTION_INDEX.json" not in rulebook:
    problems.append("rulebook-evolution-index-ref-missing")

if caps.get("common_behavior_assurance_min") != "1.2.0":
    problems.append("common-behavior-min")
if caps.get("canonical_evolution_evidence_ref") != "audits/EVOLUTION_INDEX.json":
    problems.append("canonical-evolution-ref")
cap_ids = {c.get("capability_id") for c in caps.get("capabilities", [])}
for cap_id in ("recover_before_user_escalation", "problem_to_action_closure"):
    if cap_id not in cap_ids:
        problems.append("missing-common-behavior-capability:" + cap_id)

if evolution.get("owner") != "DOMAIN:novel":
    problems.append("evolution-owner")
if evolution.get("common_behavior_assurance_min") != "1.2.0":
    problems.append("evolution-common-behavior-min")
open_items = evolution.get("current_open_items")
current_refs = evolution.get("current_problem_refs")
resolved = evolution.get("recent_resolved_or_promoted")
if not isinstance(open_items, list):
    problems.append("evolution-open-items-not-list")
if not isinstance(current_refs, dict):
    problems.append("evolution-problem-map-not-object")
if isinstance(open_items, list) and isinstance(current_refs, dict):
    if set(open_items) != set(current_refs):
        problems.append("evolution-open-item-map-mismatch")
if not isinstance(resolved, list) or not resolved:
    problems.append("evolution-resolved-history-missing")
else:
    if not any(row.get("problem_ref") == "N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR" for row in resolved if isinstance(row, dict)):
        problems.append("evolution-current-promotion-receipt-missing")

result = {
    "status": "PASS" if not problems else "FAIL",
    "controller": manifest.get("controller"),
    "common_behavior_assurance_min": caps.get("common_behavior_assurance_min"),
    "canonical_evolution_evidence_ref": caps.get("canonical_evolution_evidence_ref"),
    "retired_active_authority_semantics_absent": not any(
        p.startswith("retired-active-authority-semantics:") for p in problems
    ),
    "owner_behavior_admission": "runtime/owner_behavior_admission.py",
    "open_evolution_items": len(open_items) if isinstance(open_items, list) else None,
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
