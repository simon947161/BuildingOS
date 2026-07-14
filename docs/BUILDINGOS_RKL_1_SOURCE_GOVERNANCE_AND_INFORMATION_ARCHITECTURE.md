# BuildingOS RKL-1 Source Governance and Information Architecture

## Record Status

`DOCUMENTATION_ARCHITECTURE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-14

## Bounded Correction Date

2026-07-14

## Purpose

Define the first documentation-only information architecture for a future BuildingOS Regulatory Knowledge Layer covering source governance, version and effective-date context, jurisdictional variation, project references, applicability and compliance-related claims, source change, supersession, and mandatory human review.

This record does not authorize source connectors, web scraping, automated monitoring, a database, API, permissions, workflow execution, legal interpretation, certification, compliance approval, or production interface implementation.

## Governing Principle

```text
Official sources remain authoritative.
BuildingOS records what source was considered, in which version, for which project question, by whom, and with what limitations.
```

## Relationship to Frozen Foundation and Core

RKL-1 consumes the frozen Governance Kernel concepts without modifying them:

- `Actor` — source curator, author, project participant, reviewer, practitioner, or authority contact;
- `Evidence` — official source metadata, source link, amendment notice, project document, inspection record, or lawful source excerpt;
- `Claim` — project-specific applicability or compliance-related statement with explicit limitations;
- `Review` — attributed human assessment without autonomous decision authority;
- `Procedure` — documented source research, update, and review procedure without automatic execution;
- `Lifecycle` — recorded source, claim, and review state without automatic transition;
- `RegisteredObject` — project, source, instrument, standard, design item, approval, asset, or regulated subject reference;
- `GovernanceLedgerEntry` — traceable registration, review, change, supersession, correction, or decision event;
- `ModuleContract` — future declared inputs, outputs, obligations, and exclusions.

The frozen C00 through C01-I Foundation and Core Batch 01 baseline remain unchanged.

## Scope

RKL-1 defines documentation architecture for:

1. authoritative-source identification;
2. source-type and authority vocabulary;
3. source metadata and stable identity;
4. edition, version, amendment, commencement, adoption, transition, and effective-date context;
5. public, restricted, confidential, licensed, archived, and authorised source locators;
6. jurisdiction and geographic scope;
7. referenced-document relationships;
8. project and lifecycle-stage references;
9. applicability and compliance-related claims;
10. human review and competence context;
11. source change, supersession, and re-review;
12. repository and Knowledge Garden organisation;
13. manual, reviewable source-governance procedures.

## Explicit Exclusions

RKL-1 does not:

- determine which law applies;
- interpret legislation for a project;
- certify NCC or standards compliance;
- replace a lawyer, certifier, consent authority, planner, engineer, building surveyor, accredited practitioner, regulator, standards owner, or other qualified professional;
- copy the NCC, standards, legislation, paid legal databases, or protected guidance into a shadow repository;
- authorize regulatory connectors or automated monitoring;
- silently update project claims when a source changes;
- create executable data models or schemas;
- authorize a live pilot.

## Planned Source Coverage

### 1. Australian National Construction Code

Support metadata for:

- NCC edition and volume;
- amendment, correction, or errata;
- publication date;
- adoption and commencement context;
- transition arrangements;
- state or territory variation;
- referenced documents;
- official publisher and locator;
- access date;
- effective-from and effective-to context;
- source status;
- supersession relationship.

The newest published edition must not be assumed to apply automatically to every project.

### 2. Referenced Standards

Support metadata for:

- standard identifier and title;
- issuing body;
- edition, revision, amendment, or reconfirmation;
- publication date;
- NCC, legislative, contractual, or project relationship;
- access method and source locator;
- copyright and licensing note;
- project applicability claim;
- human review status;
- supersession relationship.

Full copyrighted standards must not be reproduced without clear permission or licence.

### 3. NSW Legislation and Regulation

Support official metadata for:

- Act;
- regulation;
- environmental planning instrument;
- commencement instrument;
- amendment;
- savings or transitional provision;
- historical version;
- future or not-yet-commenced provision;
- repeal status;
- approval or consent record;
- authority guideline or practice note;
- official publication authority;
- version-specific locator;
- accessed-on date;
- geographic and jurisdiction scope;
- relationship to planning, building, environment, water, heritage, safety, operation, or other project subjects.

The source register should remain selective and project-driven rather than attempting to mirror the complete NSW legal corpus.

### 4. Commonwealth, State, Territory, and Local Variations

Distinguish:

- national base source;
- adopting jurisdiction;
- varying jurisdiction;
- variation or addition;
- affected topic or provision;
- commencement and effective period;
- local planning or authority context;
- official evidence;
- applicability assumptions;
- reviewer;
- supersession relationship.

Local planning controls, consent conditions, approval pathways, and authority guidance must remain distinguishable from legislation, regulation, the NCC, and referenced standards.

## Source Authority Classes

Every source record should declare one authority class:

- `OFFICIAL_PRIMARY`;
- `OFFICIAL_DERIVED`;
- `AUTHORISED_PROJECT_RECORD`;
- `PROFESSIONAL_SECONDARY`;
- `PUBLIC_SECONDARY`;
- `AI_GENERATED_SUMMARY`;
- `UNVERIFIED`.

Authority class describes provenance and expected review treatment. It does not independently determine legal effect.

## Canonical Source Status Vocabulary

RKL-1 uses one canonical source-status vocabulary:

- `DRAFT`;
- `PUBLISHED_NOT_YET_EFFECTIVE`;
- `IN_FORCE_OR_CURRENT`;
- `TRANSITIONAL`;
- `HISTORICAL`;
- `REPEALED`;
- `SUPERSEDED`;
- `WITHDRAWN`;
- `UNKNOWN`;
- `REQUIRES_HUMAN_VERIFICATION`.

All illustrative records, indexes, and future fictional demonstrations must use this vocabulary or explicitly declare a reviewed mapping.

Source status is descriptive and must identify the authority, version, jurisdiction, and date context supporting it.

## Source Locator and Access Model

A regulatory source may be publicly available, restricted, licensed, archived, held in an authorised project system, or available only through metadata.

Every source record should distinguish:

- `public_official_url` — public official URL when available;
- `authorised_source_locator` — non-public or system-specific reference when lawfully available;
- `access_boundary` — `PUBLIC`, `RESTRICTED`, `CONFIDENTIAL`, `LICENSED`, or `UNKNOWN`;
- `storage_policy` — `METADATA_ONLY`, `LINK_ONLY`, `LAWFUL_EXCERPT`, or `AUTHORISED_PROJECT_REFERENCE`;
- `access_note` — human-readable access and handling limitations.

A public URL is not mandatory when a lawful authorised locator or metadata-only record is appropriate.

At least one source-identification route must exist, but restricted or confidential locators must not be exposed in public records.

## Core Documentation Records

### 1. Regulatory Source Record

Illustrative minimum fields:

```yaml
record_type: regulatory-source
record_id: stable-string
title: string
source_type: string
authority_class: OFFICIAL_PRIMARY|OFFICIAL_DERIVED|AUTHORISED_PROJECT_RECORD|PROFESSIONAL_SECONDARY|PUBLIC_SECONDARY|AI_GENERATED_SUMMARY|UNVERIFIED
issuing_authority: string
jurisdiction: string
geographic_scope: string
public_official_url: string-or-empty
authorised_source_locator: string-or-empty
access_boundary: PUBLIC|RESTRICTED|CONFIDENTIAL|LICENSED|UNKNOWN
storage_policy: METADATA_ONLY|LINK_ONLY|LAWFUL_EXCERPT|AUTHORISED_PROJECT_REFERENCE
access_note: string
source_identifier: string
edition_or_version: string
amendment: string
publication_date: YYYY-MM-DD-or-empty
commencement_date: YYYY-MM-DD-or-empty
effective_from: YYYY-MM-DD-or-empty
effective_to: YYYY-MM-DD-or-empty
status: DRAFT|PUBLISHED_NOT_YET_EFFECTIVE|IN_FORCE_OR_CURRENT|TRANSITIONAL|HISTORICAL|REPEALED|SUPERSEDED|WITHDRAWN|UNKNOWN|REQUIRES_HUMAN_VERIFICATION
accessed_on: YYYY-MM-DD
licensing_note: string
supersedes: []
superseded_by: []
related_sources: []
review_status: unreviewed|reviewed|needs-re-review
reviewer: string-or-empty
limitations: []
```

This is a documentation model, not an approved database schema.

### 2. Regulatory Provision Reference

A bounded reference to a section, clause, part, schedule, performance requirement, deemed-to-satisfy provision, standard clause, approval condition, guideline section, or other defined source location.

Minimum fields:

- provision reference ID;
- parent source record;
- exact citation or locator;
- short user-authored topic description;
- source version;
- effective-date context;
- jurisdiction;
- lawful excerpt or no-copy note;
- related project subject;
- limitations;
- review status.

### 3. Regulatory Relationship Record

Describes relationships such as:

- NCC references standard;
- Act authorises regulation;
- regulation supports approval pathway;
- state varies national provision;
- local instrument applies within a geographic area;
- approval condition refers to a report or standard;
- amendment supersedes a prior version;
- project claim cites a provision;
- source change triggers re-review.

### 4. Project Regulatory Reference

Connects a source or provision to a Project Genome, site, building, asset, system, design element, lifecycle stage, approval, inspection, test, commissioning activity, operational obligation, adaptation, or end-of-life activity.

The reference identifies a review need. It does not determine applicability.

### 5. Applicability Claim

A bounded claim that a source or provision may, may not, or is not yet known to apply to a defined project subject.

It must identify:

- project and subject;
- jurisdiction;
- source and exact version;
- effective date considered;
- project date or decision context;
- assumptions;
- supporting and contradicting evidence;
- uncertainty and exclusions;
- reviewer identity and capacity;
- review date;
- re-review trigger;
- whether external legal or authority confirmation is required.

An applicability claim is not a legal determination.

### 6. Compliance-Related Claim

A bounded statement about the relationship between a defined project state and a defined requirement.

It must identify:

- exact subject assessed;
- requirement and source version;
- design, construction, as-built, commissioned, or operational state considered;
- evidence reviewed;
- method or review basis;
- exclusions, limitations, defects, and outstanding items;
- reviewer identity and attributed capacity;
- review date and validity context;
- re-review trigger;
- required external certification or approval;
- explicit statement that the record is not general certification.

BuildingOS must not present a compliance-related claim as a certificate, consent, approval, or universal conclusion.

### 7. Human Review Record

A review record must identify:

- reviewer identity;
- attributed role or capacity;
- evidence of competence or authority where relevant;
- review scope;
- sources and claims reviewed;
- date and effective-date context;
- findings and limitations;
- conflicts or dissent;
- recommendation where applicable;
- decision-authority boundary;
- re-review trigger.

System access does not establish competence or authority.

### 8. Source Change Notice

A source-change notice should identify:

- prior and candidate versions;
- publication or effective date;
- detection source;
- verification state;
- affected projects, claims, stages, and decisions;
- reviewer;
- required follow-up;
- closure and supersession relationships.

A change notice must not silently rewrite existing claims or lifecycle records.

### 9. Regulatory Review Queue Item

A documentation-only record may identify matters requiring human attention, such as:

- source version changed;
- effective date reached;
- transition period ending;
- project scope or jurisdiction changed;
- approval condition changed;
- evidence superseded;
- claim expired;
- conflicting official sources;
- missing or inaccessible standard;
- uncertain legal or authority pathway.

A queue item does not create workflow execution or permissions.

## Source Identity Rules

1. Each source record should have a stable repository ID independent of title changes.
2. Each edition, version, or materially different legal state should remain distinguishable.
3. Historical records should remain linked rather than overwritten.
4. Public URLs should be preserved with access dates when available.
5. Restricted source locators should remain controlled and must not be exposed publicly.
6. A source title alone is insufficient identity.
7. Consolidated, point-in-time, historical, future, and repealed versions must be distinguished.
8. Project references must identify the source version and date context considered.
9. Unknown version or effective-date context must remain visible.

## Version and Effective-Date Model

Distinguish:

- publication date;
- assent or issue date;
- commencement date;
- adoption date;
- effective-from date;
- effective-to date;
- repeal date;
- transition period;
- project decision date;
- approval date;
- construction or installation date;
- inspection or certification date;
- access date;
- review date.

These dates must not be collapsed into one generic date field.

## Jurisdiction Model

Every consequential record should distinguish where relevant:

- Commonwealth;
- state or territory;
- local government area;
- consent or approval authority;
- site or corridor;
- cross-border or multi-jurisdiction context;
- national source with local variation;
- project-specific condition;
- geographic uncertainty.

The system must not flatten multiple jurisdictions into one answer.

## Manual Source-Governance Procedure

```text
Identify Project Question
→ Locate Candidate Official Source
→ Verify Authority and Exact Version
→ Record Publication, Commencement, Effective Date, and Jurisdiction Context
→ Record Public or Authorised Locator, Access Boundary, Storage Policy, and Licensing Limits
→ Link Related Sources and Supersession
→ Draft Bounded Applicability or Compliance-Related Claim
→ Obtain Attributed Human Review
→ Record Limitations and Re-review Trigger
→ Link to Project Genome and Lifecycle Stage
→ Preserve Change and Review History
```

No step is automatically executed by this architecture.

## Source Selection Priority

When sources conflict or overlap, documentation should prefer:

1. exact official controlling source;
2. official point-in-time or versioned source;
3. official amendment, commencement, adoption, or variation record;
4. official explanatory material;
5. authorised project approval or condition;
6. professional secondary analysis;
7. public secondary reporting;
8. AI-generated summary;
9. unverified material.

Priority does not replace qualified human legal or professional judgment.

## Change and Supersession Procedure

When a source change is identified:

1. register the change notice;
2. verify the official source and version;
3. preserve the prior source record;
4. identify affected project references, claims, reviews, stages, and decisions;
5. determine whether the change is published, effective, transitional, historical, or uncertain;
6. request human re-review;
7. create revised claims only when supported;
8. link superseded and successor records;
9. record the review and decision history;
10. do not silently alter past project decisions or external approvals.

## Lifecycle Stage Graph Relationship

Regulatory records may link to stage entry, exit, hold, review, and re-entry conditions.

The Regulatory Knowledge Layer may identify a review need or hold condition in documentation. It must not automatically move a Lifecycle Stage Graph node or edge.

## Human Interface Relationship

A future read-only interface may show:

- source identity and authority class;
- exact version and effective-date context;
- jurisdiction;
- public or controlled source-locator status without exposing restricted locators;
- related and superseded sources;
- project references;
- applicability and compliance-related claims;
- reviewer identity, capacity, findings, and limitations;
- source-change notices;
- unresolved questions;
- re-review triggers;
- links to official sources and approved repository records.

The interface must state clearly that BuildingOS is not providing legal or certification advice.

## Repository Information Architecture

A future approved Markdown-first structure may use:

```text
docs/regulatory/
  INDEX.md
  SOURCES_INDEX.md
  JURISDICTIONS_INDEX.md
  CLAIMS_INDEX.md
  REVIEWS_INDEX.md
  CHANGE_NOTICES_INDEX.md
  sources/
  provisions/
  relationships/
  jurisdictions/
  project-references/
  claims/
  reviews/
  change-notices/
  procedures/

docs/knowledge-garden/
  INDEX.md
  MAP_OF_CONTENT.md
```

These directories are planning proposals only and are not created by this record.

## Markdown and Knowledge Garden Rules

1. GitHub `main` remains authoritative for approved records.
2. Stable Markdown filenames and record IDs are required.
3. Ordinary Markdown links should be preferred in authoritative files.
4. Backlinks, indexes, and maps of content should remain readable outside Obsidian.
5. Simple YAML frontmatter may support navigation but is not an approved runtime schema.
6. Draft and private research areas must remain distinguishable from approved records.
7. Promotion requires reviewable diff, pull request, or equivalent recorded review.
8. Blind two-way synchronisation is prohibited.
9. Official legal and standards content must be linked and cited rather than copied into a shadow library.
10. Confidential project information and security-sensitive material must remain outside public records.

## Licensing and Content Boundaries

The repository may preserve:

- source metadata;
- public official URLs and controlled locator metadata;
- identifiers;
- version and date context;
- lawful short excerpts where necessary and permitted;
- user-authored summaries;
- project-specific references;
- claims, reviews, and change notes.

The repository must not preserve without authority:

- full copyrighted standards;
- copied NCC or legal databases beyond lawful use;
- paid subscription content;
- confidential legal advice;
- confidential project approvals or reports;
- personal information;
- restricted source-system locators in public records;
- security-sensitive or critical-infrastructure information.

## Quality Checks

Every consequential regulatory record should be checked for:

1. stable identity;
2. official or clearly classified source authority;
3. exact version or explicit uncertainty;
4. canonical source status;
5. publication, commencement, effective-date, and access-date context;
6. jurisdiction and geographic scope;
7. public or authorised locator, access boundary, and storage policy;
8. licensing and content boundary;
9. supersession relationship;
10. project and lifecycle relationship;
11. claim scope and limitations;
12. supporting and contradicting evidence;
13. human reviewer and capacity;
14. re-review trigger;
15. no legal, certification, or professional overclaim;
16. no automatic lifecycle or project effect.

## Manual Fictional Demonstration Boundary

A future RKL-2 demonstration may use fictional examples for:

- NCC source metadata;
- referenced-standard metadata;
- NSW legislation or regulation metadata;
- jurisdictional variation;
- public and restricted locator handling;
- source change notice;
- applicability claim;
- compliance-related claim;
- human review;
- re-review trigger.

RKL-2 requires separate approval and must remain clearly fictional and non-advisory.

## Implementation Entry Criteria

No RKL implementation may begin until:

- RKL-1 architecture is reviewed;
- authoritative-source policy is approved;
- licensing policy is approved;
- human authority and reviewer requirements are approved;
- claim semantics are approved;
- change and supersession procedure is approved;
- privacy, publication, locator, and security boundaries are approved;
- data and interface architecture are separately reviewed;
- explicit Chief Architect implementation authorization is issued.

## Current Decision

```text
RKL_1_SOURCE_GOVERNANCE_AND_INFORMATION_ARCHITECTURE_V0_1_PREPARED
BOUNDED_DOCUMENTATION_CORRECTIONS_APPLIED
CANONICAL_STATUS_VOCABULARY_ESTABLISHED
PUBLIC_AND_RESTRICTED_SOURCE_LOCATORS_DISTINGUISHED
DOCUMENTATION_ONLY
NO_SOURCE_CONNECTOR_AUTHORIZATION
NO_LEGAL_OR_CERTIFICATION_AUTHORITY
NO_IMPLEMENTATION_AUTHORIZATION
```

## Next Safe Activity

RKL-1 is ready for a bounded correction verification.

After verification, RKL-2 fictional demonstration work remains separately gated. Any live source ingestion, connector, monitoring, database, API, permissions, workflow, production UI, legal conclusion, certification conclusion, or implementation code requires explicit Chief Architect authorization.