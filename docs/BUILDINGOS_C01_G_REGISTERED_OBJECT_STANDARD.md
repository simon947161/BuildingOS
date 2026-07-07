# BuildingOS C01-G Registered Object Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## 1. Purpose

The Registered Object Standard defines how BuildingOS records governed objects
that require traceability across evidence, claims, reviews, lifecycle, and
ledger records.

## 2. Scope

In scope: object registration, identifiers, object type, provenance, owner
Actor, related evidence, claims, reviews, lifecycle, and status.

Out of scope: asset database implementation, runtime object registry,
inventory automation, APIs, MCP, Python, SQLite, PRI implementation.

## 3. Glossary References

Depends on C00 v1.0.

## 4. Related Standards

Depends on C01-A Evidence, C01-B Claim, C01-C Identity, and C01-F Lifecycle.

## 5. Core Concepts

- Object: identifiable item BuildingOS can reference.
- Registered Object: Object formally recorded for governance traceability.
- Object Status: registration lifecycle state.
- Object Context: evidence, claims, reviews, procedure, lifecycle, ledger links.

## 6. Required Fields

| Field | Requirement |
| --- | --- |
| object_id | Stable identifier. |
| object_type | Controlled or declared object type. |
| object_name | Human-readable label. |
| registration_basis | Evidence or governance basis for registration. |
| registered_by | Actor registering the object. |
| owner_actor | Responsible Actor where known. |
| related_evidence | Evidence references. |
| related_claims | Claim references. |
| lifecycle_ref | Lifecycle reference. |
| object_status | Current object status. |

## 7. Behaviour

Registration makes an Object traceable. It does not make the Object approved,
valid, compliant, certified, or operationally authorized.

## 8. Constraints

Registered Objects must not become a generic asset database or bypass Evidence,
Claim, Review, Decision, or Lifecycle rules.

## 9. Conformance Requirements

Conformance requires stable IDs, provenance, actor attribution, lifecycle
reference, explicit status, and preservation of frozen upstream boundaries.

## 10. Examples

Conformant: a building component is registered with evidence and lifecycle
status `under_review`, but is not approved for operation.

## 11. Non-conformance Examples

Non-conformant: "The object is registered, therefore it is compliant."

## 12. Rationale

Registered Objects follow Lifecycle because registration must be governed by
traceable state and history.

## 13. Review Status

`FROZEN_V1_0`

