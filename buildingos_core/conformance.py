"""Deterministic M1 conformance checks for Core Batch 01."""

from __future__ import annotations

from collections.abc import Iterable

from .models import (
    Actor,
    Claim,
    ConformanceResult,
    ConformanceStatus,
    Evidence,
    ModuleContract,
    Review,
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
) -> ConformanceResult:
    message_tuple = tuple(messages)
    status = ConformanceStatus.PASS if not message_tuple else ConformanceStatus.FAIL
    return ConformanceResult(
        record_id=f"conformance:{check_id}:{subject_id}",
        check_id=check_id,
        m1_source=m1_source,
        subject_type=subject_type,
        subject_id=subject_id,
        status=status,
        messages=message_tuple,
    )


def check_actor_attribution(actor: Actor) -> ConformanceResult:
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
    )


def check_claim_evidence_links(
    claim: Claim, evidence_records: Iterable[Evidence]
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
    )


def check_review_boundary(review: Review) -> ConformanceResult:
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
    )


def check_module_contract_types(contract: ModuleContract) -> ConformanceResult:
    declared = set(contract.input_types).union(contract.output_types)
    unknown = sorted(declared - KNOWN_CORE_TYPES)
    messages = [f"Unknown Core object type: {item}" for item in unknown]
    return _result(
        check_id="module-contract.known-types",
        m1_source="C01-I Module Contract Standard v1.0",
        subject_type="ModuleContract",
        subject_id=contract.record_id,
        messages=messages,
    )
