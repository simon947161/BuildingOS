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

## Architecture-Level Changes

| Date | Change | Impact | Decision |
| --- | --- | --- | --- |
| 2026-07-05 | C00 introduced before C01-A. | Establishes frozen glossary dependency before all later specifications. | APPROVE_AND_FREEZE_C00 |
| 2026-07-05 | Specification index introduced. | Creates master tracking for specification ID, name, version, status, dependency, and owner. | Engineering housekeeping before C01-B |
| 2026-07-05 | Specification dependency map introduced. | Makes M1 dependency graph explicit and prevents downstream redefinition of frozen upstream boundaries. | Engineering housekeeping before C01-B |
| 2026-07-05 | Related Standards section required from C01-D onward. | Each new specification must explicitly reference dependent standards. | Architecture instruction before C01-D |

## Current Frozen Baseline

The current frozen baseline is:

```text
C00 v1.0 -> C01-A v1.0 -> C01-B v1.0 -> C01-C v1.0
```

Next active package:

```text
C01-D - Review Standard
```

