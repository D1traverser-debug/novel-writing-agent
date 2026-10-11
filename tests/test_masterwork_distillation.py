from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def test_masterwork_distillation_protocol_is_broad_and_not_user_prompt_dependent():
    text = (ROOT / "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md").read_text(encoding="utf-8")
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
        assert stage in text
    for dimension in (
        "psychological portrayal",
        "environmental / spatial description",
        "plot causality and progression",
        "dialogue / subtext / voice",
        "POV / psychic distance",
        "emotional progression",
        "quality audit",
    ):
        assert dimension.lower() in text.lower()
    assert "视为 C20 meta-learning incident" in text


def test_masterwork_registry_is_learning_evidence_not_execution_authority():
    registry = json.loads((ROOT / "research/masterworks/INDEX.json").read_text(encoding="utf-8"))
    assert registry["status"] == "ACTIVE"
    assert registry["authority_role"] == "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY"
    assert registry["copyright_policy"]["pirated_fulltext_allowed"] is False
    assert registry["copyright_policy"]["store_substitute_for_original_work"] is False
    study = registry["active_studies"][0]
    assert study["work_id"] == "SHIRI_ZHONGYAN"
    assert study["execution_authority"] is False
    assert study["current_status"] == "OPENING_CHARACTER_ENSEMBLE_MYSTERY_WORLD_DISTILLED__PROJECT_TRANSFER_PENDING"
    assert study["next_pass"] == "PASS_05_PACING_ENGINE_ROTATION_AND_CONVERGENCE"
    assert "MORE_COMPLEXITY_IS_ALWAYS_BETTER" in study["explicitly_not_promoted"]
    assert "PROTAGONIST_SECRET_MASTERMIND_AS_UNIVERSAL_RETENTION_TOOL" in study["explicitly_not_promoted"]
    assert len(study["completed_passes"]) == 4
    for rel in study["completed_passes"]:
        assert (ROOT / rel).exists()


def test_ten_day_endgame_passes_have_claim_and_imitation_boundaries():
    paths = [
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md",
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md",
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_03_CHARACTER_ENSEMBLE.md",
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_04_MYSTERY_WORLD_RULES.md",
    ]
    p1, p2, p3, p4 = [(ROOT / path).read_text(encoding="utf-8") for path in paths]
    for text in (p1, p2, p3, p4):
        assert "status: LEARNING_EVIDENCE" in text
    assert "NOT PROMOTED" in p1
    assert "no pirated full-text storage" in p1
    assert "does not prove the full 1496-chapter work has been line-by-line analyzed" in p2
    assert "does not authorize imitation" in p2
    for heading in (
        "Psychological portrayal",
        "Environment and spatial description",
        "Dialogue and voice",
        "Plot progression",
        "Chapter architecture / hooks",
        "Emotion and attachment",
    ):
        assert heading in p2
    for concept in ("Independent agency", "Character familiarity", "Voice", "Attachment object", "Emotional progression"):
        assert concept.lower() in p3.lower()
    for concept in ("Rule design", "Worldbuilding", "Information asymmetry", "Mystery ladder", "Complexity is not the goal"):
        assert concept.lower() in p4.lower()
    assert "PROJECT_TRANSFER_PENDING" in p2
    assert "PROJECT_TRANSFER_PENDING" in p3
    assert "PROJECT_TRANSFER_PENDING" in p4


def test_continuity_index_binds_masterwork_learning_without_promoting_it():
    canonical = json.loads((ROOT / "continuity/TASK_INDEX.json").read_text(encoding="utf-8"))
    alias = json.loads((ROOT / "TASK_INDEX.json").read_text(encoding="utf-8"))
    c = canonical["system"]["masterwork_learning"]
    a = alias["system"]["masterwork_learning"]
    assert c["protocol_ref"] == "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md"
    assert c["registry_ref"] == "research/masterworks/INDEX.json"
    assert c["authority_role"] == "LEARNING_EVIDENCE_NOT_EXECUTION_AUTHORITY"
    assert c["active_study"] == "SHIRI_ZHONGYAN"
    assert c["active_study_ref"] == a["active_study_ref"]
    assert c["copyright_rule"] == "OFFICIAL_OR_LAWFUL_SOURCES_ONLY_NO_PIRATED_FULLTEXT"


def test_execution_capability_registers_masterwork_learning_with_claim_ceiling():
    caps = json.loads((ROOT / "continuity/EXECUTION_CAPABILITIES.json").read_text(encoding="utf-8"))
    mw = next(c for c in caps["capabilities"] if c["capability_id"] == "masterwork_distillation_and_transfer_learning")
    det = next(c for c in caps["capabilities"] if c["capability_id"] == "deterministic_guards")
    assert mw["assurance_ceiling"] == "SESSION_EXECUTABLE"
    assert "PROJECT_TRANSFER" in mw["scope"]
    assert "POSITIVE_NEGATIVE_DIFF" in mw["scope"]
    assert "CROSS_WORK_TRIANGULATION" in mw["scope"]
    assert "masterwork_distillation_guard.py" in mw["release_enforcement"]
    assert "MASTERWORK_LEARNING_STATE" in det["scope"]
    assert "masterwork_distillation_guard.py" in det["invocation_path"]
    assert any("learning capability, not a prose or Canon authority" in note for note in caps["owner_notes"])
