# BuildingOS Modular Infrastructure Interface Technical Design

## 1. Purpose

BuildingOS Modular Infrastructure Interface (BOMI) is the first software skeleton for governing modular building infrastructure objects.

It describes, registers, verifies, inspects, and tracks components, service spines, interface ports, evidence records, lifecycle events, and runtime objects.

## 2. Architecture

```text
Source
-> Evidence
-> Claim
-> Review
-> Decision
-> Ledger
-> Continuous Governance
```

BOMI applies the same evidence-first architecture used by IPI, but its governed object is different.

Observation: IPI governs infrastructure projects.

Interpretation: BOMI governs physical building infrastructure systems.

Recommendation: keep the two modules separate but compatible through shared evidence, claim, review, runtime, and lifecycle concepts.

## 3. Entity Relationships

- `building_components` register physical components such as wall panels, floor cassettes, pods, frames, and service modules.
- `service_spines` register building-scale utility corridors.
- `interface_ports` connect components and spines through typed service interfaces.
- `claims` store structured assertions about an object.
- `evidence_records` support claims without becoming facts by default.
- `inspection_records` capture human inspection accountability.
- `lifecycle_events` record installation, inspection, maintenance, repair, replacement, and retirement.
- `runtime_objects` provide stable BuildingOS IDs for future runtime integration.

## 4. Evidence-First Design

Evidence is not fact. A certificate, drawing, inspection photo, test report, or manufacturer document supports a claim. The claim still needs review and verification before it can drive approval or operational decisions.

The schema separates `claims` from `evidence_records` so the system can preserve uncertainty, conflict, and review history.

## 5. Interface-First Design

BOMI treats the interface as the real standard. A modular wall, service pod, or panel is only governable when its ports are explicit:

- Port type
- Position
- Connection standard
- Inspection requirement
- Sensor capability
- Compliance status

Compatibility is deterministic in v0.1: two ports match when port type and connection standard match.

## 6. Runtime Object Model

Runtime IDs are stable identifiers generated from object type and object reference ID.

Examples:

- Component runtime ID
- Service spine runtime ID
- Interface port runtime ID
- Sensor node runtime ID

Runtime IDs prepare future BuildingOS and ClimateOS integration without implementing real IoT ingestion in v0.1.

## 7. Data Flow

1. Register component or service spine.
2. Define interface ports.
3. Add claims about compliance, material, fire rating, water connection, electrical connection, or inspection status.
4. Attach evidence records to claims.
5. Record inspections by accountable roles.
6. Update lifecycle events.
7. Bind runtime IDs when the object is ready for BuildingOS runtime governance.

## 8. Validation Requirements

- Component profiles must include manufacturer, material, component type, lifecycle stage, and runtime status.
- Interface ports must reference either a component or service spine.
- Evidence records must point to claims.
- Inspection records must preserve inspector role and result.
- Runtime objects must not imply automation or certification.

## 9. Risks and Controls

Risk: treating manufacturer data as certified compliance.

Control: manufacturer data is evidence, not approval.

Risk: hiding service paths behind finished surfaces.

Control: service spine standard requires visible route, inspection access, and replaceability principles.

Risk: premature automation.

Control: runtime IDs are registration identifiers only in v0.1.

Risk: proprietary lock-in.

Control: interface protocol is manufacturer-neutral and connection-standard based.

## 10. Conversation Radar

Knowledge points:

- BOMI extends BuildingOS from project governance into physical system governance.
- Building Service Spine is the core infrastructure object.
- Interface ports are the standardization unit.

Idea points:

- Use evidence and claims for component compliance.
- Treat runtime ID as readiness, not automation.
- Use service spine inspection access as a governance control.

Decisions:

- Create BOMI as a separate folder beside IPI.
- Use Python standard library and SQLite.
- Keep real compliance certification and IoT ingestion out of v0.1.

Risks:

- Building code interpretation requires qualified review.
- Physical interface standards need domain validation.
- Runtime readiness can be mistaken for operational automation.

Open questions:

- Which pilot object should be registered first: service spine, wall panel, or bathroom pod?
- Which jurisdiction's inspection roles should be modeled first?
- Should future versions align port standards with existing Australian or Chinese standards first?

Next actions:

- Add real source fixture examples.
- Add role-specific inspection checklists.
- Add schema migrations after initial validation.
- Add API contract once object model stabilizes.

Related project keywords:

- BuildingOS
- Modular Building Interface
- Building Service Spine
- Open Building Interface Protocol
- Lifecycle governance
- Runtime readiness
- ClimateOS integration

