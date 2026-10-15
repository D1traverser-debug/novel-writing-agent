import pytest

from runtime.story_dependency_graph import (
    CanonPromotionReceipt,
    StoryDependencyGraph,
    StoryEdge,
    StoryGraphError,
    StoryNode,
    admit_canon_promotion,
    invalidation_closure,
    validate_graph,
)


def graph():
    return StoryDependencyGraph(
        nodes=(
            StoryNode("premise", "STORY_PREMISE", "CANDIDATE", ("candidate:A",)),
            StoryNode("arc", "OUTLINE_NODE", "PLAN", ("outline:arc",)),
            StoryNode("promise", "READER_PROMISE", "PLAN", ("outline:promise",)),
            StoryNode("event", "EVENT", "PLAN", ("outline:event",)),
        ),
        edges=(
            StoryEdge("arc", "premise", "DEPENDS_ON", ("architecture",)),
            StoryEdge("promise", "arc", "DEPENDS_ON", ("architecture",)),
            StoryEdge("event", "arc", "DEPENDS_ON", ("architecture",)),
        ),
    )


def test_graph_validates_and_computes_downstream_invalidation():
    assert validate_graph(graph()) == "STORY_DEPENDENCY_GRAPH_VALID"
    assert set(invalidation_closure(graph(), ("premise",))) == {"premise", "arc", "promise", "event"}


def test_dependency_cycle_is_rejected():
    bad = StoryDependencyGraph(
        nodes=(
            StoryNode("a", "OUTLINE_NODE", "PLAN", ("a",)),
            StoryNode("b", "OUTLINE_NODE", "PLAN", ("b",)),
        ),
        edges=(
            StoryEdge("a", "b", "DEPENDS_ON", ("e1",)),
            StoryEdge("b", "a", "DEPENDS_ON", ("e2",)),
        ),
    )
    with pytest.raises(StoryGraphError):
        validate_graph(bad)


def test_plan_cannot_become_canon_without_accepted_prose_and_reconciliation():
    with pytest.raises(StoryGraphError):
        admit_canon_promotion(
            graph(),
            CanonPromotionReceipt(
                node_ids=("event",),
                accepted_prose_refs=(),
                acceptance_refs=("acceptance",),
                canon_reconciliation_refs=("canon-review",),
                research_only_refs=("masterwork",),
            ),
        )


def test_plan_to_canon_promotion_requires_release_evidence():
    assert admit_canon_promotion(
        graph(),
        CanonPromotionReceipt(
            node_ids=("event",),
            accepted_prose_refs=("manuscript/accepted",),
            acceptance_refs=("reviews/acceptance",),
            canon_reconciliation_refs=("canon/reconcile",),
        ),
    ).startswith("CANON_PROMOTION_ADMITTED")
