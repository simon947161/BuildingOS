# BuildingOS Read-Only Operator Console Prototype Brief

## Record Status

`DOCUMENTATION_BRIEF_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-14

## Purpose

Define a bounded, reviewable brief for a future non-production, read-only BuildingOS Operator Console prototype that demonstrates human visibility across project classification, lifecycle stages, evidence, claims, reviews, decisions, and governance history.

This brief authorizes documentation and design planning only. It does not authorize frontend or backend code, a database, API, permissions, user management, workflow automation, external connectors, automatic lifecycle transitions, autonomous approval, live-project operation, or application migration.

## Prototype Intent

The prototype should answer one question:

```text
Can BuildingOS make complex project evidence and governance easier for a human to understand without pretending to decide or act?
```

## Governing References

The prototype brief depends on:

- `docs/BUILDINGOS_PRODUCT_NORTH_STAR.md`;
- `docs/BUILDINGOS_PROJECT_GENOME_AND_CLASSIFICATION_STANDARD.md`;
- `docs/BUILDINGOS_LIFECYCLE_STAGE_GRAPH_ARCHITECTURE.md`;
- `docs/BUILDINGOS_HUMAN_INTERFACE_ARCHITECTURE.md`;
- `docs/BUILDINGOS_CLIMATEOS_CROSS_DOMAIN_EVIDENCE_INTAKE_CONTRACT.md`;
- `docs/BUILDINGOS_S7_SYDNEY_CANDIDATE_EVIDENCE_INTAKE_PROFILE.md`;
- `docs/BUILDINGOS_REGULATORY_KNOWLEDGE_AND_KNOWLEDGE_GARDEN_PLAN.md`.

The frozen Foundation and Core Batch 01 baseline remain unchanged.

## Prototype Classification

```text
READ_ONLY
NON_PRODUCTION
NON_OPERATIONAL
FICTIONAL_OR_APPROVED_PUBLIC_INFORMATION_ONLY
NO_DECISION_AUTHORITY
NO_IMPLEMENTATION_AUTHORIZATION
```

## Primary Users for Evaluation

The prototype may be evaluated from the perspective of:

- project owner or sponsor;
- programme or project manager;
- planner;
- architect or building designer;
- engineer or technical coordinator;
- BIM or information manager;
- environmental or climate-risk practitioner;
- construction or commissioning coordinator;
- operator or asset manager;
- governance, audit, or evidence reviewer;
- Chief Architect reviewing BuildingOS product direction.

These are evaluation perspectives only. The prototype must not assign professional, statutory, contractual, or decision authority.

## Prototype Goals

1. Demonstrate navigation from portfolio to project, lifecycle stage, evidence, claim, review, decision, and ledger history.
2. Show how Project Genome scale and governance depth influence information density.
3. Demonstrate a lifecycle graph with branches, hold points, parallel paths, partial completion, and re-entry.
4. Keep evidence, claims, reviews, decisions, and execution visibly separate.
5. Show uncertainty, conflicting evidence, missing information, supersession, and re-review triggers.
6. Demonstrate how climate-risk evidence may enter from ClimateOS without importing conclusions or authority.
7. Demonstrate how future regulatory source metadata and compliance-related claims may be displayed without providing legal or certification advice.
8. Show repository links, document versions, and Markdown-first Knowledge Garden relationships.
9. Test whether a calm Mission Control-style interface can support both compact and complex projects.
10. Produce reviewable design evidence for a later Chief Architect decision on whether any implementation should be authorized.

## Explicit Non-Goals

The prototype must not:

- create or edit live project records;
- execute procedures;
- advance lifecycle stages;
- approve, reject, certify, sign off, issue consent, or make go/no-go decisions;
- connect to ClimateOS, NCC, NSW legislation, standards services, BIM platforms, project systems, email, calendars, PRI, MCP Runtime, QClaw, n8n, or other external systems;
- introduce login, permissions, roles, access control, or user administration;
- create a production database or public API;
- upload or process confidential, personal, licensed, critical-infrastructure, or security-sensitive material;
- duplicate NCC, referenced standards, legislation, paid databases, or protected project documents;
- select or activate a live pilot;
- represent AI output as legal, compliance, certification, engineering, planning, safety, contractual, or professional advice.

## Demonstration Information Model

The prototype may use static, fictional, or explicitly approved public demonstration records for:

- Portfolio;
- Project Genome;
- Lifecycle Stage Graph;
- Stage;
- Evidence;
- Claim;
- Review;
- Decision supplied by an authorised fictional human role;
- Governance Ledger Entry;
- Module Contract;
- Regulatory Source Metadata;
- Source Change Notice;
- Applicability Claim;
- Compliance-Related Claim with limitations;
- ClimateOS Evidence Intake Item;
- Unresolved Question;
- Re-review Trigger.

These demonstration records must not be mistaken for an approved runtime schema.

## Minimum Prototype Surfaces

## 1. Portfolio Console

The prototype should show at least three fictional or bounded candidate project cards representing:

- a `BOS-S` compact case;
- a `BOS-M` coordinated case;
- a `BOS-LC` large or complex case.

Each card should expose:

- stable project ID;
- project title and short boundary;
- internal operating scale and provisional governance depth;
- current recorded lifecycle stage;
- attention items separated by evidence, claim, review, decision, dependency, and source-change state;
- unresolved-question count;
- publication or information-boundary notice;
- link to the Project Cockpit.

No universal project ranking or unexplained health score should be used.

## 2. Project Cockpit

The project-level view should show:

- project identity and Genome version;
- scope and exclusions;
- typology, jurisdiction context, scale, governance depth, and confidence;
- lifecycle map and current recorded position;
- systems, packages, sites, disciplines, and interfaces;
- evidence, claim, review, and decision summaries;
- unresolved questions and assumptions;
- source changes and re-review triggers;
- latest ledger events;
- links to authoritative Markdown records.

## 3. Stage Workspace

The stage view should show:

- stage identity, purpose, boundary, and graph context;
- entry and exit criteria;
- evidence requirements;
- claim requirements;
- review requirements;
- decision authority reference;
- hold points;
- dependencies and parallel paths;
- defects, exceptions, and re-entry triggers;
- next permitted stages;
- stage history.

All action-looking controls must be absent or visibly disabled in a design mock. The screen must state that recorded readiness is not permission to act.

## 4. Decision and Evidence Room

The prototype should demonstrate one bounded fictional decision packet containing:

- decision question;
- scope and exclusions;
- evidence table;
- claim map;
- supporting and contradicting evidence;
- reviews, limitations, and dissent;
- externally established fictional decision role;
- unresolved items;
- conditions and re-review triggers;
- recorded decision history;
- governance ledger references.

The prototype must not generate the decision.

## 5. Lifecycle Board

The prototype should show:

- stages and stable stage IDs;
- transition edges;
- current recorded position;
- a parallel path;
- a hold point;
- a partial-completion boundary;
- a return-for-correction path;
- a source-change re-review trigger;
- current and superseded graph versions.

## 6. Evidence Desk

The prototype should show evidence with:

- identity;
- source and provenance;
- date, version, and access date;
- project, stage, system, and claim relationships;
- limitations and uncertainty;
- review status;
- supersession;
- licensing, confidentiality, or publication note;
- link to the authoritative or original location where lawful.

## 7. Regulatory Context Panel

A bounded panel may show fictional or metadata-only examples for:

- NCC edition, volume, amendment, adoption, commencement, and jurisdiction context;
- a referenced standard identifier and licensing note;
- a NSW Act, regulation, environmental planning instrument, approval record, or authority guidance reference;
- source version and effective date;
- jurisdictional variation;
- source-change notice;
- applicability or compliance-related claim;
- human review and re-review trigger.

The panel must prominently state that it is not legal or certification advice and that official publishers remain authoritative.

## 8. Governance Ledger View

The prototype should show a chronological, append-oriented history of:

- evidence registration;
- claim revision;
- review;
- decision supplied by a fictional authorised role;
- lifecycle record change;
- source change;
- supersession;
- correction;
- hold and release record;
- re-entry.

## Demonstration Cases

The prototype planning may use three non-live cases:

### Compact Case

A fictional small building alteration, local asset upgrade, or modest retrofit suitable for testing a compact lifecycle graph and `GD-1` or `GD-2` visibility.

### Coordinated Case

A fictional regional community facility, community energy facility, substantial retrofit, or multi-disciplinary public asset suitable for testing coordinated design, procurement, construction, commissioning, and handover evidence.

### Large or Complex Case

S7 may be used only as a public-information and structure-learning candidate for testing large-project information architecture.

S7 must remain:

```text
CANDIDATE_LARGE_COMPLEX_PROJECT_LEARNING_CASE
NOT_APPROVED_AS_LIVE_BUILDINGOS_PILOT
NO_PROJECT_AUTHORITY
NO_CONFIDENTIAL_DATA_ACCESS
```

Any S7 demonstration must distinguish public reporting from official planning records, approved design, as-built condition, and operational evidence. Sensitive critical-infrastructure detail is prohibited.

## ClimateOS Demonstration Boundary

A static ClimateOS evidence package may demonstrate:

- source and provenance;
- observation or model-output type;
- method;
- date and version;
- spatial and temporal scope;
- uncertainty;
- site, climate-risk, building, MEP, BIM, fixture, construction, commissioning, operations, or source relationship;
- BuildingOS human review state.

The demonstration must not include a live connector, automated transfer, ClimateOS conclusion presented as a BuildingOS decision, or automatic lifecycle effect.

## Regulatory Knowledge and Knowledge Garden Boundary

The prototype may link to Markdown-first indexes and metadata-only source records.

It must preserve:

- GitHub `main` as the approved source of truth;
- stable filenames and record IDs;
- ordinary links, backlinks, indexes, and maps of content;
- controlled draft promotion;
- separation of private research and approved records;
- controlled sync without blind two-way replication;
- no shadow copying of NCC, standards, legislation, paid databases, confidential project records, or security-sensitive content.

## Prototype Deliverables Requiring Later Approval

If implementation is later explicitly authorized, the minimum prototype package should be limited to:

1. information-architecture map;
2. low-fidelity wireframes;
3. visual hierarchy and component inventory;
4. fictional or approved public static data fixtures;
5. clickable read-only navigation or static rendered screens;
6. usability-review script;
7. architecture-boundary checklist;
8. prototype review record;
9. no-production declaration.

This list does not itself authorize those deliverables to be implemented.

## Evaluation Questions

Reviewers should assess:

1. Can a human understand the project boundary and current evidence state?
2. Can a human distinguish evidence, claim, review, decision, and execution?
3. Can a human find the source, version, effective date, and provenance?
4. Are uncertainty and unresolved questions visible?
5. Is decision authority clear and externally grounded?
6. Does the lifecycle display support branches, parallel paths, partial completion, and re-entry?
7. Does the interface adapt across `BOS-S`, `BOS-M`, and `BOS-LC` without false uniformity?
8. Are regulatory claims clearly bounded and subordinate to official sources and human review?
9. Does the ClimateOS handoff preserve evidence without importing conclusions?
10. Is S7 visibly candidate-only and security-safe?
11. Can the authoritative record still be understood in Markdown and repository history?
12. Does any element accidentally imply approval, legal advice, certification, professional sign-off, or operational authority?

## Stop Conditions

Prototype planning or future authorised work must stop if it requires:

- modification of frozen Foundation or Core;
- production database or API;
- permissions or user management;
- live external data or system connection;
- workflow execution or automatic lifecycle transition;
- autonomous approval or decision-making;
- confidential or critical-infrastructure data;
- copying controlled legal or standards content;
- legal, certification, contractual, safety, engineering-signoff, or professional conclusions;
- live pilot selection or activation;
- product-scope or architecture-boundary change;
- implementation without explicit Chief Architect approval.

## Current Decision

```text
READ_ONLY_OPERATOR_CONSOLE_PROTOTYPE_BRIEF_V0_1_PREPARED
DOCUMENTATION_ONLY
NO_UI_IMPLEMENTATION_AUTHORIZATION
```

## Next Safe Activity

After verification of this brief, prepare a documentation-only pilot candidate plan covering small, medium, and large or complex learning cases without selecting or activating a live pilot.