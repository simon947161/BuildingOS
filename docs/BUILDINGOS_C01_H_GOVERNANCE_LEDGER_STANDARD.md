# BuildingOS C01-H Governance Ledger Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## 1. Purpose

The Governance Ledger Standard defines durable records for governed BuildingOS
events, transitions, reviews, decisions, registrations, and version changes.

## 2. Scope

In scope: ledger entry identity, event type, actor attribution, referenced
objects, basis records, timestamp, previous state, new state, and limitations.

Out of scope: blockchain, distributed ledger, event streaming, runtime logging,
general audit log implementation, APIs, MCP, Python, SQLite, PRI
implementation.

## 3. Glossary References

Depends on C00 v1.0.

## 4. Related Standards

Depends on Identity, Review, Procedure, Lifecycle, and Registered Object
standards.

## 5. Core Concepts

- Ledger Entry: durable record of governed event.
- Ledger Event Type: controlled or declared governed event category.
- Ledger Basis: evidence, claim, review, decision, procedure, lifecycle, or
  object reference that explains the event.

## 6. Required Fields

| Field | Requirement |
| --- | --- |
| ledger_entry_id | Stable identifier. |
| event_type | Governed event type. |
| event_time | Date or time of event. |
| actor | Actor attributed to event. |
| subject_ref | Object, claim, review, decision, procedure, lifecycle, or module reference. |
| basis_refs | Evidence, Claim, Review, Decision, or Procedure references. |
| previous_state | Prior state where applicable. |
| new_state | New state where applicable. |
| limitations | Known scope limits. |

## 7. Behaviour

Ledger entries record that a governed event was recorded. They do not prove the
event is correct, valid, approved, compliant, or authorized.

## 8. Constraints

The Ledger must not become a general runtime event log, blockchain commitment,
or substitute for Evidence, Review, or Decision.

## 9. Conformance Requirements

Conformance requires durable event identity, actor attribution, subject
reference, basis references, state preservation, and no implementation-specific
assumptions.

## 10. Examples

Conformant: a ledger entry records that C01-D was frozen, referencing the
freeze record and decision.

## 11. Non-conformance Examples

Non-conformant: "The ledger entry exists, therefore the decision is correct."

## 12. Rationale

Ledger follows Lifecycle and Registered Object because it records governed
changes and their basis.

## 13. Review Status

`FROZEN_V1_0`

