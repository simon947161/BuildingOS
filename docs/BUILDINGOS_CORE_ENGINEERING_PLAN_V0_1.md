# BuildingOS Core Engineering Plan v0.1

## 1. Purpose

This engineering plan prepares BuildingOS Core implementation without starting implementation.

Architecture review and governance review have passed for the Core + Modules direction. This plan refines that direction into a stable engineering sequence that can later be assigned to QClaw.

This document is planning-only. It does not create `buildingos-core`, refactor BOMI, refactor IPI, or assign implementation work.

## 2. Accepted Architecture Direction

Accepted decisions:

- Create a dedicated `buildingos-core` repository.
- Keep BOMI and IPI stable during Core development.
- Move shared governance concepts into Core.
- Keep domain-specific models inside each module.
- Build Core first, then migrate modules through adapters.
- Do not refactor BOMI directly before Core contracts exist.

Product scope remains unchanged:

- BuildingOS remains a Reality Operating System for Infrastructure Governance.
- This planning phase does not expand product scope into new verticals or market promises.
- The focus is implementation readiness for the approved architecture.

## 3. Refined Layer Model

Recommended internal architecture:

```text
BuildingOS
|
|-- Kernel
|-- Core Runtime
|-- Module SDK
`-- Modules
    |-- IPI
    |-- BOMI
    |-- ClimateOS
    |-- WaterOS
    |-- EnergyOS
    `-- Future Modules
```

Layer interpretation:

- Kernel: most stable platform contracts and governance primitives.
- Core Runtime: executable shared runtimes built on Kernel contracts.
- Module SDK: adapter contracts, module registration, test harnesses, and integration helpers.
- Modules: domain-specific systems such as IPI and BOMI.

Important boundary:

The Kernel is an internal platform layer. It does not change external product positioning.

## 4. Repository Strategy

Recommended repositories:

```text
buildingos-spec/
buildingos-core/
buildingos-modules/
```

### 4.1 `buildingos-spec`

Purpose:

Language-neutral platform standards.

Contents:

- Evidence Standard
- Claim Standard
- Review Standard
- Procedure Standard
- Lifecycle Standard
- Runtime / Registered Object Standard
- Identity Standard
- Module Contract Standard
- Governance Ledger Standard

Rule:

`buildingos-spec` defines platform semantics. It should not contain Python package code or runtime implementation.

### 4.2 `buildingos-core`

Purpose:

Reference implementation of shared BuildingOS governance runtimes.

Contents:

- Kernel contracts
- Core runtime models
- SQLite-compatible persistence
- Module SDK
- Core tests
- Contract fixtures

Rule:

`buildingos-core` implements approved standards. It should not contain BOMI- or IPI-specific domain models.

### 4.3 `buildingos-modules`

Purpose:

Domain modules that depend on BuildingOS Core.

Initial modules:

- `ipi`
- `bomi`

Future modules:

- `climateos`
- `wateros`
- `energyos`

Rule:

Modules provide domain objects, domain workflows, domain matching logic, and domain documentation. They must not redefine Core evidence, claim, identity, review, lifecycle, procedure, runtime registry, or ledger semantics once Core contracts are available.

## 5. Proposed `buildingos-spec` Structure

```text
buildingos-spec/
|-- README.md
|-- specs/
|   |-- EVIDENCE_STANDARD.md
|   |-- CLAIM_STANDARD.md
|   |-- IDENTITY_STANDARD.md
|   |-- REVIEW_STANDARD.md
|   |-- PROCEDURE_STANDARD.md
|   |-- LIFECYCLE_STANDARD.md
|   |-- RUNTIME_OBJECT_STANDARD.md
|   |-- GOVERNANCE_LEDGER_STANDARD.md
|   `-- MODULE_CONTRACT_STANDARD.md
|-- schemas/
|   |-- json/
|   |   |-- evidence_record.schema.json
|   |   |-- claim.schema.json
|   |   |-- actor.schema.json
|   |   |-- review_record.schema.json
|   |   |-- procedure.schema.json
|   |   |-- lifecycle_event.schema.json
|   |   |-- registered_object.schema.json
|   |   `-- ledger_entry.schema.json
|   `-- examples/
|       |-- evidence_record.example.json
|       |-- claim.example.json
|       |-- actor.example.json
|       |-- procedure.example.json
|       `-- registered_object.example.json
`-- docs/
    |-- VERSIONING_POLICY.md
    |-- COMPATIBILITY_POLICY.md
    `-- REVIEW_PROCESS.md
```

## 6. Proposed `buildingos-core` Structure

```text
buildingos-core/
|-- README.md
|-- pyproject.toml
|-- docs/
|   |-- TECHNICAL_DESIGN.md
|   |-- KERNEL_ARCHITECTURE.md
|   |-- CORE_RUNTIME_ARCHITECTURE.md
|   |-- MODULE_SDK_GUIDE.md
|   |-- MIGRATION_GUIDE_IPI_BOMI.md
|   |-- TESTING_STRATEGY.md
|   `-- REPOSITORY_STRUCTURE.md
|-- buildingos_core/
|   |-- __init__.py
|   |-- kernel/
|   |   |-- __init__.py
|   |   |-- object_ref.py
|   |   |-- statuses.py
|   |   |-- events.py
|   |   |-- errors.py
|   |   `-- contracts.py
|   |-- identity/
|   |   |-- __init__.py
|   |   |-- actors.py
|   |   |-- roles.py
|   |   |-- attribution.py
|   |   `-- repository.py
|   |-- evidence/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- ranking.py
|   |   |-- verification.py
|   |   `-- repository.py
|   |-- claims/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- confidence.py
|   |   `-- repository.py
|   |-- review/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- outcomes.py
|   |   `-- repository.py
|   |-- procedures/
|   |   |-- __init__.py
|   |   |-- procedure.py
|   |   |-- stage.py
|   |   |-- gate.py
|   |   |-- decision.py
|   |   `-- repository.py
|   |-- lifecycle/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- transitions.py
|   |   `-- repository.py
|   |-- registry/
|   |   |-- __init__.py
|   |   |-- ids.py
|   |   |-- registered_object.py
|   |   `-- repository.py
|   |-- ledger/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   `-- repository.py
|   |-- persistence/
|   |   |-- __init__.py
|   |   |-- sqlite.py
|   |   |-- migrations.py
|   |   `-- unit_of_work.py
|   `-- module_sdk/
|       |-- __init__.py
|       |-- module_manifest.py
|       |-- adapters.py
|       |-- contract_tests.py
|       `-- validation.py
|-- schemas/
|   |-- sqlite/
|   |   |-- 001_kernel.sql
|   |   |-- 002_identity.sql
|   |   |-- 003_evidence.sql
|   |   |-- 004_claims.sql
|   |   |-- 005_review.sql
|   |   |-- 006_procedures.sql
|   |   |-- 007_lifecycle.sql
|   |   |-- 008_registry.sql
|   |   `-- 009_ledger.sql
|   `-- json/
|-- examples/
|-- tests/
|   |-- unit/
|   |-- integration/
|   |-- contract/
|   `-- fixtures/
`-- .github/
    `-- workflows/
        `-- ci.yml
```

## 7. Kernel Layer

Kernel responsibilities:

- Stable object references
- Platform status primitives
- Error types
- Event envelope
- Actor attribution requirement
- Module identity
- Contract interfaces

Kernel should not contain:

- Domain models
- Business workflows
- Database-heavy implementation logic
- BOMI/IPI-specific terminology

Kernel should change rarely. Core Runtime can evolve faster than Kernel.

## 8. Identity Runtime Evaluation

Recommendation: include Identity Runtime in Core v0.1 planning.

Rationale:

Evidence, reviews, decisions, lifecycle events, and ledger entries must always be attributable to an actor.

Candidate actor types:

- Human
- Organisation
- AI Agent
- Device
- Sensor
- Contractor
- Authority

Minimum v0.1 actor model:

```text
Actor
|-- actor_id
|-- actor_type
|-- display_name
|-- organisation_id
|-- authority_level
|-- external_reference
|-- active_status
```

Minimum attribution rule:

No evidence verification, review outcome, decision, lifecycle transition, or ledger entry should be accepted without an actor reference.

Open question:

Should sensors and devices be direct actors, or should they be evidence sources attributed to a responsible human/organisation? Recommendation: allow device actors, but require responsible owner linkage before decision use.

## 9. Expanded Procedure Runtime

Recommendation: expand Procedure Runtime beyond basic workflow execution.

Target model:

```text
Procedure
-> Stage
-> Gate
-> Review
-> Decision
-> Next Procedure
```

Objects:

- `ProcedureTemplate`
- `ProcedureRun`
- `ProcedureStage`
- `ProcedureGate`
- `GateRequirement`
- `ReviewBinding`
- `DecisionRecord`
- `NextProcedureRule`

Purpose:

This supports infrastructure approval processes where one governed procedure leads to another, such as:

- Opportunity discovery -> validation
- Validation -> legal review
- Inspection -> remediation
- Remediation -> re-inspection
- Go decision -> execution procedure

Boundary:

Procedure Runtime should orchestrate governance state. It should not implement domain calculations, compliance certification, AI decisions, or workflow UI.

## 10. Generalised Registry

Recommendation: rename or generalise Runtime Registry into Registered Object Registry.

Reason:

Not every governed object is a live runtime object. Some are documents, source systems, procedures, modules, projects, components, organisations, devices, and evidence packages.

Target concept:

```text
RegisteredObject
|-- object_id
|-- object_type
|-- module_id
|-- external_reference
|-- lifecycle_state
|-- governance_status
|-- created_by_actor_id
|-- created_at
|-- updated_at
```

Runtime objects become a subset of registered objects.

Recommended package name:

```text
buildingos_core.registry
```

Avoid naming the whole package `runtime_registry` if the intent is broader than active runtime objects.

## 11. Dependency Strategy

Principles:

- Kernel has no dependency on Core Runtime packages.
- Core Runtime packages may depend on Kernel and Identity.
- Module SDK may depend on all Core Runtime packages.
- Modules depend on Module SDK and selected Core Runtime packages.
- Core must not depend on IPI, BOMI, ClimateOS, WaterOS, or EnergyOS.

Dependency direction:

```text
buildingos-spec
    ^
    |
buildingos-core kernel
    ^
    |
buildingos-core runtimes
    ^
    |
buildingos-core module_sdk
    ^
    |
BuildingOS modules
```

Python dependency strategy:

- Start with Python standard library where possible.
- Use SQLite for v0.1 persistence compatibility.
- Avoid web frameworks in Core v0.1.
- Keep FastAPI or UI integration outside Core foundation.
- Use repository contracts so storage can evolve later.

Versioning strategy:

- `buildingos-spec` versions platform standards.
- `buildingos-core` versions implementation.
- Modules declare compatible Core and Spec versions.

## 12. Adapter Strategy

Adapters protect stable modules while Core matures.

### BOMI Adapter

Initial adapters:

- BOMI evidence -> Core evidence
- BOMI inspection -> Core review record
- BOMI lifecycle event -> Core lifecycle event
- BOMI runtime object -> Core registered object
- BOMI actor strings -> Core actor references

Keep in BOMI:

- Component models
- Service spine models
- Interface ports
- Interface compatibility logic
- BOMI examples and domain docs

### IPI Adapter

Initial adapters:

- IPI source document -> Core source/evidence reference
- IPI evidence claim -> Core claim
- IPI workflow gate -> Core procedure gate
- IPI project profile -> Core registered object reference

Keep in IPI:

- Project profile
- Project type
- Delivery model
- Candidate matching
- Infrastructure source taxonomy

Adapter rule:

Do not replace module internals until adapter contract tests pass.

## 13. Migration Roadmap

Phase 0: Planning and approval

- Review this engineering plan.
- Decide `buildingos-spec` ownership.
- Decide separate repo vs monorepo for `buildingos-core`.
- Confirm Identity Runtime inclusion.
- Confirm Registered Object Registry naming.

Phase 1: Specification foundation

- Create `buildingos-spec`.
- Write standards for evidence, claims, identity, review, procedure, lifecycle, registry, ledger, and module contracts.
- Add language-neutral JSON schemas and examples.

Phase 2: Core foundation

- Create `buildingos-core`.
- Implement Kernel primitives.
- Implement Identity Runtime.
- Implement Evidence and Claim runtimes.
- Implement Registered Object Registry.
- Add SQLite schema and unit tests.

Phase 3: Governance runtimes

- Implement Review Runtime.
- Implement Procedure Runtime.
- Implement Lifecycle Runtime.
- Implement Governance Ledger.
- Add integration tests across identity/evidence/claim/review/ledger.

Phase 4: Module SDK

- Implement module manifest.
- Implement adapter interfaces.
- Implement contract test harness.
- Add sample stub module.

Phase 5: BOMI adapter

- Add BOMI adapter package without changing BOMI domain models.
- Prove BOMI can emit Core evidence, review, lifecycle, and registered object records.
- Keep BOMI stable.

Phase 6: IPI adapter

- Add IPI adapter package.
- Prove IPI can emit Core evidence, claims, procedure gates, and registered object references.
- Keep IPI stable.

Phase 7: Cleanup and release packaging

- Remove duplicate nested BOMI folders if approved.
- Consolidate duplicated schema paths or document mirror policy.
- Prepare release notes and migration guide.

## 14. Testing Strategy

Testing layers:

1. Unit tests

   - Kernel object references
   - Identity actor model
   - Evidence ranking
   - Claim confidence
   - Review outcomes
   - Procedure transitions
   - Lifecycle transitions
   - Registry ID generation

2. Schema tests

   - SQLite initialization
   - Foreign key integrity
   - Required indexes
   - Migration order

3. Contract tests

   - Module manifests validate
   - Module adapters produce Core-compatible objects
   - Evidence and claim links remain traceable

4. Integration tests

   - Actor -> evidence -> claim -> review -> decision -> ledger
   - Registered object -> lifecycle event -> review -> next procedure
   - BOMI adapter to Core
   - IPI adapter to Core

5. Governance tests

   - No review without actor
   - No decision without evidence summary
   - No lifecycle transition without allowed transition rule
   - No module bypass of Core governance status

6. Release checks

   - Placeholder scan
   - JSON example validation
   - Schema object count
   - Git clean status
   - BEWP checklist

## 15. Estimated Implementation Batches

Batch C01: `buildingos-spec` foundation

- Standards documents
- JSON schemas
- Examples
- Compatibility policy

Estimated size: 1-2 engineering days.

Batch C02: Core repository skeleton

- Repo structure
- Kernel package
- CI
- Base docs
- Initial schema layout

Estimated size: 1 day.

Batch C03: Identity + Evidence + Claims

- Actor model
- Evidence model
- Claim model
- Attribution rules
- Unit/schema tests

Estimated size: 2-3 engineering days.

Batch C04: Registered Object Registry + Ledger

- Registered object model
- ID generation
- Ledger entries
- Registry schema
- Traceability tests

Estimated size: 2 days.

Batch C05: Review + Procedure + Lifecycle

- Review records
- Procedure model with Stage/Gate/Review/Decision/Next Procedure
- Lifecycle transitions
- Integration tests

Estimated size: 3-4 engineering days.

Batch C06: Module SDK and contract tests

- Module manifest
- Adapter interfaces
- Contract test harness
- Stub module example

Estimated size: 2-3 engineering days.

Batch C07: BOMI adapter proof

- BOMI evidence/review/lifecycle/registered object adapters
- Adapter tests
- No direct BOMI refactor

Estimated size: 2-3 engineering days.

Batch C08: IPI adapter proof

- IPI evidence/claim/procedure/registered object adapters
- Adapter tests
- No direct IPI refactor

Estimated size: 2-3 engineering days.

Batch C09: Release hardening

- Documentation alignment
- Duplicate-folder cleanup plan
- Migration guide
- BEWP closure report

Estimated size: 1-2 engineering days.

## 16. Risks

Risk: Core becomes too abstract.

Mitigation: every Core object must support at least two modules, initially IPI and BOMI.

Risk: Kernel changes too often.

Mitigation: keep Kernel minimal and stable; place evolving behavior in Core Runtime.

Risk: Identity Runtime creates premature permission complexity.

Mitigation: start with attribution and actor typing before full permissions.

Risk: Procedure Runtime becomes a workflow engine too early.

Mitigation: model governance state transitions, not UI automation or task scheduling.

Risk: Registered Object Registry becomes a generic database catalog.

Mitigation: register only governed platform objects that need evidence, lifecycle, review, or ledger linkage.

Risk: `buildingos-spec` adds governance overhead.

Mitigation: keep specs concise, versioned, and implementation-facing.

Risk: BOMI and IPI become unstable during migration.

Mitigation: use adapters first; no direct module refactor until Core contract tests pass.

## 17. Validation Requirements Before QClaw Assignment

Before implementation tasks are assigned:

- ChatGPT reviews this engineering plan.
- Simon confirms product direction remains correct.
- Core repository strategy is approved.
- `buildingos-spec` decision is made.
- Identity Runtime inclusion is approved or deferred.
- Registered Object Registry naming is approved.
- Procedure Runtime scope is approved.
- Batch sequence is accepted.

Only after these decisions should QClaw receive a scoped implementation brief.

## 18. Recommended Next Step

Move this planning task to architecture review:

```text
READY_FOR_ARCHITECT_REVIEW
```

Recommended reviewer:

```text
ChatGPT - Chief Architect / Governance Reviewer
```

Recommended review question:

Should BuildingOS Core Phase 1 proceed with Kernel + Core Runtime + Module SDK + buildingos-spec as described, or should the plan be narrowed before assigning implementation to QClaw?

## 19. Conversation Radar

Knowledge points:

- Architecture review passed for Core + Modules.
- Kernel should be the most stable internal layer.
- Identity Runtime is likely necessary for attribution.
- Procedure Runtime should model Procedure -> Stage -> Gate -> Review -> Decision -> Next Procedure.
- Runtime Registry should likely generalise to Registered Object Registry.
- `buildingos-spec` should hold language-neutral standards.

Idea points:

- Build specs before implementation to avoid inconsistent future modules.
- Use adapters before direct module refactors.
- Treat Identity first as attribution, then permissions later.
- Keep Kernel minimal and stable.

Decisions:

- No Core implementation starts in this phase.
- No QClaw implementation task is assigned yet.
- Product scope remains unchanged.

Risks:

- Over-abstracting Core.
- Under-specifying governance primitives.
- Destabilising BOMI/IPI through premature refactor.
- Confusing Runtime Registry with a generic asset database.

Open questions:

- Should `buildingos-spec` be created before or alongside `buildingos-core`?
- Should Identity Runtime be required in Core v0.1?
- Should Registered Object Registry replace Runtime Registry naming immediately?
- Should duplicate BOMI nested folders be cleaned before adapter work?

Next actions:

- Review this plan with ChatGPT.
- Confirm product direction with Simon.
- Convert approved plan into QClaw implementation batches only after review.

