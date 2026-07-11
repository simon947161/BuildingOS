# M1 Conformance Matrix

## Status

`APPROVED_PLANNING_BASELINE`

## Purpose

Map each frozen M1 specification to a minimum Core Batch 01 implementation obligation and objective test evidence.

| Frozen M1 Source | Core Object / Control | Minimum Obligation | Required Evidence | Excluded Interpretation |
| --- | --- | --- | --- | --- |
| C00 Glossary Foundation v1.0 | Shared terminology | Public names and meanings remain traceable to M1 terminology | terminology mapping test | redefining frozen terms |
| C01-C Identity Standard v1.0 | Actor | identify and attribute an actor without permissions | required-field and serialization tests | authentication, authorization, user management |
| C01-A Evidence Standard v1.0 | Evidence | represent source, type, provenance, capture time, and integrity status | valid/invalid fixture tests | treating evidence as confirmed fact |
| C01-B Claim Standard v1.0 | Claim | represent statement, evidence links, and support status | reference and status tests | automated truth determination |
| C01-D Review Standard v1.0 | Review | record reviewer, subject, findings, and review status | no-decision-authority boundary test | approval or decision authority |
| C01-E Procedure Standard v1.0 | Procedure | represent ordered descriptive steps and responsibilities | structure and ordering tests | workflow execution or automation |
| C01-F Lifecycle Standard v1.0 | Lifecycle | represent stages and current recorded stage | stage-enumeration tests | automatic state-machine transitions |
| C01-G Registered Object Standard v1.0 | Registered Object | provide stable identity, type, version, and traceability | identifier/version tests | generic asset database |
| C01-H Governance Ledger Standard v1.0 | Ledger Entry | append an immutable-style governance event record in memory | ordering and required-field tests | blockchain or generic application logging |
| C01-I Module Contract Standard v1.0 | Module Contract | declare module identity, inputs, outputs, obligations, and exclusions | contract conformance tests | runtime module execution |

## Conformance Result Format

Each check returns a deterministic record:

```text
check_id
m1_source
subject_type
subject_id
status: PASS | FAIL
messages[]
checked_at
```

A conformance check reports whether a supplied record satisfies a documented structural obligation. It does not approve the record, validate real-world truth, or make a project decision.

## Mandatory Cross-Object Checks

- Claim evidence references resolve to supplied Evidence records.
- Review subject references resolve to a supplied registered object or governance record.
- Ledger subject references are explicit.
- Module Contract declared inputs and outputs use known Core object names.
- Actor references are attributable but do not imply access rights.

## Traceability Rule

Every implementation object and test must cite one or more rows of this matrix. Any object with no M1 mapping is out of scope and triggers Architecture Review.

## Change Rule

This matrix may clarify implementation obligations but may not alter the meaning of frozen M1 documents. Any semantic conflict must be handled through Change Request rather than silent reinterpretation.
