# C01 - BuildingOS Specification Foundation Plan

## 0. Execution Order Update

Current M1 execution order now requires:

```text
C00 - BuildingOS Glossary Foundation
-> C00 Review
-> C00 Approval
-> C00 Freeze
-> C01-A Evidence Standard
```

C01 remains the Specification Foundation milestone, but C01-A must not proceed
until C00 is approved and frozen.

This update does not redesign BuildingOS and does not change the approved
architecture boundary. It clarifies the engineering sequence for M1.

Dependency status:

```text
C00_GLOSSARY_FOUNDATION_V1_0 = FROZEN
```

C01-A may proceed under the approved engineering workflow.

Current specification tracking artifacts:

- `BUILDINGOS_SPECIFICATION_INDEX.md`
- `BUILDINGOS_SPECIFICATION_DEPENDENCY_MAP.md`
- `BUILDINGOS_SPECIFICATION_CHANGELOG.md`

## 1. Purpose

C01 prepares the language-neutral BuildingOS specification foundation before any Core implementation begins.

The intended repository is:

```text
buildingos-spec
```

This plan defines the C01 scope, reviewable sub-batches, conformance requirements, validation checks, and engineering review flow.

This document does not create `buildingos-spec` and does not start Core
implementation.

## 2. Current BEWP State

```text
M1_SPECIFICATION_FOUNDATION_COMPLETE_LOCALLY
```

Target next state:

```text
C02_CORE_IMPLEMENTATION_PLANNING
```

## 3. Engineering Principles

C01 must follow:

- Stabilise before Expand.
- Standardise before Optimise.
- Governance before Automation.

Practical interpretation:

- Define standards before writing runtime code.
- Define conformance before optimizing schemas.
- Define governance boundaries before automation hooks.

## 4. Scope

In scope:

- Language-neutral specification documents
- JSON schemas
- JSON examples
- Conformance requirement checklists
- Versioning and compatibility policy
- Review process
- Repository structure for `buildingos-spec`

Out of scope:

- Python runtime implementation
- `buildingos-core` implementation
- BOMI refactor
- IPI refactor
- Permission systems
- Capability Registry implementation
- Architecture RFC repository
- Frontend/API/IoT/certification automation

## 5. Proposed C01 Repository Structure

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
|   |-- REGISTERED_OBJECT_STANDARD.md
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
|   |   |-- ledger_entry.schema.json
|   |   `-- module_manifest.schema.json
|   `-- examples/
|       |-- evidence_record.example.json
|       |-- claim.example.json
|       |-- actor.example.json
|       |-- review_record.example.json
|       |-- procedure.example.json
|       |-- lifecycle_event.example.json
|       |-- registered_object.example.json
|       |-- ledger_entry.example.json
|       `-- module_manifest.example.json
|-- docs/
|   |-- VERSIONING_POLICY.md
|   |-- COMPATIBILITY_POLICY.md
|   |-- CONFORMANCE_POLICY.md
|   |-- REVIEW_PROCESS.md
|   `-- REPOSITORY_STRUCTURE.md
`-- checks/
    |-- SPEC_CHECKLIST.md
    `-- CONFORMANCE_MATRIX.md
```

## 6. Incremental Review Rule

Every C01 sub-batch must complete:

```text
Implementation
-> Self Review
-> Codex Engineering Review
-> Architecture Review (if required)
-> Approval
-> Freeze
```

before the next C01 sub-batch begins.

After a sub-batch is approved, it is frozen. Later changes require a formal Change Request and Version Review.

## 7. C01 Sub-Batches

### C01-0 - Repository and Governance Skeleton

Deliverables:

- `README.md`
- `docs/REPOSITORY_STRUCTURE.md`
- `docs/VERSIONING_POLICY.md`
- `docs/COMPATIBILITY_POLICY.md`
- `docs/CONFORMANCE_POLICY.md`
- `docs/REVIEW_PROCESS.md`
- `checks/SPEC_CHECKLIST.md`
- `checks/CONFORMANCE_MATRIX.md`

Acceptance criteria:

- Repository is language-neutral.
- No runtime implementation exists.
- Review process is explicit.
- Conformance matrix references every standard.

### C01-A - Evidence Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_A_EVIDENCE_STANDARD.md`
- `docs/BUILDINGOS_C01_A_EVIDENCE_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_A_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_A_EVIDENCE_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- C00 v1.0 glossary dependency is referenced.
- Evidence is not treated as fact.
- Evidence strength and verification status are defined.
- Evidence records require actor attribution where verification or review occurs.
- Evidence does not create approval by itself.
- Conformance requirements are explicit.

Freeze rule:

After C01-A is approved, it is frozen. Any change to the Evidence Standard must follow Change Request and Version Review.

### C01-B - Claim Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_B_CLAIM_STANDARD.md`
- `docs/BUILDINGOS_C01_B_CLAIM_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_B_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_B_CLAIM_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- C00 v1.0 glossary dependency is referenced.
- C01-A v1.0 Evidence Standard dependency is referenced.
- Claims must be traceable to evidence or marked unsupported.
- Claims distinguish assertion, evidence support, confidence, and review status.
- Claims do not become confirmed facts without review rules.
- Conformance requirements are explicit.

### C01-C - Identity Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_C_IDENTITY_STANDARD.md`
- `docs/BUILDINGOS_C01_C_IDENTITY_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_C_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_C_IDENTITY_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Identity scope is attribution only.
- Permission systems are explicitly out of scope.
- Actor types include Human, Organisation, AI Agent, Device, Sensor, Contractor, Authority.
- Governance actions require actor attribution.

### C01-D - Review Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_D_REVIEW_STANDARD.md`
- `docs/BUILDINGOS_C01_D_REVIEW_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_D_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_D_REVIEW_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Reviews require actor attribution.
- Review records distinguish observation, assessment, decision, and recommendation.
- Review outcomes do not silently override evidence or claims.
- Conformance requirements are explicit.

### C01-E - Procedure Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_E_PROCEDURE_STANDARD.md`
- `docs/BUILDINGOS_C01_E_PROCEDURE_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_E_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_E_PROCEDURE_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Procedure model follows Procedure -> Stage -> Gate -> Review -> Decision -> Next Procedure.
- Procedure is not framed as a workflow engine.
- Conformance requirements cover review and decision boundaries.

### C01-F - Lifecycle Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_F_LIFECYCLE_STANDARD.md`
- `docs/BUILDINGOS_C01_F_LIFECYCLE_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_F_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_F_LIFECYCLE_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Lifecycle events require actor attribution.
- Lifecycle events require allowed transition semantics.
- Lifecycle history remains auditable.
- Conformance requirements are explicit.

### C01-G - Registered Object Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_G_REGISTERED_OBJECT_STANDARD.md`
- `docs/BUILDINGOS_C01_G_REGISTERED_OBJECT_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_G_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_G_REGISTERED_OBJECT_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Registered Object Registry is distinct from a generic asset database.
- Runtime objects are a subset of registered objects.
- Registered objects are governed platform objects with evidence, review, lifecycle, or ledger relevance.

### C01-H - Governance Ledger Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_H_GOVERNANCE_LEDGER_STANDARD.md`
- `docs/BUILDINGOS_C01_H_GOVERNANCE_LEDGER_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_H_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_H_GOVERNANCE_LEDGER_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Ledger entries are append-oriented and actor-attributed.
- Ledger entries preserve governance traceability.
- Ledger does not become a general event log for non-governed activity.

### C01-I - Module Contract Standard

Status:

```text
FROZEN_V1_0
```

Deliverables:

- `docs/BUILDINGOS_C01_I_MODULE_CONTRACT_STANDARD.md`
- `docs/BUILDINGOS_C01_I_MODULE_CONTRACT_STANDARD_SELF_REVIEW.md`
- `docs/CODEX_C01_I_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_C01_I_MODULE_CONTRACT_STANDARD_FREEZE_RECORD_V1_0.md`

Acceptance criteria:

- Module contracts do not assume `buildingos-modules` exists yet.
- Module contracts require declared capabilities, dependencies, and conformance targets.
- Module contracts do not bypass Core governance semantics.

### M1 Integration Review and Core Readiness

Deliverables:

- `docs/BUILDINGOS_M1_INTEGRATION_REVIEW.md`
- `docs/BUILDINGOS_CORE_READINESS_REPORT.md`

Acceptance criteria:

- Scope exclusions are explicit.
- Frozen specifications are coherent as a baseline.
- Core readiness is assessed without starting implementation.

## 8. Conformance Requirements

Every specification must include:

- Purpose
- Scope
- Out-of-scope boundaries
- Required fields
- Optional fields
- Actor attribution requirement
- Evidence/claim relationship where applicable
- Review or decision boundary where applicable
- Conformance requirements
- Non-conformance examples
- Versioning notes

Every JSON schema must:

- Be language-neutral.
- Avoid implementation-specific class names.
- Include required fields.
- Include explicit enum values where governance semantics depend on controlled vocabulary.
- Include examples that parse as valid JSON.

Every example must:

- Be fictional.
- Avoid real personal data.
- Use stable IDs.
- Show actor attribution when governance actions occur.

## 9. Validation Checks

Minimum validation expected from Codex during this milestone:

- File manifest check
- Markdown required-section check
- JSON parse check
- JSON schema example validation where tooling is available
- Placeholder scan
- Scope exclusion scan
- Conformance matrix completeness check
- Git status check

Codex review must verify:

- Required files exist.
- Standards are language-neutral.
- No implementation code was introduced.
- Conformance requirements are explicit.
- Scope boundaries are preserved.
- Git status is clean.

## 10. Engineering Risks

Risk: specification documents become too broad.

Mitigation: require each standard to state what it does not govern.

Risk: C01 drifts into implementation.

Mitigation: no Python package, database runtime, API, or UI files are allowed.

Risk: Identity becomes a permission system.

Mitigation: C01 identity is attribution-only.

Risk: Procedure becomes a workflow engine.

Mitigation: C01 procedure standard defines governance structure, not workflow automation.

Risk: Registered Object becomes an asset database.

Mitigation: only governed platform objects with evidence/review/lifecycle/ledger relevance are in scope.

## 11. Ownership

| Role | Responsibility |
| --- | --- |
| Simon | Product direction and scope confirmation |
| ChatGPT | Architecture and governance review |
| Codex | Engineering manager, brief owner, review owner |
| QClaw | No active BuildingOS Core execution responsibility during this milestone |

## 12. Internal Engineering Review

Codex review result for this plan:

```text
M1_SPECIFICATION_FOUNDATION_COMPLETE_LOCALLY
```

Reason:

- Roadmap v1.0 is approved for Milestone M1.
- C01 specification foundation is complete locally.
- Batches were completed under the Incremental Review Principle.
- Core implementation remains gated by a future implementation planning brief.

## 13. Next Step

Next engineering package:

```text
C02 - BuildingOS Core Implementation Planning Brief
```

C02 must remain planning-only until explicitly approved.

## 14. Conversation Radar

Knowledge points:

- Milestone M1 is approved to prepare.
- C01 is specification foundation only.
- Identity remains attribution-only.
- Procedure is governance structure, not workflow automation.
- Registered Object is broader than runtime object.

Idea points:

- Split C01 into reviewable, frozen sub-batches.
- Use conformance requirements as the bridge between standards and later runtime implementation.
- Make `buildingos-spec` the language-neutral source of truth.

Decisions:

- No implementation starts from this document.
- No Core runtime is created in C01 planning.
- No `buildingos-modules` repo is created.

Risks:

- Spec bloat.
- Implementation drift.
- Permission scope creep.
- Workflow engine scope creep.

Open questions:

- Should C02 include executable conformance checks, or remain documentation-only?
- Should JSON schema validation tooling be introduced during Core planning or deferred until implementation?
- Should the conformance matrix become the primary closure artifact for Core implementation batches?

Next actions:

1. Prepare C02 BuildingOS Core Implementation Planning Brief.
2. Review C02 for architecture and governance alignment.
3. Begin Core implementation only after C02 approval.
