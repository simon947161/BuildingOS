# BuildingOS C01-C Identity Standard

## Project

BuildingOS

## Milestone

M1 - Specification Foundation

## Batch

C01-C - Identity Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## Freeze Decision

Architecture Review Result:

```text
APPROVE_AND_FREEZE_C01_C
```

C01-C Identity Standard is frozen as Version 1.0.

Future changes require:

```text
Change Request -> Version Review -> Approval -> Update
```

## 1. Purpose

The Identity Standard defines how BuildingOS represents Actors for attribution.

The standard exists to ensure that Evidence, Claims, Reviews, Decisions,
Procedures, Lifecycle events, Registered Objects, and Ledger entries can record
who or what was responsible for submitting, producing, reviewing, deciding, or
recording an action.

Identity in C01-C is attribution-only. It does not define permission systems,
access control, authorization logic, authentication, credential management, or
trust scoring.

## 2. Scope

In scope:

- Actor vocabulary and boundaries.
- Required fields for Actor Records.
- Actor types.
- Attribution roles.
- Relationship between Actor, Agency, Evidence, Claim, Review, Decision,
  Lifecycle, and Ledger.
- Conformance requirements for future BuildingOS implementations.

Out of scope:

- Runtime implementation.
- Python classes.
- SQLite schema.
- API contracts.
- MCP tools.
- Authentication.
- Authorization.
- Permission systems.
- Credential management.
- Identity proofing.
- Trust scoring.
- PRI implementation.

## 3. Glossary References

Normative glossary dependency:

- `BUILDINGOS_C00_GLOSSARY_FOUNDATION.md`
- Version: `1.0`
- Status: `FROZEN`

Related upstream specifications:

- `BUILDINGOS_C01_A_EVIDENCE_STANDARD.md`
  - Version: `1.0`
  - Status: `FROZEN`
- `BUILDINGOS_C01_B_CLAIM_STANDARD.md`
  - Version: `1.0`
  - Status: `FROZEN`

C01-C uses the following C00 terms:

- Actor
- Agency
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

### Actor

An Actor is an identifiable participant or source that performs, records,
submits, reviews, decides, or is attributed to a BuildingOS record or action.

Actor identity in C01-C is for attribution only.

### Actor Record

An Actor Record is the structured representation of an Actor in BuildingOS.

It records actor identity, actor type, attribution label, lifecycle status, and
known limitations.

### Actor Type

Actor Type classifies the kind of Actor being attributed.

Minimum Actor Types:

- Human
- Organisation
- AI Agent
- Device
- Sensor
- Contractor
- Authority

### Attribution Role

Attribution Role identifies why the Actor is referenced.

Examples include:

- source actor;
- submitter;
- claimant;
- reviewer;
- decision actor;
- recorder;
- custodian;
- observer;
- responsible organisation.

Attribution Role does not create authority by itself.

### Agency

Agency is the recognised capacity of an Actor to participate in a BuildingOS
process.

Agency supports attribution. Agency does not grant permission, approval,
certification authority, compliance authority, financial authority, or
operational authority by itself.

## 5. Required Fields

An Actor Record must include:

| Field | Requirement |
| --- | --- |
| actor_id | Stable identifier for the Actor Record. |
| actor_type | Controlled Actor Type category. |
| display_name | Human-readable name or label. |
| attribution_label | Label used when attributing an action or record. |
| actor_status | Current lifecycle status of the Actor Record. |
| source_reference | Source or record supporting the Actor entry where applicable. |
| created_at | Date or time the Actor Record was created. |
| created_by | Actor that created or registered the Actor Record. |
| limitations | Known uncertainty, scope boundary, alias, or identity limitation. |
| review_status | Current review status of the Actor Record where applicable. |

## 6. Behaviour

Actor Records must behave according to the following rules:

1. Actor identity must remain separable from permission or authority.
2. Actor attribution must be explicit when an Actor submits, produces, reviews,
   decides, records, or maintains a BuildingOS record.
3. A single Actor may have multiple Attribution Roles in different contexts.
4. Actor Type must not be used as automatic authority.
5. Agency must not be treated as authorization.
6. Actor Records may be linked to Evidence, Claim, Review, Decision, Procedure,
   Lifecycle, Registered Object, and Ledger records.
7. Actor Record lifecycle changes must preserve prior status history.
8. Uncertain, conflicting, or incomplete Actor identity must remain visible for
   review.

## 7. Constraints

Actor Records must not:

- grant permissions by existence;
- authorize implementation, approval, construction, investment, compliance,
  public claim, operational action, or certification;
- replace expert review, legal review, financial review, or governance review;
- imply that an AI Agent, Device, or Sensor has human authority;
- hide uncertainty about identity or attribution;
- silently merge separate Actors;
- rely on implementation-specific classes, databases, APIs, or runtime
  behaviour for conformance.

## 8. Actor Status Categories

Minimum Actor Status categories:

| Status | Meaning |
| --- | --- |
| active | Actor Record is active for attribution. |
| inactive | Actor Record is not active for current attribution. |
| pending_review | Actor Record requires review. |
| disputed | Actor identity or attribution is disputed. |
| superseded | Actor Record remains traceable but has been replaced. |
| withdrawn | Actor Record was withdrawn by source or governance process. |
| archived | Actor Record is retained for historical traceability. |

Actor Status does not create permission or authority.

## 9. Review Status Categories

Minimum Review Status categories:

| Status | Meaning |
| --- | --- |
| not_reviewed | Actor Record has not entered review. |
| review_required | Review is required before use in governance context. |
| under_review | Review is in progress. |
| reviewed | Actor Record reviewed within defined scope. |
| disputed | Review identified unresolved identity or attribution conflict. |
| closed | Review is closed in current scope. |

Review Status does not create authorization.

## 10. Conformance Requirements

A BuildingOS implementation, module, adapter, or specification conforms to
C01-C if it:

1. Preserves Identity as attribution-only.
2. Requires stable Actor Record identifiers.
3. Requires Actor Type.
4. Requires display name or attribution label.
5. Separates Actor identity from permission, authorization, and authority.
6. Supports the minimum Actor Types defined in C01-C.
7. Records Attribution Role when an Actor is linked to a governance record.
8. Preserves uncertain, disputed, or incomplete Actor identity for review.
9. Does not allow Actor Type or Agency to authorize action by itself.
10. References C00 v1.0 without redefining frozen terms or boundaries.
11. Preserves C01-A and C01-B attribution requirements where Evidence or Claims
    reference Actors.
12. Keeps implementation details outside the standard unless a later approved
    implementation specification governs them.

## 11. Examples

### Conformant Example

```text
Actor A-001 is a Human with attribution_role = reviewer for Review R-004.
The Actor Record attributes review responsibility but does not grant approval
authority by itself.
```

### Conformant Example

```text
Actor A-020 is a Sensor with attribution_role = source actor for Evidence
E-100. The sensor can be attributed as source, but it cannot approve a Claim.
```

### Conformant Example

```text
Actor A-030 is an Authority with attribution_role = decision actor for Decision
D-010. The Decision must still state scope and basis.
```

## 12. Non-Conformance Examples

The following are non-conformant:

- "The Actor exists, therefore it has permission."
- "The Sensor submitted Evidence, therefore the Claim is approved."
- "The AI Agent reviewed the Claim, therefore the Decision is authorized."
- "The Authority Actor type alone proves the Decision is within scope."
- "Two Actors were merged without preserving prior attribution history."
- "Identity review status and authorization status are the same field."

## 13. Rationale

Identity is the third C01 specification because Evidence and Claims require
Actor attribution before Review, Procedure, Lifecycle, Registered Object, and
Ledger specifications can reliably assign responsibility.

C01-C intentionally remains attribution-only to preserve the approved M1
boundary and avoid premature permission-system design.

## 14. Review Status

Current state:

```text
FROZEN_V1_0
```

Freeze record:

- `BUILDINGOS_C01_C_IDENTITY_STANDARD_FREEZE_RECORD_V1_0.md`

Next engineering batch:

- C01-D - Review Standard.
