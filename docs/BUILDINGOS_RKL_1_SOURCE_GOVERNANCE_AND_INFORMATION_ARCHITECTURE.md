# BuildingOS RKL-1 Source Governance and Information Architecture

## Record Status

`DOCUMENTATION_ARCHITECTURE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

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

## RKL-1 Scope

RKL-1 defines documentation architecture for:

1. authoritative-source identification;
2. source-type vocabulary;
3. source metadata and stable identity;
4. edition, version, amendment, commencement, adoption, and effective-date context;
5. jurisdiction and geographic scope;
6. referenced-document relationships;
7. project and lifecycle-stage references;
8. applicability and compliance-related claims;
9. human review and competence context;
10. source change, supersession, and re-review;
11. repository and Knowledge Garden organisation;
12. manual, reviewable source-governance procedures.

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

## 1. Australian National Construction Code

The source architecture should support metadata for:

- NCC edition;
- volume;
- amendment, correction, or errata;
- publication date;
- adoption or commencement context;
- transition arrangements;
- state or territory variation;
- referenced documents;
- official publisher and URL;
- access date;
- effective-from and effective-to context;
- source status;
- supersession relationship.

The newest published edition must not be assumed to apply automatically to every project.

## 2. Referenced Standards

The architecture should support metadata for:

- standard identifier;
- title;
- issuing body;
- edition, revision, amendment, or reconfirmation;
- publication date;
- NCC, legislative, contractual, or project reference relationship;
- access method;
- copyright and licensing note;
- official or authorised location;
- project applicability claim;
- human review status;
- supersession relationship.

Full copyrighted standards must not be reproduced without clear permission or licence.

## 3. NSW Legislation and Regulation

The architecture should support official metadata for:

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
- version-specific URL;
- accessed-on date;
- geographic and jurisdiction scope;
- relationship to planning, building, environment, water, heritage, safety, operation, or other project subjects.

The source register should remain selective and project-driven rather than attempting to mirror the entire NSW legal corpus.

## 4. Commonwealth, State, Territory, and Local Variations

The architecture should distinguish:

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

Every source record should declare an authority class.

### `OFFICIAL_PRIMARY`

Material published by the responsible legislature, regulator, authority, code publisher, court, consent authority, or standards body.

### `OFFICIAL_DERIVED`

Official explanatory, guidance, practice, FAQ, or summary material that is useful but subordinate to the controlling source.

### `AUTHORISED_PROJECT_RECORD`

A project-specific approval, consent, certificate, report, drawing, specification, review, inspection, test, or other record supplied under lawful project authority.

### `PROFESSIONAL_SECONDARY`

A practitioner, legal, technical, industry, academic, or professional-body analysis that is not itself controlling authority.

### `PUBLIC_SECONDARY`

News, corporate announcement, public database, website, or other secondary source requiring careful verification.

### `AI_GENERATED_SUMMARY`

A machine-generated summary that must remain visibly subordinate to its sources and cannot be treated as authoritative.

### `UNVERIFIED`

A source or statement that has not yet been verified sufficiently for consequential use.

Authority class does not determine legal effect. It describes source provenance and expected review treatment.

## Core Documentation Records

## 1. Regulatory Source Record

Minimum fields:

```yaml
record_type: regulatory-source
record_id: stable-string
title: string
source_type: string
authority_class: OFFICIAL_PRIMARY|OFFICIAL_DERIVED|AUTHORISED_PROJECT_RECORD|PROFESSIONAL_SECONDARY|PUBLIC_SECONDARY|AI_GENERATED_SUMMARY|UNVERIFIED
issuing_authority: string
jurisdiction: string
geographic_scope: string
official_url: string
source_identifier: string
edition_or_version: string
amendment: string
publication_date: YYYY-MM-DD-or-empty
commencement_date: YYYY-MM-DD-or-empty
effective_from: YYYY-MM-DD-or-empty
effective_to: YYYY-MM-DD-or-empty
status: in-force|historical|future|repealed|superseded|draft|unknown
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

## 2. Regulatory Provision Reference

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

The reference record must not reproduce controlled content beyond lawful and necessary use.

## 3. Regulatory Relationship Record

Describes a relationship such as:

- NCC references standard;
- Act authorises regulation;
- regulation supports approval pathway;
- state varies national provision;
- local instrument applies within a geographic area;
- approval condition refers to a report or standard;
- amendment supersedes a prior version;
- project claim cites a provision;
- source change triggers re-review.

Minimum fields:

- relationship ID;
- source record A;
- relationship type;
- source record B;
- effective period;
- evidence;
- uncertainty;
- reviewer;
- supersession state.

## 4. Project Regulatory Reference

Connects a source or provision to:

- Project Genome;
- site;
- building or asset;
- system;
- design element;
- lifecycle stage;
- approval;
- inspection;
- test;
- commissioning activity;
- operational obligation;
- adaptation or end-of-life activity.

The reference identifies a review need. It does not determine applicability.

## 5. Applicability Claim

A bounded claim that a source or provision may, may not, or is not yet known to apply to a defined project subject.

Minimum fields:

- claim ID;
- project and subject;
- jurisdiction;
- source and exact version;
- effective date considered;
- project date or decision context;
- assumptions;
- supporting evidence;
- contradicting evidence;
- uncertainty;
- exclusions;
- review status;
- reviewer identity and capacity;
- review date;
- re-review trigger;
- external legal or authority confirmation required.

An applicability claim is not a legal determination.

## 6. Compliance-Related Claim

A bounded statement about the relationship between a defined project state and a defined requirement.

Minimum fields:

- claim ID;
- exact subject assessed;
- requirement and source version;
- design, construction, as-built, commissioned, or operational state considered;
- evidence reviewed;
- method or review basis;
- exclusions and limitations;
- defects or outstanding items;
- reviewer identity and attributed capacity;
- review date;
- validity or expiry context;
- re-review trigger;
- required external certification or approval;
- explicit statement that the record is not general certification.

BuildingOS must not present a compliance-related claim as a certificate, consent, approval, or universal conclusion.

## 7. Human Review Record

Minimum fields:

- review ID;
- reviewer identity;
- attributed role or capacity;
- evidence of competence or authority where relevant;
- review scope;
- sources and claims reviewed;
- date and effective-date context;
- findings;
- limitations;
- conflicts or dissent;
- recommendation where applicable;
- decision authority boundary;
- re-review trigger.

System access does not establish competence or authority.

## 8. Source Change Notice

Minimum fields:

- notice ID;
- source record;
- detected or reported change;
- previous version;
- new or candidate version;
- publication or effective date;
- detection source;
- verification state;
- potentially affected projects, claims, stages, and decisions;
- reviewer;
- required follow-up;
- closure or supersession relationship.

A change notice must not silently rewrite existing claims or lifecycle records.

## 9. Regulatory Review Queue Item

A documentation-only record identifying a matter that requires human attention.

Possible reasons:

- source version changed;
- effective date reached;
- transition period ending;
- project scope changed;
- jurisdiction changed;
- approval condition added or modified;
- evidence superseded;
- claim expired;
- reviewer requested re-review;
- conflicting official sources;
- missing or inaccessible standard;
- uncertain legal or authority pathway.

A queue item does not create workflow execution or a permission system.

## Source Identity Rules

1. Each source record should have a stable repository ID independent of title changes.
2. Each edition, version, or materially different legal state should remain distinguishable.
3. Historical records should remain linked rather than overwritten.
4. Official URLs should be preserved with accessed-on dates.
5. A source title alone is insufficient identity.
6. Consolidated, point-in-time, historical, future, and repealed versions must be distinguished.
7. Project references must identify the source version and date context considered.
8. Unknown version or effective-date context must be visible.

## Version and Effective-Date Model

The architecture should distinguish:

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

## Source Status Model

Suggested source states:

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

Status is descriptive and must identify the authority and date context supporting it.

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

## Source-Governance Procedure

RKL-1 defines the following manual, reviewable procedure:

```text
Identify Project Question
→ Locate Candidate Official Source
→ Verify Authority and Exact Version
→ Record Publication, Commencement, Effective Date, and Jurisdiction Context
→ Record Licensing and Access Boundary
→ Link Related Sources and Supersession
→ Draft Bounded Applicability or Compliance-Related Claim
→ Obtain Attributed Human Review
→ Record Limitations and Re-review Trigger
→ Link to Project Genome and Lifecycle Stage
→ Preserve Change and Review History
```

No step is automatically executed by this architecture.

## Source Selection Priority

When sources conflict or overlap, the documentation process should prefer:

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

Regulatory records may be linked to stage entry, exit, hold, review, and re-entry conditions.

Examples:

- planning source change before application;
- approval condition before design release;
- NCC or standard version question before technical documentation;
- inspection or certification evidence before handover;
- operational obligation before service commencement;
- source change triggering adaptation or re-review.

The Regulatory Knowledge Layer may trigger a review need in documentation. It must not automatically move the Lifecycle Stage Graph.

## Human Interface Relationship

A future read-only interface may show:

- source identity and authority class;
- exact version and effective-date context;
- jurisdiction;
- related and superseded sources;
- project references;
- applicability and compliance-related claims;
- reviewer identity, capacity, findings, and limitations;
- source-change notices;
- unresolved questions;
- re-review triggers;
- links to official sources and approved repository records.

The interface must display a clear disclaimer that BuildingOS is not providing legal or certification advice.

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
- official URLs;
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
- security-sensitive or critical-infrastructure information.

## Quality Checks

Every consequential regulatory record should be checked for:

1. stable identity;
2. official or clearly classified source authority;
3. exact version or explicit uncertainty;
4. publication, commencement, effective-date, and access-date context;
5. jurisdiction and geographic scope;
6. licensing and access boundary;
7. supersession relationship;
8. project and lifecycle relationship;
9. claim scope and limitations;
10. supporting and contradicting evidence;
11. human reviewer and capacity;
12. re-review trigger;
13. authoritative-source link;
14. no legal, certification, or professional overclaim;
15. no automatic lifecycle or project effect.

## Manual Fictional Demonstration Boundary

A future RKL-2 demonstration may use fictional examples for:

- NCC source metadata;
- referenced-standard metadata;
- NSW legislation or regulation metadata;
- jurisdictional variation;
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
- privacy, publication, and security boundaries are approved;
- data and interface architecture are separately reviewed;
- explicit Chief Architect implementation authorization is issued.

## Current Decision

```text
RKL_1_SOURCE_GOVERNANCE_AND_INFORMATION_ARCHITECTURE_V0_1_PREPARED
DOCUMENTATION_ONLY
NO_SOURCE_CONNECTOR_AUTHORIZATION
NO_LEGAL_OR_CERTIFICATION_AUTHORITY
NO_IMPLEMENTATION_AUTHORIZATION
```

## Next Safe Activity

The next safe action is a bounded review of RKL-1 against the combined BuildingOS documentation architecture.

After review, a fictional RKL-2 demonstration set may be proposed only under separate documentation approval. Any live source connector, automated monitoring, database, production interface, legal conclusion, certification function, or implementation code requires explicit Chief Architect authorization.