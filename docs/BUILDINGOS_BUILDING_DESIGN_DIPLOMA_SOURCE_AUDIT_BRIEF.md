# BuildingOS Building Design Diploma Source Audit Brief

## Project

BuildingOS

## Brief Status

`DOCUMENTATION_ONLY_LOCAL_SOURCE_AUDIT_AUTHORIZED`

## Prepared Date

2026-07-19

## Chief Architect Direction

The Chief Architect has identified a local Building Design Diploma material collection under the local Simon workspace as a potential source for BuildingOS small-building planning and design capability.

Expected local workspace root:

```text
D:\Codex\Simon
```

Expected collection name or search term:

```text
Building Design Diploma
```

The exact folder path must be resolved locally before analysis.

## Purpose

Perform a read-only, evidence-based audit of the Building Design Diploma materials and determine whether they can support a future BuildingOS small-building knowledge baseline, capability pack, fictional demonstration, or pilot-preparation package.

This audit must not assume that educational material is current, authoritative, licensed for redistribution, suitable for professional reliance, or sufficient for legal, regulatory, engineering, planning, building-approval, certification, or construction decisions.

## Required Preflight

Before modifying the BuildingOS repository, verify the official local BuildingOS workspace against GitHub `main`:

```text
cd /d D:\Codex\BuildingOS
git fetch origin main
git status --short --branch
git rev-list --left-right --count HEAD...origin/main
git log -1 --format="%H%n%ci%n%s"
git log -1 --format="%H%n%ci%n%s" origin/main
```

Required rule:

- Continue only if the working tree is clean and `HEAD...origin/main` reports `0 0`.
- If local is behind, ahead, dirty, or diverged, stop and report before editing or pushing.
- Do not force-push or merge stale local work.

## Audit Boundary

The audit is read-only for the source collection.

Do not:

- rename, move, delete, edit, convert, or reorganise source files;
- upload the Diploma collection to the public BuildingOS repository;
- copy full NCC, Australian Standards, paid course material, licensed textbooks, lecturer materials, assessment solutions, confidential documents, personal information, or protected content;
- treat course notes as current law, current NCC requirements, professional advice, certification evidence, or authority guidance;
- write implementation code;
- create a database, API, connector, monitor, crawler, workflow, permission system, runtime, or production UI;
- modify the frozen BuildingOS Foundation or Core Batch 01 baseline;
- activate a live pilot.

## Source Discovery Tasks

### 1. Resolve Collection Location

Search under:

```text
D:\Codex\Simon
```

for likely folder names including:

- `Building Design Diploma`
- `Diploma of Building Design`
- `Building Design`
- `TAFE Building Design`
- unit-code folders associated with the qualification

Record the resolved path or paths without exposing private user paths beyond what is necessary for the audit report.

### 2. Produce a File Inventory

Create a metadata-only inventory containing, where available:

- relative path;
- filename;
- extension;
- file size;
- modified date;
- probable subject or unit;
- probable source or author class;
- duplicate or near-duplicate indication;
- readability status;
- access or licensing concern;
- personal, confidential, or sensitive-content flag;
- apparent date or version context;
- preliminary BuildingOS relevance.

Do not hash or inspect restricted files more deeply than necessary to classify them.

### 3. Classify Material Types

Classify the collection into at least:

1. qualification and unit structure;
2. design-process material;
3. site and context analysis;
4. planning and development controls;
5. NCC and regulatory learning material;
6. referenced standards and technical guidance;
7. construction systems and detailing;
8. structures and services awareness;
9. sustainability, climate-responsive design, energy, water, landscape, and resilience;
10. accessibility, fire safety, health, amenity, and safety awareness;
11. documentation, drawing, specification, BIM, CAD, Revit, and presentation workflows;
12. cost, scheduling, procurement, project administration, and contract awareness;
13. inspections, quality, commissioning, handover, operation, maintenance, and defects;
14. assignments and fictional project examples;
15. the Chief Architect's own student work and portfolio evidence;
16. lecturer or institution-provided material;
17. licensed, copyrighted, paid, restricted, personal, or confidential content;
18. obsolete, superseded, uncertain, or unverified material.

### 4. Assess Source Authority and Currency

For each major material group, distinguish:

- personal student work;
- institutional course guidance;
- official primary source;
- official derived source;
- professional secondary source;
- public secondary source;
- licensed or restricted source;
- unknown or unverified source.

Identify visible dates, NCC editions, standard editions, legislation versions, software versions, course years, and supersession risks.

No material may be marked `current` merely because it is the newest file in the folder.

### 5. Assess BuildingOS Reuse Suitability

Assign one provisional outcome:

- `REUSABLE_AS_PERSONAL_KNOWLEDGE_EVIDENCE`
- `REUSABLE_AS_FICTIONAL_PROJECT_EXAMPLE`
- `REUSABLE_AS_WORKFLOW_OR_TEMPLATE_REFERENCE`
- `REUSABLE_AS_SKILLS_AND_COMPETENCY_EVIDENCE`
- `REFERENCE_ONLY_REQUIRES_CURRENT_SOURCE_VERIFICATION`
- `RESTRICTED_METADATA_ONLY`
- `PERSONAL_OR_CONFIDENTIAL_DO_NOT_IMPORT`
- `OUTDATED_OR_SUPERSEDED_DO_NOT_RELY`
- `UNCERTAIN_REQUIRES_HUMAN_REVIEW`

This outcome is an audit classification, not legal, professional, academic, copyright, or regulatory advice.

## Required Analytical Questions

The audit must answer:

1. Which materials genuinely reflect the Chief Architect's own knowledge, drawings, models, decisions, and project work?
2. Which materials can help define a BuildingOS small-building lifecycle and Stage Graph?
3. Which materials can help define a `BOS-S` Project Genome for a small residential or community-building project?
4. Which materials can help establish planning, design, documentation, construction, inspection, handover, and operation checklists?
5. Which materials contain useful fictional project examples suitable for a non-advisory demonstration?
6. Which materials are outdated and require current NCC, NSW, council, standards, or authority verification?
7. Which files cannot be copied because of copyright, licence, privacy, confidentiality, assessment-integrity, or institutional restrictions?
8. What important small-building knowledge areas are absent or weak?
9. Can the collection support a future `Small Building Design Capability Pack`, and under what limits?
10. Which one small-building fictional demonstration should be recommended after the audit?

## Proposed BuildingOS Outputs

Create only documentation outputs in the BuildingOS repository:

### Required

```text
docs/BUILDINGOS_BUILDING_DESIGN_DIPLOMA_SOURCE_AUDIT_REPORT.md
docs/BUILDINGOS_BUILDING_DESIGN_DIPLOMA_SOURCE_MAP.md
docs/BUILDINGOS_SMALL_BUILDING_CAPABILITY_GAP_REGISTER.md
```

### Optional, only if justified by the audit

```text
docs/BUILDINGOS_SMALL_BUILDING_DESIGN_CAPABILITY_PACK_PROPOSAL.md
docs/BUILDINGOS_SMALL_BUILDING_FICTIONAL_DEMONSTRATION_CANDIDATE.md
```

Do not copy source binaries into BuildingOS.

## Source Map Requirements

The source map should reference local materials using stable, privacy-conscious relative references and should record:

- source group ID;
- source category;
- ownership or authority class;
- date or version context;
- access boundary;
- reuse boundary;
- BuildingOS capability relevance;
- current-source verification requirement;
- human-review requirement.

Where a local path may expose personal information, use an audit-local alias instead of publishing the full path.

## Small-Building Capability Areas to Evaluate

Assess whether the collection can support future planning for:

- client brief and project definition;
- site and climate analysis;
- local planning pathway identification;
- small-building Project Genome;
- concept design and option comparison;
- spatial planning and accessibility awareness;
- envelope, structure, materials, moisture, fire, acoustic, thermal, lighting, ventilation, water, and services coordination awareness;
- climate-adaptive and passive-design strategies;
- drawings, schedules, specifications, BIM and model coordination;
- cost, programme, procurement and change awareness;
- approval-document preparation;
- construction-stage information and RFIs;
- inspections, defects, commissioning and handover;
- operation, maintenance, adaptation and end-of-life considerations;
- evidence, claim, review and governance records.

The audit must distinguish design-assistance capability from professional engineering, certifier, surveyor, planner, legal, authority, builder, trade, and specialist responsibilities.

## Regulatory Knowledge Layer Relationship

The Diploma collection may provide historical learning context and project questions for the future Regulatory Knowledge Layer, but it must not become the authoritative legal library.

The audit must preserve:

- Australian NCC edition and effective-date context;
- referenced-standard identifiers and licence boundaries;
- NSW legislation and regulation version context;
- jurisdictional variations;
- source, version, access date, effective date, and supersession tracking;
- applicability and compliance-related claims;
- attributed human review;
- explicit limitations and re-review triggers.

Official publishers and authorised sources remain authoritative.

## Knowledge Garden Compatibility

Outputs must remain:

- Markdown-first;
- readable outside Obsidian;
- stable in filename and record identity;
- linkable through ordinary Markdown links, backlinks, indexes, and maps of content;
- governed by GitHub `main` as the approved source of truth;
- suitable for controlled promotion from private research to approved repository records;
- protected against blind two-way sync;
- free of duplicated authoritative legal, standards, paid, confidential, or protected content.

## Review Gates

### Gate 1 — Inventory Review

Confirm:

- resolved collection path;
- inventory coverage;
- source and ownership classes;
- restricted and personal material handling;
- no source files modified.

### Gate 2 — Suitability Review

Confirm:

- reusable categories;
- outdated or uncertain categories;
- regulatory verification needs;
- copyright and licence boundaries;
- small-building capability coverage and gaps.

### Gate 3 — BuildingOS Adoption Decision

Return to the Chief Architect before:

- promoting any material into an approved BuildingOS knowledge pack;
- selecting a real small-building pilot;
- using real project or client data;
- relying on any material for legal, planning, NCC, certification, construction, safety, or professional conclusions;
- copying restricted or licensed content;
- authorising code, ingestion, database, search, RAG, connector, UI, workflow, or automation.

## Stop Conditions

Stop and report if:

- the local Simon workspace is missing, inaccessible, dirty in a consequential way, or unexpectedly diverged from its own remote context;
- the Building Design Diploma folder cannot be resolved;
- the source collection contains significant personal, confidential, licensed, or assessment-sensitive content that cannot be safely inventoried;
- a source appears to require circumvention of access controls;
- an audit output would expose personal or protected data;
- a current legal or professional conclusion is required;
- the task would require implementation code or frozen-baseline modification.

## Acceptance Criteria

The audit is complete only when:

1. the local collection has been inventoried without modifying it;
2. material classes and authority classes are recorded;
3. date, version, licence, privacy, and supersession risks are visible;
4. reusable, restricted, outdated, and uncertain material groups are distinguished;
5. BuildingOS small-building capability coverage and gaps are documented;
6. no legal, certification, professional, approval, or construction authority is claimed;
7. no protected or authoritative source content is copied into the public repository;
8. the frozen Foundation and Core Batch 01 baseline remain unchanged;
9. a clear Chief Architect decision gate is provided for any future adoption.

## Next Safe Action

Codex should run the local read-only audit from the verified local workspaces and produce the three required documentation outputs in small, reviewable commits.

No small-building capability pack, pilot, implementation, ingestion, RAG, database, UI, workflow, connector, or automation is authorised by this brief.