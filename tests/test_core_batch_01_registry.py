import unittest

from buildingos_core import (
    Actor,
    Claim,
    ConformanceStatus,
    Evidence,
    GovernanceLedgerEntry,
    RegisteredObject,
    Review,
    ReviewFinding,
    check_claim_actor_reference,
    check_evidence_actor_reference,
    check_ledger_references,
    check_record_id_uniqueness,
    check_registered_object_owner,
    check_review_references,
)
from fixtures import build_fictional_core_batch_01_fixture


class CoreBatch01RegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = build_fictional_core_batch_01_fixture()
        self.actors = [self.fixture["owner"], self.fixture["reviewer"]]
        self.subject_records = [
            self.fixture["registered_object"],
            self.fixture["claim"],
            self.fixture["review"],
        ]
        self.evidence_records = [self.fixture["evidence"]]

    def test_fixed_fixture_covers_every_in_scope_record_type(self) -> None:
        actual_types = {type(record).__name__ for record in self.fixture.values()}
        expected_types = {
            "Actor",
            "Evidence",
            "Claim",
            "Review",
            "Procedure",
            "Lifecycle",
            "RegisteredObject",
            "GovernanceLedgerEntry",
            "ModuleContract",
        }
        self.assertEqual(expected_types, actual_types)

    def test_fixed_fixture_serialization_is_stable(self) -> None:
        claim = self.fixture["claim"]
        self.assertEqual(
            {
                "record_id": "claim-envelope-001",
                "created_at": "2026-07-12T00:00:00+00:00",
                "statement": (
                    "The fictional envelope record includes a shaded opening."
                ),
                "asserted_by_actor_id": "actor-owner-001",
                "evidence_ids": ("evidence-photo-001",),
                "support_status": "SUPPORTED",
            },
            claim.to_dict(),
        )

    def test_fixture_record_ids_are_unique(self) -> None:
        result = check_record_id_uniqueness(
            self.fixture.values(), collection_id="fictional-core-batch-01"
        )
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_duplicate_record_ids_fail(self) -> None:
        duplicate = Actor(
            record_id=self.fixture["owner"].record_id,
            display_name="Fictional Duplicate Actor",
            actor_type="human",
        )
        result = check_record_id_uniqueness(
            [*self.fixture.values(), duplicate],
            collection_id="fictional-core-batch-01-duplicate",
        )
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertEqual(
            ("Duplicate record_id: actor-owner-001",), result.messages
        )

    def test_evidence_actor_reference_resolves(self) -> None:
        result = check_evidence_actor_reference(
            self.fixture["evidence"], self.actors
        )
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_evidence_actor_reference_reports_missing_actor(self) -> None:
        evidence = Evidence(
            record_id="evidence-missing-actor-001",
            title="Fictional missing actor evidence",
            source_reference="fixture://missing-actor/evidence",
            captured_by_actor_id="actor-does-not-exist",
            captured_at="2026-07-12T00:00:00+00:00",
        )
        result = check_evidence_actor_reference(evidence, self.actors)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertIn("actor-does-not-exist", result.messages[0])

    def test_claim_actor_reference_resolves(self) -> None:
        result = check_claim_actor_reference(self.fixture["claim"], self.actors)
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_claim_actor_reference_reports_missing_actor(self) -> None:
        claim = Claim(
            record_id="claim-missing-actor-001",
            statement="A fictional claim with a missing actor reference.",
            asserted_by_actor_id="actor-does-not-exist",
        )
        result = check_claim_actor_reference(claim, self.actors)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertIn("actor-does-not-exist", result.messages[0])

    def test_review_references_resolve(self) -> None:
        result = check_review_references(
            self.fixture["review"],
            self.actors,
            self.subject_records,
            self.evidence_records,
        )
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_review_references_report_all_missing_links(self) -> None:
        review = Review(
            record_id="review-missing-references-001",
            subject_id="subject-does-not-exist",
            reviewer_actor_id="actor-does-not-exist",
            findings=(
                ReviewFinding(
                    finding_id="finding-missing-evidence-001",
                    text="A fictional finding with a missing evidence reference.",
                    evidence_ids=("evidence-does-not-exist",),
                ),
            ),
        )
        result = check_review_references(
            review, self.actors, self.subject_records, self.evidence_records
        )
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertEqual(3, len(result.messages))

    def test_registered_object_owner_resolves(self) -> None:
        result = check_registered_object_owner(
            self.fixture["registered_object"], self.actors
        )
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_registered_object_owner_reports_missing_actor(self) -> None:
        registered_object = RegisteredObject(
            record_id="fictional-building-missing-owner",
            object_type="FictionalBuilding",
            version="1.0",
            title="Fictional Building Missing Owner",
            owner_actor_id="actor-does-not-exist",
        )
        result = check_registered_object_owner(registered_object, self.actors)
        self.assertEqual(ConformanceStatus.FAIL, result.status)

    def test_ledger_references_resolve(self) -> None:
        result = check_ledger_references(
            self.fixture["ledger_entry"], self.actors, self.subject_records
        )
        self.assertEqual(ConformanceStatus.PASS, result.status)

    def test_ledger_references_report_missing_actor_and_subject(self) -> None:
        entry = GovernanceLedgerEntry(
            record_id="ledger-missing-references-001",
            event_type="FICTIONAL_EVENT",
            actor_id="actor-does-not-exist",
            subject_id="subject-does-not-exist",
            summary="A fictional ledger entry with unresolved references.",
        )
        result = check_ledger_references(entry, self.actors, self.subject_records)
        self.assertEqual(ConformanceStatus.FAIL, result.status)
        self.assertEqual(2, len(result.messages))


if __name__ == "__main__":
    unittest.main()
