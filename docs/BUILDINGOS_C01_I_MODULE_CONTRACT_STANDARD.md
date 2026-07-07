# BuildingOS C01-I Module Contract Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## 1. Purpose

The Module Contract Standard defines how future BuildingOS modules declare
their conformance, dependencies, capabilities, and governance boundaries.

## 2. Scope

In scope: module identity, declared capability, conformance targets, dependency
declarations, evidence/claim/review/lifecycle/ledger boundaries, and adapter
readiness.

Out of scope: creating `buildingos-modules`, module runtime implementation,
SDK code, APIs, MCP, Python, SQLite, deployment, PRI implementation.

## 3. Glossary References

Depends on C00 v1.0.

## 4. Related Standards

Depends on all prior C01 standards: Evidence, Claim, Identity, Review,
Procedure, Lifecycle, Registered Object, and Governance Ledger.

## 5. Core Concepts

- Module Contract: declaration of module boundaries and conformance.
- Capability: bounded function the module exposes conceptually.
- Conformance Target: standards the module agrees to follow.
- Dependency Declaration: standards and external dependencies required.

## 6. Required Fields

| Field | Requirement |
| --- | --- |
| module_id | Stable identifier. |
| module_name | Human-readable module name. |
| module_scope | Scope and exclusions. |
| capabilities | Declared conceptual capabilities. |
| conformance_targets | BuildingOS standards followed. |
| dependencies | Required standards or systems. |
| evidence_boundary | How evidence semantics are preserved. |
| claim_boundary | How claim semantics are preserved. |
| review_boundary | How review semantics are preserved. |
| lifecycle_boundary | How lifecycle semantics are preserved. |
| ledger_boundary | How ledger semantics are preserved. |

## 7. Behaviour

Modules may extend BuildingOS into domains but must not redefine Core
governance semantics.

## 8. Constraints

Module Contracts must not imply implementation exists, bypass Core semantics,
create the deferred modules repository, or authorize runtime integration.

## 9. Conformance Requirements

Conformance requires explicit scope, dependencies, conformance targets,
capabilities, and preservation of all frozen M1 standards.

## 10. Examples

Conformant: an IPI module contract declares project discovery capability while
using BuildingOS Evidence, Claim, Review, Lifecycle, and Ledger semantics.

## 11. Non-conformance Examples

Non-conformant: "The module defines its own evidence model that overrides
BuildingOS Evidence Standard."

## 12. Rationale

Module Contract closes M1 by defining how future modules depend on Core
standards without implementing those modules.

## 13. Review Status

`FROZEN_V1_0`

