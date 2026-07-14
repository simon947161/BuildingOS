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

`POST_CORE_BATCH_01_COMBINED_DOCUMENTATION_REVIEW`

## Current Milestone

Review the completed post-freeze product architecture and pilot-candidate documentation package before any pilot selection or implementation authorization.

## Current Status

`ROADMAP_DOCUMENTATION_BASELINES_COMPLETE_READY_FOR_COMBINED_REVIEW`

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

Changes to any frozen baseline require:

```text
Change Request
→ Engineering Review
→ Architecture Review when required
→ Chief Architect Approval
→ Updated Freeze Record
```

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
- BuildingOS Project Genome and Classification Standard prepared.
- BuildingOS Lifecycle Stage Graph Architecture prepared.
- BuildingOS Human Interface Architecture prepared.
- Read-Only Operator Console Prototype Brief prepared.
- Small, medium, and large or complex pilot candidates proposed without selection or activation.
- Regulatory Knowledge Layer and Knowledge Garden planning status refreshed after Core freeze.

## Implementation and Test Artifacts

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

All post-freeze roadmap work through the pilot-candidate plan is documentation-only. It did not modify frozen Core source, tests, workflows, or Foundation records.

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
- `docs/BUILDINGOS_PROJECT_GENOME_AND_CLASSIFICATION_STANDARD.md`
- `docs/BUILDINGOS_LIFECYCLE_STAGE_GRAPH_ARCHITECTURE.md`
- `docs/BUILDINGOS_HUMAN_INTERFACE_ARCHITECTURE.md`
- `docs/BUILDINGOS_READ_ONLY_OPERATOR_CONSOLE_PROTOTYPE_BRIEF.md`
- `docs/BUILDINGOS_PILOT_CANDIDATE_PLAN.md`
- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

## Active Boundaries

The frozen Core Batch 01 and current documentation planning do not authorize:

- production database;
- public API;
- production Operator Console;
- prototype frontend or backend implementation;
- permissions and user management;
- workflow automation;
- automatic lifecycle transitions;
- autonomous decision-making or approval authority;
- PRI, MCP Runtime, generic agent runtime, QClaw, and n8n integration;
- application migration;
- automated ClimateOS-to-BuildingOS transfer;
- regulatory source connectors;
- legal, compliance, certification, contractual, statutory, engineering-signoff, safety, planning-approval, or professional conclusions;
- live pilot selection or activation;
- confidential, critical-infrastructure, personal, licensed, or security-sensitive publication;
- frozen Foundation or Core edits.

## Product North Star

Authoritative record:

- `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`

BuildingOS is being developed as an AI-native, evidence-driven, human-governed operating system for helping people progress built-environment and infrastructure projects through their full lifecycle with visible evidence, explicit claims, accountable review, and traceable decisions.

The architecture direction supports different project scales and types through a shared Governance Kernel, Project Genome, project-specific Lifecycle Stage Graphs, domain capability packs, jurisdiction knowledge packs, evidence exchange contracts, tool adapters, and an adaptive human interface.

The North Star is a documentation baseline and does not authorize implementation.

## Cross-Domain Evidence Direction

Authoritative record:

- `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`

ClimateOS may contribute observations, climate-risk evidence, model outputs, sources, provenance, dates, methods, uncertainty, and authorised building, MEP, BIM, fixture, construction, commissioning, operations, and site-context evidence.

BuildingOS may register and organise eligible inputs as project evidence subject to human review.

ClimateOS conclusions, automated compliance decisions, approval authority, lifecycle control, runtime capability, and unsupported project claims must not be imported as BuildingOS decisions.

No connector, database, API, queue, webhook, MCP tool, agent runtime, permissions model, or automated transfer is authorised.

## S7 Sydney Candidate Direction

Current candidate profile:

- `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`

S7 is treated only as a candidate large and complex public-information learning case for information architecture, project classification, lifecycle, MEP, BIM, construction, commissioning, operations, climate-risk, source-provenance, and regulatory-evidence planning.

Current status:

```text
CANDIDATE_LARGE_COMPLEX_PROJECT_LEARNING_CASE
DOCUMENTATION_LEARNING_CASE
NOT_APPROVED_AS_LIVE_BUILDINGOS_PILOT
NO_PROJECT_AUTHORITY
NO_CONFIDENTIAL_DATA_ACCESS
```

Public reporting and corporate statements must remain distinguished from official planning records, approved design, as-built condition, and operational evidence.

Critical-infrastructure, security-sensitive, confidential, personal, network, access-control, and protected operational information must not be placed in the public repository.

## Project Genome Direction

Authoritative record:

- `docs/BUILDINGOS_PROJECT_GENOME_AND_CLASSIFICATION_STANDARD.md`

The Project Genome is a versioned, evidence-linked description of a project, programme, site, asset, or bounded work package. It records project identity, boundary, typology, internal operating scale, jurisdiction context, lifecycle position, systems, stakeholders, complexity, evidence burden, governance depth, capability needs, security constraints, uncertainty, and escalation triggers.

BuildingOS internal operating-scale classes:

- `BOS-S` — small;
- `BOS-M` — medium;
- `BOS-LC` — large or complex.

Provisional governance depths:

- `GD-1` — compact;
- `GD-2` — coordinated;
- `GD-3` — enhanced;
- `GD-4` — major or high-consequence.

These are internal planning labels. They must not be confused with NCC building classes, planning categories, legal classifications, certification states, professional opinions, or approval decisions.

## Lifecycle Stage Graph Direction

Authoritative record:

- `docs/BUILDINGOS_LIFECYCLE_STAGE_GRAPH_ARCHITECTURE.md`

A Lifecycle Stage Graph is a versioned, project-specific governance map of stage nodes, transition edges, entry and exit criteria, evidence, claims, reviews, authorised human decisions, hold points, branches, parallel paths, partial completion, re-entry, correction, supersession, and traceable history.

Governing rule:

```text
The graph describes possible and recorded progression.
Evidence supports claims.
Humans review and decide.
No node or edge moves itself.
```

The architecture supports `BOS-S`, `BOS-M`, and `BOS-LC` projects without forcing identical process weight.

No executable transition, workflow, permission, or automatic lifecycle movement is authorized.

## Human Interface Direction

Authoritative records:

- `docs/BUILDINGOS_HUMAN_INTERFACE_ARCHITECTURE.md`
- `docs/BUILDINGOS_READ_ONLY_OPERATOR_CONSOLE_PROTOTYPE_BRIEF.md`

Defined primary surfaces:

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

The interface direction is evidence-linked, lifecycle-aware, human-governed, uncertainty-visible, repository-traceable, and read-only at the first prototype boundary.

The prototype brief permits documentation and design planning only. No frontend, backend, production UI, database, permissions, workflow, connector, or live-project action is authorized.

## Pilot Candidate Direction

Authoritative record:

- `docs/BUILDINGOS_PILOT_CANDIDATE_PLAN.md`

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

The safest future demonstration sequence is fictional `BOS-S`, fictional `BOS-M`, then S7 public-information `BOS-LC` structure learning, followed by review before any real pilot selection.

## Future Regulatory Knowledge Layer

Planning record:

- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

Planning status:

```text
PLANNING_BASELINE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION
STATUS_REFRESHED_2026_07_14
```

The planned Regulatory Knowledge Layer preserves:

- Australian NCC source, edition, volume, amendment, adoption, commencement, effective-date, and jurisdiction context;
- referenced standards identifiers, editions, relationships, access, and licensing boundaries;
- NSW legislation, regulations, environmental planning instruments, approval records, authority guidance, and version status;
- Commonwealth, state, territory, and local jurisdictional variations;
- source-change and supersession tracking;
- project-specific applicability and compliance-related claims;
- visible assumptions, limitations, unresolved questions, and re-review triggers;
- mandatory attributed human review.

BuildingOS may organise and support review. It must not determine legal applicability, certify compliance, replace an authority, or provide legal or certification advice.

The next possible regulatory deliverable is a documentation-only RKL-1 Source Governance and Information Architecture brief after review of the combined package.

## Markdown-First Knowledge Garden Compatibility

The Knowledge Garden model preserves:

- GitHub `main` as the authoritative approved source;
- portable Markdown and stable filenames;
- ordinary links, backlinks, indexes, and maps of content that remain readable outside Obsidian;
- reviewable promotion of drafts through branches, diffs, pull requests, or equivalent recorded review;
- separation of private research from approved project records;
- controlled synchronisation;
- no blind two-way folder sync;
- no copied shadow library of NCC material, referenced standards, legislation, paid legal databases, confidential project files, or security-sensitive material.

Official publishers and authorised project systems remain authoritative for controlled source content.

## Combined Documentation Review Scope

The next review should assess the package as one architecture chain:

```text
Product North Star
→ Cross-Domain Evidence Intake
→ S7 Candidate Evidence Profile
→ Project Genome
→ Lifecycle Stage Graph
→ Human Interface Architecture
→ Read-Only Prototype Brief
→ Pilot Candidate Plan
→ Regulatory Knowledge and Knowledge Garden Boundaries
```

Review questions:

1. Are product scope and architecture boundaries coherent?
2. Do Project Genome, lifecycle, interface, and pilot scales align?
3. Are evidence, claims, reviews, decisions, and execution consistently separated?
4. Is human authority explicit?
5. Are Regulatory Knowledge Layer and Knowledge Garden boundaries preserved?
6. Does ClimateOS contribute evidence without importing conclusions or authority?
7. Is S7 consistently candidate-only and security-safe?
8. Does any record accidentally authorize implementation, a live pilot, legal advice, certification, or autonomous action?
9. Is the documentation package sufficient to prepare a future bounded implementation authorization brief, if the Chief Architect later chooses to do so?

## Next Governed Planning Sequence

1. Perform a combined documentation architecture review.
2. Correct bounded documentation inconsistencies if found.
3. Optionally prepare an RKL-1 Source Governance and Information Architecture brief as documentation only.
4. Return to the Chief Architect before selecting a live pilot or authorizing any implementation.
5. If implementation is later approved, prepare a separately bounded implementation brief, tests, review plan, stop conditions, and freeze pathway.

## Decisions Requiring Chief Architect Review

Routine documentation review and bounded documentation correction may proceed.

Return to the Chief Architect before:

- materially changing BuildingOS product scope;
- changing the BuildingOS–PRI–ClimateOS architecture boundary;
- selecting or activating a live pilot project;
- asserting legal, compliance, certification, contractual, statutory, engineering-signoff, safety, planning-approval, or professional authority;
- authorizing implementation code for the next milestone;
- modifying the frozen Foundation or Core Batch 01 baseline;
- introducing a database, public API, permissions, automated workflow, external connector, production UI, application migration, or autonomous approval capability;
- using confidential, critical-infrastructure, licensed, personal, or protected operational data.

## Current Blockers and Maintenance Items

No blocker prevents the combined documentation review.

The official local workspace `D:\Codex\BuildingOS` was not independently inspected during the GitHub connector run. GitHub `main` remains the source of truth, and the local workspace should pull the latest commits before local work resumes.

The repository `README.md` contains historical project-status wording from before Core Batch 01 implementation and freeze. A bounded documentation refresh is safe and should not change product scope or frozen records.

## Safe Re-entry Point

Continue from:

`POST_FREEZE_COMBINED_DOCUMENTATION_ARCHITECTURE_REVIEW`

Read first:

1. `PROJECT_CONTEXT.md`
2. `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`
3. `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`
4. `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`
5. `docs/BUILDINGOS_PROJECT_GENOME_AND_CLASSIFICATION_STANDARD.md`
6. `docs/BUILDINGOS_LIFECYCLE_STAGE_GRAPH_ARCHITECTURE.md`
7. `docs/BUILDINGOS_HUMAN_INTERFACE_ARCHITECTURE.md`
8. `docs/BUILDINGOS_READ_ONLY_OPERATOR_CONSOLE_PROTOTYPE_BRIEF.md`
9. `docs/BUILDINGOS_PILOT_CANDIDATE_PLAN.md`
10. `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`

Do not modify the frozen Foundation or Core Batch 01 baseline without formal Change Request governance.

## Context Protocol

Every major milestone, repository transition, workspace transition, or long-thread closure must update this file and create a context transfer packet when needed.