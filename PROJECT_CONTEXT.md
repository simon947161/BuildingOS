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

## Source of Truth

GitHub `main` is the authoritative approved source.

The official local workspace must be freshly fetched and verified before non-trivial work.

Required local preflight:

```text
git fetch origin main
git status --short --branch
git rev-list --left-right --count HEAD...origin/main
git log -1 --format="%H%n%ci%n%s"
git log -1 --format="%H%n%ci%n%s" origin/main
```

If local and `origin/main` diverge, stop and inspect both sides. Do not push from a diverged state.

Local divergence retrospective:

- `docs/BUILDINGOS_LOCAL_DIVERGENCE_RETROSPECTIVE_ADDENDUM.md`

## Current Phase

`POST_FREEZE_RKL_2_BRIEF_REVIEW_COMPLETE_CHIEF_ARCHITECT_RECORD_SET_DECISION_GATE`

## Current Milestone

RKL-2 fictional documentation demonstration planning has been approved. The RKL-2 brief has been prepared and reviewed. Creation of the complete fictional Markdown record set now requires a separate Chief Architect decision.

## Current Status

`RKL_2_BRIEF_REVIEW_PASS_NO_RECORD_SET_OR_IMPLEMENTATION_AUTHORIZATION`

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

Changes to a frozen baseline require:

```text
Change Request
→ Engineering Review
→ Architecture Review when required
→ Chief Architect Approval
→ Updated Freeze Record
```

## Core Verification State

```text
Ran 34 tests
OK

Workflow: Core Batch 01
Run ID: 29159400862
Run number: 11
Job: test
Conclusion: success

Engineering review: PASS
Baseline integrity: VERIFIED_IMPLEMENTATION_BASELINE_UNCHANGED
Freeze: CORE_BATCH_01_FROZEN
```

## Completed Product Architecture and Documentation Gates

- BuildingOS Product North Star prepared.
- ClimateOS-to-BuildingOS Cross-Domain Evidence Intake Contract prepared.
- NEXTDC S7 Sydney candidate evidence profile prepared.
- Project Genome and Classification Standard prepared.
- Lifecycle Stage Graph Architecture prepared.
- Human Interface Architecture prepared.
- Read-Only Operator Console Prototype Brief prepared.
- Small, medium, and large or complex pilot candidates proposed without selection or activation.
- Post-Freeze Documentation Architecture Review completed with PASS.
- Regulatory Knowledge Layer and Knowledge Garden planning baseline prepared.
- RKL-1 Source Governance and Information Architecture prepared.
- RKL-1 Documentation Review completed with PASS.
- RKL-1 canonical source-status and public/restricted-locator corrections applied.
- RKL-1 bounded corrections independently verified.
- RKL-2 fictional documentation demonstration planning approved by the Chief Architect on 2026-07-16.
- RKL-2 Fictional Documentation Demonstration Brief prepared.
- RKL-2 Brief Review completed with PASS.

All post-freeze work remains documentation-only. Frozen Core source, tests, workflow, and Foundation records were not modified.

## Current Product Architecture Records

- `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`
- `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`
- `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`
- `docs/BUILDINGOS_PROJECT_GENOME_AND_CLASSIFICATION_STANDARD.md`
- `docs/BUILDINGOS_LIFECYCLE_STAGE_GRAPH_ARCHITECTURE.md`
- `docs/BUILDINGOS_HUMAN_INTERFACE_ARCHITECTURE.md`
- `docs/BUILDINGOS_READ_ONLY_OPERATOR_CONSOLE_PROTOTYPE_BRIEF.md`
- `docs/BUILDINGOS_PILOT_CANDIDATE_PLAN.md`
- `docs/BUILDINGOS_POST_FREEZE_DOCUMENTATION_ARCHITECTURE_REVIEW.md`
- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`
- `docs/BUILDINGOS_RKL_1_SOURCE_GOVERNANCE_AND_INFORMATION_ARCHITECTURE.md`
- `docs/BUILDINGOS_RKL_1_DOCUMENTATION_REVIEW.md`
- `docs/BUILDINGOS_RKL_1_BOUNDED_CORRECTION_VERIFICATION.md`
- `docs/BUILDINGOS_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_APPROVAL_RECORD.md`
- `docs/BUILDINGOS_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_BRIEF.md`
- `docs/BUILDINGOS_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_BRIEF_REVIEW.md`

## Product Direction

BuildingOS is an AI-native, evidence-driven, human-governed operating system for helping people progress built-environment and infrastructure projects through their full lifecycle with visible evidence, explicit claims, accountable review, and traceable decisions.

It supports different project scales through one frozen Governance Kernel, Project Genome, project-specific Lifecycle Stage Graphs, evidence exchange contracts, human-interface surfaces, and future domain and jurisdiction knowledge packs.

## Cross-Domain Evidence Boundary

ClimateOS may contribute source, provenance, site, climate-risk, building, MEP, BIM, fixture, construction, commissioning, operations, and environmental evidence.

ClimateOS conclusions, approval recommendations presented as decisions, compliance conclusions, lifecycle control, runtime authority, and unsupported project claims must not be imported as BuildingOS decisions.

## S7 Candidate Boundary

S7 remains:

```text
CANDIDATE_LARGE_COMPLEX_PROJECT_LEARNING_CASE
DOCUMENTATION_LEARNING_CASE
NOT_APPROVED_AS_LIVE_BUILDINGOS_PILOT
NO_PROJECT_AUTHORITY
NO_CONFIDENTIAL_DATA_ACCESS
```

Public reporting must remain distinguishable from official planning records, approved design, as-built condition, and operational evidence.

Critical-infrastructure, network, access-control, vulnerability, customer, confidential, and protected operational information must not be placed in the public repository.

## Project Genome and Lifecycle

Internal operating scales:

- `BOS-S` — small;
- `BOS-M` — medium;
- `BOS-LC` — large or complex.

Provisional governance depths:

- `GD-1` — compact;
- `GD-2` — coordinated;
- `GD-3` — enhanced;
- `GD-4` — major or high-consequence.

These labels are internal planning aids and must not be confused with NCC building classes, statutory classifications, approvals, certification, or professional opinions.

Lifecycle rule:

```text
The graph describes possible and recorded progression.
Evidence supports claims.
Humans review and decide.
No node or edge moves itself.
```

## Human Interface Direction

Primary surfaces:

- Portfolio Console;
- Project Cockpit;
- Stage Workspace;
- Decision and Evidence Room.

Supporting surfaces:

- Evidence Desk;
- Claim Desk;
- Review Workspace;
- Lifecycle Board;
- Governance Ledger View;
- Module Contract Registry.

The first prototype boundary remains read-only, non-production, non-operational, fictional or approved-public-information only, and not authorised for implementation.

## Pilot Candidate Direction

Candidate set:

- `S-01` — Tumut small building adaptation and secondary-dwelling concept candidate;
- `S-02` — fictional small community asset documentation learning case;
- `M-01` — Batlow community energy and resilience hub concept candidate;
- `M-02` — fictional regional community facility retrofit documentation learning case;
- `LC-01` — NEXTDC S7 Sydney public-information documentation learning case;
- `LC-02` — fictional major regional infrastructure programme documentation learning case.

Current decision:

```text
SMALL_MEDIUM_LARGE_PILOT_CANDIDATES_PROPOSED
NO_CANDIDATE_SELECTED
NO_LIVE_PILOT_AUTHORIZED
NO_IMPLEMENTATION_AUTHORIZATION
```

## Regulatory Knowledge Layer

RKL-1 preserves:

- Australian NCC source, edition, volume, amendment, adoption, commencement, transition, effective-date, and jurisdiction context;
- referenced standards identifiers, editions, relationships, access, copyright, and licensing boundaries;
- NSW Acts, regulations, environmental planning instruments, approval records, authority guidance, and version status;
- Commonwealth, state, territory, and local jurisdictional variations;
- source change and supersession tracking;
- project-specific applicability and compliance-related claims;
- visible assumptions, limitations, unresolved questions, and re-review triggers;
- mandatory attributed human review.

BuildingOS may organise and support review. It must not determine legal applicability, certify compliance, replace an authority, or provide legal or certification advice.

## RKL-2 Current Boundary

Chief Architect decision recorded on 2026-07-16:

```text
APPROVE_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_BRIEF
```

RKL-2 brief review decision:

```text
RKL_2_FICTIONAL_DEMONSTRATION_BRIEF_REVIEW_PASS
RKL_1_SOURCE_GOVERNANCE_BOUNDARIES_PRESERVED
FICTIONAL_AND_NON_ADVISORY_BOUNDARY_PRESERVED
KNOWLEDGE_GARDEN_COMPATIBILITY_PRESERVED
FROZEN_FOUNDATION_AND_CORE_PRESERVED
NO_IMPLEMENTATION_AUTHORIZATION
READY_FOR_CHIEF_ARCHITECT_RECORD_SET_DECISION
```

The brief uses one entirely fictional project context:

```text
DEMO-RKL2-001
Fictional Regional Community Facility Retrofit
Fictional locality, New South Wales
```

No complete RKL-2 fictional record set has been created.

No real NCC, standard, NSW legislative, approval, certification, or project content is authorised.

## Markdown-First Knowledge Garden Compatibility

The Knowledge Garden model preserves:

- GitHub `main` as the authoritative approved source;
- portable Markdown and stable filenames;
- ordinary links, backlinks, indexes, and maps of content readable outside Obsidian;
- reviewable promotion of drafts;
- separation of private research from approved project records;
- controlled synchronisation;
- no blind two-way folder sync;
- no copied shadow library of NCC, standards, legislation, paid databases, confidential project files, or security-sensitive material.

Official publishers and authorised project systems remain authoritative for controlled source content.

## Active Boundaries

The frozen Core Batch 01 and current documentation records do not authorize:

- production database;
- public API;
- prototype or production UI implementation;
- permissions and user management;
- workflow automation;
- automatic lifecycle transitions;
- autonomous decision-making or approval authority;
- PRI, MCP Runtime, generic agent runtime, QClaw, or n8n integration;
- application migration;
- automated ClimateOS-to-BuildingOS transfer;
- regulatory source connectors, web scraping, or automated monitoring;
- legal, compliance, certification, contractual, statutory, engineering-signoff, safety, planning-approval, or professional conclusions;
- live pilot selection or activation;
- real S7 regulatory use;
- confidential, critical-infrastructure, personal, licensed, paid, or security-sensitive publication;
- frozen Foundation or Core edits;
- implementation code for RKL-2.

## Next Chief Architect Decision Gate

The next non-routine decision is:

```text
APPROVE_RKL_2_FICTIONAL_DOCUMENTATION_RECORD_SET
```

That decision would authorise only creation of the bounded fictional Markdown record set described by the RKL-2 brief and review conditions.

It would not authorise real sources, real project use, implementation code, database, API, connectors, monitoring, workflow, permissions, runtime, UI, pilot activation, legal advice, certification conclusions, or frozen baseline changes.

Other available Chief Architect paths remain:

- revise the RKL-2 brief;
- reject RKL-2 and return to the RKL-1 gate;
- select one pilot candidate for a formal Candidate Selection Record without implementation or activation;
- authorize preparation of a bounded implementation brief only without code;
- pause BuildingOS at the current verified state.

## Decisions Requiring Chief Architect Review

Chief Architect review is required before:

- creating the complete RKL-2 fictional demonstration record set;
- selecting or activating a live pilot;
- approving real project data use;
- materially changing BuildingOS product scope;
- changing the BuildingOS–ClimateOS–PRI architecture boundary;
- authorizing implementation code or production design;
- modifying frozen Foundation or Core;
- introducing a database, public API, permissions, workflow, external connector, production UI, application migration, runtime, or autonomous approval capability;
- asserting legal, compliance, certification, contractual, statutory, engineering-signoff, safety, planning-approval, or professional authority;
- using confidential, critical-infrastructure, licensed, personal, paid, or protected operational data.

## Safe Re-entry Point

Continue from:

`POST_RKL_2_BRIEF_REVIEW_CHIEF_ARCHITECT_RECORD_SET_DECISION_GATE`

Read first:

1. `PROJECT_CONTEXT.md`
2. `docs/BUILDINGOS_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_APPROVAL_RECORD.md`
3. `docs/BUILDINGOS_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_BRIEF.md`
4. `docs/BUILDINGOS_RKL_2_FICTIONAL_DOCUMENTATION_DEMONSTRATION_BRIEF_REVIEW.md`
5. `docs/BUILDINGOS_RKL_1_SOURCE_GOVERNANCE_AND_INFORMATION_ARCHITECTURE.md`
6. `docs/BUILDINGOS_RKL_1_DOCUMENTATION_REVIEW.md`
7. `docs/BUILDINGOS_RKL_1_BOUNDED_CORRECTION_VERIFICATION.md`

Do not create the complete fictional record set before Chief Architect approval.

Do not modify the frozen Foundation or Core Batch 01 baseline without formal Change Request governance.

## Context Protocol

Every major milestone, repository transition, workspace transition, or long-thread closure must update this file and create a context transfer packet when needed.
