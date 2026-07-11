import unittest

from buildingos_core import check_evidence_structure, check_record_id_uniqueness
from fixtures import build_fictional_core_batch_01_fixture
from fixtures.core_batch_01 import FIXTURE_TIMESTAMP


class CoreBatch01DeterministicRegressionTests(unittest.TestCase):
    def test_complete_fixture_serialization_repeats_exactly(self) -> None:
        first = build_fictional_core_batch_01_fixture()
        second = build_fictional_core_batch_01_fixture()
        first_serialized = {key: value.to_dict() for key, value in first.items()}
        second_serialized = {key: value.to_dict() for key, value in second.items()}
        self.assertEqual(first_serialized, second_serialized)

    def test_conformance_result_uses_fixed_checked_at_alias(self) -> None:
        fixture = build_fictional_core_batch_01_fixture()
        first = check_evidence_structure(
            fixture["evidence"], checked_at=FIXTURE_TIMESTAMP
        )
        second = check_evidence_structure(
            fixture["evidence"], checked_at=FIXTURE_TIMESTAMP
        )
        self.assertEqual(first.to_dict(), second.to_dict())
        self.assertEqual(FIXTURE_TIMESTAMP, first.checked_at)
        self.assertEqual(FIXTURE_TIMESTAMP, first.to_dict()["checked_at"])
        self.assertEqual(FIXTURE_TIMESTAMP, first.to_dict()["created_at"])

    def test_registry_result_can_be_reproduced_with_fixed_check_time(self) -> None:
        fixture = build_fictional_core_batch_01_fixture()
        first = check_record_id_uniqueness(
            fixture.values(),
            collection_id="fictional-core-batch-01",
            checked_at=FIXTURE_TIMESTAMP,
        )
        second = check_record_id_uniqueness(
            fixture.values(),
            collection_id="fictional-core-batch-01",
            checked_at=FIXTURE_TIMESTAMP,
        )
        self.assertEqual(first.to_dict(), second.to_dict())


if __name__ == "__main__":
    unittest.main()
