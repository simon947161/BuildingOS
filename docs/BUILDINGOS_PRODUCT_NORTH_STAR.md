# BuildingOS Product North Star

## Record Status

`DOCUMENTATION_BASELINE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-13

## Purpose

Define the durable product direction for BuildingOS after the formal freeze of Core Batch 01.

This record guides future planning, architecture, review, pilot selection, and interface design. It does not authorize implementation code, production infrastructure, automated workflow execution, professional conclusions, or autonomous approval authority.

## North Star Statement

BuildingOS is an AI-native, evidence-driven, human-governed operating system for helping people progress built-environment and infrastructure projects through their full lifecycle with visible evidence, explicit claims, accountable review, and traceable decisions.

Its purpose is not to replace architects, engineers, planners, builders, certifiers, lawyers, owners, operators, regulators, or communities. Its purpose is to make the information, assumptions, procedures, reviews, and decisions surrounding their work easier to organise, inspect, challenge, and govern.

## Product Promise

For any project, at any stage, an authorised human should be able to answer:

1. What project or asset are we dealing with?
2. What stage is it currently in?
3. What evidence exists, where did it come from, and how current is it?
4. What claims are being made from that evidence?
5. Which claims remain uncertain, disputed, incomplete, or superseded?
6. Who reviewed each consequential matter, in what capacity, and with what limitations?
7. What decision was made, by whom, on what basis, and what remains outside the decision?
8. What must happen next before the project can safely advance?

## Product Character

BuildingOS should remain:

- **evidence-first** — source material remains distinguishable from summaries, claims, and decisions;
- **human-governed** — consequential decisions remain attributable to authorised people;
- **lifecycle-aware** — the system represents the project from early need through end-of-life;
- **scale-adaptive** — the same governance principles support small, medium, and large projects without forcing identical process weight;
- **domain-extensible** — specialist capability packs may support buildings, infrastructure, climate risk, energy, water, ecology, procurement, commissioning, and operations;
- **jurisdiction-aware** — legal and regulatory context is versioned, sourced, and reviewed without pretending universal applicability;
- **interoperable by contract** — external systems exchange bounded evidence packages rather than silently importing conclusions or authority;
- **readable before executable** — architecture and governance must be understandable in documentation before runtime behaviour is authorised;
- **portable and durable** — approved records remain accessible through Markdown, Git history, stable identifiers, and open reviewable formats;
- **honest about uncertainty** — missing evidence, conflicting sources, assumptions, and unresolved questions stay visible.

## Primary Users

BuildingOS is intended to support, without collapsing their distinct responsibilities:

- project owners and asset owners;
- planners and development managers;
- architects, building designers, engineers, and specialist consultants;
- builders, contractors, subcontractors, suppliers, and commissioning teams;
- facilities, maintenance, and operations teams;
- sustainability, climate-risk, energy, water, and environmental practitioners;
- financiers, insurers, procurement teams, and governance reviewers;
- government agencies, councils, consent authorities, and public infrastructure bodies;
- community representatives and affected stakeholders;
- auditors, reviewers, and authorised decision-makers.

System access must never imply professional competence, statutory authority, contractual delegation, certification power, or decision rights.

## Project Scale Model

BuildingOS should support three broad operating scales through configurable governance depth rather than separate cores.

### Small Projects

Examples may include a dwelling alteration, small community facility, modest retrofit, local landscape or water intervention, or a simple asset upgrade.

The system should favour:

- minimal required records;
- simple evidence packs;
- compact stage graphs;
- clearly identified approval and inspection points;
- low administrative burden;
- visible escalation when complexity increases.

### Medium Projects

Examples may include a commercial building, community energy facility, multi-disciplinary public asset, regional development, or substantial retrofit.

The system should support:

- multiple disciplines and organisations;
- coordinated design packages;
- procurement and construction interfaces;
- structured risk, evidence, and review registers;
- commissioning and handover evidence;
- operational readiness and maintenance planning.

### Large and Complex Projects

Examples may include hospitals, transport infrastructure, utility systems, precincts, industrial facilities, major data centres, or nationally significant assets.

The system should support:

- portfolio and programme relationships;
- multiple approval pathways and jurisdictions;
- staged design and construction packages;
- extensive MEP, BIM, commissioning, and operations evidence;
- long-duration provenance and version control;
- formal review and decision rooms;
- high consequence uncertainty and escalation;
- project-specific governance overlays.

Large scale must not be treated as permission for hidden automation. Greater consequence requires greater visibility and stronger human authority controls.

## Full Lifecycle Scope

BuildingOS should be capable of representing:

1. strategic need and project discovery;
2. feasibility and options assessment;
3. site and context investigation;
4. business case, finance, and delivery strategy;
5. planning, environmental assessment, and approvals;
6. concept, schematic, developed, and detailed design;
7. procurement, tendering, contracting, and mobilisation;
8. construction and installation;
9. testing, commissioning, verification, and defects management;
10. handover, occupancy, and operational readiness;
11. operation, maintenance, monitoring, and performance review;
12. adaptation, refurbishment, expansion, or change of use;
13. decommissioning, disassembly, reuse, remediation, and end-of-life.

A project-specific lifecycle graph may omit, combine, repeat, or branch stages, provided the variation is explicit and governed.

## Core Product Architecture Direction

Future BuildingOS architecture should develop around the following layers.

### 1. Governance Kernel

The frozen Core Batch 01 representational baseline provides foundational records for Actor, Evidence, Claim, Review, Procedure, Lifecycle, Registered Object, Governance Ledger Entry, Module Contract, and Conformance Result.

Future layers must consume this kernel through approved contracts rather than casually rewriting it.

### 2. Project Genome

A structured description of what the project is, including scale, type, asset class, location, jurisdiction, delivery model, lifecycle state, complexity, systems, stakeholders, risk profile, evidence burden, and capability requirements.

### 3. Lifecycle Stage Graph

A project-specific map of stages, gates, dependencies, required evidence, reviews, decisions, loops, branches, and re-entry conditions.

### 4. Domain Capability Packs

Bounded specialist knowledge and record patterns for areas such as:

- architecture and building design;
- structures and civil works;
- mechanical, electrical, hydraulic, fire, controls, and vertical transport systems;
- BIM and information management;
- climate risk and resilience;
- energy, carbon, water, biodiversity, and environmental performance;
- procurement, construction, commissioning, operations, and maintenance;
- finance, insurance, contracts, and delivery governance.

Capability packs do not gain authority merely by being installed or referenced.

### 5. Jurisdiction Knowledge Packs

Versioned and sourced regulatory context for the relevant country, state, territory, local government area, approval pathway, code edition, and referenced standards.

These packs remain decision support. They do not issue legal advice, certification, consent, or compliance conclusions.

### 6. Evidence Intake and Exchange Contracts

External systems, consultants, data rooms, sensors, models, and research environments may provide bounded evidence packages with provenance, dates, methods, uncertainty, and declared exclusions.

No external system may transfer its own decision authority into BuildingOS.

### 7. Human Interface Layer

A read-first interface direction including:

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

Initial interface work must remain documentation-only and read-only until separately authorised.

### 8. Tool Adapters

Future adapters may connect approved design, document, BIM, GIS, asset, field, environmental, and project systems through explicit contracts.

Adapters must not bypass source provenance, review boundaries, privacy, licensing, security, or governance gates.

## Evidence and Decision Model

BuildingOS must preserve the following separation:

```text
Source or Observation
→ Evidence Record
→ Claim
→ Human Review
→ Authorised Decision
→ Governance Ledger Entry
```

The arrows represent governed relationships, not automatic entitlement to advance.

A strong source may still support a weak or over-broad claim. A reviewed claim may still remain unresolved. A decision may remain limited, conditional, temporary, or reversible.

## AI Role

AI may assist with:

- document intake and classification;
- metadata extraction;
- source comparison;
- evidence indexing;
- draft summaries;
- claim drafting;
- inconsistency and missing-evidence detection;
- lifecycle and dependency visualisation;
- review preparation;
- change and supersession analysis;
- preparation of questions for qualified humans.

AI must not independently:

- grant approval;
- certify compliance;
- assert professional authority;
- sign contracts;
- accept design liability;
- determine legal applicability;
- issue construction, safety, environmental, or operational directions;
- hide uncertainty or conflicting evidence;
- trigger irreversible project actions.

## Product Non-Goals

BuildingOS is not:

- a replacement for professional judgement;
- a building certifier, consent authority, legal service, or engineering signatory;
- a generic autonomous agent runtime;
- a substitute for BIM authoring, CAD, GIS, document management, ERP, project scheduling, or facilities management products;
- a universal database into which all project information must be copied;
- a mechanism for importing ClimateOS, PRI, QClaw, n8n, or any other system's authority into BuildingOS Core;
- a licence to duplicate copyrighted standards, confidential project records, or controlled regulatory material;
- a production application authorised by this record.

## Relationship to ClimateOS

ClimateOS may supply observations, model outputs, climate-risk evidence, source references, uncertainty, methods, and provenance through a bounded evidence intake contract.

BuildingOS may register and organise those inputs as project evidence subject to human review.

ClimateOS conclusions, automated compliance statements, project approvals, lifecycle transitions, and decision authority must not be imported as BuildingOS decisions.

## Relationship to PRI and Other Runtimes

BuildingOS documentation may describe external coordination boundaries. BuildingOS Core must not absorb PRI, MCP Runtime, generic agent runtime, QClaw, n8n, or application migration without a separate architecture decision and explicit implementation authorization.

## Regulatory Knowledge and Knowledge Garden Boundary

The planned Regulatory Knowledge Layer must preserve source, version, jurisdiction, effective-date, licensing, and human-review context.

The Markdown-first Knowledge Garden model must preserve:

- GitHub as the authoritative approved record;
- portable Markdown and stable links;
- reviewable promotion of drafts;
- separation of private research notes from approved records;
- no blind two-way synchronisation;
- no copied shadow library of controlled legal or standards material.

## Product Success Measures

Future success should be assessed through evidence such as:

- reduced time required to locate decision-relevant evidence;
- higher proportion of consequential claims linked to attributable sources;
- clear visibility of missing, conflicting, expired, or superseded evidence;
- fewer unrecorded assumptions crossing project stages;
- better traceability from design and construction decisions into commissioning and operations;
- improved handover completeness;
- more consistent human review and decision records;
- ability to adapt governance depth across project scales;
- successful portability of approved records across GitHub, local workspaces, and Markdown-based knowledge environments;
- absence of unauthorised automated approvals or professional claims.

Success must not be measured merely by the number of records, integrations, agents, dashboards, or automated actions.

## Near-Term Governed Planning Sequence

1. Define the ClimateOS-to-BuildingOS Cross-Domain Evidence Intake Contract.
2. Prepare the NEXTDC S7 Sydney candidate large-project evidence intake profile.
3. Define the Project Genome and Classification Standard.
4. Define the Lifecycle Stage Graph Architecture.
5. Define the Human Interface Architecture and bounded read-only Operator Console Prototype Brief.
6. Propose small, medium, and large pilot project candidates.
7. Continue Regulatory Knowledge Layer and Knowledge Garden planning without implementation.

## Decisions Reserved for the Chief Architect

Chief Architect review is required before:

- materially changing the product mission or system boundary;
- changing the BuildingOS–ClimateOS–PRI relationship;
- selecting or activating a live pilot;
- asserting professional, legal, regulatory, contractual, or certification authority;
- modifying a frozen Foundation or Core baseline;
- authorising implementation code, production UI, database, public API, permissions, automated workflow, external connector, or autonomous decision capability.

## Current Safe Next Action

Prepare the documentation-only ClimateOS-to-BuildingOS Cross-Domain Evidence Intake Contract without modifying the frozen Foundation or Core Batch 01 implementation baseline.