import pytest

from runtime.learning_transfer_admission import (
    ClosedContextReconstruction,
    CrossWorkComparisonReceipt,
    LearningTransferAdmissionError,
    ObservationRef,
    PromotionEvidenceBundle,
    SharedFactorAssessment,
    TransferProbeReceipt,
    admit_active_rule_promotion,
    admit_closed_context_reconstruction,
    admit_interbook_comparison,
    admit_transfer_probe,
)


def test_closed_context_reconstruction_requires_mechanisms_and_boundaries():
    receipt = ClosedContextReconstruction(
        work_id="GUI_MI_ZHI_ZHU",
        compact_index_ref="research/masterworks/MECHANISM_REGISTRY.json",
        recalled_mechanisms=("M001", "M002"),
        recalled_boundaries=("central genius can flatten ensemble agency",),
        missed_or_distorted=("relationship engine underweighted",),
        correction_refs=("GUI_MI_ZHI_ZHU ledger",),
    )
    assert admit_closed_context_reconstruction(receipt) == "CLOSED_CONTEXT_RECONSTRUCTION_ADMITTED"


def valid_comparison(**overrides):
    payload = dict(
        claim_id="M005_RELATIONSHIP_ADHESION_REQUIRES_COST",
        target_dimensions=("N05_RELATIONSHIP_NETWORK_ARCS", "N08_EMOTION_TENSION_READER_AFFECT"),
        observations=(
            ObservationRef("SHIRI_ZHONGYAN", "ledger:relationship-cost", "SUPPORT", "ARC"),
            ObservationRef("DAO_MU_BI_JI", "ledger:shared-survival-cost", "SUPPORT", "VOLUME"),
        ),
        comparison_designs=("CROSS_GENRE_SAME_FUNCTION",),
        shared_factor_assessments=(
            SharedFactorAssessment(
                factor_id="F_GENRE",
                affected_work_ids=("SHIRI_ZHONGYAN", "DAO_MU_BI_JI"),
                relevance_to_claim="MEDIUM",
                rationale="both use suspense but different surface engines",
                mitigation_or_contrast="compare function rather than trope surface and seek later literary counterexample",
            ),
        ),
        common_or_candidate_mechanisms=("shared cost changes trust/debt",),
        conflicts_or_boundary_conditions=("rescue without reciprocal agency may not build durable attachment",),
        negative_evidence_refs=("ledger:automatic-rescuer-risk",),
        alternative_explanations=("repetition/familiarity rather than shared cost may explain attachment",),
        updated_observation_axes=("time-to-first relationship delta", "reciprocal agency"),
        unresolved_confounds=("target-reader difference",),
        promotion_requested=False,
    )
    payload.update(overrides)
    return CrossWorkComparisonReceipt(**payload)


def test_interbook_comparison_is_claim_conditioned_not_family_counted():
    completed = {"SHIRI_ZHONGYAN", "GUI_MI_ZHI_ZHU", "DAO_MU_BI_JI"}
    assert admit_interbook_comparison(valid_comparison(), completed_work_ids=completed) == (
        "INTERBOOK_COMPARISON_ADMITTED__CLAIM_CONDITIONED__NON_PROMOTIONAL"
    )


def test_same_author_or_series_is_not_automatic_merge_key():
    receipt = CrossWorkComparisonReceipt(
        claim_id="within-author-structure-variation",
        target_dimensions=("N02_DISCOURSE_TEMPORAL_ORDER", "N07_INFORMATION_MYSTERY_REVELATION"),
        observations=(
            ObservationRef("DEVOTION_OF_SUSPECT_X", "future:devotion-structure", "SUPPORT", "WORK"),
            ObservationRef("MALICE", "future:malice-structure", "CONTRADICT", "WORK"),
        ),
        comparison_designs=("WITHIN_AUTHOR_CROSS_WORK",),
        shared_factor_assessments=(
            SharedFactorAssessment(
                factor_id="F_AUTHOR",
                affected_work_ids=("DEVOTION_OF_SUSPECT_X", "MALICE"),
                relevance_to_claim="HIGH",
                rationale="same author is intentionally held partly constant to test within-author structural variation",
                mitigation_or_contrast="do not generalize beyond author; later pair with cross-author same-genre comparison",
            ),
        ),
        common_or_candidate_mechanisms=("author can vary revelation architecture across works",),
        conflicts_or_boundary_conditions=("author identity does not imply identical structure",),
        negative_evidence_refs=("future:counterexample",),
        alternative_explanations=("genre/subgenre or publication context may drive variation",),
        updated_observation_axes=("revelation order", "narrator reliability"),
        unresolved_confounds=("publication context",),
    )
    completed = {"DEVOTION_OF_SUSPECT_X", "MALICE"}
    assert admit_interbook_comparison(receipt, completed_work_ids=completed).startswith("INTERBOOK_COMPARISON_ADMITTED")


def test_material_shared_factor_cannot_be_silently_ignored():
    receipt = valid_comparison(
        shared_factor_assessments=(
            SharedFactorAssessment(
                factor_id="F_AUTHOR",
                affected_work_ids=("SHIRI_ZHONGYAN", "DAO_MU_BI_JI"),
                relevance_to_claim="UNKNOWN",
                rationale="unknown relevance",
                mitigation_or_contrast="",
            ),
        )
    )
    with pytest.raises(LearningTransferAdmissionError):
        admit_interbook_comparison(receipt, completed_work_ids={"SHIRI_ZHONGYAN", "DAO_MU_BI_JI"})


def test_interbook_comparison_cannot_promote_during_active_campaign():
    with pytest.raises(LearningTransferAdmissionError):
        admit_interbook_comparison(
            valid_comparison(promotion_requested=True),
            completed_work_ids={"SHIRI_ZHONGYAN", "DAO_MU_BI_JI"},
        )


def test_transfer_probe_requires_target_dimensions_and_adversarial_review():
    receipt = TransferProbeReceipt(
        capability_id="C05_RELATIONSHIP",
        target_case_id="synthetic-urban-suspense-01",
        target_dimensions=("N05_RELATIONSHIP_NETWORK_ARCS", "N08_EMOTION_TENSION_READER_AFFECT"),
        source_mechanism_ids=("M005_RELATIONSHIP_ADHESION_REQUIRES_COST",),
        alternatives=("shared operational risk", "conflicting obligation"),
        predicted_gain=("earlier attachment",),
        predicted_side_effects=("may slow mystery exposition",),
        adversarial_findings=("do not copy tomb-adventure rescue surface",),
        outcome="SUPPORTED",
        evidence_refs=("benchmark:synthetic-urban-suspense-01",),
    )
    assert admit_transfer_probe(receipt) == "TRANSFER_PROBE_ADMITTED"


def valid_promotion(**overrides):
    payload = dict(
        mechanism_id="M005",
        target_dimensions=("N05_RELATIONSHIP_NETWORK_ARCS",),
        comparison_receipt_refs=("within-author-contrast", "cross-genre-function-match"),
        comparison_designs=("WITHIN_AUTHOR_CROSS_WORK", "CROSS_GENRE_SAME_FUNCTION"),
        supporting_work_ids=("A", "B", "C", "D"),
        boundary_or_contradiction_refs=("counterexample",),
        resolved_high_relevance_factor_refs=("author-held-constant", "genre-crossed"),
        unresolved_high_relevance_factors=(),
        transfer_probe_refs=("probe-1", "probe-2"),
        external_or_live_outcome_refs=("project-benchmark",),
    )
    payload.update(overrides)
    return PromotionEvidenceBundle(**payload)


def test_active_rule_promotion_blocked_before_campaign_complete():
    with pytest.raises(LearningTransferAdmissionError):
        admit_active_rule_promotion(valid_promotion(), corpus_campaign_complete=False)


def test_active_rule_promotion_rejects_unresolved_high_relevance_confound():
    with pytest.raises(LearningTransferAdmissionError):
        admit_active_rule_promotion(
            valid_promotion(
                target_dimensions=("N11_PROSE_STYLOMETRY_SURFACE",),
                comparison_designs=("WITHIN_AUTHOR_CROSS_WORK", "WITHIN_SERIES_CROSS_STAGE"),
                unresolved_high_relevance_factors=("F_AUTHOR",),
            ),
            corpus_campaign_complete=True,
        )


def test_active_rule_promotion_uses_multiple_comparison_designs_not_fixed_author_counts():
    assert admit_active_rule_promotion(valid_promotion(), corpus_campaign_complete=True).startswith(
        "ACTIVE_RULE_PROMOTION_ADMITTED"
    )
