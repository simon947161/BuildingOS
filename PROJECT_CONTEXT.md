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

`POST_CORE_BATCH_01_PRODUCT_ARCHITECTURE_PLANNING`

## Current Milestone

BuildingOS Product North Star, cross-domain evidence intake, project classification, lifecycle architecture, and human-interface planning.

## Current Status

`CORE_BATCH_01_FROZEN_READY_FOR_NEXT_PLANNING_BATCH`

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

## Active Boundaries

The frozen Core Batch 01 excludes and does not authorize:

- production database;
- public API;
- production Operator Console;
- permissions and user management;
- workflow automation;
- automatic lifecycle transitions;
- autonomous decision-making or approval authority;
- PRI, MCP Runtime, generic agent runtime, QClaw, and n8n integration;
- application migration;
- regulatory source connectors;
- legal, compliance, certification, or professional conclusions;
- frozen Foundation edits.

## Product Direction

BuildingOS is being developed as an AI-native, evidence-driven, human-governed operating system for progressing built-environment and infrastructure projects through planning, design, approvals, procurement, construction, commissioning, handover, operation, maintenance, adaptation, and end-of-life activities.

The next architecture must support different project scales and types through a shared governance kernel, Project Genome, project-specific lifecycle graphs, domain capability packs, jurisdiction knowledge packs, tool adapters, and an adaptive human interface.

## Cross-Domain Evidence Direction

A documentation-only ClimateOS-to-BuildingOS evidence intake contract is planned.

ClimateOS may contribute observations, climate-risk evidence, model outputs, sources, provenance, dates, methods, and uncertainty. BuildingOS may register and organise these as project evidence subject to human review.

ClimateOS conclusions, automated compliance decisions, approval authority, and unsupported project claims must not be imported as BuildingOS decisions.

The NEXTDC S7 Sydney project may be treated as a candidate large and complex project evidence case for learning about data-centre buildings, MEP systems, BIM, fixtures, construction, commissioning, operations, site context, climate risk, source provenance, and regulatory interfaces. It is not yet an approved live BuildingOS implementation.

## Human Interface Direction

A future read-only BuildingOS Operator Console may provide Mission Control-style human visibility through:

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

A bounded documentation-only Operator Console Prototype Brief may now be prepared.

Production UI implementation remains deferred until separate architecture review and explicit Chief Architect implementation approval.

## Future Regulatory and Knowledge Garden Planning

Planning record:

- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

The plan preserves a future Regulatory Knowledge Layer covering NCC source/version/effective-date context, referenced standards, NSW legislation and regulations, jurisdictional variations, applicability and compliance-related claims, source change tracking, and mandatory human review.

It also records a Markdown-first Obsidian/Knowledge Garden compatibility model in which GitHub remains the authoritative source, portable links and indexes are preferred, synchronisation is controlled, and authoritative legal or standards content is not duplicated without permission.

Planning status:

```text
PLANNING_BASELINE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION
```

This planning does not approve legal or certification advice, regulatory connectors, paid-standard duplication, or automated compliance conclusions.

## Next Governed Planning Sequence

1. Create or refine the BuildingOS Product North Star.
2. Define the ClimateOS-to-BuildingOS Cross-Domain Evidence Intake Contract.
3. Prepare an S7 Sydney candidate large-project evidence intake profile.
4. Define the Project Genome and Classification Standard.
5. Define the Lifecycle Stage Graph Architecture.
6. Define the Human Interface Architecture and bounded read-only Operator Console Prototype Brief.
7. Propose small, medium, and large pilot projects.
8. Continue Regulatory Knowledge Layer and Markdown-first Knowledge Garden planning without implementation.

## Decisions Requiring Chief Architect Review

Routine documentation may proceed within the above sequence.

Return to the Chief Architect before:

- materially changing BuildingOS product scope;
- changing the BuildingOS–PRI–ClimateOS architecture boundary;
- selecting or activating a live pilot project;
- asserting legal, compliance, certification, contractual, or professional authority;
- authorizing implementation code for the next milestone;
- introducing a database, public API, permissions, automated workflow, external connector, production UI, or autonomous approval capability.

## Safe Re-entry Point

Continue from:

`POST_CORE_BATCH_01_PRODUCT_NORTH_STAR_AND_EVIDENCE_INTAKE_PLANNING`

Do not modify the frozen Foundation or Core Batch 01 baseline without formal Change Request governance.

## Context Protocol

Every major milestone, repository transition, workspace transition, or long-thread closure must update this file and create a context transfer packet when needed.