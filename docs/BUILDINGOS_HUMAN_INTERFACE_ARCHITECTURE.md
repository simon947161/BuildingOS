# BuildingOS Human Interface Architecture

## Record Status

`DOCUMENTATION_ARCHITECTURE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-14

## Purpose

Define a reviewable, documentation-only human-interface architecture for BuildingOS that gives authorised people clear, evidence-linked, lifecycle-aware visibility across portfolios, projects, stages, decisions, evidence, claims, reviews, and governance history.

This architecture describes information surfaces and interaction principles. It does not authorize production UI implementation, a database, permissions, user management, workflow execution, external connectors, automatic lifecycle transitions, autonomous approval, or application migration.

## Human Interface North Star

```text
Show what is known.
Show why it is believed.
Show who reviewed it.
Show what remains unresolved.
Show who may decide.
Never make the screen look more authoritative than the evidence.
```

## Relationship to Frozen Foundation and Core

The interface architecture consumes the frozen Governance Kernel concepts without changing them:

- Actor and attribution;
- Evidence;
- Claim;
- Review without decision authority;
- Procedure without execution;
- Lifecycle without automatic transition;
- Registered Object;
- Governance Ledger Entry;
- Module Contract;
- Conformance Result.

The frozen C00 through C01-I Foundation and Core Batch 01 baseline remain unchanged.

The interface must not add hidden semantics that contradict the Foundation. A visual control cannot convert a review into a decision, a claim into evidence, a recorded state into permission, or an AI summary into professional authority.

## Relationship to Current Product Architecture

The Human Interface Architecture should display and connect:

- Product North Star context;
- Project Genome and classification;
- Lifecycle Stage Graph;
- ClimateOS-to-BuildingOS evidence intake records;
- candidate learning-case records such as S7;
- future Regulatory Knowledge Layer records;
- Markdown-first Knowledge Garden indexes and reviewed documentation.

It must remain possible to understand the authoritative record outside the interface through stable Markdown documents and repository history.

## Interface Principles

### 1. Evidence Before Confidence

Every consequential statement should expose its supporting evidence, source, date, version, provenance, limitations, and review state.

### 2. Human Authority Is Explicit

Decision authority must be separately displayed and externally evidenced. It must not be inferred from account access, screen position, document authorship, job title, AI output, or review participation.

### 3. Recorded State Is Not Permission

A stage marked active, ready, complete, or approved must identify the record and authority supporting that label. The interface must not imply legal, contractual, professional, operational, occupancy, construction, procurement, or certification permission.

### 4. Uncertainty Is a First-Class Object

Unknowns, assumptions, conflicting evidence, unresolved questions, expired reviews, source changes, and re-review triggers must remain visible.

### 5. History Must Not Disappear

Superseded, corrected, returned, and re-entered records remain traceable. The interface should distinguish current records without erasing history.

### 6. Scale Without Losing Governance

The interface should adapt to `BOS-S`, `BOS-M`, and `BOS-LC` projects without forcing identical information density or removing consequential evidence and review.

### 7. Readability Before Decoration

The first interface direction should favour clear hierarchy, calm density, stable terminology, accessible navigation, and printable or exportable human-readable views over animated dashboards or ornamental complexity.

### 8. No False Green

Colour, progress bars, scores, badges, and percentages must not create unsupported certainty. Readiness should be decomposed into evidence, claim, review, decision, dependency, and unresolved-item states.

### 9. Repository Traceability

Every authoritative view should provide a path back to the approved repository record, version, commit, or stable document reference where available.

### 10. Security and Publication Boundaries

The architecture must support visible indications that information is public, controlled, confidential, licensed, private-research, security-sensitive, or externally authoritative without defining or implementing a permissions system.

## Primary Human Interface Surfaces

## 1. Portfolio Console

### Purpose

Provide a cross-project view for human oversight without flattening projects into a single score.

### Core Questions

- Which projects or work packages exist?
- What is each Project Genome classification and confidence?
- What lifecycle stage is currently recorded?
- Which gates, hold points, source changes, or re-reviews require attention?
- Which evidence or claims are missing, disputed, stale, restricted, or superseded?
- Which decisions are pending, and who is authorised to decide?
- Which projects have security, confidentiality, jurisdiction, or publication constraints?

### Suggested Information Groups

- portfolio identity and date context;
- project cards or rows with stable IDs;
- `BOS-S`, `BOS-M`, or `BOS-LC` internal operating-scale label;
- provisional governance depth;
- recorded lifecycle position;
- gate and hold-point summary;
- evidence, claim, review, and decision attention counts;
- source-change and re-review notices;
- unresolved risks and dependencies;
- publication or information-boundary indicators;
- links to the Project Cockpit and authoritative records.

### Prohibited Simplifications

The Portfolio Console must not:

- rank projects with an unexplained universal score;
- convert incomplete evidence into a red/amber/green conclusion without context;
- imply that portfolio visibility creates authority over project decisions;
- expose restricted or critical-infrastructure detail in public views;
- select or activate a pilot.

## 2. Project Cockpit

### Purpose

Provide a project-level command-of-information view for humans while keeping decision authority and execution outside the interface unless separately authorised.

### Core Questions

- What is the project boundary and current Project Genome version?
- What is known, unknown, assumed, disputed, or restricted?
- What lifecycle graph and stage position are recorded?
- Which systems, packages, sites, disciplines, authorities, and stakeholders matter now?
- Which evidence, claims, reviews, and decisions support the current position?
- What changed recently?
- What must be reviewed next?

### Suggested Information Regions

- project identity and boundary;
- Genome summary;
- lifecycle map;
- current stage and parallel-path summary;
- major systems, packages, sites, and interfaces;
- evidence and claim readiness;
- review and decision timeline;
- unresolved questions and assumptions;
- change, defect, exception, and re-entry summary;
- regulatory source and effective-date context;
- climate-risk evidence references;
- governance ledger history;
- linked project documents and Knowledge Garden indexes.

### Project Cockpit Rule

The Cockpit may organise and summarise. It must not become an automated project manager, approval engine, legal adviser, certifier, designer of record, superintendent, principal certifier, consent authority, or operator.

## 3. Stage Workspace

### Purpose

Provide a focused view of one lifecycle stage, package, system, site, authority pathway, or bounded subgraph.

### Core Questions

- What is the stage purpose, scope, and boundary?
- What are the entry and exit criteria?
- Which evidence and claims are required?
- Which reviews have occurred, and what limitations or dissent remain?
- Which decision is required, by whom, and on what basis?
- What hold points, dependencies, parallel paths, or re-entry triggers apply?
- What transfers to the next stage?

### Suggested Workspace Sections

- stage identity and graph context;
- entry criteria;
- stage activities and referenced procedures;
- evidence register filtered to stage scope;
- claim register filtered to stage scope;
- reviews and findings;
- decision requirements and authority references;
- hold points;
- dependencies and interfaces;
- defects, exceptions, departures, and unresolved items;
- exit criteria;
- return and re-entry paths;
- relevant ledger events;
- source-version and regulatory context;
- linked documents and indexes.

### Stage Workspace Rule

Buttons, labels, or controls must not imply that a user can start, approve, complete, certify, energise, occupy, operate, or close a stage unless separate implementation and authority governance is approved. The initial architecture is read-only.

## 4. Decision and Evidence Room

### Purpose

Create a bounded, traceable space for consequential human deliberation without merging evidence, claims, review, and decision into one undifferentiated dashboard.

### Core Questions

- What exact decision is being considered?
- What is included and excluded?
- What evidence supports or contradicts the claims?
- Which sources are primary, official, current, licensed, restricted, or superseded?
- What reviews exist, and what limitations, conflicts, or dissent remain?
- Who is authorised to decide?
- What conditions, consequences, dependencies, and re-review triggers apply?
- What must be preserved in the governance history?

### Required Zones

1. **Decision Frame** — decision ID, question, scope, exclusions, authority, date context.
2. **Evidence Table** — evidence items, provenance, versions, limitations, status.
3. **Claim Map** — claims, supporting and contradicting evidence, uncertainty.
4. **Review Panel** — reviewers, capacity, findings, limitations, dissent, dates.
5. **Authority Panel** — externally evidenced decision role and boundaries.
6. **Conditions and Consequences** — conditions, dependencies, hold points, expiry, re-review.
7. **Decision Record** — recorded decision and rationale when supplied by an authorised human.
8. **Ledger and History** — prior decisions, supersession, corrections, returns, and linked events.

### Decision Room Rule

The interface may prepare, compare, and display. It must not generate an autonomous decision, simulate professional sign-off, or treat a recommendation as an authorised outcome.

## Supporting Surfaces

## Evidence Desk

A focused evidence view should show:

- evidence ID and type;
- source and provenance;
- author or issuing body;
- date, version, effective date, and accessed date where relevant;
- project, stage, system, package, site, and claim relationships;
- confidence and limitations;
- review state;
- supersession relationships;
- licensing, confidentiality, security, and publication constraints;
- original or authoritative location.

AI summaries must be labelled and subordinate to source material.

## Claim Desk

A claim view should show:

- exact subject and statement;
- scope and exclusions;
- supporting and contradicting evidence;
- assumptions and uncertainty;
- stage and decision relationships;
- review status;
- expiry, change, or re-review trigger;
- whether the claim is factual, interpretive, applicability-related, compliance-related, forecast, design, operational, or other declared type.

A claim must not be displayed as evidence merely because it is frequently repeated.

## Review Workspace

A review view should show:

- reviewer identity and attributed capacity;
- review question and scope;
- evidence and claims reviewed;
- method or basis;
- findings;
- limitations;
- dissent or conflict;
- recommendation where applicable;
- review date and validity context;
- re-review trigger;
- explicit statement that review does not create decision authority.

## Lifecycle Board

A lifecycle board should display:

- stage nodes and transition edges;
- current recorded position;
- parallel paths;
- hold points;
- partial completion;
- return and re-entry paths;
- stage-level readiness decomposition;
- source changes and review triggers;
- history and supersession.

It must avoid the visual fiction that every project is a simple linear Kanban board.

## Governance Ledger View

A ledger view should show an append-oriented human-readable sequence of:

- evidence registration;
- claim creation or revision;
- review events;
- decisions supplied by authorised humans;
- lifecycle state records;
- source changes;
- supersession;
- correction;
- exception;
- hold and release records;
- module conformance events.

The view must not describe itself as blockchain unless a separately authorised architecture actually uses one.

## Module Contract Registry

A future registry view may display documentation-only module contracts:

- module identity and version;
- purpose;
- declared inputs and outputs;
- obligations;
- excluded capabilities;
- Foundation and Core conformance targets;
- authority boundaries;
- security and publication constraints;
- review and approval status.

Displaying a module contract does not activate the module.

## Cross-Surface Navigation Model

The interface should support movement through stable relationships:

```text
Portfolio
→ Project
→ Genome
→ Lifecycle Graph
→ Stage
→ Evidence / Claim / Review / Decision
→ Ledger Event
→ Authoritative Record
```

Alternative paths should include:

- source to affected claims and projects;
- claim to supporting and contradicting evidence;
- review to scope and decision;
- decision to conditions and lifecycle consequences;
- source change to re-review candidates;
- project to linked Knowledge Garden index;
- stage to regulatory and climate-risk evidence context.

## Information Hierarchy

Each view should show, in order:

1. identity and scope;
2. current date, version, and status context;
3. what is known and unknown;
4. evidence and source basis;
5. claims and interpretations;
6. reviews and limitations;
7. decision authority and pending decision;
8. lifecycle implications;
9. unresolved items and next review;
10. history and authoritative links.

## Status Semantics

Interface status labels should be decomposed rather than collapsed.

Suggested dimensions:

- evidence availability;
- provenance quality;
- claim completeness;
- review state;
- decision state;
- dependency state;
- lifecycle record state;
- source currency;
- uncertainty;
- publication or information boundary.

A single percentage-complete indicator should not substitute for these dimensions.

## Visual Language Direction

The future interface should use a restrained Mission Control character:

- strong typographic hierarchy;
- readable tables and record cards;
- clear timestamps and version labels;
- visible source and authority distinctions;
- diagrams that remain understandable when printed or exported;
- consistent warning and uncertainty patterns;
- minimal animation;
- no gamified approval cues;
- no decorative confidence scores;
- no hidden critical information behind hover-only interactions.

This is design direction, not a visual design system implementation.

## Accessibility and Human Factors

Future prototypes should consider:

- keyboard navigation;
- screen-reader structure;
- sufficient contrast;
- non-colour status indicators;
- plain-language summaries with access to technical detail;
- readable dates, units, and version labels;
- printable decision and evidence packets;
- support for long project names and complex identifiers;
- clear time-zone and effective-date context;
- avoidance of alert fatigue;
- deliberate confirmation before any future consequential action, if such actions are ever separately authorised.

## Regulatory Knowledge Layer Relationship

A future read-only regulatory view may display:

- NCC edition, volume, amendment, adoption, commencement, effective date, and jurisdiction context;
- referenced standards identifiers, editions, relationships, access, and licensing notes;
- NSW Acts, regulations, environmental planning instruments, approval records, authority guidance, and source status;
- Commonwealth, state, territory, and local variations;
- source-change and supersession notices;
- project-specific applicability and compliance-related claims;
- assumptions, limitations, unresolved questions, reviewer identity, and re-review triggers.

The interface must not:

- present itself as legal or certification advice;
- copy authoritative legal content into a shadow library;
- imply that the newest source automatically applies;
- convert an AI summary into a legal interpretation;
- state compliance without a bounded claim, evidence, qualified human review, authority context, and visible limitations;
- issue an approval, certificate, consent, or professional conclusion.

## Knowledge Garden Relationship

The interface should coexist with a Markdown-first Knowledge Garden in which:

- GitHub `main` is the authoritative approved source;
- stable Markdown documents remain readable outside Obsidian;
- ordinary links, backlinks, indexes, and maps of content support navigation;
- draft promotion is controlled and reviewable;
- private research remains separate from approved records;
- blind two-way sync is prohibited;
- official legal, standards, licensed, confidential, and security-sensitive content is referenced rather than duplicated.

The interface may link to approved Markdown indexes. It must not silently promote private notes into authoritative project records.

## ClimateOS Evidence Relationship

The interface may display eligible ClimateOS evidence under the cross-domain intake contract, including climate-risk, site, building, MEP, BIM, fixture, construction, commissioning, operations, source, and provenance evidence.

It must visibly distinguish:

- ClimateOS evidence from BuildingOS claims;
- model output from observed fact;
- scenario from forecast;
- forecast from decision;
- uncertainty from confidence;
- ClimateOS conclusions from authorised BuildingOS human decisions.

## S7 Candidate Learning-Case Boundary

S7 may be used only to test whether information architecture can represent a large and complex candidate learning case.

Public interface concepts must not expose or infer:

- critical-infrastructure layouts;
- network architecture;
- access-control arrangements;
- security vulnerabilities;
- client configurations;
- protected operational data;
- confidential commercial or project information.

S7 remains:

```text
CANDIDATE_LARGE_COMPLEX_PROJECT_LEARNING_CASE
NOT_APPROVED_AS_LIVE_BUILDINGOS_PILOT
NO_PROJECT_AUTHORITY
NO_CONFIDENTIAL_DATA_ACCESS
```

## Read-Only Prototype Boundary

A bounded prototype may later illustrate navigation, information grouping, record relationships, visual hierarchy, and fictional or approved public examples.

The prototype must remain:

- read-only;
- documentation-led;
- non-production;
- non-operational;
- non-authoritative;
- free of permissions, user administration, databases, external connectors, workflow execution, approval controls, automatic transitions, and live project actions;
- clearly labelled as a prototype.

No prototype implementation is authorized by this architecture record.

## Documentation Conformance Checklist

A Human Interface Architecture package should confirm:

1. Portfolio Console, Project Cockpit, Stage Workspace, and Decision and Evidence Room are defined;
2. evidence, claims, reviews, decisions, lifecycle states, and execution remain separate;
3. human authority is explicit and externally evidenced;
4. uncertainty, dissent, source changes, and supersession remain visible;
5. the interface does not imply legal, certification, contractual, professional, or operational authority;
6. small, medium, and large or complex projects are supported without false uniformity;
7. Regulatory Knowledge Layer boundaries are preserved;
8. Knowledge Garden compatibility does not create a second source of truth;
9. ClimateOS evidence does not import conclusions or authority;
10. S7 remains candidate-only and security-sensitive detail is excluded;
11. no permissions, database, API, runtime, connector, workflow, production UI, or autonomous approval is introduced;
12. no frozen Foundation or Core change is required;
13. no implementation is authorized.

## Current Decision

```text
HUMAN_INTERFACE_ARCHITECTURE_V0_1_PREPARED
DOCUMENTATION_ONLY
NO_PRODUCTION_UI_AUTHORIZATION
NO_IMPLEMENTATION_AUTHORIZATION
```

## Next Safe Activity

After verification of this architecture record, prepare a bounded read-only BuildingOS Operator Console Prototype Brief using fictional or explicitly approved public information only.