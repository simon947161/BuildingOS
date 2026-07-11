"""Deterministic M1 conformance checks for Core Batch 01."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from .models import (
    Actor,
    Claim,
    ConformanceResult,
    ConformanceStatus,
    Evidence,
    GovernanceLedgerEntry,
    Lifecycle,
    ModuleContract,
    Procedure,
    RegisteredObject,
    Review,
    ReviewStatus,
    SupportStatus,
    utc_now_iso,
)

KNOWN_CORE_TYPES = frozenset(
    {
        "Actor",
        "Evidence",
        "Claim",
        "Review",
        "Procedure",
        "Lifecycle",
        "RegisteredObject",
        "GovernanceLedgerEntry",
        "ModuleContract",
        "ConformanceResult",
    }
)


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
    status = ConformanceStatus.PASS if not message_tuple else ConformanceStatus.FAIL
    return ConformanceResult(
        record_id=f"conformance:{check_id}:{subject_id}",
        created_at=checked_at or utc_now_iso(),
        check_id=check_id,
        m1_source=m1_source,
        subject_type=subject_type,
        subject_id=subject_id,
        status=status,
        messages=message_tuple,
    )


def check_actor_attribution(
    actor: Actor, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not actor.display_name.strip():
        messages.append("Actor display_name is required.")
    if not actor.actor_type.strip():
        messages.append("Actor actor_type is required.")
    return _result(
        check_id="identity.actor-attribution",
        m1_source="C01-C Identity Standard v1.0",
        subject_type="Actor",
        subject_id=actor.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_evidence_structure(
    evidence: Evidence, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not evidence.provenance_note.strip():
        messages.append("Evidence provenance_note is required for conformance.")
    if not evidence.integrity_status.strip():
        messages.append("Evidence integrity_status is required for conformance.")
    return _result(
        check_id="evidence.structure",
        m1_source="C01-A Evidence Standard v1.0",
        subject_type="Evidence",
        subject_id=evidence.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_claim_structure(
    claim: Claim, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not isinstance(claim.support_status, SupportStatus):
        messages.append("Claim support_status must be a SupportStatus value.")
    return _result(
        check_id="claim.structure",
        m1_source="C01-B Claim Standard v1.0",
        subject_type="Claim",
        subject_id=claim.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_claim_evidence_links(
    claim: Claim,
    evidence_records: Iterable[Evidence],
    *,
    checked_at: str | None = None,
) -> ConformanceResult:
    known_ids = {item.record_id for item in evidence_records}
    missing = sorted(set(claim.evidence_ids) - known_ids)
    messages = [f"Evidence reference does not resolve: {item}" for item in missing]
    return _result(
        check_id="claim.evidence-links",
        m1_source="C01-B Claim Standard v1.0",
        subject_type="Claim",
        subject_id=claim.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_review_structure(
    review: Review, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not isinstance(review.status, ReviewStatus):
        messages.append("Review status must be a ReviewStatus value.")
    finding_ids = [finding.finding_id for finding in review.findings]
    duplicates = sorted(
        item for item, count in Counter(finding_ids).items() if count > 1
    )
    messages.extend(f"Duplicate review finding_id: {item}" for item in duplicates)
    return _result(
        check_id="review.structure",
        m1_source="C01-D Review Standard v1.0",
        subject_type="Review",
        subject_id=review.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_review_boundary(
    review: Review, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    forbidden_names = {"approve", "reject", "decide", "authorize"}
    exposed = forbidden_names.intersection(dir(review))
    if exposed:
        messages.append(
            "Review exposes forbidden decision-authority members: "
            + ", ".join(sorted(exposed))
        )
    return _result(
        check_id="review.no-decision-authority",
        m1_source="C01-D Review Standard v1.0",
        subject_type="Review",
        subject_id=review.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_procedure_structure(
    procedure: Procedure, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not procedure.steps:
        messages.append("Procedure must declare at least one descriptive step.")
    step_ids = [step.step_id for step in procedure.steps]
    duplicate_ids = sorted(
        item for item, count in Counter(step_ids).items() if count > 1
    )
    messages.extend(f"Duplicate procedure step_id: {item}" for item in duplicate_ids)
    sequences = [step.sequence for step in procedure.steps]
    if sequences != sorted(sequences):
        messages.append("Procedure steps must be stored in ascending sequence order.")
    return _result(
        check_id="procedure.structure",
        m1_source="C01-E Procedure Standard v1.0",
        subject_type="Procedure",
        subject_id=procedure.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_lifecycle_structure(
    lifecycle: Lifecycle, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if lifecycle.current_stage not in lifecycle.stages:
        messages.append("Lifecycle current_stage must be one of the declared stages.")
    if len(lifecycle.stages) != len(set(lifecycle.stages)):
        messages.append("Lifecycle stages must be unique.")
    return _result(
        check_id="lifecycle.structure",
        m1_source="C01-F Lifecycle Standard v1.0",
        subject_type="Lifecycle",
        subject_id=lifecycle.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_registered_object_structure(
    registered_object: RegisteredObject, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not registered_object.version.strip():
        messages.append("RegisteredObject version is required.")
    return _result(
        check_id="registered-object.structure",
        m1_source="C01-G Registered Object Standard v1.0",
        subject_type="RegisteredObject",
        subject_id=registered_object.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_ledger_structure(
    entry: GovernanceLedgerEntry, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    forbidden_names = {"append_to_blockchain", "log_application_event"}
    exposed = forbidden_names.intersection(dir(entry))
    if exposed:
        messages.append(
            "GovernanceLedgerEntry exposes excluded runtime members: "
            + ", ".join(sorted(exposed))
        )
    return _result(
        check_id="ledger.structure",
        m1_source="C01-H Governance Ledger Standard v1.0",
        subject_type="GovernanceLedgerEntry",
        subject_id=entry.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_module_contract_structure(
    contract: ModuleContract, *, checked_at: str | None = None
) -> ConformanceResult:
    messages: list[str] = []
    if not contract.obligations:
        messages.append("ModuleContract must declare at least one obligation.")
    if not contract.exclusions:
        messages.append("ModuleContract must declare at least one exclusion.")
    forbidden_names = {"execute", "run", "dispatch"}
    exposed = forbidden_names.intersection(dir(contract))
    if exposed:
        messages.append(
            "ModuleContract exposes excluded runtime members: "
            + ", ".join(sorted(exposed))
        )
    return _result(
        check_id="module-contract.structure",
        m1_source="C01-I Module Contract Standard v1.0",
        subject_type="ModuleContract",
        subject_id=contract.record_id,
        messages=messages,
        checked_at=checked_at,
    )


def check_module_contract_types(
    contract: ModuleContract, *, checked_at: str | None = None
) -> ConformanceResult:
    declared = set(contract.input_types).union(contract.output_types)
    unknown = sorted(declared - KNOWN_CORE_TYPES)
    messages = [f"Unknown Core object type: {item}" for item in unknown]
    return _result(
        check_id="module-contract.known-types",
        m1_source="C01-I Module Contract Standard v1.0",
        subject_type="ModuleContract",
        subject_id=contract.record_id,
        messages=messages,
        checked_at=checked_at,
    )
