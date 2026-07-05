# BuildingOS Specification Dependency Map

## Project

BuildingOS

## Purpose

This document describes the dependency graph between BuildingOS M1
specifications.

It is an engineering coordination artifact. It does not define runtime
implementation, database schema, API behaviour, MCP tools, repository
automation, or PRI implementation.

## Dependency Graph

```text
C00 BuildingOS Glossary Foundation
|
|-- C01-A Evidence Standard
|   |
|   `-- C01-B Claim Standard
|       |
|       |-- C01-D Review Standard
|       |   |
|       |   |-- C01-E Procedure Standard
|       |   |   |
|       |   |   `-- C01-F Lifecycle Standard
|       |   |
|       |   `-- C01-H Governance Ledger Standard
|       |
|       `-- C01-G Registered Object Standard
|
|-- C01-C Identity Standard
|   |
|   |-- C01-D Review Standard
|   |-- C01-H Governance Ledger Standard
|   `-- C01-I Module Contract Standard
|
`-- C01-I Module Contract Standard
```

## Dependency Rules

1. C00 must remain the terminology dependency for all M1 specifications.
2. C01-A must be frozen before C01-B can be frozen.
3. C01-B must be frozen before Review, Procedure, Lifecycle, Registered Object,
   Ledger, or Module Contract specifications can depend on claim semantics.
4. C01-C Identity Standard may be developed after C01-B, but later governance
   specifications must use identity for attribution only unless a later
   approved architecture decision expands scope.
5. C01-D Review Standard depends on Evidence, Claim, and Identity boundaries.
6. C01-E Procedure Standard depends on Review because procedures include gates,
   reviews, decisions, and next procedures.
7. C01-F Lifecycle Standard depends on Procedure and Review because lifecycle
   transitions require reviewable events and governed transitions.
8. C01-G Registered Object Standard depends on Evidence, Claim, and Lifecycle
   because registered objects must be traceable and governed.
9. C01-H Governance Ledger Standard depends on Identity, Review, and Lifecycle
   because ledger entries require actor attribution and governed event context.
10. C01-I Module Contract Standard depends on all prior standards because
    modules must declare conformance targets and must not bypass core
    governance semantics.

## Current Dependency State

| Specification | Dependency State |
| --- | --- |
| C00 | Root dependency; frozen v1.0. |
| C01-A | Depends on C00; frozen v1.0. |
| C01-B | Depends on C00 and C01-A; frozen v1.0. |
| C01-C | Depends on C00, C01-A, and C01-B; frozen v1.0. |
| C01-D | Depends on C00, C01-A, C01-B, and C01-C; active package. |
| C01-E | Depends on C01-D; planned. |
| C01-F | Depends on C01-D and C01-E; planned. |
| C01-G | Depends on C01-A, C01-B, and C01-F; planned. |
| C01-H | Depends on C01-C, C01-D, and C01-F; planned. |
| C01-I | Depends on C01-A through C01-H; planned. |

## Engineering Constraint

No dependent specification may redefine frozen upstream terms or boundaries.

If a downstream specification needs to change a frozen upstream dependency, the
change must follow:

```text
Change Request -> Version Review -> Approval -> Update
```
