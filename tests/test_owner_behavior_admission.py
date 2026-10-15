import pytest

from runtime.deliberation_admission import (
    HypothesisDisposition,
    ProblemLayer,
    RootScopeHypothesis,
    build_root_scope_receipt,
)
from runtime.owner_behavior_admission import (
    BehaviorAdmissionError,
    finalize_problem_closure,
    record_recovery_attempt,
    require_user_escalation_admission,
)


def root_receipt():
    return build_root_scope_receipt(
        hypotheses=[
            RootScopeHypothesis(
                hypothesis_id="checkpoint-order",
                layer=ProblemLayer.DOMAIN_WORKFLOW,
                statement="the recovery checkpoint order is the root cause",
                disposition=HypothesisDisposition.SELECTED,
                supporting_evidence_refs=("checkpoint:test",),
                falsification_or_rejection_refs=("probe:replay",),
            )
        ],
        selected_hypothesis_id="checkpoint-order",
    )


def test_recoverable_missing_context_continues_with_provisional_candidate_instead_of_user_escalation():
    receipt = record_recovery_attempt(
        outcome="PROVISIONAL",
        authority_refs=["projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json"],
        artifact_refs=["projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md"],
        context_refs=["current selected Novel task context"],
        unknowns=["live reader outcome is not yet observed"],
        confidence="MEDIUM",
        safe_to_continue=True,
    )
    with pytest.raises(BehaviorAdmissionError, match="safe owner path"):
        require_user_escalation_admission(receipt)


def test_user_escalation_is_denied_without_recovery_receipt():
    with pytest.raises(BehaviorAdmissionError, match="no recovery attempt receipt"):
        require_user_escalation_admission(None)


def test_unresolved_required_user_fact_can_be_escalated_after_recovery():
    receipt = record_recovery_attempt(
        outcome="UNRESOLVED",
        authority_refs=["projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json"],
        artifact_refs=["projects/FQ001_MINGRI_ORDER/PLATFORM_PUBLICATION_LOG.md"],
        unknowns=["whether the user actually published/replaced the external platform chapter"],
        confidence="HIGH_ABOUT_INTERNAL_STATE__UNKNOWN_EXTERNAL_FACT",
        safe_to_continue=False,
    )
    assert require_user_escalation_admission(
        receipt,
        requires_user_fact_or_authorization=True,
    ) == "ADMITTED_REQUIRED_USER_FACT_OR_AUTHORIZATION"


def test_detected_repairable_problem_cannot_bypass_root_scope_cognition():
    with pytest.raises(BehaviorAdmissionError, match="root-scope cognition"):
        finalize_problem_closure(
            problem_detected=True,
            repair_path_available=True,
            authority_permits_repair=True,
            explicit_user_choice_required=False,
            repair_attempted=False,
            repair_succeeded=False,
        )


def test_cognitively_admitted_repairable_problem_cannot_end_as_recommendation_only():
    with pytest.raises(BehaviorAdmissionError, match="repair exists but was not attempted"):
        finalize_problem_closure(
            problem_detected=True,
            repair_path_available=True,
            authority_permits_repair=True,
            explicit_user_choice_required=False,
            repair_attempted=False,
            repair_succeeded=False,
            root_scope_receipt=root_receipt(),
            evolution_disposition="EVIDENCE_ONLY",
        )


def test_successful_authorized_repair_closes_after_root_scope_and_evolution():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=True,
        authority_permits_repair=True,
        explicit_user_choice_required=False,
        repair_attempted=True,
        repair_succeeded=True,
        root_scope_receipt=root_receipt(),
        evolution_disposition="EVIDENCE_ONLY",
    ) == "REPAIR_EXECUTED"


def test_material_problem_requires_durable_problem_record():
    with pytest.raises(BehaviorAdmissionError, match="durable problem evidence"):
        finalize_problem_closure(
            problem_detected=True,
            repair_path_available=True,
            authority_permits_repair=True,
            explicit_user_choice_required=False,
            repair_attempted=True,
            repair_succeeded=True,
            root_scope_receipt=root_receipt(),
            evolution_disposition="DOMAIN_CANDIDATE",
            problem_record_required=True,
        )


def test_user_controlled_external_publication_can_block_with_reason_without_fake_root_cause():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=False,
        authority_permits_repair=False,
        explicit_user_choice_required=True,
        repair_attempted=False,
        repair_succeeded=False,
        blocker_reason="external platform publication/replacement is user-controlled",
    ) == "BLOCKED_WITH_REASON"


def test_no_change_requires_root_scope_evolution_and_evidence():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=False,
        authority_permits_repair=True,
        explicit_user_choice_required=False,
        repair_attempted=False,
        repair_succeeded=False,
        no_change_evidence=["checkpoint and Canon already agree; mutation would create drift"],
        root_scope_receipt=root_receipt(),
        evolution_disposition="NO_DURABLE_EVOLUTION",
    ) == "NO_CHANGE_WITH_EVIDENCE"
