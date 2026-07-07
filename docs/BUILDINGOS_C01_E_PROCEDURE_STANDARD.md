# BuildingOS C01-E Procedure Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## 1. Purpose

The Procedure Standard defines how BuildingOS represents governed process
structure.

It preserves the approved pattern:

```text
Procedure -> Stage -> Gate -> Review -> Decision -> Next Procedure
```

## 2. Scope

In scope: procedure vocabulary, required fields, stage and gate structure,
review and decision references, next-procedure routing, conformance
requirements.

Out of scope: runtime workflow engine, automation, APIs, MCP tools, Python,
SQLite, scheduling engines, approval automation, PRI implementation.

## 3. Glossary References

Depends on C00 v1.0.

## 4. Related Standards

| Standard | Version | Relationship |
| --- | --- | --- |
| C00 Glossary | 1.0 | Defines Procedure, Review, Decision, Lifecycle, Governance. |
| C01-A Evidence | 1.0 | Evidence can support gates and reviews. |
| C01-B Claim | 1.0 | Claims may be reviewed inside procedures. |
| C01-C Identity | 1.0 | Actors are attributed to procedure actions. |
| C01-D Review | 1.0 | Gates may require reviews before decisions. |

## 5. Core Concepts

- Procedure: governed process structure.
- Stage: bounded part of a Procedure.
- Gate: reviewable threshold between stages.
- Procedure Review: review required at a stage or gate.
- Procedure Decision: decision made through an authorized process.
- Next Procedure: allowed downstream procedure.

## 6. Required Fields

| Field | Requirement |
| --- | --- |
| procedure_id | Stable identifier. |
| procedure_name | Human-readable name. |
| procedure_scope | Scope and exclusions. |
| stages | Ordered Stage records. |
| gates | Gate records linked to stages. |
| required_reviews | Reviews required by stage or gate. |
| decision_points | Decision points and authority boundary. |
| next_procedures | Allowed downstream procedures. |
| owner_actor | Actor responsible for procedure stewardship. |
| lifecycle_status | Active, superseded, withdrawn, archived, or equivalent. |

## 7. Behaviour

Procedures must define stages, gates, review requirements, decision points, and
allowed next procedures. A Procedure may guide work but does not execute work or
authorize action by itself.

## 8. Constraints

Procedures must not become workflow automation, approval engines, compliance
engines, runtime schedulers, or substitutes for authorized Decisions.

## 9. Conformance Requirements

Conforming specifications must preserve the Procedure/Stage/Gate/Review/
Decision/Next Procedure structure, keep Review and Decision separate, attribute
responsible Actors, and avoid implementation-specific assumptions.

## 10. Examples

Conformant: a construction approval Procedure requires evidence review before a
gate and a separate Decision before moving to execution.

## 11. Non-conformance Examples

Non-conformant: "The Procedure completed, therefore construction is approved."

## 12. Rationale

Procedure is defined after Review because gates depend on review boundaries.

## 13. Review Status

```text
FROZEN_V1_0
```

