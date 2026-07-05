# BuildingOS C00 Glossary Foundation

## Project

BuildingOS

## Milestone

M1 - Specification Foundation

## Batch

C00 - BuildingOS Glossary Foundation

## Status

`FROZEN_V1_0`

## Version

`1.0`

## Freeze Decision

Architecture Review Result:

```text
APPROVE_AND_FREEZE_C00
```

C00 is frozen as Version 1.0.

Future changes require:

```text
Change Request -> Version Review -> Approval -> Update
```

## 1. Purpose

The BuildingOS Glossary Foundation defines the common vocabulary that future
BuildingOS specifications must use.

C00 exists to prevent later standards from using the same terms with different
meanings. It is a language-neutral glossary. It does not define runtime
implementation, database schema, API behaviour, Python classes, MCP tools, or
Project Runtime Initiative implementation.

## 2. Scope

In scope:

- Stable terms used by BuildingOS specifications.
- Definitions for governance, evidence, procedure, lifecycle, and attribution
  language.
- Boundary notes that prevent terms from being interpreted as implementation
  authority.

Out of scope:

- Runtime architecture.
- Software implementation.
- Database models.
- API contracts.
- Permission systems.
- PRI implementation or absorption into BuildingOS.
- New product concepts outside the frozen BuildingOS baseline.

## 3. Glossary Principles

BuildingOS glossary terms must be:

- language-neutral;
- implementation-independent;
- framework-independent;
- stable enough for conformance review;
- precise enough to prevent authority, evidence, and decision boundaries from
  being confused.

## 4. Core Terms

### Development Activity

A bounded activity within the lifecycle of a physical project or initiative.

A Development Activity may involve planning, engineering foresight, design,
approval, construction, operation, maintenance, renewal, review, or governance.

It is not automatically a project, contract, task, approval, or implementation
order.

### Actor

An identifiable participant or source that performs, records, submits, reviews,
or is attributed to an action, statement, evidence record, claim, review, or
decision.

An Actor may be human, organisational, automated, device-based, or
authority-based depending on the specification context.

Actor identity in M1 is for attribution only. It does not define permissions.

### Agency

The recognised capacity of an Actor to participate in a BuildingOS process.

Agency indicates that an Actor can be attributed to an action or record. It does
not automatically grant authority to approve, implement, certify, disclose, or
bind another Actor.

### Object

Any identifiable item that BuildingOS can reference in a governance,
engineering, evidence, review, procedure, lifecycle, or ledger context.

An Object may represent a physical component, document, project, activity,
record, evidence item, claim, procedure, lifecycle event, or other governed
reference.

An Object is not automatically registered, authoritative, approved, or active.

### Registered Object

An Object that has been formally recorded in a BuildingOS registry according to
the relevant specification.

A Registered Object must have a stable identifier, type, status, provenance,
and lifecycle context sufficient for review.

Registration makes an Object traceable. It does not make the Object approved,
valid, compliant, certified, or operationally authorized.

### Evidence

A traceable record, source, observation, document, dataset, inspection result,
or other support used to evaluate a specific Claim.

Evidence supports review. Evidence is not itself a confirmed fact, approval,
decision, or authority to act.

Evidence must preserve provenance, source context, evidence type, evidence
strength, verification status, and relationship to the Claim it supports.

### Claim

A specific assertion submitted for review.

A Claim may describe a project state, object property, event, compliance
position, engineering condition, lifecycle status, evidence interpretation, or
other reviewable statement.

A Claim must be traceable to Evidence or explicitly marked as unsupported,
unverified, conflicting, or out of scope.

### Review

A structured evaluation of Evidence, Claims, Objects, procedures, lifecycle
events, or decisions.

A Review records observations, assessments, gaps, conflicts, required expert
input, recommendations, and review outcome.

A Review does not automatically create approval, implementation authority,
compliance status, certification, public claim authority, or investment
authority.

### Decision

A recorded selection or determination made by an authorised Actor or governance
process within a defined scope.

A Decision must identify its basis, Actor attribution, authority boundary,
Evidence or Review references, status, and downstream effect.

A recommendation is not a Decision unless accepted through the required
decision process.

### Procedure

A defined governance or engineering process composed of stages, gates, reviews,
decisions, and possible next procedures.

A Procedure defines how work or review should progress. It is not merely a
workflow automation script and does not imply runtime execution.

### Lifecycle

The governed sequence of states, transitions, events, reviews, and decisions
that apply to an Object, Development Activity, project, or record over time.

Lifecycle language must preserve state history and must not overwrite prior
states without reviewable transition records.

### Ledger

A durable record of significant BuildingOS events, transitions, reviews,
decisions, registrations, evidence changes, claim changes, and governance
actions.

A Ledger records what happened, when, by whom or by which Actor, and under what
references or authority boundary.

A Ledger entry records an event. It does not by itself make the event correct,
valid, approved, or compliant.

### Governance

The set of rules, responsibilities, reviews, decisions, boundaries, and records
used to coordinate BuildingOS activities with traceability and accountability.

Governance in BuildingOS is evidence-aware, reviewable, and human-accountable.

Governance does not mean full automation or removal of human, expert, legal,
financial, technical, or public authority review where required.

### Engineering Foresight

The structured anticipation of engineering needs, constraints, risks,
interfaces, evidence requirements, lifecycle consequences, and review gates
before irreversible decisions are made.

Engineering Foresight supports planning and decision preparation. It does not
replace engineering approval.

### Engineering Experience

Accumulated practical knowledge from engineering work, reviews, operations,
failures, inspections, maintenance, and lifecycle records.

Engineering Experience may inform future procedures, reviews, and design
choices, but it must remain traceable to evidence or recorded experience
sources when used for governance.

### Experience Solidification

The process of turning repeated Engineering Experience into stable reviewable
guidance, procedures, standards, examples, or governance patterns.

Experience Solidification requires review. It must not silently convert local
experience into universal rule, compliance claim, or implementation authority.

### Conformance

The state of satisfying the explicit requirements of a BuildingOS specification.

Conformance must be assessed against defined requirements, not informal intent.

Conformance does not automatically mean legal compliance, certification,
professional approval, public disclosure readiness, investment readiness, or
operational authorization.

## 5. Cross-Term Boundary Rules

1. Evidence supports Claims but is not itself a Claim.
2. Claims require Evidence or an explicit unsupported status.
3. Reviews assess Evidence and Claims but do not automatically approve action.
4. Recommendations are not Decisions.
5. Decisions require authority attribution and scope.
6. Registered Objects are traceable but not automatically approved.
7. Ledger entries record events but do not prove correctness by existence.
8. Lifecycle transitions require reviewable records.
9. Agency supports attribution but does not automatically grant authority.
10. Conformance to a BuildingOS specification does not equal legal,
    regulatory, financial, professional, or operational approval.

## 6. Conformance Requirements

A BuildingOS specification conforms to C00 if it:

1. Uses C00 terms consistently.
2. Defines any additional term before using it as a requirement.
3. Does not redefine C00 terms without an approved Change Request and Version
   Review.
4. Preserves the distinction between Evidence, Claim, Review, Decision, and
   Ledger.
5. Preserves attribution-only Identity scope for M1.
6. Avoids implementation-specific assumptions unless the relevant later
   implementation specification explicitly allows them.
7. States when a term is used outside the C00 scope.

## 7. Examples

Conformant usage:

- "The Claim is supported by Evidence records E-001 and E-002 and remains under
  review."
- "The Review recommends expert assessment before any Decision."
- "The Registered Object is traceable but not approved for operation."
- "The Ledger records the lifecycle transition request."

## 8. Non-Conformance Examples

Non-conformant usage:

- "Evidence proves the Claim" without review status or sufficiency boundary.
- "The Review approves construction" without an authorised Decision.
- "The Ledger entry makes the event valid."
- "The Actor has permission because it has Agency."
- "The Registered Object is compliant because it is registered."
- "Conformance means legal approval."

## 9. Rationale

C00 is required before C01-A because Evidence, Claim, Identity, Review,
Procedure, Lifecycle, Registered Object, and Ledger standards all depend on the
same vocabulary.

The glossary reduces semantic drift and makes later conformance review
possible.

## 10. Review Status

Current state:

```text
FROZEN_V1_0
```

Freeze record:

- `BUILDINGOS_C00_GLOSSARY_FREEZE_RECORD_V1_0.md`

Next engineering batch:

- C01-A - Evidence Standard.
