# Core Batch 01 Test Manifest

## Status

`LOCAL_VERIFICATION_PASS_GITHUB_CI_PENDING`

## Verification Date

2026-07-12

## Verification Target

`a89c381fbd46355699b6ac6fac9c5154dec4b081`

## Purpose

Record the executable test artifacts and observed verification evidence for the bounded BuildingOS Governance Kernel Core Batch 01 implementation.

## Test Command

```text
python -m compileall -q buildingos_core tests
python -m unittest discover -s tests -v
```

## Observed Isolated Result

```text
Ran 33 tests in 0.006s
OK
```

The repository source was reconstructed in an isolated Python environment before these commands were run. This is positive local verification evidence and is not represented as a GitHub Actions pass.

## Test Artifact Inventory

### Fictional Fixtures

- `tests/fixtures/__init__.py`
- `tests/fixtures/core_batch_01.py`

The fixture set is fixed, fictional, non-production, and covers every in-scope Governance Kernel record type.

### Unit and Boundary Tests

- `tests/test_core_batch_01.py`

Covers basic records, invalid references, serialization, Review no-decision authority, Procedure no-execution behavior, Lifecycle no-transition behavior, and Module Contract known-type validation.

### Cross-Object Tests

- `tests/test_core_batch_01_registry.py`

Covers Actor attribution references, Claim and Evidence relationships, Review subjects and finding evidence, Registered Object ownership, Governance Ledger actor and subject references, and duplicate record identifiers.

### Per-Object M1 Conformance Tests

- `tests/conformance/test_object_conformance.py`

Explicit structure checks map the following objects to frozen M1 sources:

- Actor — C01-C;
- Evidence — C01-A;
- Claim — C01-B;
- Review — C01-D;
- Procedure — C01-E;
- Lifecycle — C01-F;
- Registered Object — C01-G;
- Governance Ledger Entry — C01-H;
- Module Contract — C01-I.

Negative tests cover missing Evidence provenance, invalid Claim support status, duplicate Review finding identifiers, unordered Procedure steps, and missing Module Contract obligations and exclusions.

### Deterministic Regression Tests

- `tests/regression/test_fixed_fixture_serialization.py`

Covers repeatable complete-fixture serialization and reproducible Conformance Result and registry outputs when a fixed check timestamp is supplied.

## Conformance Result Timestamp Mapping

`ConformanceResult.created_at` remains the stored Core record timestamp. The read-only `checked_at` alias and serialized `checked_at` field provide the timestamp name required by `specs/conformance/M1_CONFORMANCE_MATRIX.md` without duplicating mutable state.

## Boundary Evidence

The verified source contains no production database, public API, permissions system, workflow execution, automatic lifecycle transition, autonomous approval, PRI, MCP Runtime, generic agent runtime, QClaw, n8n, application migration, or production Operator Console.

No frozen Foundation document was edited in this increment.

## Hosted CI State

The GitHub connector returned no combined status entries and no associated workflow run for verification target `a89c381fbd46355699b6ac6fac9c5154dec4b081` at the time this manifest was prepared.

Therefore:

- local isolated verification is recorded as passing;
- GitHub Actions verification remains unresolved;
- Core Batch 01 remains unapproved and unfrozen;
- approval and freeze records must not be prepared until hosted verification and engineering review gates are satisfied.
