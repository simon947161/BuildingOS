# Core Batch 01 Test Strategy

## Status

`APPROVED_PLANNING_BASELINE`

## Test Objective

Demonstrate that the minimum Governance Kernel records are structurally valid, traceable to frozen M1 specifications, deterministic, and free of excluded runtime behavior.

## Required Test Layers

### 1. Unit Tests

Each record type must test:

- required fields;
- identifier format;
- enumerated values;
- serialization round-trip;
- rejection of invalid input;
- stable deterministic output.

### 2. Conformance Tests

Each object must map to `specs/conformance/M1_CONFORMANCE_MATRIX.md` and return an explicit `PASS` or `FAIL` result with messages.

### 3. Boundary Tests

Tests must prove that:

- Review has no approval or decision method.
- Actor has no role-based permission behavior.
- Procedure does not execute steps.
- Lifecycle does not automatically transition.
- Ledger does not provide blockchain or generic logging behavior.
- Module Contract does not execute modules.
- No external runtime, database, network, API, MCP, PRI, QClaw, or n8n dependency is required.

### 4. Cross-Object Tests

- Claim evidence references resolve.
- Review subject references resolve.
- Ledger entries identify actor and subject.
- Registered Object identifiers and versions remain stable.
- Module Contract object names are known.

### 5. Regression Tests

A fixed fictional fixture set must preserve expected validation and serialization output across future changes.

## Fictional Fixture Policy

All Batch 01 fixtures must be fictional and clearly labelled.

Fixtures must not contain:

- real people;
- real projects;
- confidential records;
- production credentials;
- legal, compliance, engineering, or financial decisions presented as real.

Recommended fixture namespace:

```text
fictional-building-alpha
actor-reviewer-001
evidence-photo-001
claim-envelope-001
```

## Minimum Test Artifacts Before Batch Closure

```text
tests/fixtures/
tests/conformance/
tests/regression/
```

Required evidence:

- test manifest;
- command used to run tests;
- passing output;
- coverage of every in-scope object;
- explicit boundary test results;
- implementation self-review;
- engineering review record.

## Quality Gate

Batch 01 cannot be frozen unless:

1. all tests pass;
2. every object maps to M1;
3. no excluded dependency is present;
4. no frozen Foundation file changed;
5. deterministic serialization is demonstrated;
6. unresolved failures are recorded rather than waived silently.

## Tooling Direction

Use the smallest standard-library-first test stack supported by the selected implementation language. Avoid framework commitments that are unnecessary for representational records.
