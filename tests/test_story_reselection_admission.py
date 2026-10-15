import pytest

from runtime.story_reselection_admission import (
    CandidateContrast,
    ReselectionDecisionReceipt,
    StoryCandidate,
    StoryReselectionAdmissionError,
    admit_pre_draft_architecture,
    admit_story_reselection,
)


def candidates():
    return (
        StoryCandidate(
            candidate_id="A",
            premise="urban future-order suspense",
            engine_family="URBAN_SUSPENSE",
            target_reader="male suspense/brain-hole",
            reader_contract="future information forces costly choices",
            acquisition_hypothesis="first-screen impossible delivery problem",
            serial_sustainability="orders expand into competing futures",
            character_attachment_engine="small-person responsibility and recurring relationships",
            differentiation="city logistics + incomplete future information",
            major_risks=("procedural verification can dominate",),
        ),
        StoryCandidate(
            candidate_id="B",
            premise="closed social survival mystery",
            engine_family="URBAN_SUSPENSE",
            target_reader="suspense ensemble",
            reader_contract="alliances and rules mutate under pressure",
            acquisition_hypothesis="immediate social contradiction",
            serial_sustainability="new institutions and coalition costs",
            character_attachment_engine="shared cost and betrayal",
            differentiation="social bargaining rather than puzzle-only escalation",
            major_risks=("can become repetitive rule-game surface",),
        ),
        StoryCandidate(
            candidate_id="C",
            premise="city-scale hidden institution mystery",
            engine_family="INSTITUTIONAL_MYSTERY",
            target_reader="urban mystery/longform",
            reader_contract="ordinary access reveals layered institutions",
            acquisition_hypothesis="first-screen institutional anomaly",
            serial_sustainability="relationship network and institution counter-agency",
            character_attachment_engine="obligation, debt and conflicting loyalties",
            differentiation="institutional consequences instead of supernatural answer machine",
            major_risks=("worldbuilding exposition overload",),
        ),
    )


def contrasts():
    return (
        CandidateContrast("A", "B", ("READER_CONTRACT", "RELATIONSHIP_ENGINE", "ACQUISITION"), ("contrast:A-B",)),
        CandidateContrast("A", "C", ("STORY_ENGINE", "WORLD_OR_INSTITUTIONAL_LOGIC", "CHARACTER_ATTACHMENT"), ("contrast:A-C",)),
        CandidateContrast("B", "C", ("STORY_ENGINE", "SERIAL_SUSTAINABILITY", "DIFFERENTIATION"), ("contrast:B-C",)),
    )


def valid_receipt(current_project_was_privileged=False, candidate_contrasts=None):
    return ReselectionDecisionReceipt(
        candidates=candidates(),
        candidate_contrasts=contrasts() if candidate_contrasts is None else tuple(candidate_contrasts),
        selected_candidate_id="C",
        pairwise_or_pareto_evidence_refs=("reselection/pareto.json",),
        platform_evidence_refs=("fanqie-current-first-party",),
        learning_synthesis_ref="formal-campaign-synthesis",
        blind_reader_refs=("blind-reader-round-1",),
        adversarial_refs=("red-team-round-1",),
        long_horizon_stress_refs=("100k-300k-800k-stress",),
        rejected_candidate_reasons=("A overweights procedural logic", "B weaker platform differentiation"),
        current_project_was_privileged=current_project_was_privileged,
    )


def test_reselection_is_blocked_before_corpus_and_formal_synthesis_complete():
    with pytest.raises(StoryReselectionAdmissionError):
        admit_story_reselection(
            valid_receipt(),
            corpus_campaign_complete=False,
            formal_cross_work_synthesis_complete=False,
        )


def test_historical_fq001_cannot_be_privileged():
    with pytest.raises(StoryReselectionAdmissionError):
        admit_story_reselection(
            valid_receipt(current_project_was_privileged=True),
            corpus_campaign_complete=True,
            formal_cross_work_synthesis_complete=True,
        )


def test_same_broad_engine_family_is_allowed_when_candidate_difference_is_material_and_evidenced():
    # A and B intentionally share a broad engine family. The system should not force fake
    # diversity when reader contract/relationship/acquisition mechanisms are materially different.
    assert admit_story_reselection(
        valid_receipt(),
        corpus_campaign_complete=True,
        formal_cross_work_synthesis_complete=True,
    ).startswith("STORY_RESELECTION_ADMITTED")


def test_missing_pairwise_material_difference_evidence_is_rejected():
    incomplete = contrasts()[:-1]
    with pytest.raises(StoryReselectionAdmissionError):
        admit_story_reselection(
            valid_receipt(candidate_contrasts=incomplete),
            corpus_campaign_complete=True,
            formal_cross_work_synthesis_complete=True,
        )


def test_pre_draft_architecture_requires_dynamic_hierarchy_and_benchmarks():
    assert admit_pre_draft_architecture(
        selected_candidate_id="C",
        series_end_state_ref="architecture/series-end.md",
        dynamic_hierarchical_outline_refs=(
            "outline/series.md",
            "outline/volume1.md",
            "outline/arc1.md",
            "outline/opening20k.md",
        ),
        canon_or_story_graph_ref="canon/story-graph.json",
        first_20k_packet_ref="outline/opening20k.md",
        benchmark_refs=("acquisition", "attachment", "longform"),
        current_platform_evidence_refs=("fanqie-current",),
    ).startswith("PRE_DRAFT_ARCHITECTURE_ADMITTED")


def test_pre_draft_architecture_rejects_unresolved_blocker():
    with pytest.raises(StoryReselectionAdmissionError):
        admit_pre_draft_architecture(
            selected_candidate_id="C",
            series_end_state_ref="end",
            dynamic_hierarchical_outline_refs=("series", "volume", "arc", "opening"),
            canon_or_story_graph_ref="graph",
            first_20k_packet_ref="opening",
            benchmark_refs=("a", "b", "c"),
            current_platform_evidence_refs=("platform",),
            unresolved_blockers=("reader contract unresolved",),
        )
