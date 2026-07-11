# PROJECT_CONTEXT.md

## Project

BuildingOS

## Repository

`simon947161/BuildingOS`

## Branch

`main`

## Official Local Workspace

`D:\Codex\BuildingOS`

## Deprecated Local Workspace

`C:\Users\doras\OneDrive\Documents\BuildingOS`

## Current Phase

`CORE_BATCH_01_IMPLEMENTATION`

## Current Milestone

Minimum Governance Kernel representational implementation.

## Current Status

`IMPLEMENTATION_STARTED_PENDING_CI_AND_ENGINEERING_REVIEW`

## Frozen Baselines

- C00 Glossary Foundation v1.0
- C01-A Evidence Standard v1.0
- C01-B Claim Standard v1.0
- C01-C Identity Standard v1.0
- C01-D Review Standard v1.0
- C01-E Procedure Standard v1.0
- C01-F Lifecycle Standard v1.0
- C01-G Registered Object Standard v1.0
- C01-H Governance Ledger Standard v1.0
- C01-I Module Contract Standard v1.0

These documents remain frozen. Changes require Change Request, Version Review, Approval, and Update.

## Completed Gates

- M1 Specification Foundation completed and frozen.
- C02 planning brief and review completed.
- C02 approval gate completed.
- Core Batch 01 Implementation Brief completed.
- Core Batch 01 brief review completed.
- Core Batch 01 brief approved with conditions.
- Architecture boundary documented.
- M1 conformance matrix documented.
- Batch 01 test strategy documented.
- Operator Console roadmap documented.
- Core Batch 01 implementation authorization recorded.

## Implementation Added

- `buildingos_core/models.py`
- `buildingos_core/conformance.py`
- `buildingos_core/__init__.py`
- `tests/test_core_batch_01.py`
- `.github/workflows/core-batch-01.yml`

Implemented representational records:

- Actor
- Evidence
- Claim
- Review without decision authority
- Procedure without execution
- Lifecycle without automated transitions
- Registered Object
- Governance Ledger Entry
- Module Contract
- Conformance Result

## Active Boundaries

Core Batch 01 excludes:

- production database;
- public API;
- production Operator Console;
- permissions and user management;
- workflow automation;
- autonomous decision-making;
- PRI, MCP Runtime, generic agent runtime, QClaw, and n8n integration;
- application migration;
- frozen Foundation edits.

## Human Interface Direction

A future BuildingOS Operator Console is planned for human evidence inspection, claim inspection, review, lifecycle visibility, module contract visibility, and governance ledger visibility.

UI implementation remains deferred until the Governance Kernel is stable and separately authorized.

## Current Verification State

- Repository changes have been committed directly to `main` through the connected GitHub workflow.
- A GitHub Actions workflow has been added for compile and unit-test checks.
- CI result is not yet recorded in this context.
- Direct local test execution from the current ChatGPT runtime was blocked because that runtime could not resolve `github.com`; this is an environment limitation, not a passing test result.

## Next Actions

1. Confirm GitHub Actions execution and inspect any failures.
2. Fix implementation defects if CI fails.
3. Add full fictional fixture set and cross-object registry checks.
4. Perform implementation self-review.
5. Perform Codex engineering review.
6. Prepare Core Batch 01 approval and freeze record only after tests pass.
7. After Governance Kernel freeze, prepare the read-only Operator Console prototype brief.

## Safe Re-entry Point

Continue from:

`CORE_BATCH_01_CI_AND_ENGINEERING_REVIEW`

Do not claim Batch 01 complete or frozen until CI and engineering review pass.

## Context Protocol

Every major milestone, repository transition, workspace transition, or long-thread closure must update this file and create a context transfer packet when needed.
