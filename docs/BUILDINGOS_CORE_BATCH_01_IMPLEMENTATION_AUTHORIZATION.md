# BuildingOS Core Batch 01 Implementation Authorization

## Status

`CHIEF_ARCHITECT_APPROVAL_FOR_CORE_BATCH_01_IMPLEMENTATION`

## Authorization Date

2026-07-12

## Authorization Source

The Chief Architect explicitly directed BuildingOS Night Mode to continue development without repeated micro-authorization prompts and authorized the project to move forward from its verified current state.

This record converts that direction into a bounded implementation authorization under the existing BuildingOS engineering governance rules.

## Approved Preconditions

The following planning conditions have been resolved:

- Repository boundary: bounded `buildingos_core/` folder in the current repository.
- Conformance format: documented in `specs/conformance/M1_CONFORMANCE_MATRIX.md`.
- Test and fictional fixture policy: documented in `docs/CORE_BATCH_01_TEST_STRATEGY.md`.
- Human interface direction: documented separately in `docs/BUILDINGOS_OPERATOR_CONSOLE_ROADMAP.md`.

## Authorized Implementation Scope

Core Batch 01 may implement:

- Actor attribution records;
- Evidence records;
- Claim records and evidence references;
- Review records without decision authority;
- Procedure structures without execution;
- Lifecycle structures without automatic transitions;
- Registered Object records;
- Governance Ledger entries;
- Module Contract declarations;
- deterministic validation and M1 conformance checks;
- fictional fixtures and automated tests.

## Excluded Scope

This authorization does not include:

- production database;
- public API;
- production UI or Operator Console implementation;
- permissions or user management;
- workflow automation;
- autonomous approval or decision-making;
- PRI, MCP Runtime, generic agent runtime, QClaw, or n8n integration;
- application migration;
- edits to frozen Foundation documents.

## Implementation Language Direction

Use a standard-library-first Python package for the first representational kernel. This is a reversible implementation choice for typed records, deterministic serialization, validation, fixtures, and tests; it is not a commitment to the future production runtime stack.

## Review And Stop Rule

Implementation must proceed in reviewable sub-batches. Stop and raise Architecture Review if code requires a new governance concept, an excluded dependency, or a frozen Foundation edit.

## Batch 01 Completion Gate

Batch 01 may be presented for freeze only when:

1. all in-scope records exist;
2. M1 mappings are explicit;
3. conformance and boundary tests pass;
4. fictional fixtures are used;
5. no excluded dependency exists;
6. self-review and engineering review records are prepared.
