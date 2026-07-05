# BuildingOS C01-A Evidence Standard

## Project

BuildingOS

## Milestone

M1 - Specification Foundation

## Batch

C01-A - Evidence Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## Freeze Decision

Architecture Review Result:

```text
APPROVE_AND_FREEZE_C01_A
```

C01-A Evidence Standard is frozen as Version 1.0.

Future changes require:

```text
Change Request -> Version Review -> Approval -> Update
```

## 1. Purpose

The Evidence Standard defines how BuildingOS records, references, classifies,
reviews, and constrains evidence across BuildingOS specifications.

The standard exists to prevent evidence from being treated as fact, approval,
decision, certification, compliance, operational authority, or public claim
authority without the required review and decision process.

## 2. Scope

In scope:

- Evidence vocabulary and boundaries.
- Required fields for evidence records.
- Evidence strength and verification status.
- Actor attribution for evidence submission, verification, and review.
- Relationships between Evidence, Claim, Review, Decision, Ledger, and
  Registered Object.
- Conformance requirements for future BuildingOS implementations.

Out of scope:

- Runtime implementation.
- Python classes.
- SQLite schema.
- API contracts.
- MCP tools.
- Automated evidence scoring.
- Legal, professional, financial, public, or regulatory approval.
- PRI implementation.

## 3. Glossary References

Normative glossary dependency:

- `BUILDINGOS_C00_GLOSSARY_FOUNDATION.md`
- Version: `1.0`
- Status: `FROZEN`

C01-A uses the following C00 terms:

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

### Evidence

Evidence is a traceable record, source, observation, document, dataset,
inspection result, or other support used to evaluate a specific Claim.

Evidence supports review. Evidence is not itself a confirmed fact, approval,
decision, certification, compliance status, or authority to act.

### Evidence Record

An Evidence Record is the structured representation of Evidence in BuildingOS.

It records provenance, source context, evidence type, evidence strength,
verification status, relationship to Claims, and relevant Actor attribution.

### Evidence Source

An Evidence Source is the origin of an Evidence Record.

Examples include:

- official document;
- submitted file;
- inspection record;
- sensor record;
- engineering note;
- procurement record;
- disclosure;
- review record;
- public source;
- observed condition.

### Evidence Strength

Evidence Strength indicates the relative support an Evidence Record may provide
for a Claim.

Evidence Strength does not confirm the Claim by itself.

### Verification Status

Verification Status records whether the Evidence Record has been checked,
reviewed, rejected, found conflicting, or remains unverified.

Verification Status does not override Claim review or Decision authority.

### Evidence Relationship

Evidence must be related to a specific Claim, Object, Review, Procedure,
Lifecycle event, or Ledger entry when used in governance.

Unrelated evidence may be stored for context, but it must not be used as support
for a Claim until its relationship is explicit.

## 5. Required Fields

An Evidence Record must include:

| Field | Requirement |
| --- | --- |
| evidence_id | Stable identifier for the Evidence Record. |
| evidence_type | Controlled evidence category. |
| source_reference | Source identifier, document reference, link, or record pointer. |
| source_actor | Actor attributed as source, producer, submitter, or custodian when known. |
| submitted_by | Actor that submitted or registered the Evidence Record. |
| submitted_at | Date or time of submission or registration. |
| provenance | Origin and chain-of-custody notes sufficient for review. |
| evidence_strength | Declared strength category. |
| verification_status | Current verification state. |
| related_claims | Claims supported, challenged, or contextualised by the Evidence Record. |
| related_objects | Registered Objects or other Objects referenced by the Evidence Record. |
| limitations | Known gaps, uncertainty, conditions, or scope limits. |
| review_notes | Human-readable review notes where applicable. |
| lifecycle_status | Active, superseded, withdrawn, rejected, archived, or equivalent status. |

## 6. Behaviour

Evidence Records must behave according to the following rules:

1. Evidence must remain separable from Claims.
2. Evidence must not be promoted into fact without review rules.
3. Evidence may support, weaken, contradict, or contextualise a Claim.
4. Conflicting Evidence Records must remain visible for review.
5. Stronger evidence may supersede weaker evidence only through a reviewable
   process.
6. Rejected evidence must remain traceable unless removal is required by a
   separate approved governance process.
7. Evidence used for a Decision must be linked to the Decision basis.
8. Evidence changes that affect governance outcomes should create Ledger
   entries.
9. Evidence lifecycle changes must preserve prior status history.
10. Evidence attribution must distinguish source Actor, submitting Actor, and
    reviewing Actor where those roles differ.

## 7. Constraints

Evidence Records must not:

- declare a Claim confirmed without Claim or Review rules;
- authorize implementation, approval, construction, investment, compliance,
  public claim, operational action, or certification;
- replace expert review when expert review is required;
- hide conflicting evidence;
- silently overwrite prior evidence;
- convert Agency into authority;
- convert registration into compliance;
- rely on implementation-specific classes, databases, APIs, or runtime
  behaviour for conformance.

## 8. Evidence Strength Categories

BuildingOS specifications may refine categories, but the following minimum
categories must be preserved:

| Category | Meaning |
| --- | --- |
| authoritative | Produced or issued by an authorised source within its scope. |
| official | Produced by a recognised official or institutional source. |
| reviewed | Checked by a qualified reviewer or approved review process. |
| submitted | Provided by an Actor but not independently reviewed. |
| observed | Captures a recorded condition or observation. |
| contextual | Provides background but does not directly support a Claim. |
| weak | Low confidence or incomplete support. |
| conflicting | Contradicts or materially differs from other evidence. |
| unsupported | Cannot currently support the Claim. |

Evidence Strength must not be interpreted as automatic truth.

## 9. Verification Status Categories

Minimum verification statuses:

| Status | Meaning |
| --- | --- |
| unverified | Evidence is recorded but not checked. |
| under_review | Evidence is being reviewed. |
| verified | Evidence passed the relevant verification process. |
| partially_verified | Some parts passed review, but gaps remain. |
| conflicting | Evidence conflicts with another record or source. |
| rejected | Evidence was reviewed and rejected for the stated purpose. |
| superseded | Evidence remains traceable but has been replaced for current review. |
| withdrawn | Evidence was withdrawn by the source or governance process. |

Verification Status applies to the Evidence Record, not automatically to any
Claim.

## 10. Conformance Requirements

A BuildingOS implementation, module, adapter, or specification conforms to
C01-A if it:

1. Preserves the distinction between Evidence and Claim.
2. Requires stable Evidence Record identifiers.
3. Requires source reference and provenance.
4. Requires Actor attribution for submission and review where applicable.
5. Records evidence strength separately from verification status.
6. Records related Claims explicitly when Evidence is used to support a Claim.
7. Preserves conflicting evidence for review.
8. Does not allow Evidence to authorize action by itself.
9. Preserves lifecycle status and prior review status.
10. References C00 v1.0 terminology without redefining C00 terms.
11. Defines any additional evidence categories before using them as
    requirements.
12. Keeps implementation details outside the standard unless a later approved
    implementation specification governs them.

## 11. Examples

### Conformant Example

```text
Evidence E-001 is an official inspection record submitted by Actor A-101.
It supports Claim C-004 and has verification_status = under_review.
It cannot confirm Claim C-004 until the required Review is complete.
```

### Conformant Example

```text
Evidence E-009 conflicts with Evidence E-002.
Both records remain visible, and the Claim moves to conflicting review status.
```

### Conformant Example

```text
Evidence E-020 is authoritative for document issuance but not sufficient to
authorize construction.
```

## 12. Non-Conformance Examples

The following are non-conformant:

- "Evidence exists, therefore the Claim is confirmed."
- "The inspection photo approves the component for operation."
- "The latest Evidence Record overwrites the older conflicting record."
- "The submitting Actor has Agency, so the Evidence is authoritative."
- "The Evidence Record is registered, so the underlying object is compliant."
- "Verification status of the Evidence automatically becomes Decision status."

## 13. Rationale

Evidence is the first C01 specification because all later BuildingOS governance
objects depend on evidence discipline.

Claim, Review, Procedure, Lifecycle, Registered Object, and Ledger standards
must all preserve the boundary that Evidence supports review but does not
create authority by itself.

## 14. Review Status

Current state:

```text
FROZEN_V1_0
```

Freeze record:

- `BUILDINGOS_C01_A_EVIDENCE_STANDARD_FREEZE_RECORD_V1_0.md`

Next engineering batch:

- C01-B - Claim Standard.
