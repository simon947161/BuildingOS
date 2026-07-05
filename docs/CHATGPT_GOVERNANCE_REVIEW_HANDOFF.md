# ChatGPT Governance Review Handoff

## Task ID

BOMI-v0.1

## Repository Path

`buildingos-modular-interface/`

## Current State

`READY_FOR_ARCHITECT_REVIEW`

## Architecture Summary

BuildingOS Modular Infrastructure Interface (BOMI) is the physical infrastructure object governance counterpart to IPI.

IPI governs infrastructure projects. BOMI governs physical building infrastructure objects.

BOMI extends the BuildingOS evidence-first architecture:

```text
Source -> Evidence -> Claim -> Review -> Decision -> Ledger -> Continuous Governance
```

The core object is the Building Service Spine: a building-scale utility corridor for water, electricity, drainage, data, sensors, energy, HVAC, inspection access, maintenance, and lifecycle governance.

The core standard is the interface, not the modular house product.

## Files Created / Updated

Core implementation:

- `bomi/components.py`
- `bomi/interfaces.py`
- `bomi/service_spine.py`
- `bomi/evidence.py`
- `bomi/inspection.py`
- `bomi/lifecycle.py`
- `bomi/runtime.py`
- `bomi/matching.py`

Schema:

- `schemas/sqlite/schema.sql`
- `bomi/schema/bomi_schema.sql`

Documentation:

- `docs/TECHNICAL_DESIGN.md`
- `docs/SERVICE_SPINE_STANDARD.md`
- `docs/OPEN_BUILDING_INTERFACE_PROTOCOL.md`
- `docs/COMPONENT_PROFILE_TEMPLATE.md`
- `docs/INSPECTION_RECORD_TEMPLATE.md`
- `docs/LIFECYCLE_GOVERNANCE.md`
- `docs/BUILDINGOS_ENGINEERING_WORKFLOW_PROTOCOL.md`
- `docs/CODEX_ENGINEERING_REVIEW_BOMI_V0_1.md`
- `docs/QCLAW_CHANGE_REQUEST_BOMI_V0_1.md`

Examples and tests:

- `examples/*.json`
- `tests/smoke_test.py`
- `tests/test_*.py`
- `verify.py`

## Verification Summary

QClaw verification:

- Smoke tests: 7/7 passed
- Database initialization: 15 tables created
- JSON validation: 4/4 valid
- Placeholder scan: clean

Codex verification:

- Schema table-count conflict resolved.
- `schemas/sqlite/schema.sql` and `bomi/schema/bomi_schema.sql` have matching SHA256 hashes.
- Static schema count: 15 explicit tables, 3 views, 0 triggers.
- JSON examples parse locally with PowerShell.
- Placeholder scan is clean.
- Git root is valid and clean.
- Review advancement commit: `3fed713 Advance BOMI to architecture review`.

Codex environment constraint:

- Local Codex environment still lacks `python`, `py`, and `sqlite3`, so Codex did not rerun Python tests locally.

## Open Issues

- Duplicate nested folders exist: `docs/docs`, `examples/examples`, and `tests/tests`. They are not blocking architecture review, but should be cleaned or documented before release packaging.
- User role model is not yet implemented.
- Permission model is not yet implemented.
- Audit logging is not yet implemented.
- IPI-to-BOMI project context link is not yet implemented.
- ClimateOS thermal-parameter model is not yet implemented.

## Decisions Needed

Please review and decide:

1. Does BOMI correctly extend BuildingOS from project governance into physical infrastructure object governance?
2. Is Building Service Spine framed correctly as an infrastructure interface standard rather than a product feature?
3. Are evidence, claim, review, approval, lifecycle, and runtime readiness boundaries clear enough?
4. Should audit logging be required in BOMI v0.2?
5. Should user roles and permissions be required in BOMI v0.2?
6. Should IPI project context linking be part of v0.2?
7. Should ClimateOS thermal parameters be included in v0.2 or deferred?
8. Should duplicate nested folders be cleaned before release or accepted as non-blocking artifacts?

## Recommended v0.2 Direction

Recommended milestone:

```text
BOMI v0.2 Governance Integration Layer
```

Recommended scope:

- User role model
- Reviewer accountability model
- Audit log structure
- API wrapper design brief
- SQLite FTS5 search design
- IPI project-context link model
- ClimateOS thermal-parameter placeholder model
- Integration tests for API/search layer

Do not expand yet into:

- Real IoT/LoRa ingestion
- Certification automation
- Frontend dashboard
- AI decision-making
- Proprietary manufacturer workflows

## Conversation Radar

Knowledge points:

- BOMI is ready for ChatGPT architecture/governance review under BEWP.
- Engineering source-of-truth conflicts have been resolved.
- Evidence-first architecture remains intact.
- Interface-first design remains the central product principle.

Idea points:

- v0.2 should add governance integration before market-facing features.
- Runtime ID should remain registration/readiness infrastructure, not automation.
- IPI and BOMI should connect project context to physical object governance.

Decisions:

- Current state is `READY_FOR_ARCHITECT_REVIEW`.
- Next owner is ChatGPT.
- Codex does not declare task closed yet.

Risks:

- Duplicate nested folders may confuse future packaging.
- Without user roles and audit logs, real pilot governance remains incomplete.
- ClimateOS integration needs domain framing before implementation.

Open questions:

- What is the minimum governance model for certifier/plumber/electrician/builder review?
- What lifecycle events are mandatory for pilot readiness?
- What evidence strength model is sufficient for physical building components?

Next actions:

- ChatGPT architecture review.
- Simon domain validation after architecture review.
- Codex converts review decisions into v0.2 engineering brief.
