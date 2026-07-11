"""Cross-object reference checks for the Core Batch 01 record set."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from .models import (
    Actor,
    Claim,
    ConformanceResult,
    ConformanceStatus,
    CoreRecord,
    Evidence,
    GovernanceLedgerEntry,
    RegisteredObject,
    Review,
    utc_now_iso,
)


def _record_ids(records: Iterable[CoreRecord]) -> set[str]:
    return {record.record_id for record in records}


def _result(
    *,
    check_id: str,
    m1_source: str,
    subject_type: str,
    subject_id: str,
    messages: Iterable[str],
    checked_at: str | None = None,
) -> ConformanceResult:
    message_tuple = tuple(messages)
    return ConformanceResult(
        record_id=f"conformance:{check_id}:{subject_id}",
        created_at=checked_at or utc_now_iso(),
        check_id=check_id,
        m1_source=m1_source,
        subject_type=subject_type,
        subject_id=subject_id,
        status=(
            ConformanceStatus.PASS
            if not message_tuple
            else ConformanceStatus.FAIL
        ),
        messages=message_tuple,
    )


def check_evidence_actor_reference(
    evidence: Evidence,
    actors: Iterable[Actor],
    *,
    checked_at: str | None = None,
) -> ConformanceResult:
    messages: list[str] = []
    if evidence.captured_by_actor_id not in _record_ids(actors):
        messages.append(
            "Evidence captured_by_actor_id does not resolve: "
            f"{evidence.captured_by_actor_id}"
        )
    return _result(
        check_id="evidence.actor-reference",
        m1_source="C01-A Evidence Standard v1.0; C01-C Identity Standard v1.0",
        subject_type="Evidence",
        subject_id=evidence.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_claim_actor_reference(
    claim: Claim,
    actors: Iterable[Actor],
    *,
    checked_at: str | None = None,
) -> ConformanceResult:
    messages: list[str] = []
    if claim.asserted_by_actor_id not in _record_ids(actors):
        messages.append(
            "Claim asserted_by_actor_id does not resolve: "
            f"{claim.asserted_by_actor_id}"
        )
    return _result(
        check_id="claim.actor-reference",
        m1_source="C01-B Claim Standard v1.0; C01-C Identity Standard v1.0",
        subject_type="Claim",
        subject_id=claim.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_review_references(
    review: Review,
    actors: Iterable[Actor],
    subject_records: Iterable[CoreRecord],
    evidence_records: Iterable[Evidence],
    *,
    checked_at: str | None = None,
) -> ConformanceResult:
    actor_ids = _record_ids(actors)
    subject_ids = _record_ids(subject_records)
    evidence_ids = _record_ids(evidence_records)
    messages: list[str] = []

    if review.reviewer_actor_id not in actor_ids:
        messages.append(
            "Review reviewer_actor_id does not resolve: "
            f"{review.reviewer_actor_id}"
        )
    if review.subject_id not in subject_ids:
        messages.append(f"Review subject_id does not resolve: {review.subject_id}")

    finding_evidence_ids = {
        evidence_id
        for finding in review.findings
        for evidence_id in finding.evidence_ids
    }
    for missing_id in sorted(finding_evidence_ids - evidence_ids):
        messages.append(
            f"Review finding evidence reference does not resolve: {missing_id}"
        )

    return _result(
        check_id="review.references",
        m1_source=(
            "C01-D Review Standard v1.0; C01-C Identity Standard v1.0; "
            "C01-A Evidence Standard v1.0"
        ),
        subject_type="Review",
        subject_id=review.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_registered_object_owner(
    registered_object: RegisteredObject,
    actors: Iterable[Actor],
    *,
    checked_at: str | None = None,
) -> ConformanceResult:
    messages: list[str] = []
    if registered_object.owner_actor_id not in _record_ids(actors):
        messages.append(
            "RegisteredObject owner_actor_id does not resolve: "
            f"{registered_object.owner_actor_id}"
        )
    return _result(
        check_id="registered-object.owner-reference",
        m1_source=(
            "C01-G Registered Object Standard v1.0; "
            "C01-C Identity Standard v1.0"
        ),
        subject_type="RegisteredObject",
        subject_id=registered_object.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_ledger_references(
    entry: GovernanceLedgerEntry,
    actors: Iterable[Actor],
    subject_records: Iterable[CoreRecord],
    *,
    checked_at: str | None = None,
) -> ConformanceResult:
    actor_ids = _record_ids(actors)
    subject_ids = _record_ids(subject_records)
    messages: list[str] = []
    if entry.actor_id not in actor_ids:
        messages.append(f"Ledger actor_id does not resolve: {entry.actor_id}")
    if entry.subject_id not in subject_ids:
        messages.append(f"Ledger subject_id does not resolve: {entry.subject_id}")
    return _result(
        check_id="ledger.references",
        m1_source=(
            "C01-H Governance Ledger Standard v1.0; "
            "C01-C Identity Standard v1.0"
        ),
        subject_type="GovernanceLedgerEntry",
        subject_id=entry.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_record_id_uniqueness(
    records: Iterable[CoreRecord],
    *,
    collection_id: str,
    checked_at: str | None = None,
) -> ConformanceResult:
    record_ids = [record.record_id for record in records]
    duplicates = sorted(
        record_id for record_id, count in Counter(record_ids).items() if count > 1
    )
    messages = [f"Duplicate record_id: {record_id}" for record_id in duplicates]
    return _result(
        check_id="registered-object.record-id-uniqueness",
        m1_source="C01-G Registered Object Standard v1.0",
        subject_type="CoreRecordCollection",
        subject_id=collection_id,
        messages=messages,
        checked_at=checked_at,
    )
