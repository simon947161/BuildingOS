# BuildingOS Regulatory Knowledge Layer and Knowledge Garden Compatibility Plan

## Record Status

`PLANNING_BASELINE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-12

## Status Refreshed

2026-07-14

## Purpose

Define a bounded future direction for a BuildingOS Regulatory Knowledge Layer and an Obsidian-compatible Knowledge Garden without changing the frozen M1 Foundation, the active Core Batch 01 implementation freeze, or the current documentation-only product architecture boundaries.

This plan is documentation only. It does not authorize implementation code, legal interpretation, certification, compliance approval, external integration, automated decisions, or production Operator Console implementation.

## Current Governance Relationship

Core Batch 01 was formally approved and frozen on 2026-07-13 at implementation baseline:

```text
f84b22bf4921e4f98e15598c5c5a5aa18bcaa996
```

The current post-freeze roadmap has prepared documentation baselines for Product North Star, cross-domain evidence intake, Project Genome, Lifecycle Stage Graph, Human Interface Architecture, a read-only Operator Console Prototype Brief, and pilot candidates.

This planning record does not modify the frozen Foundation or Core, select a live pilot, activate a regulatory capability, or authorize implementation.

## Product Intent

The future Regulatory Knowledge Layer should help a qualified human determine:

- which regulatory sources may be relevant to a project;
- which jurisdiction, edition, version, and effective date are being considered;
- what evidence supports an applicability or compliance-related claim;
- what assumptions and unresolved questions remain;
- who reviewed the claim and when it requires re-review;
- whether a source has been superseded, amended, delayed, varied, or replaced.

BuildingOS may retrieve, organise, compare, summarise, and draft. It must not present itself as a lawyer, building certifier, accredited practitioner, consent authority, standards owner, or final compliance decision-maker.

## Planned Regulatory Coverage

### 1. National Construction Code

Track official National Construction Code material published by the Australian Building Codes Board, including:

- the applicable NCC edition and volume;
- amendment or correction information;
- adoption and commencement context;
- referenced documents;
- state and territory variations;
- source URL, access date, version, and effective-date metadata.

Primary source starting points:

- `https://ncc.abcb.gov.au/`
- `https://www.abcb.gov.au/`

The repository should not assume that the newest published edition is automatically the legally applicable edition for every project.

### 2. Referenced Standards

Track metadata and project references for standards cited by the NCC or other governing instruments, including:

- standard identifier and title;
- issuing body;
- edition or revision;
- NCC or legislative reference relationship;
- access and licensing notes;
- project applicability claim;
- human review status.

Primary source starting point:

- `https://www.standards.org.au/`

BuildingOS must not reproduce copyrighted standards unless the repository has a clear licence or permission. Metadata, lawful citations, user-authored summaries, and links should be preferred.

### 3. New South Wales Legislation and Regulation

Track official NSW Acts, regulations, environmental planning instruments, and other relevant instruments through official sources, including:

- instrument title and identifier;
- source authority;
- in-force, historical, repealed, or future status;
- commencement and amendment dates;
- jurisdiction and geographic scope;
- relationships to approvals, certification, planning, construction, environment, water, heritage, safety, and operation;
- version-specific source link and access date.

Primary source starting point:

- `https://legislation.nsw.gov.au/`

The first source register should remain selective and project-driven rather than attempting to copy the complete NSW legal corpus.

### 4. Jurisdictional Variations

Represent differences between Commonwealth, state, territory, and local requirements without flattening them into one national answer.

A future variation record should identify:

- base source;
- varying jurisdiction;
- variation type;
- affected provision or topic;
- effective period;
- official evidence;
- applicability assumptions;
- human reviewer;
- supersession relationship.

Local planning controls, consent conditions, approval pathways, and authority guidance must remain distinguishable from legislation, regulation, the NCC, and referenced standards.

## Conceptual Record Set

The following are planning concepts only. They do not change the frozen Core object model.

### Regulatory Source Record

Minimum metadata:

- stable source ID;
- title;
- source type;
- issuing authority;
- jurisdiction;
- official URL;
- edition or version;
- publication date;
- effective-from date;
- effective-to date when known;
- source status;
- accessed-on date;
- licensing or access note;
- supersedes and superseded-by links.

### Regulatory Reference Record

Connects a source or provision to a project, asset, design element, lifecycle stage, approval, inspection, or operational obligation.

### Applicability Claim

A bounded claim that a source or provision may or may not apply to a defined project scope. It must state:

- project and subject;
- jurisdiction;
- source version;
- effective date considered;
- assumptions;
- supporting evidence;
- uncertainty;
- review status;
- review trigger.

An applicability claim is not a legal determination.

### Compliance Claim

A compliance-related statement must be scoped to a specific requirement, design state, evidence set, date, and reviewer. It must never be presented as general certification.

Every compliance claim should expose:

- the exact subject assessed;
- the source and version used;
- evidence reviewed;
- exclusions and limitations;
- outstanding items;
- reviewer identity and capacity;
- date of review;
- expiry or re-review trigger;
- whether formal external certification is still required.

### Human Review Record

Records who reviewed the applicability or compliance claim, the review basis, findings, limitations, and outcome. Review does not create authority that the reviewer does not legally or professionally hold.

### Source Change Notice

Records a detected or reported source change pending human verification. A notice should not silently update existing project claims.

## Mapping to the Existing Governance Kernel

A future Regulatory Knowledge Layer should consume the frozen Core rather than rewrite it:

- `Actor` — source curator, author, reviewer, practitioner, or authority contact;
- `Evidence` — official source snapshot metadata, link, amendment notice, project document, or inspection record;
- `Claim` — applicability or compliance-related statement with explicit limitations;
- `Review` — attributed human review without autonomous decision authority;
- `Procedure` — documented research or review procedure without automatic execution;
- `Lifecycle` — recorded source, claim, or review state without automatic transition;
- `RegisteredObject` — project, source, instrument, standard, design item, or regulated asset reference;
- `GovernanceLedgerEntry` — traceable change, review, supersession, or decision event;
- `ModuleContract` — declared inputs, outputs, obligations, and exclusions for future regulatory modules.

No new Core type or Core modification is authorized by this plan.

## Human Authority and Safety Rules

- Official source material must be visible or directly traceable from every consequential claim.
- AI-generated summaries must be labelled as summaries and remain subordinate to official text.
- Applicability, compliance, certification, and approval must remain separate concepts.
- Human review is mandatory before a regulatory claim is used for a consequential project decision.
- Professional, statutory, contractual, and certification authority cannot be inferred from system access.
- Uncertainty, conflicting sources, and missing evidence must be shown rather than hidden.
- A source update must trigger review of affected claims; it must not silently rewrite them.
- BuildingOS outputs are decision support and recordkeeping, not legal, certification, engineering, planning, or building approval advice.

## Repository and Knowledge Garden Model

### Repository as Source of Truth

GitHub remains the authoritative project record for approved BuildingOS documents, indexes, reviews, and change history.

The Obsidian vault or Knowledge Garden is a compatible reading, linking, drafting, and research workspace. It must not become an uncontrolled second authoritative repository.

### Markdown-First Rule

Authoritative planning and governance records should use portable Markdown with:

- stable filenames and record IDs;
- standard Markdown headings and relative links;
- simple YAML frontmatter where useful;
- no dependency on proprietary canvas or database formats;
- no requirement for an Obsidian-only plugin to understand the record.

Standard Markdown links should be preferred over Obsidian-only syntax in authoritative repository files.

### Suggested Frontmatter

```yaml
---
record_type: regulatory-source
record_id: reg-source-example
status: planning
jurisdiction: AU-NSW
authority: example-authority
official_url: https://example.gov.au/source
version: example-version
effective_from: YYYY-MM-DD
effective_to:
accessed_on: YYYY-MM-DD
review_status: unreviewed
supersedes:
superseded_by:
tags:
  - buildingos
  - regulatory-knowledge
---
```

This is a documentation example, not an approved schema or implementation contract.

### Backlinks and Indexes

Use explicit indexes and links so the repository remains navigable outside Obsidian. A future approved structure may include:

```text
docs/regulatory/INDEX.md
docs/regulatory/sources/
docs/regulatory/jurisdictions/
docs/regulatory/claims/
docs/regulatory/reviews/
docs/knowledge-garden/INDEX.md
```

These directories are proposed only and are not created by this planning record.

Each note should link to:

- its authoritative source record;
- related project or registered object;
- affected claim and review records;
- superseded and successor records;
- relevant index or map-of-content page.

### Controlled Sync

Preferred control model:

1. GitHub `main` is authoritative.
2. The local Knowledge Garden pulls or clones approved Markdown.
3. Draft edits are made on a branch or in a clearly marked draft area.
4. Review occurs through diff, pull request, or equivalent documented review.
5. Approved changes return to GitHub before being treated as authoritative.
6. Blind two-way folder synchronisation is prohibited.
7. Private research notes remain separate unless deliberately promoted through review.

### No Authoritative Legal Duplication

The Knowledge Garden should store:

- source metadata;
- official links;
- lawful excerpts where necessary and permitted;
- user-authored summaries;
- project-specific references;
- claims, reviews, and change notes.

It should not become a copied shadow library of the NCC, standards, legislation, or paid legal databases. Official publishers remain the authoritative source, and licensing restrictions must be respected.

## Future Operator Console Relationship

The Human Interface Architecture and read-only Operator Console Prototype Brief are now prepared as documentation-only records.

A future prototype or interface, if separately authorized, may display:

- regulatory sources and versions;
- jurisdiction and effective-date context;
- potentially applicable requirements;
- source-change notices;
- compliance-related claims and limitations;
- human review state;
- unresolved questions and re-review triggers.

The first interface must remain read-only and must not issue approvals, certifications, legal conclusions, or automatic lifecycle transitions.

No prototype or production UI implementation is authorized by this planning record.

## Phased Planning Sequence

### RKL-0 — Planning Baseline

This document only. Status refreshed after Core Batch 01 freeze and completion of the current documentation roadmap package.

### RKL-1 — Source Governance and Information Architecture

After review of the combined documentation package, prepare a separately reviewable documentation-only source register design, vocabulary, record relationships, and update procedure.

RKL-1 must not introduce source connectors, copied legal content, automated monitoring, legal conclusions, or implementation code.

### RKL-2 — Manual Fictional Demonstration Set

After separate approval, prepare fictional source metadata, applicability claims, compliance-claim examples, and human review records. Do not use them as real legal or certification advice.

### RKL-3 — Read-Only Interface Direction

After Operator Console architecture review and explicit UI authorization, describe read-only regulatory views using fictional records.

### RKL-4 — Approved Source Connectors

Only after separate architecture, licensing, security, and implementation approval, consider connectors to official sources. Retrieval must preserve provenance, version, effective date, and human review.

## Entry Criteria for Any Implementation

Implementation must not begin until all applicable conditions are met:

- Core Batch 01 formally frozen;
- Regulatory Knowledge Layer architecture reviewed;
- authoritative-source and licensing policy approved;
- human authority model approved;
- compliance-claim semantics approved;
- update and supersession procedure approved;
- privacy and repository publication boundaries approved;
- explicit Chief Architect implementation authorization issued.

Core freeze is complete, but all remaining conditions continue to apply.

## Deferred Decisions

- first NSW project and instrument set;
- initial NCC volume and project class;
- standards access and licensing model;
- public versus private regulatory notes;
- jurisdiction expansion order;
- source monitoring frequency;
- formal reviewer roles and competence requirements;
- whether regulatory planning becomes a dedicated BuildingOS module or an application-level capability pack.

## Current Safe Next Action

Review the combined post-freeze documentation package before any pilot selection or implementation authorization.

After that review, the next documentation-only regulatory action may be an RKL-1 Source Governance and Information Architecture brief. Any live pilot, external connector, production interface, legal or certification authority, or implementation code still requires a separate Chief Architect decision.