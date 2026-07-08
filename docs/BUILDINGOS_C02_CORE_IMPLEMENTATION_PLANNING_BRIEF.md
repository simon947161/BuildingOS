# C02 - BuildingOS Core Implementation Planning Brief

## Project

BuildingOS

## Status

`DRAFT_FOR_REVIEW`

## Purpose

C02 translates the frozen M1 Specification Foundation into a bounded Core
implementation plan.

This brief does not start implementation. It defines the minimum safe path from
frozen specifications to BuildingOS Core.

## Scope

In scope:

- Core repository structure.
- Implementation batches.
- First minimal Governance Kernel scope.
- Test strategy.
- Migration path from M1 specifications to Core.
- Explicit exclusions.

Out of scope:

- Runtime implementation.
- Code generation.
- API implementation.
- UI implementation.
- Database implementation.
- MCP implementation.
- n8n or Workflow Hub automation.
- PRI implementation.
- QClaw assignment.

## Source Baseline

C02 depends on the frozen M1 baseline:

| Specification | Version | Status |
| --- | --- | --- |
| C00 Glossary Foundation | 1.0 | Frozen |
| C01-A Evidence Standard | 1.0 | Frozen |
| C01-B Claim Standard | 1.0 | Frozen |
| C01-C Identity Standard | 1.0 | Frozen |
| C01-D Review Standard | 1.0 | Frozen |
| C01-E Procedure Standard | 1.0 | Frozen |
| C01-F Lifecycle Standard | 1.0 | Frozen |
| C01-G Registered Object Standard | 1.0 | Frozen |
| C01-H Governance Ledger Standard | 1.0 | Frozen |
| C01-I Module Contract Standard | 1.0 | Frozen |

## Proposed Core Repository Structure

Target repository:

```text
buildingos-core/
|-- README.md
|-- WORKSPACE.md
|-- docs/
|   |-- CORE_SCOPE.md
|   |-- ARCHITECTURE_BOUNDARY.md
|   |-- IMPLEMENTATION_BATCHES.md
|   |-- TEST_STRATEGY.md
|   |-- MIGRATION_PATH.md
|   `-- CHANGE_REQUEST_PROCESS.md
|-- specs/
|   |-- imported/
|   |   `-- M1_BASELINE_REFERENCE.md
|   `-- conformance/
|       `-- M1_CONFORMANCE_MATRIX.md
|-- kernel/
|   |-- identity/
|   |-- evidence/
|   |-- claim/
|   |-- review/
|   |-- procedure/
|   |-- lifecycle/
|   |-- registered_object/
|   |-- ledger/
|   `-- module_contract/
|-- tests/
|   |-- conformance/
|   |-- fixtures/
|   `-- regression/
`-- CHANGELOG.md
```

This structure is a planning target only. It does not create files or choose a
programming framework.

## First Minimal Kernel Scope

The first Core implementation should be the smallest useful Governance Kernel.

Minimum kernel responsibilities:

1. Represent Actor attribution.
2. Represent Evidence without treating it as fact.
3. Represent Claims with evidence support and unsupported status.
4. Represent Reviews without decision authority.
5. Represent Procedure structure without workflow automation.
6. Represent Lifecycle transitions without runtime state-machine automation.
7. Represent Registered Objects as governed traceability objects.
8. Represent Governance Ledger entries as durable governance records.
9. Represent Module Contract declarations without module runtime execution.

The first kernel should provide stable governance primitives before any module
migration begins.

## Implementation Batches

### C02-A - Core Repository Skeleton

Goal:

Create the `buildingos-core` repository structure and documentation skeleton.

Completion criteria:

- Repository identity is clear.
- No runtime code exists unless explicitly authorized.
- M1 baseline reference is present.
- Engineering workflow is documented.

### C02-B - M1 Conformance Matrix

Goal:

Translate C00 through C01-I into a Core conformance matrix.

Completion criteria:

- Every frozen specification has mapped Core obligations.
- Exclusions are carried forward.
- No new governance concepts are introduced.

### C02-C - Governance Kernel Contract

Goal:

Define the minimal Kernel contract before implementation.

Completion criteria:

- Kernel scope is limited to frozen M1 concepts.
- Identity remains attribution-only.
- Review remains separate from Decision.
- Procedure remains structure, not automation.

### C02-D - Test Strategy Package

Goal:

Define tests before code.

Completion criteria:

- Conformance tests are mapped to M1 standards.
- Regression tests protect Evidence/Claim/Review/Decision separation.
- Fixtures use fictional data only.

### C02-E - Implementation Authorization Gate

Goal:

Prepare the final approval gate before Core implementation begins.

Completion criteria:

- Repository structure is approved.
- Kernel scope is approved.
- Test strategy is approved.
- Explicit exclusions are accepted.

## Test Strategy

Core tests should begin as conformance tests, not product behavior tests.

Required test families:

- Specification conformance tests.
- Boundary tests.
- Fixture validation tests.
- Regression tests for forbidden assumptions.
- Documentation consistency checks.

Initial test examples:

- Evidence cannot be treated as confirmed fact by default.
- Unsupported Claims remain unsupported.
- Review Recommendation cannot become Decision.
- Identity attribution does not imply permission.
- Procedure completion does not imply approval.
- Ledger entry does not imply blockchain commitment.
- Module Contract declaration does not execute a module.

## Migration Path From Specs To Core

1. Freeze M1 baseline.
2. Import M1 references into Core repository documentation.
3. Build conformance matrix from frozen specifications.
4. Define kernel contracts from conformance requirements.
5. Write tests against contracts.
6. Implement only the approved minimal kernel.
7. Review implementation against M1 baseline.
8. Begin adapters only after Core contracts stabilize.

## What Must Not Be Implemented Yet

Do not implement:

- BOMI migration.
- IPI migration.
- ClimateOS migration.
- Permission systems.
- User management.
- Production database.
- Public API.
- UI dashboard.
- Crawlers.
- Search engine.
- Workflow automation.
- AI decision-making.
- MCP tools.
- n8n or Workflow Hub automation.
- QClaw execution workflow.
- Real project decision automation.
- `buildingos-modules` repository.

## Architecture Health Check

C02 does not introduce new architecture.

It preserves:

- Stabilise before Expand.
- Standardise before Optimise.
- Governance before Automation.
- Core before Adapters.
- Adapters before Module Migration.

## Engineering Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Core implementation starts too early | High | Require C02-E authorization gate before implementation. |
| Kernel becomes too large | High | Limit first kernel to frozen M1 primitives. |
| Procedure becomes workflow automation | Medium | Preserve Procedure as governed structure only. |
| Identity becomes permissions | Medium | Keep Identity attribution-only. |
| Ledger becomes blockchain or generic event log | Medium | Keep Ledger limited to governance records. |
| Module Contract becomes runtime execution | Medium | Keep contracts declarative only. |

## Completion Criteria For C02

C02 is complete when:

- Core repository structure is approved.
- Implementation batches are approved.
- Minimal kernel scope is approved.
- Test strategy is approved.
- Migration path is approved.
- Explicit exclusions are approved.

## Recommended Next Action

Review this C02 planning brief.

If approved, prepare C02-A Core Repository Skeleton as a documentation-only
setup package. Do not start runtime implementation until the C02-E
authorization gate is complete.

