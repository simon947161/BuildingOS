# Core Batch 01 Architecture Boundary

## Status

`APPROVED_PLANNING_BASELINE`

## Purpose

Define the first bounded implementation area for the BuildingOS Governance Kernel without changing the frozen M1 Foundation.

## Repository Decision

Core Batch 01 will live as a bounded folder inside the existing `simon947161/BuildingOS` repository.

```text
buildingos_core/
  identity/
  evidence/
  claim/
  review/
  procedure/
  lifecycle/
  registered_object/
  ledger/
  module_contract/
  conformance/

tests/
  conformance/
  fixtures/
  regression/
```

A separate `buildingos-core` repository is not required for Batch 01. Separation may be reconsidered only through Architecture Review after the kernel boundary is proven.

## In-Scope Objects

- Actor attribution record.
- Evidence record.
- Claim record with evidence links and support status.
- Review record without decision authority.
- Procedure structure without workflow automation.
- Lifecycle structure without automated transitions.
- Registered Object record.
- Governance Ledger entry.
- Module Contract declaration.
- M1 conformance result.

## Implementation Character

Batch 01 is representational and deterministic.

It may:

- create typed records;
- serialize and deserialize records;
- validate required fields and enumerated values;
- check cross-record references in memory;
- produce explicit conformance results;
- use fictional fixtures;
- run unit, conformance, boundary, and regression tests.

It may not:

- make project decisions;
- approve or reject work;
- automate procedures;
- execute lifecycle transitions;
- assign permissions;
- persist to a production database;
- expose a public API;
- operate a production UI;
- call PRI, MCP Runtime, QClaw, n8n, or a generic agent runtime.

## Dependency Direction

```text
Frozen M1 specifications
        ↓
Governance Kernel record definitions
        ↓
Validation and conformance checks
        ↓
Fictional fixtures and tests
```

No dependency may point from a frozen specification into runtime code.

## Human Authority Boundary

Review records describe review activity. They do not carry approval or decision authority.

All future approval actions remain human-governed and outside Batch 01.

## Stop Conditions

Stop and request Architecture Review if implementation requires:

- changing C00 or C01-A through C01-I;
- inventing a new governance primitive;
- a database, service, public API, or workflow engine;
- permission management;
- autonomous decision-making;
- external runtime integration;
- a production Operator Console.

## Acceptance Boundary

Batch 01 is architecturally complete when all in-scope records have:

1. an M1 source mapping;
2. a minimal typed representation;
3. deterministic validation;
4. fictional fixtures;
5. passing conformance and regression tests;
6. no excluded dependency.
