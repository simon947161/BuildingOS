# BuildingOS Engineering Workflow Protocol v0.1

## Purpose

This protocol defines how Codex manages BuildingOS engineering workflow so Simon does not become the manual engineering message router.

Codex owns engineering coordination, review, routing, and closure.

## Role Chain

```text
Simon -> Chief Product Owner
ChatGPT -> Chief Architect / Governance Reviewer
Codex -> Engineering Manager / Workflow Owner
QClaw -> Software Engineer Agent
```

## Task State Machine

```text
NEW
-> ASSIGNED
-> IMPLEMENTING
-> SELF_REVIEW
-> CODEX_REVIEW
-> CHANGES_REQUESTED
-> IMPLEMENTING
-> CODEX_REVIEW
-> READY_FOR_ARCHITECT_REVIEW
-> ARCHITECT_REVIEW
-> READY_FOR_RELEASE
-> CLOSED
```

Allowed terminal states:

- `CLOSED`
- `BLOCKED_NEEDS_OWNER_DECISION`
- `BLOCKED_NEEDS_ARCHITECTURE_DECISION`
- `BLOCKED_NEEDS_ENVIRONMENT_FIX`

## Ownership by State

| State | Owner |
| --- | --- |
| NEW | Simon |
| ASSIGNED | Codex |
| IMPLEMENTING | QClaw |
| SELF_REVIEW | QClaw |
| CODEX_REVIEW | Codex |
| CHANGES_REQUESTED | Codex |
| READY_FOR_ARCHITECT_REVIEW | Codex |
| ARCHITECT_REVIEW | ChatGPT |
| READY_FOR_RELEASE | Codex |
| CLOSED | Codex |
| BLOCKED_* | Codex |

## QClaw Report Format

QClaw must report implementation status to Codex using:

```text
Task ID:
Current State:
Files Created / Updated:
Verification Performed:
Tests Run:
Failures:
Blocked Items:
Next Recommended Action:
Needs Codex Decision: yes/no
Needs Architect Review: yes/no
```

## Codex Review Checklist

Codex must review QClaw output before asking Simon anything.

Checklist:

- Required files exist.
- Schema is source of truth.
- Examples are valid.
- Tests exist.
- Tests were run or reason is documented.
- Docs match implementation.
- Git status is valid.
- Commit exists or reason is documented.
- No stale placeholder markers exist.
- Architecture was not silently changed.

## Incremental Review Principle

Every BuildingOS engineering batch must be divided into reviewable sub-batches.

Each sub-batch must complete the following sequence before the next sub-batch begins:

```text
Implementation
-> Self Review
-> Codex Engineering Review
-> Architecture Review (if required)
-> Approval
-> Freeze
```

After a sub-batch is approved, it is frozen.

Subsequent changes to an approved sub-batch must use a formal Change Request and Version Review process.

This rule applies to all future BuildingOS milestones, including specification, runtime, adapter, migration, and release-hardening work.

Codex must not allow routine implementation to continue into the next sub-batch until the previous sub-batch has reached Approval and Freeze.

## No Human Relay Rule

Codex should only ask Simon when:

1. Product direction changes.
2. Architecture decision is required.
3. External credential or permission is required.
4. Budget, public release, or partnership decision is required.

Codex must not ask Simon to manually relay routine engineering reports when a technical channel or structured handoff can be produced.

## Git Rule

A BuildingOS engineering task is not closed until Git status is resolved.

If Git is broken:

```text
State = BLOCKED_NEEDS_ENVIRONMENT_FIX
Owner = Codex
```

QClaw must either:

1. Repair the Git repository.
2. Initialize a new valid Git repository.
3. Create a patch bundle.
4. Produce a file manifest and commit plan.

## Schema Source of Truth Rule

If verification output conflicts with schema source, Codex must resolve before release.

Example:

```text
QClaw reports 15 SQLite tables.
schema.sql contains 8 explicit CREATE TABLE statements.
```

Required action:

- Return to QClaw.
- Count actual tables from schema initialization.
- Separate tables, indexes, views, triggers, and metadata.
- Update report terminology.
- Confirm `schema.sql` as source of truth.

## Architecture Review Handoff

Only after Codex Review passes, Codex may send a concise package to ChatGPT:

```text
Task ID:
Repository Path:
Current State:
Architecture Summary:
Files Created / Updated:
Verification Summary:
Open Issues:
Decisions Needed:
Recommended v0.2 Direction:
```

ChatGPT reviews governance, architecture alignment, and future direction. ChatGPT is not a substitute for engineering verification.

## Closure Rule

Only Codex may declare task closure.

Closure requires:

- Codex Review passed.
- Architecture review completed or explicitly not required.
- Git status resolved.
- Verification report completed.
- Open issues recorded.
- Next actions recorded.
- CRP generated where required by the project workflow.
