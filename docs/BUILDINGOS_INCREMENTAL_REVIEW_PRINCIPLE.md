# BuildingOS Incremental Review Principle

## Purpose

This document generalises the approved C01 sub-batch reporting rule into a permanent BuildingOS engineering rule.

It applies to all future BuildingOS engineering milestones.

## Principle

Every engineering batch shall be divided into reviewable sub-batches.

Each sub-batch must complete:

```text
Implementation
-> Self Review
-> Codex Engineering Review
-> Architecture Review (if required)
-> Approval
-> Freeze
```

before the next sub-batch begins.

## Freeze Rule

After a sub-batch is approved, it is frozen.

Subsequent changes must follow a formal:

```text
Change Request -> Version Review -> Approval
```

process.

Approved sub-batches should not be silently edited by later work.

## Scope

This rule applies to:

- Specification batches
- Core runtime batches
- Module SDK batches
- Adapter batches
- Module migration batches
- Release hardening batches

## Codex Responsibility

Codex must:

- Ensure each batch is split into reviewable sub-batches.
- Require QClaw self review before Codex review.
- Decide whether architecture review is required.
- Freeze approved sub-batches.
- Return work to QClaw if sub-batch quality does not meet standards.
- Prevent the next sub-batch from starting before the current one is approved and frozen.

## QClaw Responsibility

QClaw must:

- Implement only the assigned sub-batch.
- Self-review before reporting to Codex.
- Report using the approved BEWP format.
- Avoid modifying frozen sub-batches unless a change request is approved.

## Architecture Review Trigger

Architecture review is required when a sub-batch:

- Defines or changes platform semantics.
- Changes governance rules.
- Changes repository boundaries.
- Changes module contracts.
- Changes scope boundaries.
- Introduces new runtime concepts.

Architecture review may be skipped when a sub-batch is purely mechanical and Codex confirms no architecture or governance boundary changed.

## C01 Application

C01 is the first milestone governed by this principle.

Approved C01 sub-batch:

```text
C01-A - Evidence Standard
Status: APPROVED
```

The Evidence Standard sub-batch is frozen after implementation, self review, Codex review, and architecture approval are complete.

