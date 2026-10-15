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

for retired in ("universal-continuity-agent", "active_lease", "resume_epoch"):
    if retired in rulebook:
        problems.append("retired-authority-semantics:" + retired)
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
if not evolution.get("current_open_items"):
    problems.append("evolution-open-problem-ref-missing")
if not evolution.get("current_problem_refs"):
    problems.append("evolution-problem-map-missing")

result = {
    "status": "PASS" if not problems else "FAIL",
    "controller": manifest.get("controller"),
    "common_behavior_assurance_min": caps.get("common_behavior_assurance_min"),
    "canonical_evolution_evidence_ref": caps.get("canonical_evolution_evidence_ref"),
    "retired_authority_semantics_absent": not any(p.startswith("retired-authority-semantics:") for p in problems),
    "owner_behavior_admission": "runtime/owner_behavior_admission.py",
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
