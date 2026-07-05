# BuildingOS Roadmap v1.0

## 1. Purpose

This roadmap defines the next approved engineering path for BuildingOS after architecture and governance approval of the Core Engineering Plan.

It defines milestones, dependencies, ownership, completion criteria, and estimated engineering batches.

This is a roadmap document only. It does not start implementation, create repositories, or assign tasks to QClaw.

## 2. Current Status

Review status:

- Architecture Review: PASS
- Governance Review: PASS
- Engineering Planning Review: PASS

Current BEWP state:

```text
APPROVED_FOR_ROADMAP_PHASE
```

Implementation state:

```text
NOT_STARTED
```

## 3. Product Scope Boundary

BuildingOS positioning remains unchanged:

```text
Reality Operating System for Infrastructure Governance
```

This roadmap is about engineering maturity, not product scope expansion.

No roadmap item authorizes:

- Product repositioning
- New vertical expansion
- Certification automation
- Real IoT ingestion
- AI decision-making
- Public release
- Partnership commitments

## 4. Approved Architecture Direction

Approved internal architecture:

```text
BuildingOS
|
|-- Governance Kernel
|-- Core Runtime
|-- Module SDK
`-- Modules
```

Approved repositories for the next phase:

- `buildingos-spec`
- `buildingos-core`

Deferred repository:

- `buildingos-modules`

Future repositories for consideration only:

- `buildingos-rfcs`

## 5. Repository Boundary Decisions

### Approved Now

`buildingos-spec`

- Language-neutral standards.
- No implementation runtime.
- Defines evidence, claim, identity, review, procedure, lifecycle, registered object, ledger, and module contract standards.

`buildingos-core`

- Reference implementation of shared governance runtimes.
- Includes Governance Kernel, Core Runtime, Module SDK, SQLite-compatible persistence, and contract tests.
- Does not contain BOMI or IPI domain models.

### Deferred

`buildingos-modules`

- Deferred until Core becomes stable.
- BOMI and IPI remain stable in their current locations until adapters are ready.

`buildingos-rfcs`

- Future governance repository.
- Not part of Phase 1 implementation.

## 6. Milestone Overview

```text
M1 Specification Foundation
-> M2 BuildingOS Core Foundation
-> M3 Adapter Foundation
-> M4 Module Migration
-> M5 Release Hardening
```

## 7. Milestone M1 - Specification Foundation

### Objective

Create `buildingos-spec` as the language-neutral source of platform standards.

### Scope

Includes:

- Evidence Standard
- Claim Standard
- Identity Standard
- Review Standard
- Procedure Standard
- Lifecycle Standard
- Registered Object Standard
- Governance Ledger Standard
- Module Contract Standard
- Versioning and compatibility policy

Excludes:

- Runtime implementation
- Python package code
- BOMI/IPI refactor
- API/frontend work

### Dependencies

- Architecture approval record accepted.
- Repository boundary confirmed.
- Product scope unchanged.

### Owner

- Codex: specification structure and engineering planning
- ChatGPT: governance and architecture review
- Simon: product direction confirmation
- QClaw: implementation only after assignment

### Completion Criteria

- `buildingos-spec` repository structure approved.
- Standards documents created.
- JSON schemas and examples created.
- Compatibility policy documented.
- BEWP review passes.
- Git status clean.

### Engineering Batches

C01: `buildingos-spec` foundation.

Estimated effort: 1-2 engineering days.

## 8. Milestone M2 - BuildingOS Core Foundation

### Objective

Create `buildingos-core` and implement the first shared governance runtime foundation.

### Scope

Includes:

- Governance Kernel
- Identity Runtime focused on attribution only
- Evidence Runtime
- Claim Runtime
- Registered Object Registry
- Governance Ledger
- SQLite-compatible persistence
- Core unit and schema tests

Excludes:

- Permission systems
- Capability Registry
- RFC repository
- Module migration
- UI/API implementation

### Dependencies

- M1 Specification Foundation complete.
- Core repository boundary confirmed.
- Identity Runtime scope approved as attribution-only.
- Registered Object Registry naming confirmed.

### Owner

- QClaw: implementation after scoped brief
- Codex: engineering management, review, closure
- ChatGPT: architecture/governance review
- Simon: product owner approval when direction changes

### Completion Criteria

- `buildingos-core` repository initialized.
- Kernel contains only stable governance primitives.
- Identity actor attribution is implemented without full permissions.
- Evidence and claim models align with `buildingos-spec`.
- Registered Object Registry is implemented.
- Ledger records actor-attributed governance events.
- Unit and schema tests pass.
- BEWP Codex review passes.
- Git status clean.

### Engineering Batches

C02: Core repository skeleton.

C03: Identity + Evidence + Claims.

C04: Registered Object Registry + Ledger.

Estimated effort: 5-6 engineering days total.

## 9. Milestone M3 - Adapter Foundation

### Objective

Create stable adapter contracts before migrating BOMI or IPI.

### Scope

Includes:

- Module manifest
- Adapter interfaces
- Contract test harness
- Stub module example
- BOMI adapter proof
- IPI adapter proof

Excludes:

- Direct BOMI refactor
- Direct IPI refactor
- New product modules
- Capability Registry implementation

### Dependencies

- M2 Core Foundation complete.
- Module SDK contracts approved.
- Core contract tests pass.

### Owner

- QClaw: adapter implementation after scoped brief
- Codex: adapter review and BEWP routing
- ChatGPT: architecture review if contract boundaries change

### Completion Criteria

- BOMI can emit Core-compatible evidence, review, lifecycle, registered object, and actor references through adapters.
- IPI can emit Core-compatible evidence, claims, procedure gates, registered object references, and actor references through adapters.
- No module internals are replaced yet.
- Contract tests pass.
- Git status clean.

### Engineering Batches

C06: Module SDK and contract tests.

C07: BOMI adapter proof.

C08: IPI adapter proof.

Estimated effort: 6-9 engineering days total.

## 10. Milestone M4 - Module Migration

### Objective

Migrate modules to consume BuildingOS Core after adapter proof is accepted.

### Scope

Includes:

- BOMI migration through adapters
- IPI migration through adapters
- Removal of duplicated shared governance concepts from modules
- Module schemas focused on domain-specific tables
- Migration docs

Excludes:

- Creating `buildingos-modules` repository unless separately approved
- ClimateOS/WaterOS/EnergyOS implementation
- Capability Registry implementation

### Dependencies

- M3 Adapter Foundation complete.
- BOMI and IPI adapter tests pass.
- Module migration plan approved.
- Simon confirms no product direction change.

### Owner

- QClaw: implementation
- Codex: engineering manager and reviewer
- ChatGPT: governance review for boundary changes
- Simon: domain/product validation

### Completion Criteria

- BOMI no longer redefines Core evidence, identity, review, lifecycle, registered object, or ledger concepts.
- IPI no longer redefines Core evidence, claim, procedure, registered object, or ledger concepts.
- Existing module tests pass.
- Core contract tests pass.
- Migration documentation complete.
- Git status clean.

### Engineering Batches

M01: BOMI migration planning and adapter integration.

M02: IPI migration planning and adapter integration.

M03: Cross-module contract verification.

Estimated effort: to be estimated after M3.

## 11. Milestone M5 - Release Hardening

### Objective

Prepare Core + initial adapters for stable internal release.

### Scope

Includes:

- Release notes
- Compatibility matrix
- Duplicate folder cleanup plan
- Schema source-of-truth verification
- BEWP closure reports
- Roadmap update

Excludes:

- Public launch
- Customer-facing UI
- Production deployment

### Dependencies

- M4 module migration complete or explicitly deferred.
- Core tests pass.
- Adapter tests pass.
- Architecture review complete.

### Owner

- Codex: release readiness and closure
- QClaw: implementation fixes
- ChatGPT: architecture/governance review
- Simon: release approval

### Completion Criteria

- Git status clean.
- Test suite passing.
- Schema source of truth confirmed.
- Open issues documented.
- Next roadmap revision prepared.
- BEWP closure criteria satisfied.

## 12. Dependency Map

```text
Architecture Approval
-> Roadmap Approval
-> M1 buildingos-spec
-> M2 buildingos-core
-> M3 adapters
-> M4 module migration
-> M5 release hardening
```

Critical dependency rules:

- QClaw implementation briefs must not be issued before Roadmap approval.
- `buildingos-core` must not start before `buildingos-spec` scope is approved.
- Module migration must not start before adapters pass contract tests.
- Product scope changes require Simon approval.

## 13. Ownership Model

| Area | Owner | Responsibility |
| --- | --- | --- |
| Product direction | Simon | Approves product scope and release direction |
| Architecture/governance | ChatGPT | Reviews Core architecture, governance boundaries, standards |
| Engineering workflow | Codex | Owns BEWP routing, review, closure, implementation briefs |
| Implementation | QClaw | Implements assigned scoped tasks after approval |
| Domain validation | Simon + domain reviewers | Validates practical use and external stakeholder fit |

## 14. Engineering Batch Map

| Batch | Milestone | Scope | Implementation Owner | Status |
| --- | --- | --- | --- | --- |
| C01 | M1 | `buildingos-spec` foundation | QClaw after brief | Not assigned |
| C02 | M2 | `buildingos-core` skeleton | QClaw after brief | Not assigned |
| C03 | M2 | Identity + Evidence + Claims | QClaw after brief | Not assigned |
| C04 | M2 | Registered Object Registry + Ledger | QClaw after brief | Not assigned |
| C05 | M2 | Review + Procedure + Lifecycle | QClaw after brief | Not assigned |
| C06 | M3 | Module SDK + contract tests | QClaw after brief | Not assigned |
| C07 | M3 | BOMI adapter proof | QClaw after brief | Not assigned |
| C08 | M3 | IPI adapter proof | QClaw after brief | Not assigned |
| C09 | M5 | Release hardening | QClaw after brief | Not assigned |

No batch is assigned until Roadmap approval.

## 15. Governance Rules

Governance Kernel:

- Must remain stable.
- Must contain only governance primitives.
- Must avoid domain-specific logic.

Identity Runtime:

- Phase 1 scope is attribution only.
- Permission systems are explicitly outside Core v0.1.
- Reviews, decisions, evidence verification, lifecycle transitions, and ledger entries require actor attribution.

Procedure Runtime:

- Models procedure governance state.
- Does not become a general workflow engine.
- Must support `Procedure -> Stage -> Gate -> Review -> Decision -> Next Procedure`.

Registered Object Registry:

- Replaces narrower Runtime Registry naming.
- Registers governed platform objects.
- Does not become a generic asset database.

Capability Registry:

- Future direction only.
- Not a v0.1 implementation task.

Architecture RFC Process:

- Future direction only.
- `buildingos-rfcs` is deferred.

## 16. Completion Criteria for Roadmap Approval

This roadmap is ready for approval when reviewers confirm:

- Milestones are correctly sequenced.
- Repository boundaries are correct.
- Ownership is clear.
- Completion criteria are sufficient.
- Engineering batches are scoped at the right level.
- Product scope remains unchanged.
- No implementation task is implied before approval.

## 17. Risks

Risk: starting implementation before roadmap approval.

Mitigation: no QClaw brief is generated from this document until approval is recorded.

Risk: repository sprawl.

Mitigation: create only `buildingos-spec` and `buildingos-core` now; defer `buildingos-modules` and `buildingos-rfcs`.

Risk: Kernel becomes too broad.

Mitigation: treat Kernel as Governance Kernel and restrict it to stable primitives.

Risk: Identity Runtime turns into permissions too early.

Mitigation: Phase 1 identity is attribution only.

Risk: Capability Registry distracts from Core foundation.

Mitigation: record it as future direction only.

Risk: BOMI and IPI destabilize during migration.

Mitigation: adapter-first migration and no direct refactor before Core contracts exist.

## 18. Decisions Needed

Roadmap approval decisions:

1. Approve `buildingos-spec` and `buildingos-core` as the only near-term repositories.
2. Defer `buildingos-modules` until Core stability.
3. Approve M1-M5 milestone sequence.
4. Approve C01-C09 batch map.
5. Confirm Identity Runtime v0.1 is attribution-only.
6. Confirm permission systems are outside Core v0.1.
7. Confirm Capability Registry and RFC process are future directions only.

## 19. Next Action After Approval

If this roadmap is approved, Codex may prepare the first QClaw implementation brief:

```text
C01 - buildingos-spec foundation
```

That brief should include:

- Exact repository structure
- Required standards documents
- JSON schema requirements
- Examples
- Tests or validation checks
- BEWP reporting format
- Scope exclusions

## 20. Conversation Radar

Knowledge points:

- Architecture and governance review passed.
- Core implementation is still deferred.
- Roadmap approval is required before implementation briefs.
- `buildingos-spec` and `buildingos-core` are the only approved near-term repositories.
- `buildingos-modules`, Capability Registry, and RFC process are deferred.

Idea points:

- Use `buildingos-spec` to stabilize semantics before implementation.
- Use `buildingos-core` as reference implementation after specs are stable.
- Use adapters to protect BOMI and IPI from premature refactor.

Decisions:

- Roadmap phase is now active.
- No QClaw task is assigned yet.
- Product scope remains unchanged.

Risks:

- Premature implementation.
- Repository sprawl.
- Over-broad Kernel.
- Identity permissions scope creep.

Open questions:

- Is the M1-M5 sequence approved?
- Is C01 the correct first QClaw task after approval?
- Should Roadmap v1.0 be stored in `buildingos-spec` later as well?

Next actions:

1. Review Roadmap v1.0.
2. Approve or request changes.
3. If approved, Codex prepares C01 implementation brief.

