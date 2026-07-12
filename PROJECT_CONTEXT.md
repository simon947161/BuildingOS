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

`CORE_BATCH_01_CLOSURE`

## Current Milestone

Minimum Governance Kernel representational implementation approval and freeze gate.

## Current Status

`VERIFIED_ENGINEERING_REVIEW_PASS_PENDING_CHIEF_ARCHITECT_APPROVAL_AND_FREEZE`

## Verified Implementation Baseline

`f84b22bf4921e4f98e15598c5c5a5aa18bcaa996`

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
- C02 planning and approval gates completed.
- Core Batch 01 brief, review, architecture boundary, conformance matrix, test strategy, and implementation authorization completed.
- Minimum Governance Kernel source implemented.
- Full fictional fixture set added.
- Cross-object registry checks added.
- Explicit M1 structure checks added for all in-scope objects.
- Deterministic regression coverage added.
- Implementation self-review passed.
- GitHub Actions verification passed.
- Engineering review passed.
- Approval and freeze records prepared for Chief Architect review.

## Implementation And Test Artifacts

- `buildingos_core/models.py`
- `buildingos_core/conformance.py`
- `buildingos_core/registry.py`
- `buildingos_core/__init__.py`
- `tests/fixtures/`
- `tests/conformance/`
- `tests/regression/`
- `tests/test_core_batch_01.py`
- `tests/test_core_batch_01_registry.py`
- `tests/test_core_batch_01_ci_probe.py`
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

## Verification State

Isolated verification:

```text
Ran 34 tests
OK
```

Hosted verification:

```text
Workflow: Core Batch 01
Run ID: 29159400862
Run number: 11
Job: test
Conclusion: success
```

Engineering review decision:

```text
PASS
```

## Closure Records

- `docs/CORE_BATCH_01_TEST_MANIFEST.md`
- `docs/BUILDINGOS_CORE_BATCH_01_IMPLEMENTATION_SELF_REVIEW.md`
- `docs/BUILDINGOS_CORE_BATCH_01_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_CORE_BATCH_01_APPROVAL_RECORD.md`
- `docs/BUILDINGOS_CORE_BATCH_01_FREEZE_RECORD.md`

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

A future read-only BuildingOS Operator Console may provide Mission Control-style human visibility for evidence, claims, reviews, lifecycle state, module contracts, and governance ledger records.

Operator Console implementation remains deferred until the Chief Architect explicitly approves and activates the Core Batch 01 freeze.

## Future Regulatory and Knowledge Garden Planning

Planning record:

- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

The plan preserves a future Regulatory Knowledge Layer covering NCC source/version/effective-date context, referenced standards, NSW legislation and regulations, jurisdictional variations, applicability and compliance-related claims, source change tracking, and mandatory human review.

It also records a Markdown-first Obsidian/Knowledge Garden compatibility model in which GitHub remains the authoritative source, portable links and indexes are preferred, synchronisation is controlled, and authoritative legal or standards content is not duplicated without permission.

Planning status:

```text
PLANNING_BASELINE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION
```

This record does not alter Core, approve legal or certification advice, authorize regulatory connectors, or bypass the current freeze and UI gates.

## Decision Required

Chief Architect decision:

```text
APPROVE_CORE_BATCH_01_FOR_FREEZE
```

The batch is verified and technically ready, but it is not yet formally frozen.

## Next Actions

1. Chief Architect reviews the approval and freeze records.
2. Record approval, correction request, or rejection.
3. If approved, activate the freeze record and update this context to `CORE_BATCH_01_FROZEN`.
4. Only after freeze activation, prepare a bounded read-only Operator Console prototype brief.
5. Keep Regulatory Knowledge Layer and Knowledge Garden work at planning level until separate architecture and implementation authorization exist.

## Safe Re-entry Point

Continue from:

`CORE_BATCH_01_CHIEF_ARCHITECT_FREEZE_DECISION`

Do not claim formal freeze or begin Operator Console implementation before approval is recorded.

## Context Protocol

Every major milestone, repository transition, workspace transition, or long-thread closure must update this file and create a context transfer packet when needed.
