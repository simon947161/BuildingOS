# BuildingOS ClimateOS Cross-Domain Evidence Intake Contract

## Record Status

`DOCUMENTATION_CONTRACT_V0_1_NOT_RUNTIME_AUTHORIZATION`

## Prepared Date

2026-07-13

## Contract Parties

- **Evidence Producer:** ClimateOS or an explicitly identified ClimateOS research, modelling, observation, or source-curation workflow.
- **Evidence Receiver:** BuildingOS project-level evidence intake process.
- **Decision Authority:** Remains with identified and authorised humans outside this contract.

## Purpose

Define a documentation-only contract for transferring bounded climate, environmental, site, building, engineering-context, and provenance evidence from ClimateOS into BuildingOS.

This contract permits information exchange. It does not transfer conclusions, professional authority, approval rights, compliance status, lifecycle control, or runtime capability.

## Governing Principle

```text
ClimateOS may supply evidence.
BuildingOS may register and organise evidence.
Qualified humans decide what the evidence means for the project.
```

## Scope of Permitted Inputs

A ClimateOS evidence package may include the following categories when relevant to a defined BuildingOS project or asset.

### 1. Source and Provenance Evidence

- official or reputable source title;
- source publisher or custodian;
- source URL or stable reference;
- access date;
- publication, observation, model-run, or issue date;
- version, edition, dataset release, or revision identifier;
- licence, access, confidentiality, or reuse note;
- original file name and checksum when available;
- chain of custody or transformation history;
- distinction between primary, secondary, and derived material.

### 2. Site and Environmental Context

- site location and spatial reference;
- regional climate context;
- topography, catchment, drainage, flood, heat, wind, bushfire, drought, storm, coastal, soil, groundwater, vegetation, biodiversity, or air-quality observations;
- site exposure and sensitivity indicators;
- relevant observation periods and spatial resolution;
- known data gaps, uncertainty, and limitations.

### 3. Climate-Risk Evidence

- hazard observations and projections;
- scenarios and time horizons;
- model family and model-run metadata;
- downscaling or bias-correction method;
- baseline period;
- percentile, range, confidence, or uncertainty expression;
- exposure and sensitivity evidence;
- adaptation option evidence where clearly separated from decisions.

### 4. Building and Asset Context

- publicly documented or authorised building type, use, scale, site, and asset context;
- envelope, structural, architectural, or spatial evidence relevant to climate exposure;
- building services and MEP system descriptions;
- energy, water, cooling, ventilation, backup power, controls, and resilience context;
- fixtures, equipment, plant, and maintainable asset references;
- commissioning, handover, operational, and maintenance evidence;
- observed performance data where lawful and authorised.

### 5. BIM and Information-Management Evidence

- model, drawing, schedule, specification, asset register, or common-data-environment reference;
- authoring organisation and discipline;
- model or document revision;
- information status or suitability code where available;
- coordinate system, level of information need, and exchange format;
- object or system identifiers;
- known design-versus-as-built limitations;
- links to source files rather than uncontrolled duplication where appropriate.

### 6. Construction and Commissioning Evidence

- construction sequence or package context;
- installation records;
- inspection, test, and commissioning records;
- defects, non-conformances, unresolved items, and closure evidence;
- temporary works or staging information relevant to environmental or climate exposure;
- weather or environmental observations associated with construction events;
- provenance for photographs, field records, and test results.

### 7. Operations Evidence

- operational procedures and maintenance context;
- performance observations;
- energy, water, temperature, humidity, equipment, controls, alarms, and resilience data;
- incidents and recovery evidence;
- service history and asset-condition observations;
- declared privacy, cybersecurity, confidentiality, and access restrictions.

## Prohibited Imports

The following must not be imported as BuildingOS decisions or authoritative project conclusions:

- ClimateOS approval, rejection, go/no-go, or gate decisions;
- automated compliance, certification, legal, planning, engineering, environmental, safety, or contractual conclusions;
- unsupported statements that a project is safe, resilient, compliant, approved, viable, sustainable, or ready to proceed;
- lifecycle transitions triggered only by ClimateOS output;
- instructions to construct, operate, shut down, procure, pay, certify, or approve;
- agent, runtime, workflow, permission, or autonomous authority;
- hidden scores whose source, method, thresholds, or uncertainty cannot be inspected;
- conclusions detached from their supporting evidence and limitations;
- personal, confidential, security-sensitive, or copyrighted information without lawful authority to transfer it.

## Package-Level Minimum Manifest

Every intake package should identify:

```yaml
package_id: string
package_title: string
package_version: string
producer_system: ClimateOS
producer_workflow: string
producer_actor: string
prepared_on: YYYY-MM-DD
project_reference: string
asset_reference: string
geographic_scope: string
coordinate_reference_system: string-or-not-applicable
time_scope:
  observed_from: YYYY-MM-DD-or-empty
  observed_to: YYYY-MM-DD-or-empty
  projection_horizons: []
evidence_categories: []
source_count: integer
item_count: integer
licence_and_access_summary: string
confidentiality: public|restricted|confidential|mixed
method_summary: string
uncertainty_summary: string
known_gaps: []
declared_exclusions: []
requested_buildingos_use: string
human_review_required: true
decision_authority_transferred: false
```

This YAML block is a documentation example, not an implemented schema.

## Evidence-Item Minimum Fields

Each evidence item should expose, as applicable:

- stable item ID;
- title and short description;
- evidence category;
- subject project, asset, system, location, or lifecycle stage;
- source type;
- source publisher, author, or custodian;
- source reference or URL;
- source date and access date;
- version or revision;
- geographic extent and spatial resolution;
- temporal extent and frequency;
- units and variable definitions;
- method and transformation history;
- uncertainty and limitations;
- licensing, confidentiality, privacy, and security classification;
- related files and checksums;
- producer actor;
- review status;
- supersedes and superseded-by references;
- proposed BuildingOS claim links, if any;
- declared non-authority statement.

## Eligibility Tests

An evidence item is eligible for intake only when the receiving reviewer can answer:

1. **Identity:** What exactly is the item?
2. **Origin:** Who or what produced it?
3. **Time:** When was it observed, published, generated, or accessed?
4. **Place:** What location or spatial extent does it represent?
5. **Method:** How was it obtained or derived?
6. **Version:** Which release, revision, scenario, or model run is this?
7. **Meaning:** What variables, units, categories, or classifications are used?
8. **Limitations:** What does it not establish?
9. **Rights:** May BuildingOS lawfully store, reference, or display it?
10. **Authority:** Is it clearly separated from approval or professional judgement?

Failure of an eligibility test does not require deletion. The item may remain outside the accepted evidence set as pending, restricted, disputed, or rejected intake material.

## Evidence Quality Labels

A receiving BuildingOS workflow may apply a transparent review label such as:

- `RECEIVED_NOT_REVIEWED`;
- `SOURCE_IDENTITY_VERIFIED`;
- `PROVENANCE_INCOMPLETE`;
- `METHOD_INCOMPLETE`;
- `LICENCE_REVIEW_REQUIRED`;
- `CONFIDENTIAL_RESTRICTED`;
- `ELIGIBLE_FOR_PROJECT_EVIDENCE_REVIEW`;
- `ACCEPTED_AS_PROJECT_EVIDENCE`;
- `REJECTED_AS_PROJECT_EVIDENCE`;
- `SUPERSEDED`.

These are proposed documentation labels. They do not modify the frozen Core lifecycle model or create automatic transitions.

## Intake Procedure

### Step 1 — Package Receipt

Record the package identifier, producer, date, intended project, declared scope, and access restrictions.

### Step 2 — Boundary Check

Confirm that the package contains evidence rather than transferred decision authority, runtime instructions, or prohibited conclusions.

### Step 3 — Manifest Check

Check completeness of package and item metadata.

### Step 4 — Provenance and Rights Check

Verify source identity, version, dates, licence, confidentiality, privacy, and security restrictions.

### Step 5 — Technical Readability Check

Confirm that variables, units, coordinate systems, time horizons, methods, revisions, and file relationships are understandable.

### Step 6 — Project Relevance Review

Determine whether the item is relevant to the identified project, asset, system, stage, risk, claim, or decision question.

### Step 7 — Registration

Register accepted material through existing BuildingOS Evidence and Registered Object concepts without changing frozen Core types.

### Step 8 — Claim Separation

Create or link any BuildingOS claim separately. The evidence item itself must not silently become a project conclusion.

### Step 9 — Human Review

Record the human reviewer, review purpose, findings, competence boundary, limitations, and re-review trigger.

### Step 10 — Ledger Record

Record consequential intake, acceptance, rejection, supersession, restriction, or correction events through the Governance Ledger concept.

## Mapping to Frozen Core Batch 01

- `Actor` — ClimateOS producer, source custodian, BuildingOS intake reviewer, specialist reviewer, or decision-maker.
- `Evidence` — source record, observation, model output, report, drawing, schedule, BIM reference, field record, test result, or operational observation.
- `Claim` — a separately stated project proposition supported or challenged by evidence.
- `Review` — attributed human assessment without automatic decision authority.
- `Procedure` — the documented intake and review procedure without execution capability.
- `Lifecycle` — recorded package or evidence state without automatic transitions.
- `RegisteredObject` — project, site, asset, system, model, document, source, package, or evidence subject.
- `GovernanceLedgerEntry` — receipt, review, acceptance, rejection, restriction, correction, or supersession record.
- `ModuleContract` — this declared input, output, obligation, and exclusion boundary.
- `ConformanceResult` — a future bounded assessment of whether a package meets an approved contract, only after separate authorization.

No new Core type or Core code change is authorised by this contract.

## Output of a Successful Intake

A successful intake produces a reviewable project evidence package containing:

- an accepted package manifest;
- item-level provenance;
- explicit access restrictions;
- links to source material;
- recorded limitations and uncertainty;
- project and lifecycle relationships;
- separately stated claims;
- human review status;
- governance ledger references;
- unresolved questions and required follow-up.

It does not produce approval, compliance, certification, design acceptance, or authority to proceed.

## Change and Supersession

When ClimateOS provides a corrected, updated, or superseding item:

- preserve the prior item and its historical use;
- identify the relationship between versions;
- record the reason for change;
- identify affected BuildingOS claims and reviews;
- require human re-review where consequential;
- do not silently rewrite prior decisions or ledger history.

## Security and Confidentiality Boundary

Public-repository documentation must not expose:

- security-sensitive data-centre layouts or systems;
- detailed critical-infrastructure vulnerabilities;
- personal information;
- confidential design, contract, operational, or customer information;
- credentials, access details, network topology, or protected asset information.

A package may be represented by metadata and controlled references rather than copied files.

## S7 Sydney Candidate Package Relationship

The NEXTDC S7 Sydney evidence package may be prepared as a candidate large and complex project learning case under this contract.

Permitted learning categories include:

- project and site context;
- data-centre building typology;
- MEP and critical-service system categories;
- BIM and information-management needs;
- fixtures, plant, and maintainable asset categories;
- construction and commissioning evidence patterns;
- operational evidence needs;
- climate-risk and resilience evidence;
- source, version, date, and provenance requirements.

The package must not assert that S7 is an approved live BuildingOS pilot, disclose restricted critical-infrastructure information, or import ClimateOS conclusions as BuildingOS decisions.

## Regulatory Knowledge and Knowledge Garden Compatibility

Evidence packages should remain compatible with the planned Regulatory Knowledge Layer and Markdown-first Knowledge Garden by using:

- stable identifiers;
- portable Markdown indexes;
- explicit source and project links;
- version and effective-date metadata;
- lawful references rather than uncontrolled source duplication;
- GitHub review history as the authoritative approved record;
- controlled promotion of private research into public or authoritative documentation.

## Implementation Boundary

This contract does not authorize:

- a connector between ClimateOS and BuildingOS;
- automated data transfer;
- an API, database, queue, webhook, MCP tool, agent runtime, or n8n workflow;
- permissions or user management;
- automatic conformance scoring;
- automatic lifecycle transition;
- production interface work;
- modification of frozen Foundation or Core Batch 01 code.

## Current Safe Next Action

Prepare a documentation-only NEXTDC S7 Sydney candidate large-project evidence intake profile using public or otherwise authorised sources, clearly separating verified facts, reported information, assumptions, research questions, and prohibited material.