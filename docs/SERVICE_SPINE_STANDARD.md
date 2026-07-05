# Building Service Spine Standard

## 1. Concept

The Building Service Spine is a building-scale utility corridor. It organizes services that are usually scattered, hidden, or hard to inspect.

It may include:

- Electrical services
- Plumbing services
- Drainage
- Data services
- LoRa and sensor nodes
- Solar, battery, EV, and energy interfaces
- HVAC and ventilation interfaces
- Inspection access
- Maintenance and replacement records

## 2. Design Principle

The real standard is not the wall panel. The real standard is the interface.

## 3. Water and Electrical Separation

Water, drainage, electrical, data, and energy pathways should be logically separated in the registered service spine. The database should record the relevant zones rather than assuming co-location is acceptable.

## 4. Visible Route Principle

The service route should be inspectable and explainable. A future reviewer should be able to understand where services run, what they connect to, and how they can be accessed.

## 5. Inspection Access Principle

Inspection access is a first-class field, not a note. A spine without inspection access should not be treated as lifecycle-ready.

## 6. Replaceable Module Principle

Service modules should be replaceable without destructive work where possible. The helper `can_replace_without_demolition` checks for replaceable module, inspection access, and non-restricted access type.

## 7. Evidence Requirement

Claims about service zones, access, replaceability, or compliance require supporting evidence records and human review.

