# BuildingOS C01-B Claim Standard

## Project

BuildingOS

## Milestone

M1 - Specification Foundation

## Batch

C01-B - Claim Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## Freeze Decision

Architecture Review Result:

```text
APPROVE_AND_FREEZE_C01_B
```

C01-B Claim Standard is frozen as Version 1.0.

Future changes require:

```text
Change Request -> Version Review -> Approval -> Update
```

## 1. Purpose

The Claim Standard defines how BuildingOS records, scopes, supports, reviews,
and constrains claims.

The standard exists to prevent assertions from becoming accepted facts,
decisions, approvals, compliance positions, public claims, investment signals,
or operational instructions without required evidence, review, and decision
processes.

## 2. Scope

In scope:

- Claim vocabulary and boundaries.
- Required fields for Claim Records.
- Relationship between Claims and Evidence.
- Claim status and review status.
- Actor attribution for claim submission and review.
- Conformance requirements for future BuildingOS implementations.

Out of scope:

- Runtime implementation.
- Python classes.
- SQLite schema.
- API contracts.
- MCP tools.
- Automated claim scoring.
- Legal, professional, financial, public, or regulatory approval.
- PRI implementation.

## 3. Glossary References

Normative glossary dependency:

- `BUILDINGOS_C00_GLOSSARY_FOUNDATION.md`
- Version: `1.0`
- Status: `FROZEN`

Normative evidence dependency:

- `BUILDINGOS_C01_A_EVIDENCE_STANDARD.md`
- Version: `1.0`
- Status: `FROZEN`

C01-B uses the following C00 terms:

- Actor
- Agency
- Object
- Registered Object
- Evidence
- Claim
- Review
- Decision
- Procedure
- Lifecycle
- Ledger
- Governance
- Conformance

## 4. Core Concepts

### Claim

A Claim is a specific assertion submitted for review.

A Claim may describe a project state, object property, event, compliance
position, engineering condition, lifecycle status, evidence interpretation, or
other reviewable statement.

A Claim must be traceable to Evidence or explicitly marked as unsupported,
unverified, conflicting, or out of scope.

### Claim Record

A Claim Record is the structured representation of a Claim in BuildingOS.

It records the assertion, scope, claimant, related Evidence, confidence,
review status, limitations, and decision boundary.

### Claim Scope

Claim Scope defines what the Claim applies to.

Claim Scope may include:

- Object;
- Registered Object;
- Development Activity;
- project;
- procedure;
- lifecycle event;
- evidence interpretation;
- time period;
- geography;
- authority boundary.

### Claim Support

Claim Support is the relationship between a Claim and the Evidence Records that
support, weaken, contradict, or contextualise it.

Evidence can support review of a Claim, but Evidence does not confirm the Claim
by itself.

### Claim Status

Claim Status records the current state of the Claim as an assertion.

Claim Status is separate from Evidence verification status, Review outcome, and
Decision status.

### Review Status

Review Status records whether the Claim has been reviewed, is under review, is
blocked, or requires expert or governance review.

Review Status does not create approval or implementation authority.

## 5. Required Fields

A Claim Record must include:

| Field | Requirement |
| --- | --- |
| claim_id | Stable identifier for the Claim Record. |
| claim_text | Exact assertion being submitted for review. |
| claim_type | Controlled category or declared type of Claim. |
| claim_scope | Defined object, activity, project, period, geography, or governance boundary. |
| submitted_by | Actor that submitted or registered the Claim. |
| submitted_at | Date or time of submission or registration. |
| claimant | Actor responsible for the assertion when different from submitter. |
| related_evidence | Evidence Records supporting, weakening, contradicting, or contextualising the Claim. |
| evidence_summary | Human-readable summary of evidence relationship and known gaps. |
| claim_status | Current assertion status. |
| review_status | Current review state. |
| confidence_statement | Bounded statement of confidence, uncertainty, or insufficiency. |
| limitations | Known gaps, conditions, exclusions, or unsupported parts. |
| decision_boundary | Statement of what the Claim does and does not authorize. |
| lifecycle_status | Active, superseded, withdrawn, rejected, archived, or equivalent status. |

## 6. Behaviour

Claim Records must behave according to the following rules:

1. A Claim must remain separable from Evidence.
2. A Claim must not be confirmed without review rules.
3. A Claim with no Evidence must be marked unsupported or unverified.
4. A Claim with conflicting Evidence must preserve the conflict for review.
5. A Claim may be supported, weakened, contradicted, or contextualised by
   Evidence.
6. A Claim may become decision-ready only through the required Review and
   Decision process.
7. A Claim may be rejected without deleting the Claim Record.
8. Claim lifecycle changes must preserve prior status history.
9. Claim review actions should create Ledger entries when they affect
   governance outcomes.
10. Claim attribution must distinguish claimant, submitter, reviewer, and
    decision authority where those roles differ.

## 7. Constraints

Claim Records must not:

- treat Evidence as automatic confirmation;
- treat Review as automatic Decision;
- authorize implementation, approval, construction, investment, compliance,
  public claim, operational action, or certification;
- hide unsupported or conflicting status;
- silently overwrite prior Claim versions;
- convert Agency into authority;
- convert registration into compliance;
- rely on implementation-specific classes, databases, APIs, or runtime
  behaviour for conformance.

## 8. Claim Status Categories

Minimum Claim Status categories:

| Status | Meaning |
| --- | --- |
| submitted | Claim has been submitted but not reviewed. |
| unsupported | Claim lacks sufficient related Evidence. |
| evidence_linked | Claim has related Evidence but is not confirmed. |
| under_review | Claim is being reviewed. |
| conflicting | Claim has material evidence conflict. |
| partially_supported | Some parts are supported, but gaps remain. |
| review_ready | Claim is ready for formal review. |
| rejected | Claim was reviewed and rejected for the stated purpose. |
| superseded | Claim remains traceable but has been replaced. |
| withdrawn | Claim was withdrawn by the claimant or governance process. |

Claim Status applies to the assertion, not to any Decision.

## 9. Review Status Categories

Minimum Review Status categories:

| Status | Meaning |
| --- | --- |
| not_reviewed | Claim has not entered review. |
| review_required | Review is required before use. |
| under_review | Review is in progress. |
| expert_review_required | Domain expert review is required. |
| governance_review_required | Governance review is required. |
| review_completed | Review completed within defined scope. |
| decision_required | A Decision is required before the Claim can be used. |
| closed | Review is closed without further action in current scope. |

Review Status does not create approval or operational authority.

## 10. Conformance Requirements

A BuildingOS implementation, module, adapter, or specification conforms to
C01-B if it:

1. Preserves the distinction between Claim and Evidence.
2. Requires stable Claim Record identifiers.
3. Requires exact claim text.
4. Requires claim scope.
5. Requires Actor attribution for claimant and submitter.
6. Records related Evidence explicitly when Evidence is used.
7. Allows unsupported Claims only when clearly marked unsupported or
   unverified.
8. Preserves conflicting Evidence and Claim statuses for review.
9. Records Claim Status separately from Review Status and Decision Status.
10. Does not allow Claims to authorize action by themselves.
11. References C00 v1.0 and C01-A v1.0 without redefining frozen terms or
    boundaries.
12. Keeps implementation details outside the standard unless a later approved
    implementation specification governs them.

## 11. Examples

### Conformant Example

```text
Claim C-001 states that Object O-010 completed inspection on a specific date.
It is linked to Evidence E-022 and has review_status = review_required.
It cannot be used as an approval until the required Review and Decision are
complete.
```

### Conformant Example

```text
Claim C-009 is marked conflicting because Evidence E-010 and Evidence E-011
report different lifecycle states for the same Object.
```

### Conformant Example

```text
Claim C-020 is unsupported and remains visible for remediation rather than
being deleted.
```

## 12. Non-Conformance Examples

The following are non-conformant:

- "The Claim is true because Evidence exists."
- "The Claim is approved because a reviewer commented on it."
- "The Claim authorizes construction."
- "Conflicting Evidence was deleted to simplify the Claim status."
- "The Claim is compliant because it is registered."
- "Claim status and Decision status are the same field."

## 13. Rationale

Claims are the second C01 specification because BuildingOS governance depends
on controlling the movement from assertion to evidence-supported review.

The Claim Standard depends on C01-A because Claims must be traceable to
Evidence without treating Evidence as automatic truth.

## 14. Review Status

Current state:

```text
FROZEN_V1_0
```

Freeze record:

- `BUILDINGOS_C01_B_CLAIM_STANDARD_FREEZE_RECORD_V1_0.md`

Next engineering batch:

- C01-C - Identity Standard.
