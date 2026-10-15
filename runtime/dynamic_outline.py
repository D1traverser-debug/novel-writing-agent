#!/usr/bin/env python3
"""Dynamic hierarchical outline contracts for long-form Novel planning.

Principles:
1) accepted/frozen structure is harder to change than unaccepted hypotheses;
2) horizon controls planning resolution, not automatic rigidity;
3) plan revisions are evidence-driven, impact-scoped and non-destructive.

This does not replace project-specific outline prose. It provides executable invariants
for series/volume/arc/packet/chapter planning and replanning.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class OutlineAdmissionError(RuntimeError):
    pass


LEVEL_ORDER = {
    "SERIES": 0,
    "VOLUME": 1,
    "ARC": 2,
    "PACKET": 3,
    "CHAPTER": 4,
    "SCENE": 5,
}
VALID_HORIZONS = {"NEAR", "MID", "FAR"}
VALID_STATUSES = {"FLEXIBLE", "FROZEN", "SUPERSEDED", "HISTORICAL"}


@dataclass(frozen=True)
class OutlineNode:
    node_id: str
    level: str
    parent_id: str | None
    horizon: str
    status: str
    goal: str
    expected_state_changes: tuple[str, ...]
    promise_refs: tuple[str, ...]
    dependency_refs: tuple[str, ...]
    evidence_refs: tuple[str, ...]


@dataclass(frozen=True)
class DynamicOutline:
    nodes: tuple[OutlineNode, ...]
    intended_series_end_ref: str
    current_opening_packet_ref: str


@dataclass(frozen=True)
class ReplanReceipt:
    changed_node_ids: tuple[str, ...]
    trigger_refs: tuple[str, ...]
    alternatives_considered: tuple[str, ...]
    selected_change: str
    rejected_alternative_reasons: tuple[str, ...]
    invalidated_refs: tuple[str, ...]
    downstream_review_refs: tuple[str, ...]
    hard_failure_or_live_signal_refs: tuple[str, ...]
    canon_change_requested: bool = False


def _children(outline: DynamicOutline) -> dict[str, list[str]]:
    result = {n.node_id: [] for n in outline.nodes}
    for node in outline.nodes:
        if node.parent_id:
            result[node.parent_id].append(node.node_id)
    return result


def validate_outline(outline: DynamicOutline) -> str:
    if not outline.intended_series_end_ref or not outline.current_opening_packet_ref:
        raise OutlineAdmissionError("outline requires intended end-state and current opening packet refs")
    ids = [n.node_id for n in outline.nodes]
    if not ids or len(ids) != len(set(ids)):
        raise OutlineAdmissionError("outline node ids must be unique and non-empty")
    by_id = {n.node_id: n for n in outline.nodes}
    for node in outline.nodes:
        if node.level not in LEVEL_ORDER:
            raise OutlineAdmissionError(f"unknown outline level: {node.level}")
        if node.horizon not in VALID_HORIZONS or node.status not in VALID_STATUSES:
            raise OutlineAdmissionError("invalid horizon/status")
        if not node.goal or not node.expected_state_changes or not node.evidence_refs:
            raise OutlineAdmissionError(f"outline node incomplete: {node.node_id}")
        if node.parent_id:
            if node.parent_id not in by_id:
                raise OutlineAdmissionError("outline parent missing")
            parent = by_id[node.parent_id]
            if LEVEL_ORDER[parent.level] >= LEVEL_ORDER[node.level]:
                raise OutlineAdmissionError("outline hierarchy level inversion")
    for node in outline.nodes:
        seen = set()
        current = node
        while current.parent_id:
            if current.parent_id in seen:
                raise OutlineAdmissionError("outline parent cycle")
            seen.add(current.parent_id)
            current = by_id[current.parent_id]
    return "DYNAMIC_OUTLINE_VALID"


def descendant_ids(outline: DynamicOutline, node_ids: Iterable[str]) -> tuple[str, ...]:
    validate_outline(outline)
    chosen = {x for x in node_ids if x}
    known = {n.node_id for n in outline.nodes}
    if not chosen or not chosen.issubset(known):
        raise OutlineAdmissionError("unknown/empty changed node set")
    children = _children(outline)
    affected = set(chosen)
    frontier = list(chosen)
    while frontier:
        current = frontier.pop()
        for child in children[current]:
            if child not in affected:
                affected.add(child)
                frontier.append(child)
    return tuple(sorted(affected))


def admit_replan(outline: DynamicOutline, receipt: ReplanReceipt) -> str:
    validate_outline(outline)
    by_id = {n.node_id: n for n in outline.nodes}
    if not receipt.changed_node_ids or any(node_id not in by_id for node_id in receipt.changed_node_ids):
        raise OutlineAdmissionError("replan requires known changed nodes")
    if not receipt.trigger_refs:
        raise OutlineAdmissionError("replan requires evidence/trigger refs")
    if len(receipt.alternatives_considered) < 2:
        raise OutlineAdmissionError("replan requires alternatives, not first-idea execution")
    if not receipt.selected_change or not receipt.rejected_alternative_reasons:
        raise OutlineAdmissionError("replan requires selection and rejection reasoning")
    required_affected = set(descendant_ids(outline, receipt.changed_node_ids))
    declared_affected = set(receipt.invalidated_refs)
    if not required_affected.issubset(declared_affected):
        raise OutlineAdmissionError("replan under-declares downstream invalidation scope")

    # Horizon controls how much detail is planned. Rigidity comes from acceptance/freeze,
    # not merely from being near in time. A near but FLEXIBLE chapter may still be improved
    # before acceptance; a FROZEN node requires stronger evidence to reopen.
    frozen_changed = [by_id[node_id] for node_id in receipt.changed_node_ids if by_id[node_id].status == "FROZEN"]
    if frozen_changed and not receipt.hard_failure_or_live_signal_refs:
        raise OutlineAdmissionError("frozen structural change requires hard defect or live outcome signal")

    if receipt.canon_change_requested:
        raise OutlineAdmissionError("outline replan cannot silently mutate Canon; use explicit canon promotion/reconciliation")
    if not receipt.downstream_review_refs:
        raise OutlineAdmissionError("replan requires downstream review plan")
    return "REPLAN_ADMITTED__IMPACT_SCOPED__CANON_SEPARATE"