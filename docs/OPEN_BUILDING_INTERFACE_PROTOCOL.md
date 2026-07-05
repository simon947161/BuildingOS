# Open Building Interface Protocol

## 1. Purpose

The Open Building Interface Protocol defines how modular building components connect to a Building Service Spine.

It is manufacturer-neutral and interface-first.

## 2. Port Types

Supported v0.1 port types:

- `power`
- `water_supply`
- `hot_water`
- `drainage`
- `greywater`
- `data`
- `LoRa`
- `sensor`
- `HVAC`
- `solar`
- `battery`
- `EV`
- `ventilation`

## 3. Compatibility Logic

In v0.1, two ports are compatible when:

- The port type is the same.
- The connection standard is the same.

This is intentionally conservative. It does not infer compatibility from similar names or manufacturer claims.

## 4. Manufacturer Neutrality

The protocol should describe ports, standards, evidence, inspection status, and lifecycle state. It should not privilege any proprietary manufacturer database.

## 5. Compliance Readiness

Compliance readiness is not certification. It is a score that indicates whether evidence, inspection, approved ports, and replaceable service-spine access are present.

## 6. Human Accountability

The protocol supports certifiers, plumbers, electricians, builders, engineers, and reviewers. It does not replace them.

