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
    assert study["next_pass"] == "PASS_03_CHARACTER_ENSEMBLE_AND_ATTACHMENT"
    assert "MORE_COMPLEXITY_IS_ALWAYS_BETTER" in study["explicitly_not_promoted"]
    for rel in study["completed_passes"]:
        assert (ROOT / rel).exists()


def test_ten_day_endgame_passes_have_claim_and_imitation_boundaries():
    p1 = (ROOT / "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md").read_text(encoding="utf-8")
    p2 = (ROOT / "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md").read_text(encoding="utf-8")
    assert "status: LEARNING_EVIDENCE" in p1
    assert "status: LEARNING_EVIDENCE" in p2
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
