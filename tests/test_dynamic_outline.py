import pytest

from runtime.dynamic_outline import (
    DynamicOutline,
    OutlineAdmissionError,
    OutlineNode,
    ReplanReceipt,
    admit_replan,
    descendant_ids,
    validate_outline,
)


def outline():
    return DynamicOutline(
        nodes=(
            OutlineNode("series", "SERIES", None, "FAR", "FLEXIBLE", "series transformation", ("series-end",), ("promise-main",), (), ("candidate-winner",)),
            OutlineNode("volume1", "VOLUME", "series", "MID", "FLEXIBLE", "volume change", ("vol-turn",), ("promise-v1",), ("series",), ("architecture",)),
            OutlineNode("arc1", "ARC", "volume1", "MID", "FLEXIBLE", "arc change", ("arc-turn",), ("promise-a1",), ("volume1",), ("architecture",)),
            OutlineNode("opening", "PACKET", "arc1", "NEAR", "FROZEN", "first 20k acquisition packet", ("first-payoff", "relationship-entry"), ("promise-open",), ("arc1",), ("signing-benchmark",)),
            OutlineNode("ch1", "CHAPTER", "opening", "NEAR", "FLEXIBLE", "opening chapter", ("reader-question",), ("promise-open",), ("opening",), ("chapter-contract",)),
        ),
        intended_series_end_ref="architecture/series-end",
        current_opening_packet_ref="outline/opening20k",
    )


def test_dynamic_outline_valid_and_descendants_are_traceable():
    assert validate_outline(outline()) == "DYNAMIC_OUTLINE_VALID"
    assert set(descendant_ids(outline(), ("arc1",))) == {"arc1", "opening", "ch1"}


def test_replan_rejects_first_idea_execution_and_underdeclared_impact():
    with pytest.raises(OutlineAdmissionError):
        admit_replan(
            outline(),
            ReplanReceipt(
                changed_node_ids=("arc1",),
                trigger_refs=("reader-signal",),
                alternatives_considered=("only-one",),
                selected_change="change arc",
                rejected_alternative_reasons=("none",),
                invalidated_refs=("arc1",),
                downstream_review_refs=("review",),
                hard_failure_or_live_signal_refs=("reader-signal",),
            ),
        )


def test_frozen_change_requires_hard_failure_or_live_signal():
    with pytest.raises(OutlineAdmissionError):
        admit_replan(
            outline(),
            ReplanReceipt(
                changed_node_ids=("opening",),
                trigger_refs=("new craft article",),
                alternatives_considered=("change", "keep"),
                selected_change="change opening",
                rejected_alternative_reasons=("keep underperforms hypothesis",),
                invalidated_refs=("opening", "ch1"),
                downstream_review_refs=("packet-review",),
                hard_failure_or_live_signal_refs=(),
            ),
        )


def test_near_but_flexible_chapter_can_improve_before_acceptance_without_live_failure():
    assert admit_replan(
        outline(),
        ReplanReceipt(
            changed_node_ids=("ch1",),
            trigger_refs=("adversarial-review:new-opening-option",),
            alternatives_considered=("reorder reveal", "keep baseline"),
            selected_change="reorder reveal",
            rejected_alternative_reasons=("baseline has slower immediate causal clarity",),
            invalidated_refs=("ch1",),
            downstream_review_refs=("chapter-review",),
            hard_failure_or_live_signal_refs=(),
        ),
    ).startswith("REPLAN_ADMITTED")


def test_replan_cannot_silently_mutate_canon():
    with pytest.raises(OutlineAdmissionError):
        admit_replan(
            outline(),
            ReplanReceipt(
                changed_node_ids=("opening",),
                trigger_refs=("platform-rejection",),
                alternatives_considered=("change", "keep"),
                selected_change="change opening",
                rejected_alternative_reasons=("keep preserves observed weakness",),
                invalidated_refs=("opening", "ch1"),
                downstream_review_refs=("packet-review",),
                hard_failure_or_live_signal_refs=("platform-rejection",),
                canon_change_requested=True,
            ),
        )


def test_evidence_driven_frozen_replan_is_admitted_when_scope_and_review_complete():
    assert admit_replan(
        outline(),
        ReplanReceipt(
            changed_node_ids=("opening",),
            trigger_refs=("platform-rejection", "blind-reader-drop"),
            alternatives_considered=("frontload payoff", "frontload relationship", "keep baseline"),
            selected_change="combine earlier payoff with relationship engine",
            rejected_alternative_reasons=("payoff-only weak attachment", "baseline external signal failed"),
            invalidated_refs=("opening", "ch1"),
            downstream_review_refs=("packet-review", "continuity-review"),
            hard_failure_or_live_signal_refs=("platform-rejection",),
        ),
    ).startswith("REPLAN_ADMITTED")
