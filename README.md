# BuildingOS

**Reality Operating System for Infrastructure Governance**

**One governance framework. Many infrastructure applications.**

BuildingOS is an open infrastructure governance framework for connecting project intelligence, procedures, evidence, expert review, ledgers, lifecycle visibility, and human decision support across the full lifecycle of built-environment and infrastructure projects.

It is designed to bridge planning, design, approvals, financing, procurement, construction, commissioning, handover, operation, adaptation, and end-of-life governance. BuildingOS does not replace architects, engineers, planners, builders, certifiers, lawyers, owners, operators, regulators, or community decision processes. It provides a structured governance layer so project evidence, claims, reviews, and decisions can remain visible and traceable.

## Official Repository

```text
https://github.com/simon947161/BuildingOS.git
```

## Source of Truth

GitHub `main` is the authoritative approved project record.

The official local workspace is:

```text
D:\Codex\BuildingOS
```

Read `PROJECT_CONTEXT.md` before continuing project work.

## Platform Shape

```text
BuildingOS
|
|-- Climate Adaptation Applications
|   `-- Wagga ClimateOS
|
|-- Infrastructure Governance Applications
|   `-- PPP / BOT Governance
|
|-- Building Technology Applications
|   `-- Modular Building Interface
|
`-- Community Infrastructure Applications
    `-- Community Lighthouse
```

These are ecosystem directions and candidate applications. They are not automatically authorised live BuildingOS pilots.

## Core Idea

Traditional project delivery often separates planning, finance, design, construction, operation, and audit into different documents, teams, and timelines.

BuildingOS treats infrastructure governance as a continuous human-governed process:

```text
Source and Evidence
→ Claim
→ Review
→ Authorised Human Decision
→ Recorded Lifecycle Event
→ Governance Ledger
```

The goal is not merely to manage tasks. It is to make the evidence, assumptions, procedures, reviews, decisions, changes, and lifecycle history that support project delivery easier to organise, inspect, challenge, and govern.

## Current Product Architecture

```text
Product North Star
→ Governance Kernel
→ Project Genome
→ Lifecycle Stage Graph
→ Evidence Exchange Contracts
→ Human Interface Architecture
→ Regulatory and Jurisdiction Knowledge Planning
→ Candidate Pilot Evaluation
```

The first human-interface direction is read-only and documentation-led.

## Frozen Governance Kernel

BuildingOS M1 Specification Foundation is complete and frozen.

The frozen baseline includes:

- C00 Glossary Foundation v1.0;
- C01-A Evidence Standard v1.0;
- C01-B Claim Standard v1.0;
- C01-C Identity Standard v1.0;
- C01-D Review Standard v1.0;
- C01-E Procedure Standard v1.0;
- C01-F Lifecycle Standard v1.0;
- C01-G Registered Object Standard v1.0;
- C01-H Governance Ledger Standard v1.0;
- C01-I Module Contract Standard v1.0.

Core Batch 01 is formally frozen at:

```text
f84b22bf4921e4f98e15598c5c5a5aa18bcaa996
```

Verified evidence:

```text
34 tests: OK
GitHub Actions run 29159400862: success
Engineering review: PASS
Baseline integrity: VERIFIED_IMPLEMENTATION_BASELINE_UNCHANGED
Freeze: CORE_BATCH_01_FROZEN
```

Frozen records must not be silently edited. Changes require documented change governance and Chief Architect approval.

## Implemented Core Scope

The minimum representational Governance Kernel currently includes:

- Actor;
- Evidence;
- Claim;
- Review without decision authority;
- Procedure without execution;
- Lifecycle without automatic transition;
- Registered Object;
- Governance Ledger Entry;
- Module Contract;
- Conformance Result;
- deterministic conformance and cross-object checks;
- fictional fixtures and regression tests.

The frozen Core does not include production workflow, permissions, database, API, autonomous decisions, regulatory connectors, or production UI.

## Start Here

### Project Passport

- `PROJECT_CONTEXT.md`

### Frozen Foundation and Core

- `docs/BUILDINGOS_SPECIFICATION_INDEX.md`
- `docs/BUILDINGOS_SPECIFICATION_DEPENDENCY_MAP.md`
- `docs/BUILDINGOS_SPECIFICATION_CHANGELOG.md`
- `docs/BUILDINGOS_CORE_BATCH_01_APPROVAL_RECORD.md`
- `docs/BUILDINGOS_CORE_BATCH_01_FREEZE_RECORD.md`

### Current Product Architecture

- `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`
- `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`
- `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`
- `docs/BUILDINGOS_PROJECT_GENOME_AND_CLASSIFICATION_STANDARD.md`
- `docs/BUILDINGOS_LIFECYCLE_STAGE_GRAPH_ARCHITECTURE.md`
- `docs/BUILDINGOS_HUMAN_INTERFACE_ARCHITECTURE.md`
- `docs/BUILDINGOS_READ_ONLY_OPERATOR_CONSOLE_PROTOTYPE_BRIEF.md`
- `docs/BUILDINGOS_PILOT_CANDIDATE_PLAN.md`
- `docs/BUILDINGOS_POST_FREEZE_DOCUMENTATION_ARCHITECTURE_REVIEW.md`

### Regulatory Knowledge and Knowledge Garden

- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`
- `docs/BUILDINGOS_RKL_1_SOURCE_GOVERNANCE_AND_INFORMATION_ARCHITECTURE.md`
- `docs/BUILDINGOS_RKL_1_DOCUMENTATION_ARCHITECTURE_REVIEW.md`
- `docs/BUILDINGOS_RKL_1_DOCUMENTATION_REVIEW.md`
- `docs/BUILDINGOS_RKL_1_BOUNDED_CORRECTION_VERIFICATION.md`

The detailed RKL-1 Documentation Architecture Review is the canonical RKL-1 review. The shorter Documentation Review remains supplemental.

## Human Interface Direction

The documentation architecture defines:

- Portfolio Console;
- Project Cockpit;
- Stage Workspace;
- Decision and Evidence Room;
- Evidence Desk;
- Claim Desk;
- Review Workspace;
- Lifecycle Board;
- Governance Ledger View;
- Module Contract Registry.

No frontend, backend, production UI, permissions, database, workflow, or live-project action is authorised.

## Regulatory Knowledge Direction

The future Regulatory Knowledge Layer is planned to preserve:

- Australian NCC edition, volume, amendment, adoption, commencement, transition, effective date, and jurisdiction context;
- referenced standards identifiers, editions, relationships, access, copyright, and licensing boundaries;
- NSW legislation, regulations, environmental planning instruments, approval records, authority guidance, and version status;
- Commonwealth, state, territory, and local variations;
- source change and supersession;
- project-specific applicability and compliance-related claims;
- mandatory human review and re-review triggers.

RKL-1 now has one canonical source-status vocabulary and distinguishes public official URLs from authorised or restricted source locators, access boundaries, and metadata-only storage policies.

BuildingOS is decision support and recordkeeping. It is not legal or certification advice.

## Markdown-First Knowledge Garden

Approved records remain portable Markdown in GitHub.

The Obsidian or Knowledge Garden direction uses:

- GitHub `main` as source of truth;
- stable filenames and record IDs;
- ordinary Markdown links, backlinks, indexes, and maps of content;
- reviewable draft promotion;
- controlled synchronisation;
- separation of private research and approved records;
- no blind two-way sync;
- no shadow copying of NCC, standards, legislation, paid databases, confidential project files, or security-sensitive material.

## Pilot Candidate Direction

Small, medium, and large or complex candidates have been proposed for future review.

Current decision:

```text
NO_CANDIDATE_SELECTED
NO_LIVE_PILOT_AUTHORIZED
NO_IMPLEMENTATION_AUTHORIZATION
```

NEXTDC S7 Sydney remains a candidate large and complex public-information learning case only. It is not an approved live BuildingOS implementation.

## Current Governed Roadmap

| Gate | Status |
| --- | --- |
| M1 Specification Foundation | Frozen |
| Core Batch 01 | Verified and frozen |
| Product North Star | Documentation baseline prepared |
| ClimateOS evidence intake contract | Documentation contract prepared |
| Project Genome | Documentation standard prepared |
| Lifecycle Stage Graph | Documentation architecture prepared |
| Human Interface Architecture | Documentation architecture prepared |
| Read-only Operator Console brief | Documentation brief prepared; no implementation |
| Pilot candidate plan | Candidates proposed; none selected |
| Post-freeze documentation review | PASS |
| RKL-1 source governance architecture | Prepared, reviewed, corrected, and verified |
| RKL-2 fictional demonstration | Not authorised; Chief Architect gate required |
| Prototype or production implementation | Not authorised |

## Active Boundaries

BuildingOS currently does not authorize:

- PRI, MCP Runtime, generic agent runtime, QClaw, or n8n integration;
- production database;
- public API;
- permissions or user management;
- workflow automation;
- automatic lifecycle transitions;
- autonomous approval or decision-making;
- production Operator Console;
- regulatory source connectors, web scraping, or automated monitoring;
- application migration;
- legal, compliance, certification, contractual, statutory, engineering-signoff, safety, planning-approval, or professional conclusions;
- live pilot selection or activation;
- modification of frozen Foundation or Core without formal change governance.

## Applications

BuildingOS is the parent infrastructure governance framework. Possible applications or learning cases include:

- [Wagga ClimateOS](https://github.com/simon947161/wagga-climate-os): regional climate adaptation, planning intelligence, and resilience prototype for Wagga Wagga and the Riverina;
- [Wagga ClimateOS public demo](https://simon947161.github.io/wagga-climate-os/): current public demonstration for the Wagga and Riverina climate adaptation prototype;
- Modular Building Interface: micro-scale building component and interface governance direction;
- PPP / BOT Governance: macro-scale infrastructure procedure, evidence, and delivery governance direction;
- Community Lighthouse: community-scale energy, shelter, resilience, and local infrastructure concept.

These relationships do not transfer decision authority or automatically activate BuildingOS pilots.

## Positioning

BuildingOS is not a conventional BIM platform, project management app, consulting report system, legal service, certifier, or autonomous workflow engine.

It is an evidence-driven, human-governed infrastructure and built-environment governance framework.

```text
Evidence supports Claims.
Claims receive Review.
Authorised Humans decide.
Lifecycle history preserves accountability.
```

## Project Status

```text
CORE_BATCH_01_FROZEN
POST_FREEZE_DOCUMENTATION_ARCHITECTURE_REVIEW_PASS
RKL_1_DOCUMENTATION_ARCHITECTURE_REVIEW_PASS
RKL_1_BOUNDED_DOCUMENTATION_CORRECTIONS_VERIFIED
NO_LIVE_PILOT_SELECTED
NO_IMPLEMENTATION_AUTHORIZATION
```

The next non-routine gate is:

```text
APPROVE_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_BRIEF
```

That gate would permit only a fictional, non-advisory Markdown demonstration set. It would not authorize live source ingestion, connectors, monitoring, database, API, permissions, workflow, production UI, legal conclusions, certification conclusions, pilot activation, or implementation code.

## License

To be confirmed.

Apache-2.0 remains recommended for future enterprise-friendly open collaboration, subject to formal repository licensing decision.