# BuildingOS Workspace Relocation Report

## Status

`WORKSPACE_RELOCATED_TO_D_DRIVE`

## Old Path

```text
C:\Users\doras\OneDrive\Documents\BuildingOS
```

Status:

```text
DEPRECATED
```

Reason:

- C drive storage is limited.
- OneDrive may create sync conflicts.

## New Path

```text
D:\Codex\BuildingOS
```

Status:

```text
OFFICIAL_LOCAL_WORKSPACE
```

## Remote URL

```text
https://github.com/simon947161/BuildingOS.git
```

## Branch

```text
main
```

## Latest Commit At Relocation Start

```text
24fde24 Add BuildingOS remote sync report and C02 planning brief
```

## Files Preserved

- `BUILDINGOS_CODEX_REENTRY_REPORT.md`
- `CODEX_CONTEXT_TRANSFER_PACKET.md`
- `PROJECT_CONTEXT.md`

## Files Moved Into New Workspace

- `BUILDINGOS_CODEX_REENTRY_REPORT.md`
- `CODEX_CONTEXT_TRANSFER_PACKET.md`
- `PROJECT_CONTEXT.md`

## Files Updated For Relocation

- `WORKSPACE.md`
- `PROJECT_CONTEXT.md`
- `CODEX_CONTEXT_TRANSFER_PACKET.md`

## Files Created For Relocation

- `BUILDINGOS_WORKSPACE_RELOCATION_REPORT.md`

## Git Status Target

After relocation commit and push, the target state is:

```text
## main...origin/main
```

with a clean working tree.

## Risks

- Old C drive / OneDrive workspace may be opened accidentally.
- OneDrive sync behavior may create duplicate or stale files if the old
  workspace continues to be used.
- Core implementation may start too early if the C02 review gate is skipped.
- Frozen M1 specifications must not be silently changed.
- Any future M1 edits require Change Request + Version Review.

## Next Recommended Action

```text
REVIEW_C02_CORE_IMPLEMENTATION_PLANNING_BRIEF
```

Then confirm:

1. Core repository structure.
2. First minimal Governance Kernel scope.
3. Test strategy.
4. C02-A documentation-only repository skeleton planning.

Do not start Core implementation until C02 is approved.

Do not involve QClaw.
