from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def test_protocol_still_covers_full_distillation_pipeline():
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


def test_study_state_is_durable_one_book_at_a_time():
    state = json.loads((ROOT / "research/masterworks/STUDY_STATE.json").read_text(encoding="utf-8"))
    assert state["status"] == "ACTIVE"
    assert state["authority_role"] == "SYSTEM_LEARNING_CHECKPOINT_NOT_PROSE_OR_CANON_AUTHORITY"
    assert state["study_policy"]["mode"] == "ONE_BOOK_AT_A_TIME"
    assert state["study_policy"]["rule"] == "COMPLETE_CURRENT_WORK_BEFORE_NEXT"
    assert state["study_policy"]["cross_work_synthesis"] == "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE"
    assert set(state["user_locked_business_constraints"]) == {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}
    assert state["reopenable_design_scope"] == "ALL_OTHER_STORY_DESIGN_MAY_BE_REBUILT_AFTER_LEARNING"
    active = state["active_work"]
    assert active["work_id"] == "GUI_MI_ZHI_ZHU"
    assert active["status"] in {"ACTIVE__PENDING_FIRST_SEQUENTIAL_READ", "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS"}
    if active["status"] == "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ":
        assert active["next_pass"] == "SEQUENTIAL_FULLTEXT_FROM_BEGINNING"
    else:
        assert active["next_pass"].startswith("SEQUENTIAL_CONTINUE__")
        assert len(active["source_sha256"]) == 64
        assert active["coverage"]["sequential_completed"]
        assert active["coverage"]["next_location"]
        assert active["rolling_ledger"]
    assert any(w["work_id"] == "SHIRI_ZHONGYAN" and w["status"] == "COMPLETE" for w in state["queue"])
    assert any(w["work_id"] == "GUI_MI_ZHI_ZHU" and w["status"] == "ACTIVE" for w in state["queue"])
    assert any(w["work_id"] == "NORWEGIAN_WOOD" and w["status"] == "EXCLUDED_BY_USER" for w in state["queue"])


def test_registry_moves_shiri_to_completed_and_guimi_to_active():
    registry = json.loads((ROOT / "research/masterworks/INDEX.json").read_text(encoding="utf-8"))
    state = json.loads((ROOT / "research/masterworks/STUDY_STATE.json").read_text(encoding="utf-8"))
    assert registry["status"] == "ACTIVE"
    assert registry["study_state_ref"] == "research/masterworks/STUDY_STATE.json"
    assert registry["authority_role"] == "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY"
    assert registry["copyright_policy"]["pirated_fulltext_allowed"] is False
    assert registry["copyright_policy"]["store_substitute_for_original_work"] is False
    assert "USER_LAWFULLY_PROVIDED_TEXT" in registry["copyright_policy"]["allowed_sources"]

    active = registry["active_studies"]
    assert len(active) == 1
    assert active[0]["work_id"] == "GUI_MI_ZHI_ZHU"
    assert active[0]["current_status"] == state["active_work"]["status"]
    assert active[0]["next_pass"] == state["active_work"]["next_pass"]
    assert active[0]["execution_authority"] is False

    completed = {s["work_id"]: s for s in registry["completed_studies"]}
    shiri = completed["SHIRI_ZHONGYAN"]
    assert shiri["current_status"] == "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"
    assert shiri["next_pass"] == "NEXT_BOOK__GUI_MI_ZHI_ZHU"
    coverage = shiri["fulltext_coverage"]
    assert coverage["user_source_numbered_mainline_through"] == 1359
    assert coverage["user_source_chapter_heading_occurrences"] == 1360
    assert coverage["source_numbering_anomaly"] == "two distinct headings labelled CH1357"
    assert coverage["sequential_study_completed"] == "SOURCE_ORDER_1-1360"
    assert coverage["body_numbering"] == "CH1-CH1359"
    assert coverage["study_scope"] == "USER_PROVIDED_TEXT_ONLY_PER_USER_DIRECTION"
    assert coverage["official_supplement_status"] == "OUT_OF_SCOPE_FOR_THIS_STUDY"
    assert "MORE_COMPLEXITY_IS_ALWAYS_BETTER" in shiri["explicitly_not_promoted"]
    assert "HYPERINTELLIGENT_PROTAGONIST_TEMPLATE" in shiri["explicitly_not_promoted"]


def test_shiri_evidence_files_remain_present_after_completion():
    paths = [
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md",
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md",
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_03_CHARACTER_ENSEMBLE.md",
        "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_04_MYSTERY_WORLD_RULES.md",
        "research/masterworks/SHIRI_ZHONGYAN/FULLTEXT_CORPUS_INGEST_2026-10-11.md",
    ]
    for rel in paths:
        assert (ROOT / rel).exists()
    p1, p2, p3, p4 = [(ROOT / rel).read_text(encoding="utf-8") for rel in paths[:4]]
    for text in (p1, p2, p3, p4):
        assert "status: LEARNING_EVIDENCE" in text
    assert "NOT PROMOTED" in p1
    assert "PROJECT_TRANSFER_PENDING" in p2
    assert "PROJECT_TRANSFER_PENDING" in p3
    assert "PROJECT_TRANSFER_PENDING" in p4


def test_continuity_indexes_point_to_active_guimi_study():
    canonical = json.loads((ROOT / "continuity/TASK_INDEX.json").read_text(encoding="utf-8"))
    alias = json.loads((ROOT / "TASK_INDEX.json").read_text(encoding="utf-8"))
    c = canonical["system"]["masterwork_learning"]
    a = alias["system"]["masterwork_learning"]
    assert c["protocol_ref"] == "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md"
    assert c["registry_ref"] == "research/masterworks/INDEX.json"
    assert c["study_state_ref"] == "research/masterworks/STUDY_STATE.json"
    assert c["authority_role"] == "LEARNING_EVIDENCE_NOT_EXECUTION_AUTHORITY"
    assert c["active_study"] == "GUI_MI_ZHI_ZHU"
    assert c["completed_studies"] == ["SHIRI_ZHONGYAN"]
    assert c["active_study_ref"] == a["active_study_ref"]


def test_execution_capability_keeps_learning_claim_ceiling():
    caps = json.loads((ROOT / "continuity/EXECUTION_CAPABILITIES.json").read_text(encoding="utf-8"))
    mw = next(c for c in caps["capabilities"] if c["capability_id"] == "masterwork_distillation_and_transfer_learning")
    det = next(c for c in caps["capabilities"] if c["capability_id"] == "deterministic_guards")
    assert mw["assurance_ceiling"] == "SESSION_EXECUTABLE"
    assert "PROJECT_TRANSFER" in mw["scope"]
    assert "CROSS_WORK_TRIANGULATION" in mw["scope"]
    assert "masterwork_distillation_guard.py" in mw["release_enforcement"]
    assert "MASTERWORK_LEARNING_STATE" in det["scope"]
    assert "masterwork_distillation_guard.py" in det["invocation_path"]
    assert any("learning capability, not a prose or Canon authority" in note for note in caps["owner_notes"])
