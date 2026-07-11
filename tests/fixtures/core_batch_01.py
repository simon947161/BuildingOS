"""Fixed fictional fixture set for Governance Kernel regression tests."""

from buildingos_core import (
    Actor,
    Claim,
    Evidence,
    GovernanceLedgerEntry,
    Lifecycle,
    ModuleContract,
    Procedure,
    ProcedureStep,
    RegisteredObject,
    Review,
    ReviewFinding,
    ReviewStatus,
    SupportStatus,
)

FIXTURE_TIMESTAMP = "2026-07-12T00:00:00+00:00"


def build_fictional_core_batch_01_fixture() -> dict[str, object]:
    """Return a complete, fixed, non-production fictional record set."""

    owner = Actor(
        record_id="actor-owner-001",
        created_at=FIXTURE_TIMESTAMP,
        display_name="Fictional Project Owner",
        actor_type="human",
    )
    reviewer = Actor(
        record_id="actor-reviewer-001",
        created_at=FIXTURE_TIMESTAMP,
        display_name="Fictional Independent Reviewer",
        actor_type="human",
    )
    evidence = Evidence(
        record_id="evidence-photo-001",
        created_at=FIXTURE_TIMESTAMP,
        title="Fictional envelope photograph",
        evidence_type="photograph",
        source_reference="fixture://fictional-building-alpha/photo-001",
        captured_by_actor_id=owner.record_id,
        captured_at=FIXTURE_TIMESTAMP,
        provenance_note="Fictional regression fixture only.",
        integrity_status="FIXTURE_DECLARED",
    )
    claim = Claim(
        record_id="claim-envelope-001",
        created_at=FIXTURE_TIMESTAMP,
        statement="The fictional envelope record includes a shaded opening.",
        asserted_by_actor_id=owner.record_id,
        evidence_ids=(evidence.record_id,),
        support_status=SupportStatus.SUPPORTED,
    )
    registered_object = RegisteredObject(
        record_id="fictional-building-alpha",
        created_at=FIXTURE_TIMESTAMP,
        object_type="FictionalBuilding",
        version="1.0",
        title="Fictional Building Alpha",
        owner_actor_id=owner.record_id,
    )
    review = Review(
        record_id="review-envelope-001",
        created_at=FIXTURE_TIMESTAMP,
        subject_id=claim.record_id,
        reviewer_actor_id=reviewer.record_id,
        status=ReviewStatus.COMPLETED,
        findings=(
            ReviewFinding(
                finding_id="finding-evidence-link-001",
                text="The fictional evidence reference resolves.",
                evidence_ids=(evidence.record_id,),
            ),
        ),
    )
    procedure = Procedure(
        record_id="procedure-evidence-review-001",
        created_at=FIXTURE_TIMESTAMP,
        name="Fictional evidence review procedure",
        purpose="Describe a review sequence without executing it.",
        steps=(
            ProcedureStep(
                step_id="step-inspect-001",
                sequence=1,
                description="Inspect the fictional evidence record.",
                responsible_actor_type="human-reviewer",
            ),
            ProcedureStep(
                step_id="step-record-001",
                sequence=2,
                description="Record a fictional review finding.",
                responsible_actor_type="human-reviewer",
            ),
        ),
    )
    lifecycle = Lifecycle(
        record_id="lifecycle-fictional-object-001",
        created_at=FIXTURE_TIMESTAMP,
        name="Fictional object lifecycle",
        stages=("DRAFT", "REVIEW", "FROZEN"),
        current_stage="REVIEW",
    )
    ledger_entry = GovernanceLedgerEntry(
        record_id="ledger-review-recorded-001",
        created_at=FIXTURE_TIMESTAMP,
        event_type="REVIEW_RECORDED",
        actor_id=reviewer.record_id,
        subject_id=review.record_id,
        summary="A fictional review record was added without approval authority.",
    )
    module_contract = ModuleContract(
        record_id="module-contract-governance-kernel-001",
        created_at=FIXTURE_TIMESTAMP,
        module_name="governance-kernel-records",
        purpose="Represent governance records without executing project work.",
        input_types=("Actor", "Evidence", "Claim"),
        output_types=("Review", "GovernanceLedgerEntry"),
        obligations=("Preserve record identifiers", "Preserve evidence references"),
        exclusions=("Approval authority", "Workflow execution"),
    )

    return {
        "owner": owner,
        "reviewer": reviewer,
        "evidence": evidence,
        "claim": claim,
        "registered_object": registered_object,
        "review": review,
        "procedure": procedure,
        "lifecycle": lifecycle,
        "ledger_entry": ledger_entry,
        "module_contract": module_contract,
    }
