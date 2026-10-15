#!/usr/bin/env python3
"""Novel-owner executable admission for recovery, user escalation and problem closure.

This module realizes UAOS Common Behavior Assurance 1.3 inside the Novel domain with
owner-native receipts. It does not replace UAOS or create a second control plane.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .deliberation_admission import RootScopeReceipt


RECOVERY_OUTCOMES = {"RESOLVED", "PROVISIONAL", "UNRESOLVED"}
CLOSURE_TERMINALS = {"REPAIR_EXECUTED", "BLOCKED_WITH_REASON", "NO_CHANGE_WITH_EVIDENCE"}


class BehaviorAdmissionError(RuntimeError):
    pass


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


def _present(value: str | None) -> bool:
    return isinstance(value, str) and bool(value.strip())


@dataclass(frozen=True)
class RecoveryReceipt:
    outcome: str
    authority_refs: tuple[str, ...]
    artifact_refs: tuple[str, ...]
    context_refs: tuple[str, ...]
    external_evidence_refs: tuple[str, ...]
    unknowns: tuple[str, ...]
    confidence: str
    safe_to_continue: bool

    @property
    def attempted(self) -> bool:
        return bool(
            self.authority_refs
            or self.artifact_refs
            or self.context_refs
            or self.external_evidence_refs
        )


def record_recovery_attempt(
    *,
    outcome: str,
    authority_refs: Iterable[str] | None = None,
    artifact_refs: Iterable[str] | None = None,
    context_refs: Iterable[str] | None = None,
    external_evidence_refs: Iterable[str] | None = None,
    unknowns: Iterable[str] | None = None,
    confidence: str = "UNSPECIFIED",
    safe_to_continue: bool,
) -> RecoveryReceipt:
    if outcome not in RECOVERY_OUTCOMES:
        raise BehaviorAdmissionError(f"invalid recovery outcome: {outcome}")
    receipt = RecoveryReceipt(
        outcome=outcome,
        authority_refs=_clean(authority_refs),
        artifact_refs=_clean(artifact_refs),
        context_refs=_clean(context_refs),
        external_evidence_refs=_clean(external_evidence_refs),
        unknowns=_clean(unknowns),
        confidence=confidence.strip() if isinstance(confidence, str) else "UNSPECIFIED",
        safe_to_continue=bool(safe_to_continue),
    )
    if not receipt.attempted:
        raise BehaviorAdmissionError("recovery receipt has no inspected evidence source")
    if outcome == "UNRESOLVED" and not receipt.unknowns:
        raise BehaviorAdmissionError("UNRESOLVED recovery requires concrete unknowns/blockers")
    if outcome in {"RESOLVED", "PROVISIONAL"} and not safe_to_continue:
        raise BehaviorAdmissionError(f"{outcome} recovery cannot be marked unsafe to continue")
    return receipt


def require_user_escalation_admission(
    receipt: RecoveryReceipt | None,
    *,
    explicit_user_confirmation: bool = False,
    requires_user_fact_or_authorization: bool = False,
) -> str:
    if explicit_user_confirmation:
        return "ADMITTED_EXPLICIT_USER_CONFIRMATION"
    if receipt is None or not receipt.attempted:
        raise BehaviorAdmissionError("user escalation denied: no recovery attempt receipt")
    if receipt.outcome in {"RESOLVED", "PROVISIONAL"} and receipt.safe_to_continue:
        raise BehaviorAdmissionError("user escalation denied: safe owner path remains available")
    if requires_user_fact_or_authorization and receipt.outcome == "UNRESOLVED" and receipt.unknowns:
        return "ADMITTED_REQUIRED_USER_FACT_OR_AUTHORIZATION"
    if receipt.outcome == "UNRESOLVED" and receipt.unknowns and not receipt.safe_to_continue:
        return "ADMITTED_UNRESOLVED_AFTER_RECOVERY"
    raise BehaviorAdmissionError("user escalation denied: blocker conditions are not satisfied")


def _require_cognition_and_evolution(
    *,
    root_scope_receipt: RootScopeReceipt | None,
    evolution_disposition: str | None,
    problem_record_required: bool,
    problem_record_ref: str | None,
) -> None:
    if root_scope_receipt is None:
        raise BehaviorAdmissionError("problem action denied: root-scope cognition receipt is missing")
    if not _present(evolution_disposition):
        raise BehaviorAdmissionError("problem action denied: evolution/learning disposition is missing")
    if problem_record_required and not _present(problem_record_ref):
        raise BehaviorAdmissionError("material/evolution-relevant problem requires durable problem evidence")


def finalize_problem_closure(
    *,
    problem_detected: bool,
    repair_path_available: bool,
    authority_permits_repair: bool,
    explicit_user_choice_required: bool,
    repair_attempted: bool,
    repair_succeeded: bool,
    blocker_reason: str | None = None,
    no_change_evidence: Iterable[str] | None = None,
    root_scope_receipt: RootScopeReceipt | None = None,
    evolution_disposition: str | None = None,
    problem_record_required: bool = False,
    problem_record_ref: str | None = None,
) -> str:
    """Reject action/closure before root-scope and learning admission.

    A real external blocker may still be surfaced without fabricating a root cause. Repair
    and no-change require the owner-native cognition/evolution transaction first.
    """
    if not problem_detected:
        return "CLEAN_NO_PROBLEM"

    evidence = _clean(no_change_evidence)
    blocker = blocker_reason.strip() if isinstance(blocker_reason, str) else ""

    if explicit_user_choice_required and blocker:
        if problem_record_required and not _present(problem_record_ref):
            raise BehaviorAdmissionError("material blocked problem requires durable problem evidence")
        return "BLOCKED_WITH_REASON"
    if not authority_permits_repair and blocker:
        if problem_record_required and not _present(problem_record_ref):
            raise BehaviorAdmissionError("material blocked problem requires durable problem evidence")
        return "BLOCKED_WITH_REASON"
    if not repair_path_available and blocker:
        if problem_record_required and not _present(problem_record_ref):
            raise BehaviorAdmissionError("material blocked problem requires durable problem evidence")
        return "BLOCKED_WITH_REASON"

    if repair_path_available and authority_permits_repair and not explicit_user_choice_required:
        _require_cognition_and_evolution(
            root_scope_receipt=root_scope_receipt,
            evolution_disposition=evolution_disposition,
            problem_record_required=problem_record_required,
            problem_record_ref=problem_record_ref,
        )
        if not repair_attempted:
            raise BehaviorAdmissionError(
                "problem closure denied: cognitively-admitted authorized repair exists but was not attempted"
            )
        if repair_succeeded:
            return "REPAIR_EXECUTED"
        if blocker:
            return "BLOCKED_WITH_REASON"
        raise BehaviorAdmissionError(
            "problem closure denied: failed repair requires a concrete blocker or further repair"
        )

    if evidence:
        _require_cognition_and_evolution(
            root_scope_receipt=root_scope_receipt,
            evolution_disposition=evolution_disposition,
            problem_record_required=problem_record_required,
            problem_record_ref=problem_record_ref,
        )
        return "NO_CHANGE_WITH_EVIDENCE"

    raise BehaviorAdmissionError(
        "problem closure denied: no valid cognitively-admitted repair, blocker, or evidence-backed no-change terminal"
    )
