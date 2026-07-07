# BuildingOS Specification Changelog

## Project

BuildingOS

## Purpose

This document records approved BuildingOS specification versions and
architecture-level changes during M1 Specification Foundation.

It is a governance record. It does not define runtime implementation, database
schema, API behaviour, MCP tools, repository automation, or PRI
implementation.

## Changelog Rules

- Frozen specification versions must be recorded here.
- Architecture-level changes must be recorded here.
- Routine drafting changes do not need entries unless they affect approved
  specification status, dependencies, or architecture-level boundaries.
- Frozen specifications may only change through:

```text
Change Request -> Version Review -> Approval -> Update
```

## Approved Specification Versions

| Date | Specification ID | Name | Version | Status | Architecture Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-07-05 | C00 | BuildingOS Glossary Foundation | 1.0 | Frozen | APPROVE_AND_FREEZE_C00 |
| 2026-07-05 | C01-A | Evidence Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_A |
| 2026-07-05 | C01-B | Claim Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_B |
| 2026-07-05 | C01-C | Identity Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_C |
| 2026-07-07 | C01-D | Review Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_D |
| 2026-07-07 | C01-E | Procedure Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_E |
| 2026-07-07 | C01-F | Lifecycle Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_F |
| 2026-07-07 | C01-G | Registered Object Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_G |
| 2026-07-07 | C01-H | Governance Ledger Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_H |
| 2026-07-07 | C01-I | Module Contract Standard | 1.0 | Frozen | APPROVE_AND_FREEZE_C01_I |

## Architecture-Level Changes

| Date | Change | Impact | Decision |
| --- | --- | --- | --- |
| 2026-07-05 | C00 introduced before C01-A. | Establishes frozen glossary dependency before all later specifications. | APPROVE_AND_FREEZE_C00 |
| 2026-07-05 | Specification index introduced. | Creates master tracking for specification ID, name, version, status, dependency, and owner. | Engineering housekeeping before C01-B |
| 2026-07-05 | Specification dependency map introduced. | Makes M1 dependency graph explicit and prevents downstream redefinition of frozen upstream boundaries. | Engineering housekeeping before C01-B |
| 2026-07-05 | Related Standards section required from C01-D onward. | Each new specification must explicitly reference dependent standards. | Architecture instruction before C01-D |
| 2026-07-07 | C01-D Review Standard frozen. | Establishes review as assessment and recommendation, separate from decision authority. | APPROVE_AND_FREEZE_C01_D |
| 2026-07-07 | C01-E Procedure Standard frozen. | Establishes Procedure -> Stage -> Gate -> Review -> Decision -> Next Procedure as governance structure, not a workflow engine. | APPROVE_AND_FREEZE_C01_E |
| 2026-07-07 | C01-F Lifecycle Standard frozen. | Establishes governed states, transitions, lifecycle events, and lifecycle history. | APPROVE_AND_FREEZE_C01_F |
| 2026-07-07 | C01-G Registered Object Standard frozen. | Establishes traceable governed platform objects without creating an asset database implementation. | APPROVE_AND_FREEZE_C01_G |
| 2026-07-07 | C01-H Governance Ledger Standard frozen. | Establishes durable governance event traceability without creating blockchain or runtime logging scope. | APPROVE_AND_FREEZE_C01_H |
| 2026-07-07 | C01-I Module Contract Standard frozen. | Establishes language-neutral module conformance declarations without creating module runtime implementation. | APPROVE_AND_FREEZE_C01_I |
| 2026-07-07 | M1 Integration Review completed. | Confirms C00 through C01-I are coherent as the local Specification Foundation baseline. | M1_INTEGRATION_REVIEW_PASS |
| 2026-07-07 | Core Readiness Report completed. | Moves BuildingOS to Core implementation planning readiness, while keeping implementation gated. | READY_FOR_CORE_IMPLEMENTATION_PLANNING |

## Current Frozen Baseline

The current frozen baseline is:

```text
C00 v1.0 -> C01-A v1.0 -> C01-B v1.0 -> C01-C v1.0 -> C01-D v1.0 -> C01-E v1.0 -> C01-F v1.0 -> C01-G v1.0 -> C01-H v1.0 -> C01-I v1.0
```

Next engineering package:

```text
C02 - BuildingOS Core Implementation Planning Brief
```
