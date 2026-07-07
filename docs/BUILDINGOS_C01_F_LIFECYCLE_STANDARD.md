# BuildingOS C01-F Lifecycle Standard

## Status

`FROZEN_V1_0`

## Version

`1.0`

## 1. Purpose

The Lifecycle Standard defines governed states, transitions, events, and
history for BuildingOS objects and activities.

## 2. Scope

In scope: lifecycle state, transition records, transition evidence, review and
decision references, actor attribution, history preservation.

Out of scope: runtime state machines, automation, APIs, MCP, Python, SQLite,
operational control, PRI implementation.

## 3. Glossary References

Depends on C00 v1.0.

## 4. Related Standards

C01-F depends on C01-D Review and C01-E Procedure. It also preserves Evidence,
Claim, and Identity boundaries from C01-A through C01-C.

## 5. Core Concepts

- Lifecycle: governed sequence of states and transitions.
- Lifecycle Event: recorded transition or state event.
- Transition Basis: evidence, claim, review, procedure gate, or decision basis.
- Prior State: previous state preserved for audit.
- Current State: active lifecycle state.

## 6. Required Fields

| Field | Requirement |
| --- | --- |
| lifecycle_id | Stable identifier. |
| subject_ref | Object, activity, or record governed by the lifecycle. |
| prior_state | Previous state. |
| current_state | Current state. |
| transition_event | Event causing transition. |
| transition_basis | Evidence, Claim, Review, Procedure, or Decision references. |
| actor | Actor attributed to the event. |
| occurred_at | Event date or time. |
| limitations | Known gaps or scope limits. |

## 7. Behaviour

Lifecycle history must be preserved. Transitions must be traceable and must not
silently overwrite prior states.

## 8. Constraints

Lifecycle status does not create approval, compliance, operational authority, or
certification by itself.

## 9. Conformance Requirements

Conformance requires transition traceability, actor attribution, prior-state
preservation, review/decision separation, and no implementation assumptions.

## 10. Examples

Conformant: an object moves from `under_review` to `decision_ready` after a
Review, but still requires a Decision before execution.

## 11. Non-conformance Examples

Non-conformant: "Lifecycle status is active, therefore the object is approved."

## 12. Rationale

Lifecycle follows Procedure because governed transitions depend on stages,
gates, reviews, and decisions.

## 13. Review Status

`FROZEN_V1_0`

