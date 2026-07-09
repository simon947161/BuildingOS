# BuildingOS Core Batch 01 Implementation Brief

## Project

BuildingOS

## Brief Status

`DRAFT_FOR_REVIEW`

## Authorization Source

Chief Architect approval has authorized drafting this brief only.

This brief is derived from:

- `docs/BUILDINGOS_C02_CORE_IMPLEMENTATION_APPROVAL_RECORD.md`
- `docs/BUILDINGOS_C02_CORE_IMPLEMENTATION_PLANNING_REVIEW.md`
- `docs/BUILDINGOS_C02_CORE_IMPLEMENTATION_PLANNING_BRIEF.md`

## Boundary Statement

This document does not authorize implementation.

This document does not authorize code changes.

This document does not modify frozen Foundation documents.

This document does not introduce PRI, MCP Runtime, generic agent runtime, or
QClaw.

Implementation remains pending until separate Chief Architect approval is
given.

## 1. Batch 01 Objective

Core Batch 01 objective:

```text
Define the minimum BuildingOS Governance Kernel implementation boundary before
any Core code is written.
```

Batch 01 should prepare the first implementation-ready plan for representing
the frozen M1 governance primitives as Core objects, modules, conformance
obligations, and tests.

Batch 01 must remain a planning and review package until implementation is
separately approved.

## 2. Scope Strictly Derived From C02 Approval Record

Batch 01 scope is limited to the safe first implementation candidates named in
the C02 approval record:

- Actor attribution records.
- Evidence records.
- Claim records with evidence links and support status.
- Review records without decision authority.
- Procedure structures without workflow automation.
- Lifecycle structures without automated state-machine behavior.
- Registered Object records for traceability.
- Governance Ledger records for governance traceability.
- Module Contract declarations and conformance checks.

The scope must map directly to frozen M1 specifications:

| M1 Source | Batch 01 Planning Target |
| --- | --- |
| C00 Glossary Foundation v1.0 | Shared terminology reference. |
| C01-C Identity Standard v1.0 | Actor attribution record boundary. |
| C01-A Evidence Standard v1.0 | Evidence record boundary. |
| C01-B Claim Standard v1.0 | Claim record and support-status boundary. |
| C01-D Review Standard v1.0 | Review record boundary without decision authority. |
| C01-E Procedure Standard v1.0 | Procedure structure boundary without automation. |
| C01-F Lifecycle Standard v1.0 | Lifecycle structure boundary without automated execution. |
| C01-G Registered Object Standard v1.0 | Registered Object traceability boundary. |
| C01-H Governance Ledger Standard v1.0 | Governance Ledger record boundary. |
| C01-I Module Contract Standard v1.0 | Module Contract declaration and conformance boundary. |

## 3. Items Safe For First Implementation

The following items are safe for first implementation only after separate Chief
Architect implementation approval:

- Minimal Actor attribution record.
- Minimal Evidence record.
- Minimal Claim record with evidence support status.
- Minimal Review record without decision authority.
- Minimal Procedure structure.
- Minimal Lifecycle structure.
- Minimal Registered Object record.
- Minimal Governance Ledger record.
- Minimal Module Contract declaration.
- Minimal M1 conformance checks.

These are safe because they are representational, traceable to frozen M1
standards, and do not require runtime automation or scope expansion.

## 4. Excluded Items

The following items are excluded from Batch 01:

- Runtime implementation before approval.
- Production runtime.
- BOMI migration.
- IPI migration.
- ClimateOS migration.
- Permission systems.
- User management.
- Production database.
- Public API.
- UI dashboard.
- Crawlers.
- Search engine.
- Workflow automation.
- AI decision-making.
- MCP tools.
- MCP Runtime.
- n8n or Workflow Hub automation.
- QClaw execution workflow.
- Real project decision automation.
- `buildingos-modules` repository.
- Generic agent runtime.
- PRI integration.
- Any edit to frozen Foundation documents.

## 5. Required Files Or Modules To Be Created Later

If this brief is approved and a later Chief Architect decision authorizes
implementation planning artifacts, the following files or modules may be
created later.

Planning files:

- `docs/CORE_BATCH_01_SCOPE.md`
- `docs/CORE_BATCH_01_ARCHITECTURE_BOUNDARY.md`
- `docs/CORE_BATCH_01_IMPLEMENTATION_BATCHES.md`
- `docs/CORE_BATCH_01_TEST_STRATEGY.md`
- `docs/CORE_BATCH_01_ACCEPTANCE_CRITERIA.md`
- `docs/CORE_BATCH_01_CHANGE_REQUEST_RULE.md`

Conformance files:

- `specs/imported/M1_BASELINE_REFERENCE.md`
- `specs/conformance/M1_CONFORMANCE_MATRIX.md`

Candidate Core modules:

- `kernel/identity/`
- `kernel/evidence/`
- `kernel/claim/`
- `kernel/review/`
- `kernel/procedure/`
- `kernel/lifecycle/`
- `kernel/registered_object/`
- `kernel/ledger/`
- `kernel/module_contract/`
- `kernel/conformance/`

Candidate test areas:

- `tests/conformance/`
- `tests/fixtures/`
- `tests/regression/`

These files and modules must not be created as code until a later approval
explicitly authorizes implementation.

## 6. Acceptance Criteria

Batch 01 brief acceptance criteria:

| Criterion | Acceptance Requirement |
| --- | --- |
| Foundation integrity | C00 through C01-I remain frozen and unchanged. |
| Scope discipline | Batch 01 scope maps only to M1 governance primitives. |
| Boundary clarity | Excluded items are explicit and preserved. |
| Architecture review readiness | Repository or folder boundary questions are listed for review. |
| Implementation control | No code or runtime files are created by this brief. |
| Conformance readiness | M1 conformance matrix is identified as required before code. |
| Test readiness | Conformance, boundary, fixture, and regression test categories are identified before code. |
| Approval control | Implementation remains pending until separate Chief Architect approval. |

## 7. Review Procedure

Review procedure:

1. Chief Architect reviews this Batch 01 brief.
2. Confirm that the scope is strictly derived from the C02 approval record.
3. Confirm that the frozen M1 Foundation remains unchanged.
4. Confirm excluded items remain outside Batch 01.
5. Resolve Architecture Review questions before implementation approval.
6. Decide whether to authorize the next planning artifact or request revision.

Reviewable decision options:

1. Approve this brief as the basis for Batch 01 planning artifacts.
2. Request revision to this brief.
3. Reject this brief and return to the C02 approval gate.

## 8. Stop Conditions

Stop immediately and return for Architecture Review if any of the following
conditions appear:

- A frozen Foundation document appears to require editing.
- Batch 01 requires concepts not present in C00 through C01-I.
- Implementation would require runtime automation.
- Implementation would require a database, API, UI, crawler, or search engine.
- Implementation would require permissions or user management.
- Review begins to imply Decision authority.
- Evidence begins to be treated as confirmed fact by default.
- Procedure begins to become workflow automation.
- Identity begins to become permissions.
- Ledger begins to become blockchain or generic logging.
- Module Contract begins to become module runtime execution.
- PRI, MCP Runtime, generic agent runtime, or QClaw becomes necessary.

If any stop condition is triggered, do not edit Foundation documents. Propose a
Change Request instead.

## 9. Evidence Required Before Implementation Approval

Before any implementation approval, the following evidence is required:

- Approved Batch 01 objective.
- Approved repository or folder boundary.
- Approved M1 conformance matrix plan.
- Approved Governance Kernel object list.
- Approved module naming.
- Approved test strategy.
- Approved fixture policy using fictional data only.
- Approved excluded-items list.
- Confirmed no changes to frozen Foundation documents.
- Confirmed no PRI, MCP Runtime, generic agent runtime, or QClaw dependency.
- Confirmed implementation approval record that explicitly authorizes code.

## 10. Implementation Approval Requirement

Implementation remains pending until a separate Chief Architect approval is
given.

This brief does not authorize:

- Code creation.
- Runtime implementation.
- Repository skeleton creation as implementation.
- Database implementation.
- API implementation.
- UI implementation.
- Workflow automation.
- Foundation edits.
- Scope expansion.

Required future gate:

```text
CHIEF_ARCHITECT_APPROVAL_FOR_CORE_BATCH_01_IMPLEMENTATION
```

Until that future gate is explicitly approved, Core Batch 01 remains planning
only.

## Recommended Next Gate

Recommended next gate:

```text
CHIEF_ARCHITECT_REVIEW_OF_CORE_BATCH_01_IMPLEMENTATION_BRIEF
```

Recommended decision:

```text
APPROVE_OR_REVISE_CORE_BATCH_01_IMPLEMENTATION_BRIEF
```

## Conversation Radar

Knowledge points:

- Chief Architect approved drafting this brief only.
- Batch 01 is limited to minimum Governance Kernel planning.
- Implementation is still not authorized.

Idea points:

- Treat Batch 01 as representational Core primitives before any runtime system.
- Require conformance evidence before code.

Decisions:

- This brief is `DRAFT_FOR_REVIEW`.
- No implementation decision is made by this brief.

Risks:

- Treating brief approval as code approval.
- Expanding Batch 01 into runtime, automation, integration, or migration.
- Editing frozen Foundation documents instead of using Change Request.

Open questions:

- Should Batch 01 use a new `buildingos-core` repository or a bounded folder in
  the current repository?
- What exact format should the M1 conformance matrix use?
- Which test artifacts must exist before code approval?

Next actions:

1. Chief Architect reviews this brief.
2. Chief Architect approves, revises, or rejects this brief.
3. If approved, prepare the next planning artifact named by the Chief
   Architect.

Related project keywords:

- BuildingOS
- Core Batch 01
- Governance Kernel
- M1 Specification Foundation
- C02 Approval Gate
- Evidence
- Claim
- Identity
- Review
- Procedure
- Lifecycle
- Registered Object
- Governance Ledger
- Module Contract
