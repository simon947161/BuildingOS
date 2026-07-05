# QClaw C01 BuildingOS Specification Foundation Brief

## Status

`DRAFT - NOT ASSIGNED`

This brief is prepared for review. It is not yet an implementation assignment.

QClaw should not begin work until Codex marks this brief as assigned.

## Task ID

C01 - BuildingOS Specification Foundation

## Milestone

M1 - Specification Foundation

## Repository

Target repository to create after assignment:

```text
buildingos-spec
```

## Objective

Create the language-neutral specification foundation for BuildingOS governance primitives.

The repository must define standards, JSON schemas, examples, conformance requirements, and review policies.

## Scope

Implement only the specification foundation.

Required standards:

- Evidence
- Claim
- Identity
- Review
- Procedure
- Lifecycle
- Registered Object
- Governance Ledger
- Module Contract

Required policy docs:

- Versioning policy
- Compatibility policy
- Conformance policy
- Review process
- Repository structure

## Required Repository Structure

```text
buildingos-spec/
|-- README.md
|-- specs/
|-- schemas/
|   |-- json/
|   `-- examples/
|-- docs/
`-- checks/
```

Exact file list must follow `BUILDINGOS_C01_SPECIFICATION_FOUNDATION_PLAN.md`.

## Incremental Review Principle

Every C01 sub-batch must complete:

```text
Implementation
-> Self Review
-> Codex Engineering Review
-> Architecture Review (if required)
-> Approval
-> Freeze
```

before the next sub-batch begins.

After a sub-batch is approved, it is frozen. Subsequent changes require Change Request and Version Review.

## Sub-Batch Execution

Implement in small reviewable batches:

- C01-0: Repository and governance skeleton
- C01-A: Evidence Standard
- C01-B: Claim Standard
- C01-C: Identity Standard
- C01-D: Review Standard
- C01-E: Procedure Standard
- C01-F: Lifecycle Standard
- C01-G: Registered Object Standard
- C01-H: Governance Ledger Standard
- C01-I: Module Contract Standard
- C01-J: Final review package

QClaw should report after each sub-batch.

Current approved first specification sub-batch:

```text
C01-A - Evidence Standard
Status: APPROVED
```

## Scope Exclusions

Do not implement:

- Python runtime
- Database runtime
- API layer
- Frontend
- BOMI refactor
- IPI refactor
- Permission system
- Capability Registry
- RFC repository
- Certification automation
- Real IoT ingestion
- AI decision-making

## Required Conformance Rules

Every standard must include:

- Purpose
- Scope
- Out-of-scope boundaries
- Required fields
- Optional fields
- Actor attribution requirement
- Review or decision boundary where applicable
- Conformance requirements
- Non-conformance examples
- Versioning notes

Every JSON example must parse as valid JSON.

## Verification Required

QClaw must verify:

- Required files exist.
- JSON examples parse.
- JSON schemas are valid JSON.
- Standards include required sections.
- Conformance matrix covers every standard.
- No placeholder markers remain.
- No implementation code was introduced.
- Git status is clean.

## Reporting Format

QClaw must report to Codex using:

```text
Task ID:
Current State:
Sub-Batch:
Files Created / Updated:
Verification Performed:
Tests / Checks Run:
Failures:
Blocked Items:
Next Recommended Action:
Needs Codex Decision: yes/no
Needs Architect Review: yes/no
```

## Acceptance Criteria

Codex may accept C01 when:

- All required files exist.
- All standards are language-neutral.
- All JSON examples parse.
- Conformance matrix is complete.
- Scope exclusions are respected.
- Git status is clean.
- QClaw report is complete.
- Codex engineering review passes.

## Current Assignment State

```text
NOT_ASSIGNED
```

This brief becomes active only after C01 plan review and Codex assignment.
