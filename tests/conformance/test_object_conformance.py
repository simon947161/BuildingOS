import unittest

from buildingos_core import (
    Claim,
    ConformanceStatus,
    Evidence,
    ModuleContract,
    Procedure,
    ProcedureStep,
    Review,
    ReviewFinding,
    check_actor_attribution,
    check_claim_structure,
    check_evidence_structure,
    check_ledger_structure,
    check_lifecycle_structure,
    check_module_contract_structure,
    check_procedure_structure,
    check_registered_object_structure,
    check_review_structure,
)
from fixtures import build_fictional_core_batch_01_fixture


class CoreBatch01ObjectConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = build_fictional_core_batch_01_fixture()

    def test_every_m1_object_has_explicit_passing_structure_check(self) -> None:
        checks = (
            check_actor_attribution(self.fixture["owner"]),
            check_evidence_structure(self.fixture["evidence"]),
            check_claim_structure(self.fixture["claim"]),
            check_review_structure(self.fixture["review"]),
            check_procedure_structure(self.fixture["procedure"]),
            check_lifecycle_structure(self.fixture["lifecycle"]),
            check_registered_object_structure(self.fixture["registered_object"]),
            check_ledger_structure(self.fixture["ledger_entry"]),
            check_module_contract_structure(self.fixture["module_contract"]),
        )
        self.assertTrue(all(result.status is ConformanceStatus.PASS for result in checks))
        self.assertEqual(9, len({result.m1_source for result in checks}))

    def test_evidence_without_provenance_fails_conformance(self) -> None:
        evidence = Evidence(
            record_id="evidence-no-provenance-001",
            title="Fictional evidence without provenance",
            source_reference="fixture://fictional/no-provenance",
            captured_by_actor_id="actor-owner-001",
            captured_at="2026-07-12T00:00:00+00:00",
        )
        result = check_evidence_structure(evidence)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertIn("provenance_note", result.messages[0])

    def test_claim_with_invalid_support_status_fails_conformance(self) -> None:
        claim = Claim(
            record_id="claim-invalid-status-001",
            statement="A fictional claim with an invalid status value.",
            asserted_by_actor_id="actor-owner-001",
            support_status="INVALID",  # type: ignore[arg-type]
        )
        result = check_claim_structure(claim)
        self.assertEqual(ConformanceStatus.FAIL, result.status)

    def test_duplicate_review_finding_ids_fail_conformance(self) -> None:
        review = Review(
            record_id="review-duplicate-findings-001",
            subject_id="claim-envelope-001",
            reviewer_actor_id="actor-reviewer-001",
            findings=(
                ReviewFinding("finding-duplicate-001", "First fictional finding."),
                ReviewFinding("finding-duplicate-001", "Second fictional finding."),
            ),
        )
        result = check_review_structure(review)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertIn("finding-duplicate-001", result.messages[0])

    def test_unordered_procedure_steps_fail_conformance(self) -> None:
        procedure = Procedure(
            record_id="procedure-unordered-001",
            name="Fictional unordered procedure",
            purpose="Demonstrate a structural conformance failure.",
            steps=(
                ProcedureStep("step-two", 2, "Second fictional step.", "human"),
                ProcedureStep("step-one", 1, "First fictional step.", "human"),
            ),
        )
        result = check_procedure_structure(procedure)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertIn("ascending sequence", result.messages[0])

    def test_empty_module_contract_obligations_and_exclusions_fail(self) -> None:
        contract = ModuleContract(
            record_id="module-contract-empty-boundaries-001",
            module_name="fictional-empty-contract",
            purpose="Demonstrate missing declarative boundaries.",
        )
        result = check_module_contract_structure(contract)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertEqual(2, len(result.messages))

    def test_excluded_runtime_and_authority_members_remain_absent(self) -> None:
        self.assertFalse(hasattr(self.fixture["owner"], "grant_permission"))
        self.assertFalse(hasattr(self.fixture["procedure"], "execute"))
        self.assertFalse(hasattr(self.fixture["lifecycle"], "transition"))
        self.assertFalse(hasattr(self.fixture["ledger_entry"], "append_to_blockchain"))
        self.assertFalse(hasattr(self.fixture["module_contract"], "execute"))


if __name__ == "__main__":
    unittest.main()
