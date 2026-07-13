# BuildingOS Project Genome and Classification Standard

## Record Status

`DOCUMENTATION_STANDARD_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-13

## Purpose

Define a reviewable, documentation-only standard for describing what a BuildingOS project is, how much governance it requires, which evidence and capabilities it needs, and which project-specific lifecycle architecture should be prepared next.

The Project Genome is a project description and classification instrument. It does not approve a project, determine legal applicability, certify compliance, assign professional authority, activate a pilot, or authorise implementation code.

## Governing Principle

```text
Describe the project before designing its workflow.
Expose uncertainty before assigning governance depth.
Use classification to scale human visibility, not to transfer decision authority.
```

## Relationship to the Frozen Foundation and Core

This standard consumes the frozen BuildingOS Governance Kernel concepts without changing them.

The frozen Foundation and Core Batch 01 implementation baseline remain unchanged. Any future executable representation of a Project Genome requires separate architecture review and explicit Chief Architect implementation authorization.

## What a Project Genome Is

A Project Genome is a versioned, evidence-linked description of a project, programme, site, asset, or bounded work package.

It records, at an appropriate level of confidence:

- identity and scope;
- project and asset type;
- operating scale;
- location and jurisdiction context;
- lifecycle position;
- delivery and ownership context;
- physical, technical, and information-system composition;
- stakeholder and authority relationships;
- complexity and consequence signals;
- evidence burden;
- governance depth;
- capability-pack requirements;
- security, confidentiality, licensing, and publication constraints;
- unresolved questions and escalation triggers.

A genome may describe a whole project or a governed sub-project. The boundary must be explicit.

## What a Project Genome Is Not

A Project Genome is not:

- an NCC building classification;
- a planning approval category;
- a legal interpretation;
- a certification or compliance conclusion;
- a professional opinion;
- a contract allocation of risk;
- an automated risk score;
- a substitute for a project brief, BIM execution plan, programme, cost plan, design report, safety plan, environmental assessment, commissioning plan, or asset register;
- permission to operate an autonomous agent, workflow, database, connector, or production interface.

BuildingOS internal operating-scale labels must remain visibly separate from statutory, regulatory, contractual, insurance, financing, or professional classifications.

## Core Terms

### Genome Record

The complete versioned project description at a stated date and confidence level.

### Genome Field

A single bounded attribute, relationship, classification, uncertainty, or evidence reference within the genome.

### Operating Scale Class

A BuildingOS internal classification used to estimate information and governance depth. It is not a statutory project or building class.

### Complexity Signal

A visible characteristic that may require additional coordination, evidence, review, branching, security, or escalation.

### Governance Depth

The minimum expected strength of evidence, review, decision traceability, and change control for the project or work package.

### Evidence Burden

The amount, diversity, provenance quality, review effort, retention period, and lifecycle linkage expected for decision-relevant evidence.

### Escalation Trigger

A condition requiring reclassification, additional review, a stronger lifecycle gate, or Chief Architect consideration.

## Genome Structure

A Project Genome should address the following domains. Unknown values must remain explicit rather than being guessed.

## 1. Identity and Boundary

Minimum fields:

- genome ID;
- genome version;
- project or work-package name;
- stable project reference;
- description;
- included scope;
- excluded scope;
- parent programme, portfolio, precinct, project, or asset relationship;
- related sites and assets;
- current record owner;
- prepared date;
- review status;
- source and evidence references.

The identity record must distinguish a proposed project, approved project, active delivery project, completed asset, operational asset, and research-only candidate.

## 2. Location and Jurisdiction Context

Minimum fields where known:

- country;
- state or territory;
- local government area;
- site or corridor description;
- geographic extent;
- cadastral or spatial reference where lawful and appropriate;
- consent, approval, or authority context;
- relevant jurisdiction layers;
- declared jurisdiction uncertainties;
- source version and effective-date references.

Jurisdiction metadata identifies research and review needs. It does not determine which law applies.

## 3. Project and Asset Typology

A genome should identify one or more project activity types:

- new build;
- alteration or addition;
- fit-out;
- retrofit or upgrade;
- repair or recovery;
- adaptive reuse or change of use;
- expansion;
- maintenance or renewal;
- remediation;
- temporary works;
- decommissioning, disassembly, reuse, or end-of-life;
- research, demonstration, or candidate learning case.

A genome should also identify one or more asset families, such as:

- residential;
- commercial;
- community and civic;
- education;
- health and care;
- data centre and digital infrastructure;
- industrial and manufacturing;
- energy;
- water and wastewater;
- transport;
- civil and public realm;
- landscape, ecology, and land management;
- precinct or campus;
- mixed or hybrid infrastructure.

Asset-family selection is descriptive. It does not replace authoritative project, planning, NCC, asset-management, or industry classification.

## 4. BuildingOS Operating Scale

Every genome should state one provisional internal operating scale.

### BOS-S — Small

Typical characteristics may include:

- one site or asset;
- limited disciplines and organisations;
- a compact lifecycle graph;
- a small number of consequential gates;
- modest evidence volume;
- limited commissioning or operational handover complexity;
- low coordination burden, while still preserving required professional and statutory review.

Examples may include a dwelling alteration, modest retrofit, local landscape intervention, small community facility, or bounded asset upgrade.

### BOS-M — Medium

Typical characteristics may include:

- multiple disciplines or organisations;
- coordinated design packages;
- procurement and construction interfaces;
- material environmental, community, commercial, or operational considerations;
- structured commissioning, handover, and maintenance evidence;
- more than one approval, review, or delivery pathway.

Examples may include a commercial building, regional community facility, multi-disciplinary public asset, substantial retrofit, or community energy facility.

### BOS-LC — Large or Complex

Typical characteristics may include:

- programme, portfolio, campus, precinct, network, or staged-delivery relationships;
- multiple jurisdictions, approval pathways, packages, or major interfaces;
- extensive building-services, civil, BIM, commissioning, operations, or asset evidence;
- high-consequence uncertainty;
- long-duration delivery and retention requirements;
- substantial security, confidentiality, safety, environmental, financial, or community considerations;
- formal evidence and decision rooms;
- project-specific governance overlays.

Examples may include hospitals, transport infrastructure, utilities, major industrial facilities, precincts, or hyperscale data-centre campuses.

### Scale Classification Rule

Scale is determined from the combined project characteristics, not from cost, floor area, capacity, headcount, or publicity alone.

A smaller project may require stronger governance because of heritage, safety, environmental, community, jurisdictional, or technical consequences. A large project must not be simplified merely because its organisations already have mature systems.

## 5. Complexity Dimensions

The genome should assess each dimension qualitatively as `LOW`, `MODERATE`, `HIGH`, `VERY_HIGH`, or `UNKNOWN`, with supporting evidence and limitations.

### 5.1 Spatial Complexity

- number and distribution of sites;
- corridor, network, campus, precinct, or remote-area relationships;
- land, access, interface, and staging constraints.

### 5.2 Jurisdictional Complexity

- number of authority layers;
- cross-border or multi-council relationships;
- interacting approval pathways;
- edition, commencement, transition, and variation questions.

### 5.3 Disciplinary Complexity

- number and interdependence of professional, technical, environmental, commercial, and operational disciplines;
- specialist review requirements;
- coordination and interface burden.

### 5.4 System Complexity

- number and criticality of physical and digital systems;
- redundancy, resilience, controls, integration, failure-mode, testing, and recovery relationships;
- maintainable-asset and configuration-management burden.

### 5.5 Delivery Complexity

- staging, packaging, procurement, contracting, mobilisation, and construction interfaces;
- temporary works;
- design responsibility and change relationships;
- supply-chain and long-lead dependencies.

### 5.6 Lifecycle Complexity

- number of stage branches, loops, hold points, handovers, partial completions, operational transitions, refurbishments, or end-of-life pathways;
- coexistence of design, construction, commissioning, and operation.

### 5.7 Evidence Complexity

- evidence volume, diversity, provenance, formats, access rights, review effort, retention period, and supersession rate;
- dependence on models, field evidence, tests, operational observations, or external source registers.

### 5.8 Stakeholder and Authority Complexity

- number and diversity of owners, funders, communities, authorities, consultants, contractors, operators, reviewers, and decision-makers;
- disputed interests or unclear authority boundaries.

### 5.9 Consequence Complexity

- potential consequences for people, environment, community, continuity, finance, infrastructure, reputation, heritage, or essential services;
- reversibility and recoverability of decisions.

### 5.10 Information, Security, and Confidentiality Complexity

- privacy;
- commercial confidentiality;
- critical-infrastructure sensitivity;
- cybersecurity and access restrictions;
- copyright and licensing;
- public-versus-controlled repository boundaries.

### 5.11 Novelty and Uncertainty

- unfamiliar technology, design, delivery model, operating context, climate condition, or regulatory pathway;
- immature evidence;
- conflicting sources;
- significant assumptions or future intentions.

## 6. Governance Depth

The genome should assign a provisional governance depth based on scale, complexity, consequences, and uncertainty.

### GD-1 — Compact

Suitable only where the project is bounded and evidence, review, and authority relationships are straightforward.

Expected characteristics:

- minimal but explicit evidence register;
- compact stage graph;
- named review and approval points;
- visible assumptions and unresolved items;
- simple change and supersession record.

### GD-2 — Coordinated

Expected characteristics:

- discipline and package relationships;
- structured evidence and claim registers;
- defined review responsibilities;
- procurement, construction, commissioning, and handover gates;
- change-control and decision traceability.

### GD-3 — Enhanced

Expected characteristics:

- formal stage and decision rooms;
- cross-disciplinary evidence dependencies;
- jurisdiction and source-version tracking;
- stronger configuration, commissioning, operational-readiness, and re-review controls;
- documented escalation and exception handling.

### GD-4 — Major or High-Consequence

Expected characteristics:

- project-specific governance overlay;
- multiple evidence and decision rooms;
- formal package, system, stage, and authority relationships;
- long-duration provenance and retention;
- security and publication controls;
- independent or specialist reviews where required by authorised humans;
- explicit treatment of high-consequence uncertainty and irreversible decisions.

Governance depth is an internal planning aid. It does not create competence, delegation, statutory power, contractual authority, or a professional duty.

## 7. Evidence Burden Profile

The genome should state the expected evidence burden across:

- source and provenance;
- site and environmental context;
- climate risk and resilience;
- planning and regulatory context;
- design and coordination;
- BIM and information management;
- procurement and supply chain;
- construction and installation;
- inspection and testing;
- commissioning and integrated systems testing;
- defects and non-conformance;
- handover and operational readiness;
- operation, maintenance, incidents, performance, and adaptation;
- decommissioning and end-of-life.

Each category may be labelled `MINIMAL`, `STANDARD`, `ENHANCED`, `EXTENSIVE`, `RESTRICTED`, `NOT_APPLICABLE`, or `UNKNOWN`.

`RESTRICTED` means evidence may require controlled references or private handling. It does not mean the evidence requirement disappears.

## 8. Lifecycle and Delivery Context

The genome should record:

- known current lifecycle stage;
- stage confidence and source date;
- proposed or approved delivery model where evidenced;
- package and staging strategy;
- design, procurement, construction, commissioning, handover, and operations relationships;
- partial completion or parallel-stage conditions;
- expected re-entry, adaptation, refurbishment, expansion, or decommissioning pathways;
- unresolved stage and authority questions.

The genome informs the Lifecycle Stage Graph. It must not automatically move the project between stages.

## 9. Physical and Technical System Profile

The genome should identify the project-relevant system families, including where applicable:

- site, landscape, ecology, and external works;
- architecture and envelope;
- structure;
- civil, earthworks, roads, drainage, and utilities;
- mechanical;
- electrical and energy;
- hydraulic, water, wastewater, and fire water;
- fire and life-safety systems;
- controls, monitoring, metering, and building management;
- communications and digital infrastructure;
- vertical transport;
- security at a non-sensitive descriptive level;
- fixtures, fittings, equipment, plant, and maintainable assets;
- temporary works;
- testing, commissioning, and operational systems.

Public repository records must avoid confidential or security-sensitive design and operational detail.

## 10. Information and BIM Profile

The genome should describe, where known:

- information-management maturity;
- document and model environment;
- discipline-model relationships;
- spatial and asset identifiers;
- model or document status conventions;
- design-to-fabrication, as-built, commissioning, and asset-information relationships;
- required exchange formats;
- record retention and access constraints;
- information gaps and responsibility boundaries.

This profile identifies information needs. It does not authorise copying confidential project models or replacing the authoritative common data environment.

## 11. Stakeholder, Actor, and Authority Profile

The genome should identify categories of:

- project and asset owners;
- sponsors and funders;
- planners and development managers;
- designers and specialist consultants;
- contractors, subcontractors, suppliers, and commissioning teams;
- operators and maintainers;
- consent authorities, councils, agencies, utilities, and regulators;
- communities and affected stakeholders;
- reviewers, auditors, certifiers, signatories, and authorised decision-makers.

Every authority statement must be sourced and scoped. Presence in a genome does not prove current appointment, competence, delegation, or legal authority.

## 12. Capability-Pack Requirements

The genome may identify future capability needs for:

- planning and approvals;
- architecture and building design;
- structures and civil works;
- MEP and fire systems;
- BIM and information management;
- climate risk and resilience;
- energy, carbon, water, biodiversity, and environmental performance;
- procurement and contracts;
- construction and quality;
- commissioning and handover;
- operations and maintenance;
- finance, insurance, and governance;
- Regulatory Knowledge Layer support.

A capability requirement is a planning signal. It does not install a module or grant authority.

## 13. Regulatory Knowledge Context

The genome should carry references, not conclusions, for:

- country, state or territory, and local jurisdiction;
- candidate NCC edition and volume where relevant;
- NCC adoption, commencement, transition, and jurisdiction-variation questions;
- referenced standards identifiers and edition metadata;
- NSW Acts, regulations, environmental planning instruments, approval records, and authority guidance where relevant;
- local planning controls and consent conditions;
- source version, effective date, access date, status, and supersession;
- applicability and compliance-related claims;
- required human reviewers and re-review triggers.

The genome must not state that a source applies, that a requirement is satisfied, or that a project is compliant unless a separately scoped claim and authorised human review support that statement.

A BuildingOS operating-scale class such as `BOS-S`, `BOS-M`, or `BOS-LC` must never be confused with an NCC building class or another statutory classification.

## 14. Knowledge Garden Compatibility

Project Genome records should remain Markdown-first and portable through:

- stable genome and project identifiers;
- ordinary Markdown headings and links;
- explicit indexes and maps of content;
- links to evidence, claims, reviews, lifecycle records, and regulatory sources;
- version and supersession history;
- backlinks where useful without depending on an Obsidian-only feature;
- GitHub as the authoritative approved source;
- branch, diff, or pull-request review for promoted changes;
- controlled synchronisation;
- separation of private research notes from approved records.

The Knowledge Garden must not duplicate authoritative NCC text, referenced standards, legislation, paid legal databases, confidential project files, or security-sensitive material without lawful permission.

## 15. Minimum Documentation Manifest

The following YAML is a documentation example, not an implemented schema.

```yaml
genome_id: BOS-GENOME-EXAMPLE-001
genome_version: 0.1
record_status: draft_for_human_review
prepared_on: YYYY-MM-DD
project:
  project_id: string
  project_name: string
  description: string
  boundary:
    included: []
    excluded: []
  parent_relationships: []
  candidate_or_live_status: string
location_and_jurisdiction:
  country: string
  state_or_territory: string
  local_government_area: string
  geographic_scope: string
  jurisdiction_questions: []
project_typology:
  activity_types: []
  asset_families: []
operating_scale:
  provisional_class: BOS-S|BOS-M|BOS-LC|UNKNOWN
  rationale: string
complexity:
  spatial: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  jurisdictional: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  disciplinary: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  systems: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  delivery: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  lifecycle: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  evidence: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  stakeholder_authority: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  consequence: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  information_security: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
  novelty_uncertainty: LOW|MODERATE|HIGH|VERY_HIGH|UNKNOWN
governance:
  provisional_depth: GD-1|GD-2|GD-3|GD-4|UNKNOWN
  escalation_triggers: []
lifecycle_context:
  current_stage_claim: string
  stage_confidence: string
  stage_source_date: YYYY-MM-DD-or-empty
  delivery_model_claim: string
  package_and_staging_notes: []
systems: []
information_and_bim:
  profile: string
  restrictions: []
stakeholders_and_authority:
  actors: []
  unresolved_authority_questions: []
evidence_burden: {}
capability_requirements: []
regulatory_context:
  source_references: []
  applicability_claims: []
  compliance_claims: []
  human_review_required: true
security_and_publication:
  classification: public|restricted|confidential|mixed
  public_repository_exclusions: []
uncertainty_and_gaps: []
evidence_references: []
review:
  prepared_by: string
  reviewed_by: []
  review_status: string
  next_review_trigger: string
decision_authority_transferred: false
implementation_authorized: false
```

## 16. Classification Procedure

### Step 1 — Define the Boundary

State exactly what project, asset, programme, site, or work package the genome covers.

### Step 2 — Gather Attributable Evidence

Use project records, official sources, authorised documents, public sources, and clearly labelled assumptions. Record source dates, versions, access restrictions, and confidence.

### Step 3 — Separate Facts, Claims, and Unknowns

Do not convert a proposal, future intention, secondary report, or assumption into a verified project fact.

### Step 4 — Assign Provisional Typology and Scale

Choose the internal operating-scale class and explain the evidence-based rationale.

### Step 5 — Assess Complexity Dimensions

Record each dimension, its evidence, limitations, and unresolved questions.

### Step 6 — Assign Provisional Governance Depth

Select the minimum governance depth needed to keep evidence, claims, reviews, decisions, and change visible.

### Step 7 — Define Evidence Burden and Capability Needs

Identify which evidence categories and specialist capabilities are expected across the lifecycle.

### Step 8 — Record Regulatory and Authority Questions

Link relevant sources and claims while reserving applicability, compliance, approval, certification, and professional conclusions for authorised human review.

### Step 9 — Apply Security and Publication Controls

Separate public, restricted, confidential, copyrighted, personal, and critical-infrastructure material.

### Step 10 — Human Review and Ledger Record

Record who reviewed the genome, in what capacity, with what limitations, and which changes or decisions were recorded.

## 17. Classification Confidence

Each significant genome field should use one of the following confidence labels where appropriate:

- `VERIFIED_FROM_PRIMARY_OR_AUTHORISED_SOURCE`;
- `CORROBORATED_FROM_MULTIPLE_INDEPENDENT_SOURCES`;
- `REPORTED_NOT_PRIMARY_SOURCE_VERIFIED`;
- `PROPOSED_OR_FUTURE_INTENTION`;
- `ASSUMPTION_FOR_PLANNING_ONLY`;
- `UNKNOWN`;
- `RESTRICTED_REQUIRES_AUTHORISED_REVIEW`;
- `SUPERSEDED`.

Repeated secondary reporting from the same original announcement does not create independent corroboration.

## 18. Reclassification and Escalation Triggers

The genome must be reviewed when:

- project scope or site changes materially;
- a candidate becomes an approved project, demonstration, or pilot;
- a new jurisdiction, authority, approval pathway, or statutory source becomes relevant;
- project scale, staging, delivery model, asset use, or system composition changes;
- high-consequence complexity is discovered;
- confidential or critical-infrastructure material enters scope;
- a major source, NCC edition, standard, law, regulation, consent, or condition changes;
- a lifecycle stage, package, or operational transition is proposed;
- new evidence contradicts an existing classification;
- a professional or decision-authority relationship changes;
- implementation authorization is proposed.

Reclassification must preserve prior versions and explain the reason for change.

## 19. Candidate Demonstration Profiles

These profiles test the standard only. They do not select live pilots.

### 19.1 Fictional Small Example

```text
Candidate: single-dwelling energy and accessibility retrofit
Operating scale: BOS-S
Indicative governance depth: GD-1 or GD-2
Key escalation signals: structural change, heritage, bushfire, flood, major electrical work, occupancy change, unresolved approvals
Status: fictional classification example only
```

### 19.2 Fictional Medium Example

```text
Candidate: regional multi-purpose community facility with energy, water, landscape, and public-use interfaces
Operating scale: BOS-M
Indicative governance depth: GD-2 or GD-3
Key escalation signals: multiple funding bodies, public procurement, environmental assessment, multi-discipline commissioning, operational handover
Status: fictional classification example only
```

### 19.3 NEXTDC S7 Sydney Candidate Learning Case

The S7 profile may be used to test a provisional classification such as:

```text
Candidate status: research and learning case only
Possible asset family: data centre and digital infrastructure; campus or precinct
Possible operating scale: BOS-LC
Likely complexity signals: systems, evidence, lifecycle, delivery, jurisdiction, security, commissioning, operations, climate risk
Likely governance depth for a comparable authorised project: GD-4
Official project stage: not determined by this standard
Live BuildingOS pilot status: not approved
Decision authority: not transferred
```

This is a BuildingOS planning hypothesis based on the candidate profile. It is not an official classification of the S7 project, a representation by NEXTDC or OpenAI, or evidence of project approval, design, construction, operation, resilience, compliance, or participation in BuildingOS.

## 20. Mapping to Frozen Core Batch 01

- `Actor` — genome preparer, source custodian, reviewer, project actor, authority contact, specialist, or decision-maker.
- `Evidence` — project records, official sources, authorised documents, public reports, models, drawings, tests, observations, and source metadata.
- `Claim` — project identity, scale, stage, typology, complexity, applicability, evidence-burden, or capability proposition.
- `Review` — attributed human assessment of genome content without automatic decision authority.
- `Procedure` — the documented classification and review method without execution capability.
- `Lifecycle` — the recorded genome state and project stage claim without automatic transition.
- `RegisteredObject` — project, site, asset, system, package, source, stage, or other genome subject.
- `GovernanceLedgerEntry` — creation, review, correction, reclassification, supersession, or decision event.
- `ModuleContract` — future declared boundaries between genome, lifecycle, regulatory, capability, evidence-intake, and interface components.
- `ConformanceResult` — a future bounded assessment against an approved documentation or implementation contract, only after separate authorization.

No Core object, test, workflow, or runtime behaviour is changed by this standard.

## 21. Human Review Questions

A reviewer should be able to answer:

1. Is the project boundary explicit?
2. Are live, proposed, candidate, and research-only states distinguished?
3. Are operating-scale labels separated from statutory classifications?
4. Is each consequential classification supported by evidence or labelled as an assumption?
5. Are unknowns and contradictory sources visible?
6. Does governance depth reflect consequence and uncertainty, not merely project size?
7. Are evidence burden and capability needs traceable to project characteristics?
8. Are jurisdiction and regulatory references versioned and reserved for human review?
9. Are professional and decision-authority claims sourced and scoped?
10. Are privacy, confidentiality, licensing, copyright, and security boundaries visible?
11. Can the genome inform a Lifecycle Stage Graph without causing an automatic transition?
12. Can the record be read outside Obsidian and traced through GitHub history?
13. Does the record avoid legal advice, certification conclusions, and unauthorised implementation?

## 22. Implementation Boundary

This standard does not authorize:

- changes to frozen Foundation or Core Batch 01 records or code;
- a Project Genome database or executable schema;
- APIs, connectors, queues, webhooks, MCP tools, generic agent runtimes, QClaw, or n8n;
- permissions or user management;
- automated classification, scoring, approval, or lifecycle transition;
- production interface or application migration;
- regulatory-source connectors;
- duplication of controlled legal, standards, confidential, or security-sensitive content;
- legal, compliance, certification, planning, engineering-signoff, contractual, safety, or professional conclusions;
- activation of S7 or any other live pilot.

## Current Safe Next Action

Define the documentation-only BuildingOS Lifecycle Stage Graph Architecture using this Project Genome standard to describe stage selection, branches, loops, gates, required evidence, human reviews, decisions, and re-entry conditions without introducing automatic transitions or implementation code.
