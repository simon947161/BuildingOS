# BuildingOS C02 Core Implementation Planning Review

## Project

BuildingOS

## Review Status

`REVIEW_READY_FOR_CHIEF_ARCHITECT`

## Source Reviewed

- `docs/BUILDINGOS_C02_CORE_IMPLEMENTATION_PLANNING_BRIEF.md`
- `docs/BUILDINGOS_CORE_READINESS_REPORT.md`
- `docs/BUILDINGOS_M1_ENGINEERING_DASHBOARD.md`
- `docs/BUILDINGOS_SPECIFICATION_INDEX.md`
- `PROJECT_CONTEXT.md`
- `CODEX_CONTEXT_TRANSFER_PACKET.md`

## Review Boundary

This review does not authorize implementation.

This review does not edit frozen Foundation documents.

This review does not introduce PRI, MCP Runtime, generic agent runtime, QClaw,
or runtime automation.

If a Foundation change appears necessary during future implementation planning,
it must be handled through Change Request and Version Review.

## 1. Current Core Readiness Status

Current readiness status:

```text
READY_FOR_CORE_IMPLEMENTATION_PLANNING
```

Observation:

- M1 Specification Foundation is complete.
- C00 through C01-I are frozen at Version 1.0.
- M1 Integration Review is complete.
- Core Readiness Report is complete.
- C02 Core Implementation Planning Brief is drafted for review.
- Remote GitHub synchronization and workspace relocation have been completed.

Interpretation:

BuildingOS is ready to approve a bounded Core implementation plan, but not to
begin coding automatically.

Recommendation:

Approve C02 only if the Chief Architect accepts the Core boundary,
implementation sequence, test strategy, and explicit exclusions below.

## 2. Proposed Minimal BuildingOS Core Boundary

The minimal BuildingOS Core should be limited to governed representations of
the frozen M1 primitives.

In boundary:

- Actor attribution.
- Evidence records.
- Claim records.
- Review records.
- Procedure structures.
- Lifecycle structures.
- Registered Object records.
- Governance Ledger records.
- Module Contract declarations and conformance checks.

Out of boundary:

- Production runtime.
- Workflow automation.
- Permissions or user management.
- Database implementation.
- Public API.
- UI dashboard.
- Crawlers or search engine.
- AI decision-making.
- MCP tools.
- n8n or Workflow Hub automation.
- PRI implementation.
- QClaw execution workflow.
- Application migrations.

Boundary rule:

```text
Core represents governance primitives.
Core does not automate governance decisions.
```

## 3. Core Object And Module List Derived From M1

The Core object and module list should map directly to the frozen M1 baseline.

| M1 Source | Core Object Or Module | Boundary |
| --- | --- | --- |
| C00 Glossary Foundation | Shared terminology reference | Definitions only; no runtime behavior. |
| C01-C Identity Standard | Actor Attribution | Attribution only; no permissions. |
| C01-A Evidence Standard | Evidence Record | Evidence is not treated as confirmed fact by default. |
| C01-B Claim Standard | Claim Record | Claims require support status and evidence links. |
| C01-D Review Standard | Review Record | Review remains separate from Decision. |
| C01-E Procedure Standard | Procedure Structure | Procedure is governed structure, not workflow automation. |
| C01-F Lifecycle Standard | Lifecycle Structure | Lifecycle transitions are represented, not auto-executed. |
| C01-G Registered Object Standard | Registered Object Registry | Traceability object registry only. |
| C01-H Governance Ledger Standard | Governance Ledger Record | Governance record, not blockchain or generic event log. |
| C01-I Module Contract Standard | Module Contract Declaration | Declarative contract and conformance, not module runtime execution. |

Recommended Core modules:

1. `identity`
2. `evidence`
3. `claim`
4. `review`
5. `procedure`
6. `lifecycle`
7. `registered_object`
8. `ledger`
9. `module_contract`
10. `conformance`

## 4. Items Safe For First Implementation

The following items are safe for first implementation only after C02-E
Implementation Authorization is approved:

- Actor attribution records.
- Evidence records.
- Claim records with evidence links and support status.
- Review records without decision authority.
- Procedure structures without workflow automation.
- Lifecycle structures without automated state-machine behavior.
- Registered Object records for traceability.
- Governance Ledger records for governance traceability.
- Module Contract declarations and conformance checks.

Safe first implementation does not include production runtime, external
integrations, automation, application migration, or real project decisions.

## 5. Recommended Implementation Sequence

Recommended sequence:

1. Approve C02 planning boundary.
2. Prepare C02-A Core Repository Skeleton as documentation only.
3. Prepare C02-B M1 Conformance Matrix.
4. Prepare C02-C Governance Kernel Contract.
5. Prepare C02-D Test Strategy Package.
6. Complete C02-E Implementation Authorization Gate.
7. Begin minimal Core implementation only after C02-E approval.

Sequence rule:

```text
Conformance before contracts.
Contracts before tests.
Tests before code.
Code only after authorization.
```

## 6. Reviewable Engineering Sub-Batches

### C02-A - Core Repository Skeleton Review

Purpose:

Confirm the future Core repository structure before creating implementation
files.

Review focus:

- Repository identity.
- Documentation skeleton.
- M1 baseline reference.
- Engineering workflow.
- Explicit absence of runtime code.

### C02-B - M1 Conformance Matrix Review

Purpose:

Translate frozen M1 specifications into Core obligations.

Review focus:

- Coverage of C00 through C01-I.
- Preservation of exclusions.
- No new governance concepts.
- Traceability from specification to Core obligation.

### C02-C - Governance Kernel Contract Review

Purpose:

Define the minimum Governance Kernel contract before implementation.

Review focus:

- Core primitive boundaries.
- Evidence and Claim separation.
- Review and Decision separation.
- Identity attribution-only boundary.
- Procedure as structure, not automation.

### C02-D - Test Strategy Review

Purpose:

Define tests before code.

Review focus:

- Conformance tests.
- Boundary tests.
- Fixture validation.
- Regression tests for forbidden assumptions.
- Documentation consistency checks.

### C02-E - Implementation Authorization Review

Purpose:

Decide whether Core implementation may begin.

Review focus:

- Approved repository structure.
- Approved conformance matrix.
- Approved kernel contract.
- Approved test strategy.
- Accepted exclusions.

## 7. Acceptance Criteria For Each Batch

| Batch | Acceptance Criteria |
| --- | --- |
| C02-A | Repository structure is approved; documentation skeleton is approved; no runtime code exists; M1 baseline reference is present. |
| C02-B | Every frozen M1 specification maps to one or more Core obligations; exclusions are carried forward; unmapped requirements are identified. |
| C02-C | Kernel contract is limited to frozen M1 concepts; Identity remains attribution-only; Review remains separate from Decision; Procedure remains non-automated. |
| C02-D | Tests are defined before implementation; fixtures are fictional; conformance and boundary tests are mapped to M1 requirements. |
| C02-E | Chief Architect approves or rejects implementation start; open architecture questions are resolved or deferred with explicit boundaries. |

## 8. Risks Of Premature Implementation

| Risk | Severity | Why It Matters | Mitigation |
| --- | --- | --- | --- |
| Core starts before C02 approval | High | Implementation may bypass architecture governance. | Require C02-E before coding. |
| Kernel scope expands | High | Core may become product runtime instead of governance primitive layer. | Limit first kernel to C00 through C01-I. |
| Evidence becomes fact | High | Evidence integrity boundary would break. | Add conformance and regression tests. |
| Review becomes Decision | High | Human approval boundary would collapse. | Keep Decision outside minimal Core unless separately approved. |
| Procedure becomes automation | Medium | BuildingOS would drift into workflow runtime. | Represent procedure structure only. |
| Identity becomes permissions | Medium | Attribution would be confused with access control. | Keep permission systems out of Core. |
| Ledger becomes blockchain or generic log | Medium | Ledger meaning would drift from governance traceability. | Restrict ledger to governance records. |
| Module Contract becomes execution | Medium | Contract declarations could become runtime module loading. | Keep module contracts declarative. |

## 9. Items Requiring Architecture Review Before Coding

The following items require Architecture Review before any implementation:

- Final Core repository location and relationship to this repository.
- Whether `buildingos-core` is a new repository or a bounded folder structure.
- Minimum Governance Kernel contract.
- C00 through C01-I conformance matrix.
- Test strategy and fixture policy.
- Change Request process for any Foundation adjustment.
- Whether Decision is excluded from the first Core or reserved for a later
  approved package.
- Naming of Core modules and object records.
- Handling of imported M1 baseline references.
- Definition of implementation authorization evidence for C02-E.

## 10. Items That Must Remain Outside BuildingOS Core

The following items must remain outside BuildingOS Core at this stage:

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
- Generic agent runtime.
- PRI integration.

## 11. Recommended Next Approval Gate

Recommended next approval gate:

```text
APPROVE_OR_REVISE_C02_CORE_IMPLEMENTATION_PLANNING_BRIEF
```

Decision options:

1. Approve C02 as the planning basis and authorize C02-A documentation-only
   Core Repository Skeleton planning.
2. Request revisions to C02 before any further planning.
3. Reject C02 and require a new planning brief.

Recommended decision:

```text
APPROVE_C02_WITH_C02_E_IMPLEMENTATION_AUTHORIZATION_REQUIRED_BEFORE_CODE
```

This means C02 may proceed through C02-A to C02-D planning packages, but Core
implementation must not begin until C02-E is explicitly approved.

## Final Review Finding

C02 is directionally sound and consistent with the frozen M1 baseline.

The brief is strong because it preserves:

- Stabilise before Expand.
- Standardise before Optimise.
- Governance before Automation.
- Core before Adapters.
- Adapters before Module Migration.

The main condition for approval is discipline: C02 should authorize planning
sub-batches, not implementation.

## Conversation Radar

Knowledge points:

- BuildingOS M1 is frozen and complete.
- C02 is a planning bridge from frozen specifications to Core.
- Minimal Core must be limited to governance primitives.

Idea points:

- Use a conformance matrix as the control surface between M1 and Core.
- Use tests before code to protect frozen boundaries.

Decisions:

- No implementation is authorized by this review.
- The recommended next gate is C02 approval or revision.

Risks:

- Premature implementation.
- Silent Foundation edits.
- Scope drift into runtime, automation, MCP, PRI, or QClaw.

Open questions:

- Should Core live in a new `buildingos-core` repository or as a bounded
  structure inside the existing repository?
- Is Decision excluded from first Core or reserved for a later approved package?
- What evidence is required to complete C02-E authorization?

Next actions:

1. Chief Architect reviews this planning review.
2. Chief Architect approves or revises C02.
3. If approved, prepare C02-A as documentation-only repository skeleton
   planning.

Related project keywords:

- BuildingOS
- M1 Specification Foundation
- C02 Core Implementation Planning Brief
- Governance Kernel
- Evidence
- Claim
- Identity
- Review
- Procedure
- Lifecycle
- Registered Object
- Governance Ledger
- Module Contract
