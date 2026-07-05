# Repository Structure

```text
buildingos-modular-interface/
|-- README.md
|-- pyproject.toml
|-- schemas/
|   `-- sqlite/
|       `-- schema.sql
|-- bomi/
|   |-- __init__.py
|   |-- components.py
|   |-- interfaces.py
|   |-- service_spine.py
|   |-- evidence.py
|   |-- inspection.py
|   |-- lifecycle.py
|   |-- runtime.py
|   `-- matching.py
|-- docs/
|   |-- TECHNICAL_DESIGN.md
|   |-- SERVICE_SPINE_STANDARD.md
|   |-- OPEN_BUILDING_INTERFACE_PROTOCOL.md
|   |-- COMPONENT_PROFILE_TEMPLATE.md
|   |-- INSPECTION_RECORD_TEMPLATE.md
|   |-- LIFECYCLE_GOVERNANCE.md
|   `-- REPOSITORY_STRUCTURE.md
|-- examples/
|   |-- sample_service_spine.json
|   |-- sample_wall_component.json
|   |-- sample_sensor_port.json
|   `-- sample_inspection_record.json
|-- tests/
|   |-- test_schema_init.py
|   |-- test_component_profile.py
|   |-- test_interface_validation.py
|   |-- test_evidence_ranking.py
|   `-- test_runtime_id.py
`-- .github/
    `-- workflows/
        `-- ci.yml
```

