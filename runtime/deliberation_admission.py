#!/usr/bin/env python3
"""Evidence-first admission for material Novel-domain decisions.

This is not a claim that every host response is physically intercepted. It provides an
owner-native executable contract that material design/learning/promotion mutations can
be trajectory-tested against before they are accepted as governed decisions.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class DeliberationAdmissionError(RuntimeError):
    pass


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


@dataclass(frozen=True)
class MaterialDecisionReceipt:
    question: str
    authority_refs: tuple[str, ...]
    internal_evidence_refs: tuple[str, ...]
    external_evidence_refs: tuple[str, ...]
    alternatives: tuple[str, ...]
    counterexamples: tuple[str, ...]
    challenged_assumptions: tuple[str, ...]
    selected_option: str
    rejection_reasons: tuple[str, ...]
    risks: tuple[str, ...]
    rollback_or_recovery: tuple[str, ...]
    external_research_not_material_reason: str = ""

    @property
    def has_external_grounding(self) -> bool:
        return bool(self.external_evidence_refs or self.external_research_not_material_reason.strip())


def build_material_decision_receipt(
    *,
    question: str,
    authority_refs: Iterable[str],
    internal_evidence_refs: Iterable[str],
    external_evidence_refs: Iterable[str] | None,
    alternatives: Iterable[str],
    counterexamples: Iterable[str],
    challenged_assumptions: Iterable[str],
    selected_option: str,
    rejection_reasons: Iterable[str],
    risks: Iterable[str],
    rollback_or_recovery: Iterable[str],
    external_research_not_material_reason: str = "",
) -> MaterialDecisionReceipt:
    receipt = MaterialDecisionReceipt(
        question=question.strip(),
        authority_refs=_clean(authority_refs),
        internal_evidence_refs=_clean(internal_evidence_refs),
        external_evidence_refs=_clean(external_evidence_refs),
        alternatives=_clean(alternatives),
        counterexamples=_clean(counterexamples),
        challenged_assumptions=_clean(challenged_assumptions),
        selected_option=selected_option.strip(),
        rejection_reasons=_clean(rejection_reasons),
        risks=_clean(risks),
        rollback_or_recovery=_clean(rollback_or_recovery),
        external_research_not_material_reason=external_research_not_material_reason.strip(),
    )
    if not receipt.question:
        raise DeliberationAdmissionError("material decision requires an explicit question")
    if not receipt.authority_refs or not receipt.internal_evidence_refs:
        raise DeliberationAdmissionError("material decision requires current authority and internal evidence")
    if not receipt.has_external_grounding:
        raise DeliberationAdmissionError(
            "material decision requires external evidence or an explicit reason external research is not material"
        )
    if len(receipt.alternatives) < 2:
        raise DeliberationAdmissionError("material decision requires at least two alternatives")
    if not receipt.counterexamples or not receipt.challenged_assumptions:
        raise DeliberationAdmissionError("material decision requires counterexample and assumption challenge")
    if not receipt.selected_option or not receipt.rejection_reasons:
        raise DeliberationAdmissionError("material decision requires selection and rejected-option reasoning")
    if not receipt.risks or not receipt.rollback_or_recovery:
        raise DeliberationAdmissionError("material decision requires risks and rollback/recovery")
    return receipt


def admit_material_mutation(receipt: MaterialDecisionReceipt | None) -> str:
    if receipt is None:
        raise DeliberationAdmissionError("material mutation denied: no deliberation receipt")
    # Re-run the strongest invariants in case a receipt was manually constructed.
    if len(receipt.alternatives) < 2 or not receipt.counterexamples or not receipt.challenged_assumptions:
        raise DeliberationAdmissionError("material mutation denied: deliberation floor incomplete")
    if not receipt.has_external_grounding:
        raise DeliberationAdmissionError("material mutation denied: external-grounding decision missing")
    if not receipt.authority_refs or not receipt.internal_evidence_refs:
        raise DeliberationAdmissionError("material mutation denied: evidence grounding incomplete")
    return "MATERIAL_MUTATION_ADMITTED__EVIDENCE_COMPARE_CHALLENGE_COMPLETE"
