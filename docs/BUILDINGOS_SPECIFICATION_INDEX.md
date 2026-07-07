# BuildingOS Specification Index

## Project

BuildingOS

## Purpose

This document is the master index for BuildingOS M1 specifications.

It records specification identity, version, status, dependencies, and current
owner. It is a tracking document only. It does not create runtime
implementation, repository automation, API contracts, MCP tools, or PRI
implementation.

## Status Values

| Status | Meaning |
| --- | --- |
| Planned | Specification is planned but not started. |
| In Progress | Specification drafting has started. |
| Ready For Approval | Engineering review passed and approval is requested. |
| Frozen | Approved and frozen; future change requires Change Request and Version Review. |

## Specification Index

| Specification ID | Name | Version | Status | Dependency | Current Owner |
| --- | --- | --- | --- | --- | --- |
| C00 | BuildingOS Glossary Foundation | 1.0 | Frozen | None | Codex |
| C01-A | Evidence Standard | 1.0 | Frozen | C00 v1.0 | Codex |
| C01-B | Claim Standard | 1.0 | Frozen | C00 v1.0; C01-A v1.0 | Codex |
| C01-C | Identity Standard | 1.0 | Frozen | C00 v1.0; C01-A v1.0; C01-B v1.0 | Codex |
| C01-D | Review Standard | 1.0 | Frozen | C00 v1.0; C01-A v1.0; C01-B v1.0; C01-C v1.0 | Codex |
| C01-E | Procedure Standard | 1.0 | Frozen | C00 v1.0; C01-D v1.0 | Codex |
| C01-F | Lifecycle Standard | 1.0 | Frozen | C00 v1.0; C01-D v1.0; C01-E v1.0 | Codex |
| C01-G | Registered Object Standard | 1.0 | Frozen | C00 v1.0; C01-A v1.0; C01-B v1.0; C01-F v1.0 | Codex |
| C01-H | Governance Ledger Standard | 1.0 | Frozen | C00 v1.0; C01-C v1.0; C01-D v1.0; C01-F v1.0 | Codex |
| C01-I | Module Contract Standard | 1.0 | Frozen | C00 v1.0; C01-A v1.0 through C01-H v1.0 | Codex |

## Freeze Rule

Frozen specifications must not be silently edited.

Future changes require:

```text
Change Request -> Version Review -> Approval -> Update
```

## Current Engineering Position

C00 through C01-I are frozen as the BuildingOS M1 Specification Foundation
baseline.

M1 Integration Review and Core Readiness Review are complete locally.

Next engineering package:

```text
C02 - BuildingOS Core Implementation Planning Brief
```

C02 must remain a planning package until explicitly approved.
