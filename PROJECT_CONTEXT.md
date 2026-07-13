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

`POST_CORE_BATCH_01_PROJECT_GENOME_PLANNING`

## Current Milestone

BuildingOS Project Genome and Classification Standard, followed by lifecycle architecture, human-interface architecture, and pilot planning.

## Current Status

`PRODUCT_NORTH_STAR_AND_EVIDENCE_INTAKE_BASELINES_COMPLETE_READY_FOR_PROJECT_GENOME`

## Frozen Core Batch 01 Implementation Baseline

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
- Core Batch 01 minimum Governance Kernel implementation at `f84b22bf4921e4f98e15598c5c5a5aa18bcaa996`

Changes to any frozen baseline require Change Request, Engineering Review, Architecture Review when required, Chief Architect Approval, and an updated Freeze Record.

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
- Baseline integrity verified.
- Chief Architect recorded `APPROVE_CORE_BATCH_01_FOR_FREEZE` on 2026-07-13.
- Core Batch 01 Approval Record activated.
- Core Batch 01 Freeze Record activated.
- BuildingOS Product North Star documentation baseline prepared.
- ClimateOS-to-BuildingOS Cross-Domain Evidence Intake Contract prepared.
- NEXTDC S7 Sydney candidate large-project evidence intake profile prepared.

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

Baseline integrity decision:

```text
VERIFIED_IMPLEMENTATION_BASELINE_UNCHANGED
```

Freeze decision:

```text
CORE_BATCH_01_FROZEN
```

## Closure Records

- `docs/CORE_BATCH_01_TEST_MANIFEST.md`
- `docs/BUILDINGOS_CORE_BATCH_01_IMPLEMENTATION_SELF_REVIEW.md`
- `docs/BUILDINGOS_CORE_BATCH_01_ENGINEERING_REVIEW.md`
- `docs/BUILDINGOS_CORE_BATCH_01_BASELINE_INTEGRITY_CHECK.md`
- `docs/BUILDINGOS_CORE_BATCH_01_APPROVAL_RECORD.md`
- `docs/BUILDINGOS_CORE_BATCH_01_FREEZE_RECORD.md`

## Current Product Architecture Records

- `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`
- `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`
- `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`
- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

## Active Boundaries

The frozen Core Batch 01 and the current documentation planning do not authorize:

- production database;
- public API;
- production Operator Console;
- permissions and user management;
- workflow automation;
- automatic lifecycle transitions;
- autonomous decision-making or approval authority;
- PRI, MCP Runtime, generic agent runtime, QClaw, and n8n integration;
- application migration;
- automated ClimateOS-to-BuildingOS transfer;
- regulatory source connectors;
- legal, compliance, certification, contractual, engineering-signoff, or professional conclusions;
- live pilot activation;
- frozen Foundation or Core edits.

## Product North Star

The authoritative current product-direction record is:

- `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`

BuildingOS is being developed as an AI-native, evidence-driven, human-governed operating system for helping people progress built-environment and infrastructure projects through their full lifecycle with visible evidence, explicit claims, accountable review, and traceable decisions.

The architecture direction supports different project scales and types through a shared governance kernel, Project Genome, project-specific lifecycle graphs, domain capability packs, jurisdiction knowledge packs, evidence exchange contracts, tool adapters, and an adaptive human interface.

The North Star is a documentation baseline and does not authorize implementation.

## Cross-Domain Evidence Direction

The authoritative current ClimateOS handoff contract is:

- `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`

ClimateOS may contribute observations, climate-risk evidence, model outputs, sources, provenance, dates, methods, uncertainty, and authorised building, MEP, BIM, fixture, construction, commissioning, operations, and site-context evidence.

BuildingOS may register and organise these inputs as project evidence subject to human review.

ClimateOS conclusions, automated compliance decisions, approval authority, lifecycle control, runtime capability, and unsupported project claims must not be imported as BuildingOS decisions.

No connector, database, API, queue, webhook, MCP tool, agent runtime, permissions model, or automated transfer is authorised.

## S7 Sydney Candidate Direction

The current candidate profile is:

- `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`

The NEXTDC S7 Sydney project is treated only as a candidate large and complex project learning case for information architecture, project classification, lifecycle, MEP, BIM, construction, commissioning, operations, climate-risk, source-provenance, and regulatory-evidence planning.

Current status:

```text
CANDIDATE_LARGE_COMPLEX_PROJECT_LEARNING_CASE
NOT_APPROVED_AS_LIVE_BUILDINGOS_PILOT
NO_PROJECT_AUTHORITY
NO_CONFIDENTIAL_DATA_ACCESS
```

Public reporting and corporate statements must remain distinguished from official planning records, approved design, as-built condition, and operational evidence.

Critical-infrastructure, security-sensitive, confidential, personal, network, access-control, and protected operational information must not be placed in the public repository.

## Human Interface Direction

A future read-only BuildingOS Operator Console may provide human visibility through:

- Portfolio Console;
- Project Cockpit;
- Stage Workspace;
- Decision and Evidence Room;
- Evidence Desk;
- Claim Desk;
- Review Workspace;
- Lifecycle Board;
- Governance Ledger;
- Module Contract Registry.

Human Interface Architecture and a bounded documentation-only Operator Console Prototype Brief remain future roadmap deliverables.

Production UI implementation remains deferred until separate architecture review and explicit Chief Architect implementation approval.

## Future Regulatory and Knowledge Garden Planning

Planning record:

- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

The planned Regulatory Knowledge Layer preserves NCC source, version, edition, effective-date and jurisdiction context; referenced standards metadata and licensing boundaries; NSW legislation, regulation and planning-source context; jurisdictional variations; source-change tracking; applicability and compliance-related claims; and mandatory human review.

The Markdown-first Knowledge Garden model preserves:

- GitHub as the authoritative approved source;
- portable Markdown, stable filenames, indexes, and ordinary links;
- reviewable promotion of drafts;
- separation of private research from approved records;
- controlled synchronisation;
- no blind two-way folder sync;
- no copied shadow library of NCC, standards, legislation, paid databases, or other controlled material.

Planning status:

```text
PLANNING_BASELINE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION
```

This planning does not approve legal or certification advice, regulatory connectors, paid-standard duplication, automated compliance conclusions, or production interface work.

## Next Governed Planning Sequence

1. Define the BuildingOS Project Genome and Classification Standard.
2. Define the Lifecycle Stage Graph Architecture.
3. Define the Human Interface Architecture and bounded read-only Operator Console Prototype Brief.
4. Propose small, medium, and large pilot project candidates.
5. Continue Regulatory Knowledge Layer and Markdown-first Knowledge Garden planning without implementation.
6. Review the combined documentation package before any implementation authorization.

## Decisions Requiring Chief Architect Review

Routine documentation may proceed within the above sequence.

Return to the Chief Architect before:

- materially changing BuildingOS product scope;
- changing the BuildingOS–PRI–ClimateOS architecture boundary;
- selecting or activating a live pilot project;
- asserting legal, compliance, certification, contractual, statutory, engineering-signoff, or professional authority;
- authorizing implementation code for the next milestone;
- modifying the frozen Foundation or Core Batch 01 baseline;
- introducing a database, public API, permissions, automated workflow, external connector, production UI, or autonomous approval capability.

## Current Blockers

No blocker prevents the next documentation-only roadmap item.

The official local workspace `D:\Codex\BuildingOS` was not independently inspected during the GitHub connector run. GitHub `main` remains the source of truth, and the local workspace should pull the latest commits before local work resumes.

## Safe Re-entry Point

Continue from:

`PROJECT_GENOME_AND_CLASSIFICATION_STANDARD_PLANNING`

Read first:

1. `PROJECT_CONTEXT.md`
2. `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`
3. `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`
4. `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`
5. `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

Do not modify the frozen Foundation or Core Batch 01 baseline without formal Change Request governance.

## Context Protocol

Every major milestone, repository transition, workspace transition, or long-thread closure must update this file and create a context transfer packet when needed.