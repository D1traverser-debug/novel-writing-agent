#!/usr/bin/env python3
"""Typed dependency graph for Novel planning without collapsing plan into Canon.

The graph is deliberately small: it coordinates dependencies, invalidation and promotion.
Existing project Canon files remain business authority for accepted facts. This runtime
prevents planning/research changes from silently becoming Canon and makes downstream
replanning explicit.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class StoryGraphError(RuntimeError):
    pass


VALID_LAYERS = {"LEARNING", "CANDIDATE", "PLAN", "CANON", "HISTORICAL"}
VALID_NODE_TYPES = {
    "STORY_PREMISE",
    "EVENT",
    "CHARACTER_STATE",
    "RELATIONSHIP_STATE",
    "WORLD_RULE",
    "READER_PROMISE",
    "FORESHADOW",
    "THREAD",
    "OUTLINE_NODE",
    "PLATFORM_ASSUMPTION",
}
VALID_EDGE_TYPES = {
    "DEPENDS_ON",
    "CAUSES",
    "ENABLES",
    "CONTRADICTS",
    "FORESHADOWS",
    "PAYS_OFF",
    "REQUIRES_KNOWLEDGE_OF",
    "REVISES",
}


@dataclass(frozen=True)
class StoryNode:
    node_id: str
    node_type: str
    layer: str
    source_refs: tuple[str, ...]
    status: str = "ACTIVE"


@dataclass(frozen=True)
class StoryEdge:
    source_id: str
    target_id: str
    edge_type: str
    source_refs: tuple[str, ...]


@dataclass(frozen=True)
class StoryDependencyGraph:
    nodes: tuple[StoryNode, ...]
    edges: tuple[StoryEdge, ...]


@dataclass(frozen=True)
class CanonPromotionReceipt:
    node_ids: tuple[str, ...]
    accepted_prose_refs: tuple[str, ...]
    acceptance_refs: tuple[str, ...]
    canon_reconciliation_refs: tuple[str, ...]
    research_only_refs: tuple[str, ...] = ()


def validate_graph(graph: StoryDependencyGraph) -> str:
    ids = [n.node_id for n in graph.nodes]
    if not ids or len(ids) != len(set(ids)):
        raise StoryGraphError("story graph requires unique non-empty node ids")
    by_id = {n.node_id: n for n in graph.nodes}
    for node in graph.nodes:
        if node.node_type not in VALID_NODE_TYPES:
            raise StoryGraphError(f"unknown node type: {node.node_type}")
        if node.layer not in VALID_LAYERS:
            raise StoryGraphError(f"unknown node layer: {node.layer}")
        if not node.source_refs:
            raise StoryGraphError(f"node lacks provenance: {node.node_id}")
    for edge in graph.edges:
        if edge.source_id not in by_id or edge.target_id not in by_id:
            raise StoryGraphError("edge references unknown node")
        if edge.edge_type not in VALID_EDGE_TYPES:
            raise StoryGraphError(f"unknown edge type: {edge.edge_type}")
        if not edge.source_refs:
            raise StoryGraphError("edge lacks provenance")
    # Dependency edges must be acyclic. Other semantic edges may form legitimate loops.
    adjacency = {node_id: [] for node_id in by_id}
    for edge in graph.edges:
        if edge.edge_type == "DEPENDS_ON":
            adjacency[edge.source_id].append(edge.target_id)
    visiting, visited = set(), set()

    def visit(node_id: str) -> None:
        if node_id in visiting:
            raise StoryGraphError("DEPENDS_ON cycle detected")
        if node_id in visited:
            return
        visiting.add(node_id)
        for nxt in adjacency[node_id]:
            visit(nxt)
        visiting.remove(node_id)
        visited.add(node_id)

    for node_id in adjacency:
        visit(node_id)
    return "STORY_DEPENDENCY_GRAPH_VALID"


def invalidation_closure(graph: StoryDependencyGraph, changed_node_ids: Iterable[str]) -> tuple[str, ...]:
    validate_graph(graph)
    changed = {x for x in changed_node_ids if x}
    known = {n.node_id for n in graph.nodes}
    if not changed or not changed.issubset(known):
        raise StoryGraphError("changed node set is empty or references unknown nodes")
    reverse = {node_id: set() for node_id in known}
    for edge in graph.edges:
        if edge.edge_type in {"DEPENDS_ON", "ENABLES", "FORESHADOWS", "REQUIRES_KNOWLEDGE_OF"}:
            reverse[edge.target_id].add(edge.source_id)
    affected = set(changed)
    frontier = list(changed)
    while frontier:
        current = frontier.pop()
        for downstream in reverse[current]:
            if downstream not in affected:
                affected.add(downstream)
                frontier.append(downstream)
    return tuple(sorted(affected))


def admit_canon_promotion(graph: StoryDependencyGraph, receipt: CanonPromotionReceipt) -> str:
    validate_graph(graph)
    by_id = {n.node_id: n for n in graph.nodes}
    if not receipt.node_ids or any(node_id not in by_id for node_id in receipt.node_ids):
        raise StoryGraphError("canon promotion references unknown or empty node set")
    if any(by_id[node_id].layer not in {"CANDIDATE", "PLAN"} for node_id in receipt.node_ids):
        raise StoryGraphError("only candidate/plan nodes may be promoted through this path")
    if not receipt.accepted_prose_refs or not receipt.acceptance_refs or not receipt.canon_reconciliation_refs:
        raise StoryGraphError("canon promotion requires accepted prose, acceptance evidence and canon reconciliation")
    if receipt.research_only_refs and not receipt.accepted_prose_refs:
        raise StoryGraphError("research evidence alone cannot promote Canon")
    return "CANON_PROMOTION_ADMITTED__ACCEPTED_PROSE_AND_RECONCILIATION_BOUND"
