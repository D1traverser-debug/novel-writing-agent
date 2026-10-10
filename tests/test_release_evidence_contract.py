from pathlib import Path
import hashlib
import json

from runtime.release_evidence_guard import (
    REQUIRED_PIPELINE_ROLES,
    REQUIRED_REVIEW_ROLES,
    sha256_file,
    validate_chapter,
    validate_repository,
)

ROOT = Path(__file__).resolve().parents[1]


def test_current_legacy_acceptance_is_explicit_and_guarded():
    problems = validate_repository(ROOT)
    assert problems == []
    text = (ROOT / "projects/FQ001_MINGRI_ORDER/reviews/CH0008_ACCEPTANCE.md").read_text(encoding="utf-8")
    assert "evidence_assurance: LEGACY_AGGREGATE_MIGRATED" in text
    assert "role_receipts: NOT_AVAILABLE" in text
    assert "isolated_reviewer_attestation: NOT_CLAIMED" in text


def _build_future_fixture(root: Path, *, include_evidence: bool = True) -> tuple[Path, Path]:
    task = root / "projects/FQ001_MINGRI_ORDER"
    for sub in ("manuscript", "reviews", "execution", "contracts"):
        (task / sub).mkdir(parents=True, exist_ok=True)

    final_path = task / "manuscript/CH0009_FINAL.md"
    final_path.write_text("第九章\n这是用于契约测试的最终正文。\n", encoding="utf-8")
    final_hash = sha256_file(final_path)

    contract_path = task / "contracts/CH0009_CONTRACT.md"
    contract_path.write_text("chapter_no: 9\nstatus: FROZEN_FOR_EXECUTION\n", encoding="utf-8")
    contract_hash = sha256_file(contract_path)

    context_path = task / "execution/CH0009_CONTEXT_PACK.json"
    context = {
        "schema_version": "1.0",
        "chapter_id": "CH0009",
        "status": "FROZEN",
        "authority_commit": "a" * 40,
        "contract_snapshot_ref": "projects/FQ001_MINGRI_ORDER/contracts/CH0009_CONTRACT.md",
        "contract_snapshot_sha256": contract_hash,
        "project_profile_ref": "projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md",
        "project_profile_sha256": "b" * 64,
        "canon_refs": [{"ref": "canon/THREADS.json", "sha256": "c" * 64}],
        "recent_final_refs": [{"ref": "manuscript/CH0008_FINAL.md", "sha256": "d" * 64}],
        "rule_slices": ["Scene engine", "Dialogue / relationship"],
        "frozen_at": "2026-10-10T15:01:00Z",
    }
    context_path.write_text(json.dumps(context, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    context_hash = sha256_file(context_path)

    evidence_ref = "projects/FQ001_MINGRI_ORDER/reviews/CH0009_EXECUTION_EVIDENCE.json"
    evidence_path = root / evidence_ref
    evidence_hash = "0" * 64
    if include_evidence:
        receipts = []
        for role in sorted(REQUIRED_PIPELINE_ROLES):
            receipts.append({
                "receipt_id": f"pipeline-{role}",
                "role_id": role,
                "status": "PASS",
                "executor_mode": "CHAT_BRIDGED",
                "assurance": "ROLE_SEPARATED_NOT_ATTESTED_ISOLATED",
                "input_hash": context_hash,
            })
        for role in sorted(REQUIRED_REVIEW_ROLES):
            receipts.append({
                "receipt_id": f"review-{role}",
                "role_id": role,
                "status": "RELEASE" if role == "ADVERSARIAL_RELEASE" else "PASS",
                "executor_mode": "CHAT_BRIDGED",
                "assurance": "ROLE_SEPARATED_NOT_ATTESTED_ISOLATED",
                "peer_review_visibility": "BLINDED_FROM_PEER_CONCLUSIONS",
                "source_hash": final_hash,
                "input_hash": context_hash,
            })
        evidence = {
            "schema_version": "1.0",
            "chapter_id": "CH0009",
            "source_hash": final_hash,
            "context_pack_ref": "projects/FQ001_MINGRI_ORDER/execution/CH0009_CONTEXT_PACK.json",
            "context_pack_sha256": context_hash,
            "assurance": "ROLE_SEPARATED_NOT_ATTESTED_ISOLATED",
            "role_receipts": receipts,
            "issue_ledger": {
                "opened": 0,
                "closed": 0,
                "unresolved_blocker": 0,
                "unresolved_high": 0,
                "revision_rounds": 0,
            },
        }
        evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        evidence_hash = sha256_file(evidence_path)

    acceptance_path = task / "reviews/CH0009_ACCEPTANCE.md"
    acceptance_path.write_text(
        "\n".join([
            "# CH0009 Acceptance",
            "",
            "chapter_id: CH0009",
            f"source_hash: {final_hash}",
            "status: FINAL_ACCEPTED",
            "release_status: PUBLISH_READY",
            "evidence_contract_version: 1.0",
            f"execution_evidence_ref: {evidence_ref}",
            f"execution_evidence_sha256: {evidence_hash}",
            "context_pack_ref: projects/FQ001_MINGRI_ORDER/execution/CH0009_CONTEXT_PACK.json",
            f"context_pack_sha256: {context_hash}",
            "",
        ]),
        encoding="utf-8",
    )
    return root, task


def test_future_acceptance_fails_closed_without_execution_evidence(tmp_path):
    root, task = _build_future_fixture(tmp_path, include_evidence=False)
    problems = validate_chapter(root, task, 9)
    assert "CH0009:execution-evidence-missing" in problems


def test_future_acceptance_passes_with_frozen_context_and_role_receipts(tmp_path):
    root, task = _build_future_fixture(tmp_path, include_evidence=True)
    assert validate_chapter(root, task, 9) == []


def test_false_isolated_claim_is_rejected(tmp_path):
    root, task = _build_future_fixture(tmp_path, include_evidence=True)
    evidence_path = task / "reviews/CH0009_EXECUTION_EVIDENCE.json"
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    evidence["role_receipts"][0]["assurance"] = "ATTESTED_ISOLATED"
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    acceptance_path = task / "reviews/CH0009_ACCEPTANCE.md"
    text = acceptance_path.read_text(encoding="utf-8")
    old = next(line.split(": ", 1)[1] for line in text.splitlines() if line.startswith("execution_evidence_sha256:"))
    text = text.replace(old, sha256_file(evidence_path))
    acceptance_path.write_text(text, encoding="utf-8")
    problems = validate_chapter(root, task, 9)
    assert any(p.startswith("CH0009:false-isolated-claim:") for p in problems)
