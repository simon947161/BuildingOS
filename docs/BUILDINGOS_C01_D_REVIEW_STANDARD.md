# BuildingOS C01-D Review Standard

## Project

BuildingOS

## Milestone

M1 - Specification Foundation

## Batch

C01-D - Review Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## Freeze Decision

Codex Engineering Manager decision:

```text
APPROVE_AND_FREEZE_C01_D
```

C01-D Review Standard is frozen as Version 1.0.

## 1. Purpose

The Review Standard defines how BuildingOS records structured evaluation of
Evidence, Claims, Actors, Objects, Procedures, Lifecycle events, Decisions, and
other governance records.

The standard exists to prevent review activity from being confused with
approval, decision authority, certification, compliance status, public claim
authority, investment authority, or operational authority.

## 2. Scope

In scope:

- Review vocabulary and boundaries.
- Required fields for Review Records.
- Relationships between Review, Evidence, Claim, Identity, Decision,
  Procedure, Lifecycle, Registered Object, and Ledger.
- Review status and review outcome categories.
- Actor attribution for review actions.
- Review recommendations and escalation requirements.
- Conformance requirements for future BuildingOS implementations.

Out of scope:

- Runtime implementation.
- Python classes.
- SQLite schema.
- API contracts.
- MCP tools.
- Automated review scoring.
- Workflow engine implementation.
- Legal, professional, financial, public, or regulatory approval.
- PRI implementation.

## 3. Glossary References

Normative glossary dependency:

- `BUILDINGOS_C00_GLOSSARY_FOUNDATION.md`
- Version: `1.0`
- Status: `FROZEN`

## 4. Related Standards

C01-D depends on the following frozen standards:

| Standard | Version | Status | Relationship |
| --- | --- | --- | --- |
| C00 - BuildingOS Glossary Foundation | 1.0 | Frozen | Defines Review, Evidence, Claim, Actor, Decision, Governance, and Conformance terms. |
| C01-A - Evidence Standard | 1.0 | Frozen | Defines evidence boundaries and evidence verification status used by Review Records. |
| C01-B - Claim Standard | 1.0 | Frozen | Defines claim boundaries, claim status, and review status that Review Records evaluate. |
| C01-C - Identity Standard | 1.0 | Frozen | Defines Actor attribution for reviewers, submitters, decision actors, and custodians. |

No C01-D term may redefine frozen upstream terms or boundaries.

## 5. Core Concepts

### Review

A Review is a structured evaluation of Evidence, Claims, Actors, Objects,
Procedures, Lifecycle events, Decisions, or other governed records.

A Review records observations, assessments, gaps, conflicts, required expert
input, recommendations, and review outcomes.

A Review does not automatically create approval, implementation authority,
compliance status, certification, public claim authority, investment authority,
or operational authority.

### Review Record

A Review Record is the structured representation of a Review in BuildingOS.

It records review scope, reviewed items, reviewer attribution, evidence basis,
claim basis, assessment, outcome, recommendations, limitations, and escalation
requirements.

### Review Scope

Review Scope defines what the Review covers and what it does not cover.

Review Scope may include:

- Evidence Record;
- Claim Record;
- Actor Record;
- Registered Object;
- Development Activity;
- Procedure stage or gate;
- Lifecycle event;
- Decision preparation;
- Ledger event.

### Review Basis

Review Basis is the set of Evidence, Claims, Actor attributions, prior Reviews,
and governance references considered by the Review.

Review Basis must be traceable.

### Review Observation

A Review Observation is a statement made during review about what is visible in
the reviewed material.

Review Observations must remain distinct from assessment, recommendation, and
decision.

### Review Assessment

A Review Assessment is the reviewer's structured evaluation of the Review
Basis.

An Assessment may identify sufficiency, insufficiency, conflict, uncertainty,
or required escalation.

### Review Recommendation

A Review Recommendation is a proposed next step, review action, escalation, or
decision option.

A Review Recommendation is not a Decision and does not authorize action by
itself.

### Review Outcome

Review Outcome records the result of the Review within its defined scope.

Review Outcome does not replace Decision status.

## 6. Required Fields

A Review Record must include:

| Field | Requirement |
| --- | --- |
| review_id | Stable identifier for the Review Record. |
| review_type | Controlled review category or declared review type. |
| review_scope | Defined scope and explicit exclusions. |
| reviewed_items | Evidence, Claims, Actors, Objects, Procedures, Lifecycle events, or Decisions reviewed. |
| review_basis | Evidence, Claims, prior Reviews, or governance records used as basis. |
| reviewer | Actor responsible for the Review. |
| reviewer_role | Attribution Role for the reviewer in this Review. |
| submitted_at | Date or time the Review Record was submitted or registered. |
| review_status | Current status of the Review. |
| review_outcome | Outcome within the defined Review Scope. |
| observations | Review Observations. |
| assessment | Review Assessment. |
| recommendations | Review Recommendations, if any. |
| escalation_required | Whether expert, governance, legal, financial, or technical escalation is required. |
| limitations | Known gaps, uncertainty, exclusions, or unsupported areas. |
| decision_boundary | Statement of what the Review does and does not authorize. |
| lifecycle_status | Active, superseded, withdrawn, rejected, archived, or equivalent status. |

## 7. Behaviour

Review Records must behave according to the following rules:

1. A Review must remain separable from Evidence, Claim, and Decision.
2. A Review must state Review Scope and explicit exclusions.
3. A Review must identify the Review Basis.
4. A Review must attribute reviewer Actor and reviewer role.
5. A Review must preserve Evidence and Claim conflicts rather than hiding them.
6. A Review may recommend but must not decide unless a separate Decision process
   authorizes it.
7. A Review may mark an item ready for decision, but does not itself make the
   Decision.
8. A Review that changes governance state should create or support a Ledger
   entry in later Ledger specifications.
9. A Review requiring expert input must record escalation requirement.
10. Review lifecycle changes must preserve prior status history.

## 8. Constraints

Review Records must not:

- treat Evidence as automatic fact;
- treat Claims as confirmed without evidence and review basis;
- treat Review Recommendations as Decisions;
- authorize implementation, approval, construction, investment, compliance,
  public claim, operational action, or certification;
- bypass required expert, legal, financial, technical, or governance review;
- hide unsupported, conflicting, or out-of-scope material;
- silently overwrite prior Reviews;
- convert Actor Type or Agency into authority;
- rely on implementation-specific classes, databases, APIs, or runtime
  behaviour for conformance.

## 9. Review Status Categories

Minimum Review Status categories:

| Status | Meaning |
| --- | --- |
| not_started | Review has not started. |
| under_review | Review is in progress. |
| blocked | Review cannot proceed until required material is available. |
| expert_review_required | Expert review is required. |
| governance_review_required | Governance review is required. |
| completed | Review completed within defined scope. |
| superseded | Review remains traceable but has been replaced. |
| withdrawn | Review was withdrawn by reviewer or governance process. |
| archived | Review is retained for historical traceability. |

## 10. Review Outcome Categories

Minimum Review Outcome categories:

| Outcome | Meaning |
| --- | --- |
| sufficient_for_review_scope | Reviewed material is sufficient within the defined scope. |
| insufficient_evidence | Evidence is insufficient for the reviewed Claim or scope. |
| unsupported | Required support is absent. |
| conflicting | Material conflict remains unresolved. |
| escalation_required | Additional expert, governance, legal, financial, or technical review is required. |
| decision_ready | Review package is ready for a separate Decision process. |
| rejected_for_scope | Material is rejected within the defined Review Scope. |
| out_of_scope | Material is outside the Review Scope. |

Review Outcome applies only within Review Scope.

## 11. Conformance Requirements

A BuildingOS implementation, module, adapter, or specification conforms to
C01-D if it:

1. Preserves the distinction between Review and Decision.
2. Requires stable Review Record identifiers.
3. Requires Review Scope and explicit exclusions.
4. Requires Review Basis.
5. Requires reviewer Actor attribution.
6. Records observations separately from assessment, recommendation, outcome,
   and decision.
7. Preserves Evidence and Claim conflicts for review.
8. Records escalation requirements when expert or governance review is needed.
9. Does not allow Review Recommendations to authorize action by themselves.
10. References C00 v1.0, C01-A v1.0, C01-B v1.0, and C01-C v1.0 without
    redefining frozen terms or boundaries.
11. Keeps implementation details outside the standard unless a later approved
    implementation specification governs them.

## 12. Examples

### Conformant Example

```text
Review R-001 evaluates Claim C-004 using Evidence E-001 and Evidence E-002.
The reviewer records outcome = escalation_required because the evidence is
conflicting. The Review does not approve the Claim.
```

### Conformant Example

```text
Review R-010 marks a package decision_ready within scope, but a separate
Decision Record is still required before any action is authorized.
```

### Conformant Example

```text
Review R-020 records that Actor attribution is disputed and requires
governance_review_required before the Claim can be used.
```

## 13. Non-Conformance Examples

The following are non-conformant:

- "The Review recommends approval, therefore the Decision is approved."
- "The Review hides conflicting Evidence to simplify the outcome."
- "The reviewer Actor has Agency, therefore the Review is authoritative."
- "The Review authorizes construction."
- "Review status and Decision status are the same field."
- "The Review declares compliance without required authority."

## 14. Rationale

Review is the fourth C01 specification because Review depends on stable
Evidence, Claim, and Identity boundaries.

C01-D prepares the semantic foundation for later Procedure, Lifecycle,
Registered Object, and Ledger standards without becoming a workflow engine or
decision engine.

## 15. Review Status

Current state:

```text
FROZEN_V1_0
```

Required next steps:

- `BUILDINGOS_C01_D_REVIEW_STANDARD_FREEZE_RECORD_V1_0.md`

Next engineering batch:

- C01-E - Procedure Standard.

