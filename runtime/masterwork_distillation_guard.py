#!/usr/bin/env python3
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
problems = []

EXPECTED_STATUS = "USER_FULLTEXT_MAINLINE_INGESTED__CH1_CH10_DEEP_READ__SEQUENTIAL_FULL_COVERAGE_ACTIVE"
EXPECTED_NEXT = "SEQUENTIAL_FULLTEXT_CH11_PLUS_PASS_05_PACING_ENGINE_ROTATION_AND_CONVERGENCE"
EXPECTED_FULLTEXT_SHA = "4236619fe12174798682716433d425e2351dac643c9fcb014f6876356ce667ba"
INGEST_REL = "research/masterworks/SHIRI_ZHONGYAN/FULLTEXT_CORPUS_INGEST_2026-10-11.md"

def need(rel):
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p

protocol_p = need("protocols/MASTERWORK_DISTILLATION_PROTOCOL.md")
index_p = need("research/masterworks/INDEX.json")
pass_paths = [
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_03_CHARACTER_ENSEMBLE.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_04_MYSTERY_WORLD_RULES.md",
]
pass_files = [need(rel) for rel in pass_paths]
ingest_p = need(INGEST_REL)
canonical_idx_p = need("continuity/TASK_INDEX.json")
alias_idx_p = need("TASK_INDEX.json")

if not problems:
    protocol = protocol_p.read_text(encoding="utf-8")
    registry = json.loads(index_p.read_text(encoding="utf-8"))
    passes = [p.read_text(encoding="utf-8") for p in pass_files]
    ingest = ingest_p.read_text(encoding="utf-8")
    canonical = json.loads(canonical_idx_p.read_text(encoding="utf-8"))
    alias = json.loads(alias_idx_p.read_text(encoding="utf-8"))

    if "status: ACTIVE_SYSTEM_PROTOCOL" not in protocol:
        problems.append("protocol-not-active")
    for stage in ("D0 RIGHTS_AND_SOURCE","D3 COLD_READ_TRACE","D6 POSITIVE_NEGATIVE_DIFF","D8 CROSS-WORK_TRIANGULATION","D9 PROJECT_TRANSFER_EXPERIMENT","D11 PROMOTION","D12 STOP / DECAY"):
        if stage not in protocol:
            problems.append("protocol-stage:"+stage)
    for concept in ("Psychological portrayal","Environment / atmosphere","Plot progression","Dialogue","Emotion","Quality audit"):
        if concept not in protocol:
            problems.append("microcraft-gap:"+concept)
    if "盗版" in protocol and "禁止" not in protocol:
        problems.append("copyright-boundary-ambiguous")

    if registry.get("status") != "ACTIVE":
        problems.append("registry-not-active")
    if registry.get("authority_role") != "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY":
        problems.append("registry-authority-role")
    copyright_policy = registry.get("copyright_policy", {})
    if copyright_policy.get("pirated_fulltext_allowed") is not False:
        problems.append("pirated-fulltext-not-denied")
    if copyright_policy.get("store_substitute_for_original_work") is not False:
        problems.append("copyright-substitute-risk")
    allowed_sources = set(copyright_policy.get("allowed_sources", []))
    if "USER_LAWFULLY_PROVIDED_TEXT" not in allowed_sources:
        problems.append("user-provided-source-not-allowed")

    studies = registry.get("active_studies", [])
    if len(studies) != 1 or studies[0].get("work_id") != "SHIRI_ZHONGYAN":
        problems.append("active-study-binding")
        study = {}
    else:
        study = studies[0]
        if study.get("execution_authority") is not False:
            problems.append("masterwork-promoted-to-execution-authority")
        expected_evidence = set(pass_paths + [INGEST_REL])
        if not expected_evidence.issubset(set(study.get("completed_passes", []))):
            problems.append("study-pass-registry-drift")
        for rejected in (
            "MORE_COMPLEXITY_IS_ALWAYS_BETTER",
            "MANDATORY_AUTOBIOGRAPHY_CHAPTERS",
            "DEATH_GAME_TEMPLATE",
            "HYPERINTELLIGENT_PROTAGONIST_TEMPLATE",
        ):
            if rejected not in study.get("explicitly_not_promoted", []):
                problems.append("anti-overfit-missing:"+rejected)
        if study.get("next_pass") != EXPECTED_NEXT:
            problems.append("next-pass-drift")
        if study.get("current_status") != EXPECTED_STATUS:
            problems.append("study-status-drift")

        coverage = study.get("fulltext_coverage", {})
        expected_coverage = {
            "user_source_sha256": EXPECTED_FULLTEXT_SHA,
            "user_source_numbered_mainline_through": 1359,
            "user_source_chapter_heading_occurrences": 1360,
            "source_numbering_anomaly": "two distinct headings labelled CH1357",
            "fanqie_current_catalog_chapters": 1496,
            "current_catalog_supplement_gap": "CH1360-CH1496",
            "deep_read_completed": "CH1-CH10",
            "deep_read_pending": "CH11-CH1359",
            "official_supplement_pending": "CH1360-CH1496",
        }
        for key, value in expected_coverage.items():
            if coverage.get(key) != value:
                problems.append("fulltext-coverage-drift:"+key)
        ledger = coverage.get("coverage_ledger", "")
        if "十日终焉_1496章全书覆盖台账" not in ledger:
            problems.append("fulltext-coverage-ledger-missing")

    for i, text in enumerate(passes, start=1):
        if "status: LEARNING_EVIDENCE" not in text:
            problems.append(f"pass{i}:authority-inflation")
    if "status: LEARNING_EVIDENCE" not in ingest:
        problems.append("fulltext-ingest:authority-inflation")
    for required in (
        EXPECTED_FULLTEXT_SHA,
        "第1359章 终：完结感言",
        "CH1360–CH1496",
        "CH1_CH10_DEEP_READ_FROM_USER_FULLTEXT",
        "does not contain the current post-completion catalog additions",
    ):
        if required not in ingest:
            problems.append("fulltext-ingest-evidence-gap:"+required)
    if "NOT PROMOTED" not in passes[0]:
        problems.append("pass1:no-negative-promotion-boundary")
    if "Current assurance: `OPENING_PACKET_LEARNING_EVIDENCE__PROJECT_TRANSFER_PENDING`" not in passes[1]:
        problems.append("pass2-claim-boundary")
    if "Current assurance: `CHARACTER_ENSEMBLE_LEARNING_EVIDENCE__PROJECT_TRANSFER_PENDING`" not in passes[2]:
        problems.append("pass3-claim-boundary")
    if "Current assurance: `MYSTERY_WORLD_LEARNING_EVIDENCE__PROJECT_TRANSFER_PENDING`" not in passes[3]:
        problems.append("pass4-claim-boundary")
    for skill in ("Psychological portrayal","Environment and spatial description","Dialogue and voice","Plot progression","Chapter architecture / hooks","Emotion and attachment"):
        if skill not in passes[1]:
            problems.append("pass2-skill-gap:"+skill)
    for skill in ("Independent agency","Character familiarity","Voice","Attachment object","Emotional progression"):
        if skill.lower() not in passes[2].lower():
            problems.append("pass3-skill-gap:"+skill)
    for skill in ("Rule design","Worldbuilding","Information asymmetry","Mystery ladder","Complexity is not the goal"):
        if skill.lower() not in passes[3].lower():
            problems.append("pass4-skill-gap:"+skill)

    c_learning = canonical.get("system", {}).get("masterwork_learning", {})
    a_learning = alias.get("system", {}).get("masterwork_learning", {})
    if c_learning.get("protocol_ref") != "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md":
        problems.append("canonical-index-protocol-ref")
    if c_learning.get("registry_ref") != "research/masterworks/INDEX.json":
        problems.append("canonical-index-registry-ref")
    if c_learning.get("authority_role") != "LEARNING_EVIDENCE_NOT_EXECUTION_AUTHORITY":
        problems.append("canonical-index-authority-boundary")
    if c_learning.get("active_study") != "SHIRI_ZHONGYAN":
        problems.append("canonical-index-active-study")
    if a_learning.get("active_study_ref") != c_learning.get("active_study_ref"):
        problems.append("compat-index-masterwork-drift")

result = {
    "status": "PASS" if not problems else "FAIL",
    "protocol": "MASTERWORK_DISTILLATION_PROTOCOL@1.0",
    "active_study": "SHIRI_ZHONGYAN",
    "source_mode": "USER_FULLTEXT_MAINLINE_PLUS_OFFICIAL_SUPPLEMENT",
    "deep_read_completed": study.get("fulltext_coverage", {}).get("deep_read_completed") if isinstance(study, dict) else None,
    "deep_read_pending": study.get("fulltext_coverage", {}).get("deep_read_pending") if isinstance(study, dict) else None,
    "official_supplement_pending": study.get("fulltext_coverage", {}).get("official_supplement_pending") if isinstance(study, dict) else None,
    "next_pass": EXPECTED_NEXT,
    "assurance": "LEARNING_EVIDENCE_ONLY__PROJECT_TRANSFER_PENDING",
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
