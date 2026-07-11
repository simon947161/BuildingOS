"""Minimum representational models for BuildingOS Core Batch 01.

These records are deliberately non-executing. They represent governance facts and
structures; they do not approve work, assign permissions, automate procedures, or
perform lifecycle transitions.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SupportStatus(str, Enum):
    UNSUPPORTED = "UNSUPPORTED"
    PARTIALLY_SUPPORTED = "PARTIALLY_SUPPORTED"
    SUPPORTED = "SUPPORTED"
    CONFLICTED = "CONFLICTED"
    UNKNOWN = "UNKNOWN"


class ReviewStatus(str, Enum):
    DRAFT = "DRAFT"
    IN_REVIEW = "IN_REVIEW"
    COMPLETED = "COMPLETED"


class ConformanceStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"


@dataclass(frozen=True)
class CoreRecord:
    record_id: str
    created_at: str = field(default_factory=utc_now_iso)

    def __post_init__(self) -> None:
        if not self.record_id.strip():
            raise ValueError("record_id must not be empty")
        if not self.created_at.strip():
            raise ValueError("created_at must not be empty")

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key, value in list(data.items()):
            if isinstance(value, Enum):
                data[key] = value.value
        return data


@dataclass(frozen=True)
class Actor(CoreRecord):
    display_name: str = ""
    actor_type: str = "human"
    external_reference: str | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.display_name.strip():
            raise ValueError("display_name must not be empty")
        if not self.actor_type.strip():
            raise ValueError("actor_type must not be empty")


@dataclass(frozen=True)
class Evidence(CoreRecord):
    title: str = ""
    evidence_type: str = "document"
    source_reference: str = ""
    captured_by_actor_id: str = ""
    captured_at: str = ""
    provenance_note: str = ""
    integrity_status: str = "UNASSESSED"

    def __post_init__(self) -> None:
        super().__post_init__()
        required = {
            "title": self.title,
            "evidence_type": self.evidence_type,
            "source_reference": self.source_reference,
            "captured_by_actor_id": self.captured_by_actor_id,
            "captured_at": self.captured_at,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} must not be empty")


@dataclass(frozen=True)
class Claim(CoreRecord):
    statement: str = ""
    asserted_by_actor_id: str = ""
    evidence_ids: tuple[str, ...] = ()
    support_status: SupportStatus = SupportStatus.UNKNOWN

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.statement.strip():
            raise ValueError("statement must not be empty")
        if not self.asserted_by_actor_id.strip():
            raise ValueError("asserted_by_actor_id must not be empty")
        if any(not item.strip() for item in self.evidence_ids):
            raise ValueError("evidence_ids must not contain empty values")


@dataclass(frozen=True)
class ReviewFinding:
    finding_id: str
    text: str
    evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.finding_id.strip() or not self.text.strip():
            raise ValueError("review finding id and text are required")


@dataclass(frozen=True)
class Review(CoreRecord):
    subject_id: str = ""
    reviewer_actor_id: str = ""
    status: ReviewStatus = ReviewStatus.DRAFT
    findings: tuple[ReviewFinding, ...] = ()

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.subject_id.strip():
            raise ValueError("subject_id must not be empty")
        if not self.reviewer_actor_id.strip():
            raise ValueError("reviewer_actor_id must not be empty")


@dataclass(frozen=True)
class ProcedureStep:
    step_id: str
    sequence: int
    description: str
    responsible_actor_type: str

    def __post_init__(self) -> None:
        if not self.step_id.strip() or not self.description.strip():
            raise ValueError("procedure step id and description are required")
        if self.sequence < 1:
            raise ValueError("procedure step sequence must be positive")
        if not self.responsible_actor_type.strip():
            raise ValueError("responsible_actor_type must not be empty")


@dataclass(frozen=True)
class Procedure(CoreRecord):
    name: str = ""
    purpose: str = ""
    steps: tuple[ProcedureStep, ...] = ()

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.name.strip() or not self.purpose.strip():
            raise ValueError("procedure name and purpose are required")
        sequences = [step.sequence for step in self.steps]
        if len(sequences) != len(set(sequences)):
            raise ValueError("procedure step sequences must be unique")


@dataclass(frozen=True)
class Lifecycle(CoreRecord):
    name: str = ""
    stages: tuple[str, ...] = ()
    current_stage: str = ""

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.name.strip():
            raise ValueError("lifecycle name must not be empty")
        if not self.stages:
            raise ValueError("lifecycle must contain at least one stage")
        if any(not stage.strip() for stage in self.stages):
            raise ValueError("lifecycle stages must not be empty")
        if len(self.stages) != len(set(self.stages)):
            raise ValueError("lifecycle stages must be unique")
        if self.current_stage not in self.stages:
            raise ValueError("current_stage must be one of stages")


@dataclass(frozen=True)
class RegisteredObject(CoreRecord):
    object_type: str = ""
    version: str = "1.0"
    title: str = ""
    owner_actor_id: str = ""

    def __post_init__(self) -> None:
        super().__post_init__()
        required = {
            "object_type": self.object_type,
            "version": self.version,
            "title": self.title,
            "owner_actor_id": self.owner_actor_id,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} must not be empty")


@dataclass(frozen=True)
class GovernanceLedgerEntry(CoreRecord):
    event_type: str = ""
    actor_id: str = ""
    subject_id: str = ""
    summary: str = ""

    def __post_init__(self) -> None:
        super().__post_init__()
        required = {
            "event_type": self.event_type,
            "actor_id": self.actor_id,
            "subject_id": self.subject_id,
            "summary": self.summary,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} must not be empty")


@dataclass(frozen=True)
class ModuleContract(CoreRecord):
    module_name: str = ""
    purpose: str = ""
    input_types: tuple[str, ...] = ()
    output_types: tuple[str, ...] = ()
    obligations: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.module_name.strip() or not self.purpose.strip():
            raise ValueError("module_name and purpose are required")
        for collection_name, values in {
            "input_types": self.input_types,
            "output_types": self.output_types,
            "obligations": self.obligations,
            "exclusions": self.exclusions,
        }.items():
            if any(not item.strip() for item in values):
                raise ValueError(f"{collection_name} must not contain empty values")


@dataclass(frozen=True)
class ConformanceResult(CoreRecord):
    check_id: str = ""
    m1_source: str = ""
    subject_type: str = ""
    subject_id: str = ""
    status: ConformanceStatus = ConformanceStatus.FAIL
    messages: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        super().__post_init__()
        required = {
            "check_id": self.check_id,
            "m1_source": self.m1_source,
            "subject_type": self.subject_type,
            "subject_id": self.subject_id,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} must not be empty")

    @property
    def checked_at(self) -> str:
        """Expose the M1 conformance timestamp name without duplicating storage."""

        return self.created_at

    def to_dict(self) -> dict[str, Any]:
        data = super().to_dict()
        data["checked_at"] = self.checked_at
        return data
