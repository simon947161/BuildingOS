# BuildingOS Roadmap Approval Record

## Project

BuildingOS Core

## Documents Reviewed

- `BUILDINGOS_CORE_ENGINEERING_PLAN_V0_1.md`
- `BUILDINGOS_ROADMAP_V1_0.md`

## Reviewer

ChatGPT - Chief Architect

## Review Date

2026-07-01

## Status

`APPROVED FOR MILESTONE M1`

## Overall Result

| Review Area | Result |
| --- | --- |
| Architecture Review | PASS |
| Governance Review | PASS |
| Engineering Planning Review | PASS |

The Engineering Plan is approved as the official planning document for BuildingOS Core Phase 1.

Roadmap v1.0 is approved for Milestone M1 preparation.

## Approved Decisions

### Core + Modules Architecture

Approved.

BuildingOS should evolve using:

```text
BuildingOS Core
-> Shared Governance Runtime
-> Modules
```

Modules should not independently implement shared governance concepts.

### Repository Strategy

Approved near-term repositories:

- `buildingos-spec`
- `buildingos-core`

Deferred:

- `buildingos-modules`

Do not create additional repositories until Core becomes stable.

### Adapter-First Migration

Approved.

Migration order:

```text
Core -> Adapter -> Module Migration
```

Direct refactoring of BOMI or IPI before Core contracts exist is not approved.

### Identity Runtime

Approved as a Phase 1 planning item.

Identity Runtime should initially focus on attribution only.

Permission systems are outside the scope of Core v0.1.

### Procedure Runtime

Approved.

Procedure Runtime should model:

```text
Procedure -> Stage -> Gate -> Review -> Decision -> Next Procedure
```

It should not become only a workflow engine.

### Registered Object Registry

Approved.

Generalising Runtime Registry into Registered Object Registry is the correct long-term direction.

## Engineering Principles

BuildingOS engineering should follow three permanent principles:

- Stabilise before Expand.
- Standardise before Optimise.
- Governance before Automation.

These principles should guide future engineering decisions.

## Next Milestone

Proceed with Milestone M1 only:

```text
M1 - Specification Foundation
```

Prepare:

```text
C01 - BuildingOS Specification Foundation
```

Do not begin Core implementation.

Do not begin BOMI or IPI refactoring.

## C01 Initial Specification Set

C01 should be divided into small reviewable batches covering:

- Evidence
- Claim
- Identity
- Review
- Procedure
- Lifecycle
- Registered Object
- Ledger

Each specification must define explicit conformance requirements and remain language-neutral.

## Engineering Manager Responsibilities

Codex owns engineering coordination.

From this milestone onward, Codex must:

1. Assign engineering implementation work to QClaw when implementation is approved.
2. Review QClaw deliverables before requesting architecture review.
3. Return work to QClaw when implementation, tests, documentation, repository structure, or engineering quality does not satisfy standards.
4. Continue supervising engineering progress until the milestone reaches completion.
5. Coordinate engineering activities without requiring Simon to relay routine engineering work.

## QClaw Coordination

QClaw should report engineering progress directly to Codex.

Codex decides:

- Whether QClaw continues implementation.
- Whether additional engineering work is required.
- Whether engineering review has passed.
- Whether architecture review is ready.

Simon should not act as the engineering message relay.

## Reporting Requirements

Codex should periodically report concise engineering summaries to Simon and the Chief Architect.

Reports should include:

- Current Milestone
- Current Batch
- Completed Work
- Remaining Work
- Engineering Risks
- Blocking Issues
- Decisions Required
- Recommended Next Actions

Routine implementation details should not be escalated unless architectural or product decisions are required.

## Ownership

| Role | Ownership |
| --- | --- |
| Simon | Product Direction |
| ChatGPT | Architecture and Governance Review |
| Codex | Engineering Management, Planning, Integration, Review, Milestone Delivery |
| QClaw | Engineering Implementation, Testing, Documentation, Technical Execution |

Codex owns engineering completion.

QClaw owns engineering implementation.

## Default Operating Principle

Engineering work should continue under Codex coordination until one of the following occurs:

- The milestone is completed.
- An architectural decision is required.
- A product decision is required.
- An external dependency blocks progress.

## Final Approval

Roadmap v1.0: PASS

Engineering Plan v0.1: PASS

Approved next step:

```text
Prepare C01 Specification Foundation.
```

Do not begin implementation until the specification batch has been reviewed and approved.

## BEWP State

```text
APPROVED_FOR_M1_PREPARATION
```

