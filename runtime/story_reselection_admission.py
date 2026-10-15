#!/usr/bin/env python3
"""Zero-based story reselection and pre-draft admission for Novel projects."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class StoryReselectionAdmissionError(RuntimeError):
    pass


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


@dataclass(frozen=True)
class StoryCandidate:
    candidate_id: str
    premise: str
    engine_family: str
    target_reader: str
    reader_contract: str
    acquisition_hypothesis: str
    serial_sustainability: str
    character_attachment_engine: str
    differentiation: str
    major_risks: tuple[str, ...]


@dataclass(frozen=True)
class ReselectionDecisionReceipt:
    candidates: tuple[StoryCandidate, ...]
    selected_candidate_id: str
    pairwise_or_pareto_evidence_refs: tuple[str, ...]
    platform_evidence_refs: tuple[str, ...]
    learning_synthesis_ref: str
    blind_reader_refs: tuple[str, ...]
    adversarial_refs: tuple[str, ...]
    long_horizon_stress_refs: tuple[str, ...]
    rejected_candidate_reasons: tuple[str, ...]
    current_project_was_privileged: bool = False


def admit_story_reselection(
    receipt: ReselectionDecisionReceipt,
    *,
    corpus_campaign_complete: bool,
    formal_cross_work_synthesis_complete: bool,
) -> str:
    if not corpus_campaign_complete or not formal_cross_work_synthesis_complete:
        raise StoryReselectionAdmissionError(
            "story reselection denied: complete corpus study and formal synthesis first"
        )
    if len(receipt.candidates) < 3:
        raise StoryReselectionAdmissionError("reselection requires at least three materially distinct candidates")
    ids = [c.candidate_id for c in receipt.candidates]
    if len(set(ids)) != len(ids) or receipt.selected_candidate_id not in ids:
        raise StoryReselectionAdmissionError("candidate ids must be unique and include the winner")
    if len({c.engine_family for c in receipt.candidates}) < 3:
        raise StoryReselectionAdmissionError("candidates must span at least three distinct story-engine families")
    if receipt.current_project_was_privileged:
        raise StoryReselectionAdmissionError("historical FQ001 design may compete but cannot receive incumbent privilege")
    if not receipt.learning_synthesis_ref or not receipt.platform_evidence_refs:
        raise StoryReselectionAdmissionError("reselection requires formal learning synthesis and current platform evidence")
    if not receipt.pairwise_or_pareto_evidence_refs:
        raise StoryReselectionAdmissionError("reselection requires vector comparison, pairwise evidence, or a Pareto analysis")
    if not receipt.blind_reader_refs or not receipt.adversarial_refs:
        raise StoryReselectionAdmissionError("reselection requires blind-reader and adversarial evidence")
    if not receipt.long_horizon_stress_refs:
        raise StoryReselectionAdmissionError("reselection requires long-horizon stress tests")
    if len(receipt.rejected_candidate_reasons) < len(receipt.candidates) - 1:
        raise StoryReselectionAdmissionError("reselection requires explicit rejected-candidate reasoning")
    for candidate in receipt.candidates:
        if not all(
            [
                candidate.candidate_id,
                candidate.premise,
                candidate.engine_family,
                candidate.target_reader,
                candidate.reader_contract,
                candidate.acquisition_hypothesis,
                candidate.serial_sustainability,
                candidate.character_attachment_engine,
                candidate.differentiation,
            ]
        ):
            raise StoryReselectionAdmissionError("candidate is missing required product/story dimensions")
        if not candidate.major_risks:
            raise StoryReselectionAdmissionError("every candidate must declare major risks")
    return "STORY_RESELECTION_ADMITTED__ZERO_BASED_VECTOR_EVIDENCE_COMPLETE"


def admit_pre_draft_architecture(
    *,
    selected_candidate_id: str,
    series_end_state_ref: str,
    dynamic_hierarchical_outline_refs: Iterable[str],
    canon_or_story_graph_ref: str,
    first_20k_packet_ref: str,
    benchmark_refs: Iterable[str],
    current_platform_evidence_refs: Iterable[str],
    unresolved_blockers: Iterable[str] | None = None,
) -> str:
    outline_refs = _clean(dynamic_hierarchical_outline_refs)
    benchmarks = _clean(benchmark_refs)
    platform = _clean(current_platform_evidence_refs)
    blockers = _clean(unresolved_blockers)
    if blockers:
        raise StoryReselectionAdmissionError("pre-draft architecture denied: unresolved blockers remain")
    if not selected_candidate_id.strip() or not series_end_state_ref.strip():
        raise StoryReselectionAdmissionError("pre-draft architecture requires winner identity and intended series end state")
    if len(outline_refs) < 4:
        raise StoryReselectionAdmissionError(
            "pre-draft architecture requires dynamic hierarchy at series/volume/arc/opening-packet levels"
        )
    if not canon_or_story_graph_ref.strip() or not first_20k_packet_ref.strip():
        raise StoryReselectionAdmissionError("pre-draft architecture requires story graph/canon and first-20k packet")
    if len(benchmarks) < 3:
        raise StoryReselectionAdmissionError("pre-draft architecture requires multiple independent benchmark dimensions")
    if not platform:
        raise StoryReselectionAdmissionError("pre-draft architecture requires current platform evidence")
    return "PRE_DRAFT_ARCHITECTURE_ADMITTED__DYNAMIC_HIERARCHY_AND_BENCHMARKS_PASS"
