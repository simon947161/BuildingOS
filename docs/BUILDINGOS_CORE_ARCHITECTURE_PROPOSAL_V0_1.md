# BuildingOS Core Architecture Proposal v0.1

## 1. Purpose

This proposal reviews whether BOMI should depend on a shared BuildingOS Core rather than continuing to implement evidence, review, lifecycle, and runtime concepts independently.

Recommendation: yes. BuildingOS should evolve toward a Core + Modules architecture before additional modules are added.

This is an architecture proposal only. It does not assign implementation work to QClaw and does not start refactoring.

## 2. Current Observation

IPI and BOMI now share the same architectural pattern:

```text
Source -> Evidence -> Claim -> Review -> Decision -> Ledger -> Continuous Governance
```

Observation:

- IPI implements project discovery, source documents, evidence levels, claims, candidate matching, and workflow gates.
- BOMI implements physical infrastructure objects, evidence records, inspections, lifecycle events, runtime objects, and interface matching.
- Both modules repeat shared governance concepts in module-specific code.

Interpretation:

- The shared pattern is stable enough to become BuildingOS Core.
- IPI and BOMI should become domain modules that depend on Core primitives.
- New modules such as ClimateOS, WaterOS, and EnergyOS should not each reinvent evidence, claims, review, lifecycle, and runtime registries.

## 3. Recommendation

Create a new repository:

```text
buildingos-core/
```

BuildingOS Core should provide shared governance infrastructure. Modules should provide domain-specific object models, matching rules, schemas, examples, and workflows.

Recommended target architecture:

```text
BuildingOS Core
|
|-- Evidence Runtime
|-- Procedure Runtime
|-- Review Runtime
|-- Lifecycle Runtime
|-- Runtime Registry
|-- Governance Kernel
|
`-- Modules
    |-- IPI
    |-- BOMI
    |-- ClimateOS
    |-- WaterOS
    |-- EnergyOS
    `-- Future Modules
```

## 4. What Should Move from BOMI to BuildingOS Core

These classes and concepts should become shared Core infrastructure, after review and API design:

| BOMI Area | Current Classes / Concepts | Proposed Core Home | Reason |
| --- | --- | --- | --- |
| Evidence | `EvidenceRecord`, `EvidenceStrength`, `EvidenceSourceType`, `EvidenceManager` | `buildingos_core.evidence` | Evidence, source strength, and verification are cross-module. |
| Claims | claim/evidence relationships in schema and helper functions | `buildingos_core.claims` | Claim-level governance is common to IPI, BOMI, and future modules. |
| Review / Inspection | `InspectionRecord`, `InspectionResult`, checklist/deficiency patterns | `buildingos_core.review` | Inspections are BOMI-specific in wording, but the review record pattern is shared. |
| Lifecycle | `LifecycleEvent`, `LifecycleState`, `LifecycleManager` | `buildingos_core.lifecycle` | State transitions and auditable lifecycle events are platform-level. |
| Runtime Registry | `RuntimeObject`, `RuntimeIDGenerator`, `RuntimeManager` | `buildingos_core.runtime_registry` | Stable runtime identity should be consistent across all modules. |
| Governance Status | `ComplianceStatus`, verification status, readiness status | `buildingos_core.governance` | Status semantics must be consistent across modules. |
| Audit Trail | created/updated metadata, actor fields, event records | `buildingos_core.ledger` | Governance requires consistent traceability. |
| Repositories | SQLite connection/init patterns and registry base behavior | `buildingos_core.persistence` | Repeated manager/registry patterns should share durable conventions. |

Important distinction:

- Move the abstract review record pattern into Core.
- Keep domain-specific inspection vocabulary, checklists, and building trade roles in BOMI.

## 5. What Should Remain BOMI-Specific

These classes should remain in BOMI because they describe modular building infrastructure:

| BOMI Area | Classes / Concepts | Reason |
| --- | --- | --- |
| Components | `ComponentProfile`, `ComponentCategory`, `Dimensions`, `PerformanceSpec`, `ComplianceCertification`, `ComponentRegistry` | These describe physical building components and materials. |
| Interfaces | `InterfacePort`, `ServiceType`, `PortGender`, `PortRatings`, `InterfaceValidator` | These define the Open Building Interface Protocol. |
| Service Spine | `ServiceSpine`, `ServiceCapacity`, `InterfacePosition`, `SpineOrientation`, `ServiceSpineRegistry` | Building Service Spine is the core BOMI domain object. |
| Matching | `ComponentInterfaceMatcher`, compatibility scoring, interface matching | Matching rules are domain-specific to modular infrastructure. |
| Building Examples | wall component, service spine, sensor port, inspection example JSON | Examples are BOMI-specific training and validation artifacts. |
| Building Docs | Service spine standard, open interface protocol, component templates | These documents define BOMI domain meaning. |

## 6. IPI Shared Concepts That Should Also Move to Core

IPI contains shared platform concepts that should align with Core:

| IPI Area | Current Classes / Concepts | Proposed Core Home |
| --- | --- | --- |
| Evidence ranking | `EvidenceLevel`, `EvidenceAssessment`, evidence ranking helpers | `buildingos_core.evidence` |
| Source documents | `SourceDocument`, `SourceConfig`, source collector protocol | `buildingos_core.sources` with module adapters |
| Claims | `EvidenceClaim` | `buildingos_core.claims` |
| Workflow gates | `WorkflowGate`, workflow states and gate rules | `buildingos_core.procedures` |
| Candidate status | project status, confidence and review status patterns | `buildingos_core.governance` |

IPI-specific concepts should remain in IPI:

- Project profiles
- Project types
- Delivery models
- Procurement/project stages
- Candidate matching by region, investment, stage, and delivery model
- Infrastructure project source taxonomies

## 7. Shared Runtime Objects

These runtime objects should become shared infrastructure:

1. `RuntimeObject`

   Generic registered object with:

   - runtime ID
   - module ID
   - object type
   - object reference ID
   - lifecycle state
   - governance status
   - active/inactive flag
   - created/updated metadata

2. `RuntimeID`

   Stable identifier generated by Core, not by each module independently.

3. `EvidenceRecord`

   Shared evidence artifact linked to a claim, review, lifecycle event, runtime object, or module object.

4. `Claim`

   Shared structured assertion:

   - subject
   - field
   - value
   - confidence status
   - evidence links
   - review state

5. `ReviewRecord`

   Shared review/inspection/check record:

   - reviewer role
   - review type
   - result
   - decision boundary
   - notes
   - evidence links

6. `LifecycleEvent`

   Shared auditable event:

   - from state
   - to state
   - actor
   - event type
   - evidence links
   - timestamp

7. `ProcedureRun`

   Shared workflow execution:

   - procedure template
   - current gate
   - required inputs
   - exit criteria
   - decision records

8. `LedgerEntry`

   Shared append-only governance event:

   - actor
   - action
   - object reference
   - before/after summary
   - timestamp
   - evidence reference

## 8. Proposed `buildingos-core` Repository Structure

```text
buildingos-core/
|-- README.md
|-- pyproject.toml
|-- docs/
|   |-- TECHNICAL_DESIGN.md
|   |-- CORE_GOVERNANCE_MODEL.md
|   |-- EVIDENCE_RUNTIME_STANDARD.md
|   |-- CLAIM_MODEL.md
|   |-- REVIEW_RUNTIME_STANDARD.md
|   |-- PROCEDURE_RUNTIME_STANDARD.md
|   |-- LIFECYCLE_RUNTIME_STANDARD.md
|   |-- RUNTIME_REGISTRY_STANDARD.md
|   |-- GOVERNANCE_KERNEL.md
|   |-- MODULE_INTEGRATION_GUIDE.md
|   `-- REPOSITORY_STRUCTURE.md
|-- buildingos_core/
|   |-- __init__.py
|   |-- evidence/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- ranking.py
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
|   |   |-- models.py
|   |   |-- gates.py
|   |   `-- repository.py
|   |-- lifecycle/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- transitions.py
|   |   `-- repository.py
|   |-- runtime_registry/
|   |   |-- __init__.py
|   |   |-- ids.py
|   |   |-- models.py
|   |   `-- repository.py
|   |-- governance/
|   |   |-- __init__.py
|   |   |-- statuses.py
|   |   |-- roles.py
|   |   |-- permissions.py
|   |   `-- policies.py
|   |-- ledger/
|   |   |-- __init__.py
|   |   |-- models.py
|   |   `-- repository.py
|   |-- persistence/
|   |   |-- __init__.py
|   |   |-- sqlite.py
|   |   `-- migrations.py
|   `-- module_api/
|       |-- __init__.py
|       |-- contracts.py
|       `-- registry.py
|-- schemas/
|   |-- sqlite/
|   |   |-- core_schema.sql
|   |   |-- evidence.sql
|   |   |-- claims.sql
|   |   |-- review.sql
|   |   |-- procedures.sql
|   |   |-- lifecycle.sql
|   |   |-- runtime_registry.sql
|   |   `-- governance_ledger.sql
|   `-- json/
|       |-- evidence_record.schema.json
|       |-- claim.schema.json
|       |-- review_record.schema.json
|       |-- lifecycle_event.schema.json
|       `-- runtime_object.schema.json
|-- examples/
|   |-- evidence_record.json
|   |-- claim.json
|   |-- review_record.json
|   |-- lifecycle_event.json
|   `-- runtime_object.json
|-- tests/
|   |-- test_evidence_runtime.py
|   |-- test_claim_model.py
|   |-- test_review_runtime.py
|   |-- test_procedure_runtime.py
|   |-- test_lifecycle_runtime.py
|   |-- test_runtime_registry.py
|   `-- test_module_contracts.py
`-- .github/
    `-- workflows/
        `-- ci.yml
```

## 9. Proposed Module Structure After Core Exists

IPI should become:

```text
buildingos-modules/
`-- ipi/
    |-- ipi/
    |   |-- projects.py
    |   |-- sources.py
    |   |-- matching.py
    |   `-- workflows.py
    |-- schemas/
    |-- docs/
    |-- examples/
    `-- tests/
```

BOMI should become:

```text
buildingos-modules/
`-- bomi/
    |-- bomi/
    |   |-- components.py
    |   |-- interfaces.py
    |   |-- service_spine.py
    |   `-- matching.py
    |-- schemas/
    |-- docs/
    |-- examples/
    `-- tests/
```

Modules should import Core concepts rather than redefining them:

```text
from buildingos_core.evidence import EvidenceRecord
from buildingos_core.claims import Claim
from buildingos_core.lifecycle import LifecycleEvent
from buildingos_core.runtime_registry import RuntimeObject
```

## 10. Refactor Strategy

Recommended sequencing:

1. Create `buildingos-core` proposal and review package.
2. Have ChatGPT review governance boundaries.
3. Have Simon validate product direction.
4. Assign QClaw a Core v0.1 foundation task.
5. Build Core without refactoring BOMI or IPI yet.
6. Add module contract tests.
7. Refactor BOMI to consume Core.
8. Refactor IPI to consume Core.
9. Only then start new modules such as ClimateOS, WaterOS, and EnergyOS.

Do not start by moving code out of BOMI. First define stable Core contracts and tests.

## 11. Migration Plan for BOMI

Phase 1: Compatibility Layer

- Keep BOMI API stable.
- Add adapters that convert BOMI evidence, inspection, lifecycle, and runtime objects into Core objects.
- Do not remove BOMI classes yet.

Phase 2: Core Dependency

- Replace BOMI `EvidenceRecord` with Core `EvidenceRecord`.
- Replace BOMI lifecycle event storage with Core lifecycle runtime.
- Replace BOMI runtime ID generation with Core runtime registry.
- Keep BOMI component, interface, service spine, and matching models module-specific.

Phase 3: Cleanup

- Remove duplicate nested folders.
- Remove duplicated schema definitions.
- Keep module schema focused on BOMI-specific tables.
- Move shared tables into Core schema.

## 12. Validation Requirements

Before implementation:

- Architecture review approves Core boundaries.
- Simon confirms Core + Modules direction.
- QClaw confirms implementation feasibility.
- BEWP state moves from architecture proposal to assigned implementation task.

During implementation:

- Core unit tests must pass.
- Module contract tests must prove BOMI and IPI can use Core.
- No module may bypass evidence/claim/review/lifecycle rules.
- Git status must be clean before closure.

## 13. Risks

Risk: over-abstracting too early.

Mitigation: move only concepts repeated across IPI and BOMI; keep domain objects in modules.

Risk: breaking BOMI after it has just passed architecture review.

Mitigation: build Core first, then migrate BOMI through adapters.

Risk: Core becomes a vague framework instead of governance infrastructure.

Mitigation: define Core around concrete primitives: evidence, claims, review, procedures, lifecycle, runtime registry, roles, permissions, ledger.

Risk: future modules inherit weak governance.

Mitigation: require module contract tests and BEWP review before each module is accepted.

## 14. Decisions Needed

Architecture decisions:

1. Should BuildingOS Core be a separate repository or a top-level package inside a monorepo?
2. Should IPI and BOMI remain separate repos or become modules inside a `buildingos-modules` repository?
3. Should Core v0.1 include roles and permissions immediately?
4. Should Core v0.1 include an append-only ledger immediately?
5. Should runtime IDs be globally unique across all modules from the beginning?

Engineering decisions:

1. Should Core use SQLite first, matching IPI and BOMI, or define storage-neutral repository contracts?
2. Should module schemas import Core schemas, or should each module deploy a combined schema bundle?
3. Should duplicate BOMI nested folders be cleaned before or after Core extraction?

## 15. Recommended Decision

Recommended path:

- Create `buildingos-core` as a separate repository.
- Keep IPI and BOMI stable while Core v0.1 is built.
- Make Core SQLite-compatible but repository-contract oriented.
- Include roles, permissions, audit ledger, runtime registry, evidence, claims, review, procedures, and lifecycle in Core v0.1.
- Migrate BOMI first because it already has the richest runtime/lifecycle object model.
- Migrate IPI second to align project governance with shared evidence, claim, and procedure runtime.

## 16. Conversation Radar

Knowledge points:

- IPI and BOMI duplicate evidence, claim, workflow/lifecycle, and runtime concepts.
- BOMI domain objects should remain module-specific.
- Runtime identity and evidence governance should be shared.

Idea points:

- BuildingOS Core should be governance infrastructure, not a generic utility library.
- Modules should depend on Core contracts and provide domain semantics.
- Core should be created before ClimateOS, WaterOS, and EnergyOS implementation expands.

Decisions:

- This phase is proposal-only.
- No QClaw implementation task should start until review is complete.
- BOMI should not be refactored directly before Core contracts exist.

Risks:

- Premature refactor could destabilize BOMI v0.1.
- Waiting too long will cause each module to duplicate governance code.
- A weak Core boundary would make future modules inconsistent.

Open questions:

- Separate repo or monorepo?
- Core schema deployment model?
- Minimum role and permission model?
- First migration target: BOMI only, or BOMI and IPI together?

Next actions:

- Review this proposal with ChatGPT.
- Ask Simon to confirm Core + Modules product direction.
- If approved, assign QClaw a scoped `buildingos-core v0.1 foundation` task.

