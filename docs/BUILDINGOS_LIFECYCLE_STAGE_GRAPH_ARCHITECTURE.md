# BuildingOS Lifecycle Stage Graph Architecture

## Record Status

`DOCUMENTATION_ARCHITECTURE_V0_1_NOT_IMPLEMENTATION_AUTHORIZATION`

## Prepared Date

2026-07-14

## Purpose

Define a reviewable, documentation-only architecture for representing how a BuildingOS project, asset, programme, site, or bounded work package may progress through lifecycle stages while preserving visible evidence, explicit claims, attributed human review, authorised decisions, hold points, exceptions, re-entry, and traceable history.

This architecture does not create executable workflow, automatic transition logic, a database schema, a public API, permissions, a production interface, an agent runtime, or autonomous approval authority.

## Governing Principle

```text
The graph describes possible and recorded progression.
Evidence supports claims.
Humans review and decide.
No node or edge moves itself.
```

## Relationship to Frozen Foundation and Core

This architecture consumes the frozen BuildingOS concepts without modifying them:

- Evidence;
- Claim;
- Actor and attribution;
- Review without decision authority;
- Procedure without execution;
- Lifecycle without automatic transition;
- Registered Object;
- Governance Ledger Entry;
- Module Contract;
- Conformance Result.

The frozen C00 through C01-I Foundation and Core Batch 01 implementation baseline remain unchanged.

Any executable representation, transition service, user interface, database, connector, automation, or runtime requires separate architecture review and explicit Chief Architect implementation authorization.

## Relationship to the Project Genome

The Project Genome describes what the project is and the governance depth it may require.

The Lifecycle Stage Graph describes the project-specific structure of possible, current, completed, paused, returned, superseded, and future lifecycle positions.

The Project Genome may inform:

- which stages are relevant;
- which stages may be omitted or combined;
- which systems, packages, disciplines, authorities, and evidence families must be visible;
- which governance depth applies;
- which branches, hold points, reviews, and escalation paths are required;
- which security, confidentiality, publication, and retention controls apply.

The Project Genome must not automatically generate, activate, or advance a graph.

## What the Lifecycle Stage Graph Is

A Lifecycle Stage Graph is a versioned, project-specific governance map containing:

- stage nodes;
- transition edges;
- entry and exit criteria;
- required evidence and claims;
- attributed reviews;
- authorised decision points;
- hold points;
- branches and parallel paths;
- return, correction, re-entry, supersession, and closure paths;
- package, system, asset, site, authority, and dependency relationships;
- visible current and historical position.

The graph may describe a whole project or a bounded subgraph for a package, system, site, asset, approval pathway, commissioning sequence, operational change, or end-of-life activity.

The graph boundary must be explicit.

## What the Lifecycle Stage Graph Is Not

It is not:

- an executable workflow engine;
- a project programme or construction schedule;
- a substitute for a contract, project plan, BIM execution plan, design management plan, safety plan, environmental assessment, commissioning plan, or asset-management plan;
- a legal determination of required approvals;
- certification or evidence of compliance;
- professional sign-off;
- permission to start work, procure, construct, energise, occupy, operate, modify, or decommission;
- an autonomous decision or approval mechanism;
- proof that a stage has been completed merely because a label is displayed.

## Architecture Vocabulary

### Graph

A bounded, versioned set of lifecycle nodes, edges, criteria, evidence relationships, reviews, decisions, exceptions, and history references.

### Stage Node

A named lifecycle position with a defined scope, identity, purpose, entry conditions, work context, evidence expectations, review expectations, decision conditions, and possible exits.

### Transition Edge

A permitted relationship between two lifecycle positions. An edge describes a possible or recorded transition. It does not execute the transition.

### Stage Gate

A defined review and decision point associated with entry to, continuation within, or exit from a stage.

### Hold Point

A condition at which progression must pause until an authorised human decision, external event, required evidence, correction, or other declared condition is recorded.

### Re-entry

A governed return to a previous or related stage because of change, defect, new evidence, source change, failed review, altered scope, incident, adaptation need, or other recorded trigger.

### Parallel Path

Two or more stage paths that may proceed concurrently while retaining declared dependencies and integration gates.

### Partial Completion

A condition in which a bounded package, system, site, asset, or portion has completed a stage while the wider project has not.

### Exception Path

A visible alternative path used when the normal route cannot be followed. An exception path must expose authority, reason, evidence, limitations, consequences, and review requirements.

### Supersession

A recorded relationship in which a graph version, stage state, criterion, evidence set, claim, review, or decision is replaced by a later authorised record without erasing history.

## Stage Identity

Every stage node should have a stable identity.

Minimum stage identity fields:

- graph ID;
- graph version;
- stage ID;
- stage title;
- stage category;
- stage purpose;
- included scope;
- excluded scope;
- applicable project, site, asset, package, system, or work-package references;
- parent and child stage relationships;
- applicable Project Genome version;
- current documented state;
- state confidence;
- evidence date;
- record owner;
- review status;
- security or publication classification;
- source and provenance references.

Unknown values must remain explicit.

## Stage Categories

A project graph may use project-specific stages. The following categories provide a common planning vocabulary and are not mandatory statutory phases:

1. need, opportunity, problem, or service definition;
2. strategic context and option exploration;
3. feasibility and business-case development;
4. site, corridor, precinct, or asset-context investigation;
5. concept and reference design;
6. planning, environmental, regulatory, and authority pathways;
7. developed and coordinated design;
8. technical documentation and production information;
9. procurement, packaging, contracting, and mobilisation;
10. construction, installation, fabrication, or delivery;
11. inspection, testing, verification, and defect management;
12. commissioning and integrated systems testing;
13. handover and operational readiness;
14. occupation, service commencement, or operational transition;
15. operation, maintenance, monitoring, and performance review;
16. adaptation, renewal, retrofit, expansion, repair, or recovery;
17. incident, disruption, resilience, and controlled recovery;
18. decommissioning, disassembly, reuse, remediation, or end-of-life;
19. post-occupancy, benefits, lessons, and longitudinal review.

A small project may combine categories. A large or complex project may divide them into multiple programme, site, package, system, authority, or operational subgraphs.

These categories do not determine legal pathways or replace authoritative project terminology.

## Stage State Vocabulary

A documented stage state may include:

- `PROPOSED`;
- `NOT_STARTED`;
- `READY_FOR_ENTRY_REVIEW`;
- `ENTRY_AUTHORISED`;
- `ACTIVE_RECORDED`;
- `PAUSED`;
- `ON_HOLD`;
- `PARTIALLY_COMPLETE`;
- `READY_FOR_EXIT_REVIEW`;
- `EXIT_AUTHORISED`;
- `COMPLETED_RECORDED`;
- `RETURNED_FOR_CORRECTION`;
- `RE_ENTERED`;
- `SUPERSEDED`;
- `CANCELLED_RECORDED`;
- `NOT_APPLICABLE`;
- `UNKNOWN`.

These labels describe records. They must not be interpreted as automatic permission, statutory approval, contractual entitlement, certification, occupancy authorization, operational authorization, or professional sign-off.

## Entry Criteria

Entry criteria should identify what must be visible before an authorised human may decide that a stage can begin.

Possible criteria include:

- scope and boundary defined;
- relevant Project Genome version reviewed;
- required prior stage decisions recorded;
- prerequisite evidence available and provenance checked;
- required claims stated with uncertainty and limitations;
- responsible actors and decision authority identified;
- required external approvals or dependencies evidenced where applicable;
- unresolved risks and assumptions visible;
- required security, confidentiality, and publication controls established;
- regulatory sources, versions, effective dates, and jurisdiction questions identified;
- review findings and dissent visible;
- required hold points identified;
- required plans or procedures referenced;
- exception or partial-completion conditions stated.

Entry criteria are documentation requirements. They do not themselves authorize entry.

## Exit Criteria

Exit criteria should identify the evidence, claims, reviews, decisions, and unresolved matters required before a stage may be recorded as exited.

Possible criteria include:

- stage scope addressed or explicitly deferred;
- required evidence registered and linked;
- required claims reviewed;
- review findings, limitations, dissent, and outstanding items recorded;
- authorised decision recorded;
- conditions and dependencies transferred to the next stage;
- defects, non-conformances, exceptions, or departures recorded;
- superseded information linked rather than deleted;
- affected Project Genome fields reviewed;
- regulatory source changes and effective-date issues considered;
- operational, maintenance, handover, or retention obligations recorded;
- return and re-entry triggers stated;
- next permitted stages identified.

A stage may be recorded as partially complete only when the completed and incomplete boundaries are explicit.

## Evidence, Claim, Review, and Decision Pattern

Each consequential gate should make the following chain visible:

```text
Source and Evidence
→ Bounded Claim
→ Attributed Review
→ Authorised Human Decision
→ Recorded Lifecycle Event
→ Governance Ledger Reference
```

The chain must preserve separation between:

- evidence and interpretation;
- claim and review;
- review and decision;
- decision and execution;
- BuildingOS recordkeeping and external statutory, contractual, professional, or operational authority.

## Decision Authority

The graph may reference a decision role or authorised actor only when that authority is externally established and evidenced.

The graph must not infer authority from:

- repository access;
- system role labels;
- job titles alone;
- AI output;
- document authorship;
- previous review participation;
- membership of a project team;
- possession of evidence.

Review records may recommend, identify limitations, or request correction. Review does not create decision authority.

## Transition Edge Record

A transition edge should state:

- edge ID;
- source stage;
- destination stage;
- transition type;
- prerequisite criteria;
- required evidence and claims;
- required reviews;
- authorised decision role or external authority reference;
- hold points;
- conditions and limitations;
- unresolved dependencies;
- effective or recorded date;
- supersession relationship;
- return or rollback destination where relevant;
- ledger reference;
- security or publication constraint.

## Transition Types

Suggested descriptive transition types:

- normal progression;
- conditional progression;
- partial progression;
- parallel activation;
- package or system handoff;
- authority-dependent progression;
- return for correction;
- re-entry after change;
- re-entry after incident;
- adaptation or renewal;
- suspension or hold;
- cancellation or abandonment record;
- supersession;
- operational transition;
- decommissioning or end-of-life transition.

No transition type is executable under this architecture.

## Branches and Parallel Paths

The graph must support branches where different project conditions lead to different governed paths.

A branch should identify:

- branch condition;
- evidence supporting the condition;
- uncertainty;
- human reviewer;
- authorised decision;
- paths not selected and why;
- later re-evaluation triggers.

Parallel paths should identify:

- which stages or packages may proceed concurrently;
- dependency relationships;
- required shared evidence;
- integration reviews;
- interface risks;
- conditions preventing independent completion;
- convergence or reconciliation gates.

Parallel activity must not hide unresolved cross-package or cross-system dependencies.

## Loops, Correction, and Re-entry

Lifecycle progression is not assumed to be linear.

Re-entry may be triggered by:

- design or scope change;
- failed review or test;
- defect or non-conformance;
- source or regulatory change;
- new environmental, climate, site, operational, or community evidence;
- procurement or supply-chain change;
- incident or performance failure;
- changed use, occupancy, asset strategy, or operating conditions;
- changed Project Genome classification;
- superseded assumption;
- incomplete handover or operational-readiness evidence;
- authorised request for reconsideration.

A re-entry record should preserve the previous stage history, the trigger, affected evidence and claims, required review, decision authority, and new exit conditions.

## Rollback and Return Paths

The graph may describe a return to an earlier stage, but it must not imply that physical work, legal status, contractual effect, approvals, expenditure, environmental impact, or operational change can literally be undone.

Return and rollback records must distinguish:

- information correction;
- design revision;
- governance reconsideration;
- physical remediation;
- contractual change;
- statutory re-application or modification;
- operational recovery;
- record supersession.

## Partial Completion and Progressive Handover

For staged, packaged, multi-site, campus, precinct, network, or major-system projects, the graph should support partial completion without misrepresenting the whole project.

A partial-completion record should state:

- exact completed boundary;
- incomplete boundary;
- systems, areas, packages, or assets included;
- interfaces and dependencies;
- temporary conditions;
- evidence and review basis;
- conditions of use or next activity;
- external approval references where applicable;
- outstanding defects and risks;
- handover and operational-responsibility boundaries;
- expiry or re-review triggers.

## Scale Profiles

### BOS-S — Compact Graph

A small-project graph may use:

- a short sequence of combined stages;
- a limited number of explicit gates;
- one evidence and decision room per major stage group;
- compact change and supersession records;
- clear professional and statutory review references where applicable.

Simplicity must not remove consequential review or hide uncertainty.

### BOS-M — Coordinated Graph

A medium-project graph may use:

- discipline and package subgraphs;
- coordinated design and authority pathways;
- procurement, construction, commissioning, handover, and operational-readiness gates;
- interface reviews;
- formal change, defect, and re-entry paths;
- jurisdiction and source-version tracking.

### BOS-LC — Large or Complex Graph

A large or complex graph may use:

- programme, precinct, campus, site, package, system, authority, and operational subgraphs;
- multiple evidence and decision rooms;
- formal convergence and integration gates;
- progressive completion and handover;
- long-duration source, provenance, configuration, commissioning, and operational history;
- security and publication boundaries;
- specialist or independent review references where required by authorised humans;
- project-specific escalation and exception overlays.

Graph complexity should reflect governance need, not produce ceremony for its own sake.

## Governance Depth Mapping

### GD-1 — Compact

- stable stage identity;
- minimal explicit entry and exit criteria;
- named human reviews and decisions;
- visible assumptions and unresolved items;
- simple re-entry and supersession paths.

### GD-2 — Coordinated

- discipline, package, and authority dependencies;
- structured evidence and claim requirements;
- procurement, construction, commissioning, and handover gates;
- change and defect paths;
- decision traceability.

### GD-3 — Enhanced

- formal stage rooms;
- cross-disciplinary evidence dependencies;
- regulatory source and effective-date context;
- stronger re-review, operational readiness, and configuration controls;
- documented escalation and exception handling.

### GD-4 — Major or High-Consequence

- project-specific governance overlay;
- multiple nested graphs and evidence rooms;
- formal integration, commissioning, resilience, security, and operational transition gates;
- long-duration provenance and retention;
- independent or specialist review references where required;
- explicit handling of high-consequence uncertainty and irreversible decisions.

## ClimateOS-to-BuildingOS Evidence Intake

ClimateOS may contribute evidence to lifecycle stages only under the approved documentation-only cross-domain evidence intake contract.

Permitted evidence may include:

- site and environmental observations;
- climate-risk evidence;
- model outputs with methods and uncertainty;
- source, date, version, and provenance metadata;
- authorised building, MEP, BIM, fixture, construction, commissioning, operations, and site-context evidence.

ClimateOS conclusions, approval recommendations presented as decisions, automatic compliance conclusions, lifecycle control, runtime authority, and unsupported project claims must not enter the graph as BuildingOS decisions.

Every imported item must remain attributable, reviewable, limited, and linked to the relevant stage without transferring decision authority.

## Regulatory Knowledge Layer Relationship

The future Regulatory Knowledge Layer may support stage-specific source and claim visibility for:

- Australian NCC edition, volume, amendment, adoption, commencement, effective-date, and jurisdiction context;
- referenced standards identifiers, editions, relationships, access, and licensing boundaries;
- NSW legislation, regulations, environmental planning instruments, approval records, authority guidance, and version status;
- Commonwealth, state, territory, and local jurisdictional variations;
- source change and supersession;
- applicability and compliance-related claims;
- human review and re-review triggers.

The graph may reference regulatory sources, claims, reviews, and external decisions. It must not determine legal applicability, certify compliance, replace an authority, or treat the newest source as automatically applicable.

A source change may trigger review or re-entry. It must not silently move a project, rewrite a claim, or invalidate an external approval without authorised human assessment.

## Knowledge Garden Compatibility

Authoritative graph architecture and planning records should remain Markdown-first and repository-readable.

Compatibility principles:

- GitHub `main` remains the approved source of truth;
- stable graph, stage, edge, evidence, claim, and review identifiers;
- ordinary Markdown links;
- explicit indexes, backlinks, and maps of content;
- controlled promotion of drafts through reviewable diffs or pull requests;
- private research notes separated from approved records;
- no blind two-way synchronisation;
- no shadow duplication of NCC content, referenced standards, legislation, paid legal databases, confidential project information, or security-sensitive operational material.

Official publishers and authorised project systems remain authoritative for controlled source content.

## Human Interface Implications

A future read-only human interface may display:

- lifecycle map and current recorded position;
- stage purpose, scope, criteria, and dependencies;
- evidence and claim readiness;
- reviews, dissent, unresolved items, and decisions;
- hold points, exceptions, and re-entry paths;
- partial completion and progressive handover boundaries;
- source changes and re-review triggers;
- governance ledger history.

The interface must visually distinguish:

- proposed from authorised;
- evidence from claims;
- review from decision;
- current from superseded;
- project records from external legal, statutory, contractual, certification, and professional authority;
- recorded state from permission to act.

## S7 Sydney Candidate Learning-Case Application

The NEXTDC S7 Sydney profile may be used only as a candidate `BOS-LC` learning case to test whether the architecture can describe:

- campus, site, package, building, MEP, BIM, construction, commissioning, operational, climate-risk, source-provenance, and regulatory-evidence subgraphs;
- parallel design, procurement, construction, testing, and operational-readiness paths;
- integrated systems testing and progressive handover;
- high-volume evidence and long-duration provenance;
- critical-infrastructure security and publication boundaries;
- source uncertainty and separation between public reporting, official planning records, approved design, as-built condition, and operational evidence.

This use does not classify S7 officially, select it as a live pilot, grant access to confidential information, determine its legal pathway, or assert its approval, design, construction, commissioning, compliance, capacity, or operational state.

## Documentation Conformance Checklist

A proposed Lifecycle Stage Graph documentation package should confirm:

1. graph and scope identity are explicit;
2. applicable Project Genome version is referenced;
3. stages and edges have stable IDs;
4. unknowns and uncertainties remain visible;
5. entry and exit criteria are stated;
6. evidence, claims, reviews, decisions, and execution remain separate;
7. decision authority is externally evidenced rather than inferred;
8. no automatic transition is described as authorised;
9. branches, parallel paths, loops, return, and re-entry are visible where relevant;
10. partial completion does not misrepresent whole-project completion;
11. superseded records remain traceable;
12. regulatory source, version, effective-date, and human-review context is preserved where relevant;
13. ClimateOS evidence intake does not transfer conclusions or authority;
14. security, confidentiality, licensing, and publication boundaries are visible;
15. Knowledge Garden compatibility does not create a second uncontrolled source of truth;
16. the package does not provide legal, certification, contractual, engineering-signoff, safety, or professional advice;
17. the package does not authorize implementation.

## Review Gate

This architecture may proceed to documentation review when:

- it remains consistent with the frozen Foundation and Core;
- Project Genome relationships are explicit;
- no executable transition mechanism is introduced;
- human authority boundaries remain visible;
- small, medium, and large or complex profiles are supported;
- Regulatory Knowledge Layer and Knowledge Garden boundaries are preserved;
- the S7 case remains candidate-only;
- no live pilot is selected.

## Current Decision

```text
LIFECYCLE_STAGE_GRAPH_ARCHITECTURE_V0_1_PREPARED
DOCUMENTATION_ONLY
NO_IMPLEMENTATION_AUTHORIZATION
```

## Next Safe Activity

After verification of this documentation record, the next governed activity is to define:

1. BuildingOS Human Interface Architecture;
2. a bounded read-only Operator Console Prototype Brief.

No production UI implementation is authorized.