# BuildingOS Operator Console Roadmap

## Status

`FUTURE_HUMAN_INTERFACE_WORKSTREAM`

## Purpose

Define a human-participation interface for BuildingOS, similar in operational clarity to Mission Control, while preserving human authority and Governance Kernel boundaries.

## Product Principle

The Operator Console is not an autonomous decision system.

It is a governed workspace where a human can inspect evidence, understand claims, perform reviews, record decisions through later approved modules, and see lifecycle and ledger history.

## Target Views

### 1. System Overview

- active registered objects;
- lifecycle stage distribution;
- open claims and reviews;
- conformance failures;
- recent governance ledger events;
- items waiting for human attention.

### 2. Evidence Desk

- evidence metadata and provenance;
- linked claims;
- integrity and completeness indicators;
- human annotations;
- no automatic assertion that evidence is true.

### 3. Claim Desk

- claim statement;
- supporting and conflicting evidence links;
- support status;
- review history;
- unresolved questions.

### 4. Review Workspace

- review subject;
- reviewer attribution;
- checklist and findings;
- evidence navigation;
- draft review record;
- later human approval handoff outside Batch 01.

### 5. Lifecycle Board

- current recorded stage;
- stage history;
- required evidence and review gaps;
- no automatic transitions in the first interface release.

### 6. Governance Ledger

- chronological governance events;
- actor, subject, event type, and timestamp;
- filters and traceability links;
- append-oriented presentation rather than generic application logs.

### 7. Module Contract Registry

- module purpose;
- declared inputs and outputs;
- obligations and exclusions;
- conformance status.

## Human-in-the-Loop Rules

- AI may summarize but must expose source records.
- AI may identify missing information but must not approve.
- Human actions must be attributable.
- Approval and Decision capabilities require separate architecture and authorization.
- Every consequential action must produce a governance record.

## Delivery Sequence

### Stage A — Read-Only Prototype

Use fictional fixtures from the stable Governance Kernel to display Overview, Evidence, Claim, Review, Lifecycle, Ledger, and Contract views.

### Stage B — Human Drafting

Allow humans to draft records locally with validation, without production persistence or external integration.

### Stage C — Governed Actions

After separate approval, introduce explicit human review and approval workflows with ledger recording.

### Stage D — Runtime Integration

Only after PRI/MCP boundary review, connect approved shared runtime services. BuildingOS must consume these services rather than own them.

## Technology Decision Deferred

Frontend technology will be selected after the Governance Kernel object model and serialization format are stable. The first prototype should favour a simple local web interface with low operational complexity and strong testability.

## Entry Criteria For UI Implementation

- Batch 01 Governance Kernel frozen;
- stable fictional fixture format;
- stable object serialization;
- interface architecture review completed;
- human authority model approved;
- explicit UI implementation authorization issued.

## Success Definition

A user can understand what exists, what is claimed, what evidence supports it, what has been reviewed, what stage it is in, and what still requires human action—without BuildingOS pretending to be the decision-maker.
