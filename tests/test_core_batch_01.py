import unittest

from buildingos_core import (
    Actor,
    Claim,
    ConformanceStatus,
    Evidence,
    Lifecycle,
    ModuleContract,
    Procedure,
    ProcedureStep,
    RegisteredObject,
    Review,
    ReviewFinding,
    ReviewStatus,
    SupportStatus,
    check_actor_attribution,
    check_claim_evidence_links,
    check_module_contract_types,
    check_review_boundary,
)


class CoreBatch01Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.actor = Actor(
            record_id="actor-reviewer-001",
            display_name="Fictional Reviewer",
            actor_type="human",
        )
        self.evidence = Evidence(
            record_id="evidence-photo-001",
            title="Fictional envelope photograph",
            evidence_type="photograph",
            source_reference="fixture://fictional-building-alpha/photo-001",
            captured_by_actor_id=self.actor.record_id,
            captured_at="2026-07-12T00:00:00+00:00",
            provenance_note="Fictional test fixture only.",
        )

    def test_actor_attribution_passes(self) -> None:
        result = check_actor_attribution(self.actor)
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_claim_resolves_evidence(self) -> None:
        claim = Claim(
            record_id="claim-envelope-001",
            statement="The fictional envelope contains a shaded opening.",
            asserted_by_actor_id=self.actor.record_id,
            evidence_ids=(self.evidence.record_id,),
            support_status=SupportStatus.SUPPORTED,
        )
        result = check_claim_evidence_links(claim, [self.evidence])
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_claim_reports_missing_evidence(self) -> None:
        claim = Claim(
            record_id="claim-missing-001",
            statement="A fictional unsupported statement.",
            asserted_by_actor_id=self.actor.record_id,
            evidence_ids=("evidence-does-not-exist",),
        )
        result = check_claim_evidence_links(claim, [self.evidence])
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertIn("evidence-does-not-exist", result.messages[0])

    def test_review_has_no_decision_authority(self) -> None:
        review = Review(
            record_id="review-001",
            subject_id="claim-envelope-001",
            reviewer_actor_id=self.actor.record_id,
            status=ReviewStatus.COMPLETED,
            findings=(
                ReviewFinding(
                    finding_id="finding-001",
                    text="The fictional evidence link resolves.",
                    evidence_ids=(self.evidence.record_id,),
                ),
            ),
        )
        result = check_review_boundary(review)
        self.assertEqual(ConformanceStatus.PASS, result.status)
        self.assertFalse(hasattr(review, "approve"))
        self.assertFalse(hasattr(review, "reject"))

    def test_procedure_is_structure_only(self) -> None:
        procedure = Procedure(
            record_id="procedure-001",
            name="Fictional evidence review",
            purpose="Describe review responsibilities without execution.",
            steps=(
                ProcedureStep(
                    step_id="step-001",
                    sequence=1,
                    description="Inspect the fictional evidence record.",
                    responsible_actor_type="human-reviewer",
                ),
            ),
        )
        self.assertFalse(hasattr(procedure, "execute"))

    def test_lifecycle_does_not_transition(self) -> None:
        lifecycle = Lifecycle(
            record_id="lifecycle-001",
            name="Fictional object lifecycle",
            stages=("DRAFT", "REVIEW", "FROZEN"),
            current_stage="DRAFT",
        )
        self.assertFalse(hasattr(lifecycle, "transition"))

    def test_registered_object_serializes(self) -> None:
        item = RegisteredObject(
            record_id="fictional-building-alpha",
            object_type="FictionalBuilding",
            version="1.0",
            title="Fictional Building Alpha",
            owner_actor_id=self.actor.record_id,
        )
        data = item.to_dict()
        self.assertEqual("fictional-building-alpha", data["record_id"])
        self.assertEqual("1.0", data["version"])

    def test_module_contract_known_types(self) -> None:
        contract = ModuleContract(
            record_id="module-contract-claim-001",
            module_name="claim-records",
            purpose="Represent claims without deciding truth.",
            input_types=("Actor", "Evidence"),
            output_types=("Claim",),
            obligations=("Preserve evidence references",),
            exclusions=("Automated truth determination",),
        )
        result = check_module_contract_types(contract)
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_module_contract_rejects_unknown_type(self) -> None:
        contract = ModuleContract(
            record_id="module-contract-unknown-001",
            module_name="unknown-module",
            purpose="Fictional failing contract.",
            input_types=("AutonomousDecision",),
        )
        result = check_module_contract_types(contract)
        self.assertEqual(ConformanceStatus.FAIL, result.status)


if __name__ == "__main__":
    unittest.main()
