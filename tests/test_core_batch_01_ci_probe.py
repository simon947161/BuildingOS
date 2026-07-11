import unittest

from buildingos_core import (
    ConformanceStatus,
    check_evidence_structure,
    check_record_id_uniqueness,
)
from fixtures import build_fictional_core_batch_01_fixture
from fixtures.core_batch_01 import FIXTURE_TIMESTAMP


class CoreBatch01CIVerificationTests(unittest.TestCase):
    def test_public_conformance_surface_runs_from_clean_import(self) -> None:
        fixture = build_fictional_core_batch_01_fixture()
        evidence_result = check_evidence_structure(
            fixture["evidence"], checked_at=FIXTURE_TIMESTAMP
        )
        uniqueness_result = check_record_id_uniqueness(
            fixture.values(),
            collection_id="fictional-core-batch-01",
            checked_at=FIXTURE_TIMESTAMP,
        )
        self.assertEqual(ConformanceStatus.PASS, evidence_result.status)
        self.assertEqual(ConformanceStatus.PASS, uniqueness_result.status)
        self.assertEqual(FIXTURE_TIMESTAMP, evidence_result.checked_at)


if __name__ == "__main__":
    unittest.main()
