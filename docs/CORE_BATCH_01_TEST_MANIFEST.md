# Core Batch 01 Test Manifest

## Status

`LOCAL_AND_GITHUB_CI_VERIFICATION_PASS`

## Verification Date

2026-07-12

## Verified Implementation Baseline

`f84b22bf4921e4f98e15598c5c5a5aa18bcaa996`

## Purpose

Record executable test artifacts and verification evidence for the bounded BuildingOS Governance Kernel Core Batch 01 implementation.

## Test Commands

```text
python -m compileall -q buildingos_core tests
python -m unittest discover -s tests -v
```

## Isolated Verification Result

```text
Ran 34 tests
OK
```

The repository source, including the CI smoke test merged through pull request #2, was reconstructed in an isolated Python environment. Compile and unit-test commands completed successfully.

## GitHub Actions Evidence

Pull request #2, `Verify Core Batch 01 CI on pull request`, tested head commit `f8b9a12f1472f872e3363a180df8ce4d4db806db` against the current `main` implementation.

Workflow evidence:

```text
Workflow: Core Batch 01
Run ID: 29159400862
Run number: 11
Status: completed
Conclusion: success
Job: test
Job ID: 86561756663
```

Successful hosted steps:

- Check out repository;
- Set up Python 3.12;
- Compile package and tests;
- Run Core Batch 01 tests.

The smoke test was then squash-merged to `main` as `f84b22bf4921e4f98e15598c5c5a5aa18bcaa996`.

## Test Artifact Inventory

### Fictional Fixtures

- `tests/fixtures/__init__.py`
- `tests/fixtures/core_batch_01.py`

The fixture set is fixed, fictional, non-production, and covers every in-scope Governance Kernel record type.

### Unit and Boundary Tests

- `tests/test_core_batch_01.py`
- `tests/test_core_batch_01_ci_probe.py`

Covers basic records, invalid references, serialization, public conformance imports, Review no-decision authority, Procedure no-execution behavior, Lifecycle no-transition behavior, and Module Contract known-type validation.

### Cross-Object Tests

- `tests/test_core_batch_01_registry.py`

Covers Actor attribution references, Claim and Evidence relationships, Review subjects and finding evidence, Registered Object ownership, Governance Ledger actor and subject references, and duplicate record identifiers.

### Per-Object M1 Conformance Tests

- `tests/conformance/test_object_conformance.py`

Explicit structure checks map Actor, Evidence, Claim, Review, Procedure, Lifecycle, Registered Object, Governance Ledger Entry, and Module Contract to C01-A through C01-I as applicable.

### Deterministic Regression Tests

- `tests/regression/test_fixed_fixture_serialization.py`

Covers repeatable complete-fixture serialization and reproducible Conformance Result and registry outputs when a fixed check timestamp is supplied.

## Conformance Result Timestamp Mapping

`ConformanceResult.created_at` remains the stored Core record timestamp. The read-only `checked_at` alias and serialized `checked_at` field provide the timestamp name required by `specs/conformance/M1_CONFORMANCE_MATRIX.md` without duplicating mutable state.

## Boundary Evidence

The verified source contains no production database, public API, permissions system, workflow execution, automatic lifecycle transition, autonomous approval, PRI, MCP Runtime, generic agent runtime, QClaw, n8n, application migration, or production Operator Console.

No frozen Foundation document was edited.

## Test Gate Decision

`PASS`

All required Core Batch 01 test layers have passing isolated and hosted evidence. The remaining closure gate is engineering review followed by explicit Chief Architect approval and freeze.
