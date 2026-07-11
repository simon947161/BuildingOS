# BuildingOS Core Batch 01 Brief Approval Decision

## Project

BuildingOS

## Decision Status

`APPROVED_WITH_CONDITIONS_FOR_NEXT_PLANNING_GATE`

## Decision Date

2026-07-11

## Purpose

This decision records the Chief Architect direction to continue BuildingOS in Night Mode after the Core Batch 01 Implementation Brief Review.

This decision approves the Core Batch 01 Implementation Brief for the limited purpose of preparing the next documentation-only planning gate.

This decision does not approve Core code implementation.

This decision does not authorize edits to frozen Foundation documents.

## 1. Reviewed Documents

Primary reviewed document:

```text
docs/BUILDINGOS_CORE_BATCH_01_IMPLEMENTATION_BRIEF.md
```

Review document:

```text
docs/BUILDINGOS_CORE_BATCH_01_IMPLEMENTATION_BRIEF_REVIEW.md
```

Supporting C02 approval record:

```text
docs/BUILDINGOS_C02_CORE_IMPLEMENTATION_APPROVAL_RECORD.md
```

## 2. Chief Architect Direction

The Chief Architect has authorized continued forward movement without repeated micro-authorization prompts, provided BuildingOS remains inside the approved engineering governance boundary.

This standing direction is interpreted as:

- Continue approved documentation and planning gates.
- Resolve open planning questions where the safe engineering path is clear.
- Preserve frozen Foundation documents.
- Avoid speculative expansion.
- Do not introduce implementation code until an explicit implementation authorization record exists.

## 3. Approval Decision

The Core Batch 01 Implementation Brief is approved with conditions.

Approval meaning:

```text
Core Batch 01 may proceed to documentation-only boundary, conformance, and test-planning artifacts.
```

Approval does not mean:

```text
Core Batch 01 code implementation may begin.
```

## 4. Conditions

The following conditions remain active:

1. Foundation documents C00 through C01-I remain frozen.
2. Any Foundation change requires Change Request, Version Review, Approval, and Update.
3. Batch 01 must remain limited to the minimum Governance Kernel boundary.
4. Repository or folder boundary must be resolved before code implementation.
5. M1 conformance matrix format must be documented before code implementation.
6. Test strategy and fictional fixture policy must be documented before code implementation.
7. Review records must not imply decision authority.
8. Identity records must not become permission systems.
9. Procedure structures must not become workflow automation.
10. Lifecycle structures must not become automated state machines.
11. Ledger records must not become blockchain or generic application logging.
12. Module Contracts must not become runtime module execution.
13. PRI, MCP Runtime, generic agent runtime, QClaw, production database, public API, and UI dashboard remain outside Batch 01 implementation.

## 5. Authorized Next Documentation Artifacts

The following documentation-only artifacts are authorized by this decision:

```text
docs/CORE_BATCH_01_ARCHITECTURE_BOUNDARY.md
specs/conformance/M1_CONFORMANCE_MATRIX.md
docs/CORE_BATCH_01_TEST_STRATEGY.md
docs/BUILDINGOS_OPERATOR_CONSOLE_ROADMAP.md
```

These artifacts may clarify planning, boundaries, conformance, testing, and future human interface direction.

They must not create runtime code.

## 6. Implementation Boundary

Implementation remains pending.

Required future gate:

```text
CHIEF_ARCHITECT_APPROVAL_FOR_CORE_BATCH_01_IMPLEMENTATION
```

Until that future gate exists, BuildingOS may continue planning but must not create Core runtime code.

## 7. Human Interface Note

The Chief Architect has requested a future human-participation interface similar in spirit to a Mission Control console.

This request is accepted as a future BuildingOS Operator Console workstream.

Because UI dashboard work is explicitly outside Batch 01 implementation, the current safe action is to create a roadmap only.

The Operator Console must eventually support human review, approval, evidence inspection, claim inspection, lifecycle visibility, and governance ledger visibility without turning BuildingOS into an autonomous decision system.

## 8. Recommended Next Gate

Next documentation-only gate:

```text
PREPARE_CORE_BATCH_01_ARCHITECTURE_BOUNDARY_AND_CONFORMANCE_MATRIX
```

Recommended next action:

1. Resolve Batch 01 as a bounded folder structure inside the current BuildingOS repository unless later changed by Architecture Review.
2. Create the M1 conformance matrix format.
3. Create the Batch 01 test strategy.
4. Create the Operator Console roadmap as a future interface workstream.

## Conversation Radar

### Core Knowledge Points

- Core Batch 01 Brief Review recommended approval with conditions.
- Chief Architect has authorized continued Night Mode progression.
- Documentation-only progression is approved.
- Code implementation remains unauthorized.

### Idea Points

- Treat Night Mode as bounded engineering continuation, not uncontrolled automation.
- Use the current repository as the first Core boundary unless later changed.
- Plan the human Operator Console now, but implement it only after Governance Kernel stability.

### Decision Points

- Core Batch 01 Implementation Brief is approved with conditions.
- Next documentation artifacts are authorized.
- Implementation code remains pending.

### Open Questions

- When should Core Batch 01 implementation code be authorized?
- Which schema language should be used for first representational objects?
- Which interface technology should be used for the later Operator Console?

### Next Actions

1. Create Core Batch 01 architecture boundary.
2. Create M1 conformance matrix.
3. Create Core Batch 01 test strategy.
4. Create BuildingOS Operator Console roadmap.

### Project Keywords

- BuildingOS
- Core Batch 01
- Night Mode
- Approval With Conditions
- Governance Kernel
- M1 Conformance
- Operator Console
- Human-in-the-loop
