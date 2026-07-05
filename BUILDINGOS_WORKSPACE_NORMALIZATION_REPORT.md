# BuildingOS Workspace Normalization Report

## Status

`COMPLETED`

## Purpose

Normalize BuildingOS work into a clean local Codex workspace aligned with the
official GitHub repository target.

Specification development is paused until this workspace normalization is
complete.

## Official GitHub Repository

```text
simon947161/BuildingOS
```

Remote URL configured locally:

```text
https://github.com/simon947161/BuildingOS.git
```

Remote availability was not verified from this sandboxed environment.

## Old Path

```text
C:\Users\doras\Documents\Codex\2026-06-29\task-001-infrastructure-project-intelligence-ipi\buildingos-modular-interface
```

## New Path

```text
C:\Users\doras\Documents\Codex\2026-06-29\task-001-infrastructure-project-intelligence-ipi\BuildingOS
```

## Branch

```text
main
```

## Git Status

Baseline commit created successfully.

```text
689f4d3 Initialize BuildingOS workspace
```

This report is added after the baseline commit so the report can cite the real
normalization baseline hash.

## Files Migrated

The following files were migrated from:

```text
buildingos-modular-interface\docs
```

to:

```text
BuildingOS\docs
```

Migrated document files:

- `BUILDINGOS_C00_GLOSSARY_FOUNDATION.md`
- `BUILDINGOS_C00_GLOSSARY_FREEZE_RECORD_V1_0.md`
- `BUILDINGOS_C00_GLOSSARY_SELF_REVIEW.md`
- `BUILDINGOS_C01_A_EVIDENCE_STANDARD.md`
- `BUILDINGOS_C01_A_EVIDENCE_STANDARD_APPROVAL_RECORD.md`
- `BUILDINGOS_C01_A_EVIDENCE_STANDARD_FREEZE_RECORD_V1_0.md`
- `BUILDINGOS_C01_A_EVIDENCE_STANDARD_SELF_REVIEW.md`
- `BUILDINGOS_C01_B_CLAIM_STANDARD.md`
- `BUILDINGOS_C01_B_CLAIM_STANDARD_FREEZE_RECORD_V1_0.md`
- `BUILDINGOS_C01_B_CLAIM_STANDARD_SELF_REVIEW.md`
- `BUILDINGOS_C01_C_IDENTITY_STANDARD.md`
- `BUILDINGOS_C01_C_IDENTITY_STANDARD_FREEZE_RECORD_V1_0.md`
- `BUILDINGOS_C01_C_IDENTITY_STANDARD_SELF_REVIEW.md`
- `BUILDINGOS_C01_D_REVIEW_STANDARD.md`
- `BUILDINGOS_C01_D_REVIEW_STANDARD_SELF_REVIEW.md`
- `BUILDINGOS_C01_SPECIFICATION_FOUNDATION_PLAN.md`
- `BUILDINGOS_CORE_ARCHITECTURE_APPROVAL_RECORD_2026_06_30.md`
- `BUILDINGOS_CORE_ARCHITECTURE_PROPOSAL_V0_1.md`
- `BUILDINGOS_CORE_ENGINEERING_PLAN_V0_1.md`
- `BUILDINGOS_ENGINEERING_WORKFLOW_PROTOCOL.md`
- `BUILDINGOS_INCREMENTAL_REVIEW_PRINCIPLE.md`
- `BUILDINGOS_ROADMAP_APPROVAL_RECORD_2026_07_01.md`
- `BUILDINGOS_ROADMAP_V1_0.md`
- `BUILDINGOS_SPECIFICATION_CHANGELOG.md`
- `BUILDINGOS_SPECIFICATION_DEPENDENCY_MAP.md`
- `BUILDINGOS_SPECIFICATION_INDEX.md`
- `CHATGPT_GOVERNANCE_REVIEW_HANDOFF.md`
- `CODEX_C00_ENGINEERING_REVIEW.md`
- `CODEX_C01_A_ENGINEERING_REVIEW.md`
- `CODEX_C01_B_ENGINEERING_REVIEW.md`
- `CODEX_C01_C_ENGINEERING_REVIEW.md`
- `CODEX_C01_D_ENGINEERING_REVIEW.md`
- `CODEX_C01_INTERNAL_ENGINEERING_REVIEW.md`
- `CODEX_ENGINEERING_REVIEW_BOMI_V0_1.md`
- `COMPONENT_PROFILE_TEMPLATE.md`
- `INSPECTION_RECORD_TEMPLATE.md`
- `LIFECYCLE_GOVERNANCE.md`
- `OPEN_BUILDING_INTERFACE_PROTOCOL.md`
- `QCLAW_C01_BUILDINGOS_SPEC_FOUNDATION_BRIEF_DRAFT.md`
- `QCLAW_CHANGE_REQUEST_BOMI_V0_1.md`
- `REPOSITORY_STRUCTURE.md`
- `SERVICE_SPINE_STANDARD.md`
- `TECHNICAL_DESIGN.md`

Additional workspace files created:

- `README.md`
- `WORKSPACE.md`
- `.gitignore`
- `BUILDINGOS_WORKSPACE_NORMALIZATION_REPORT.md`

## Files Not Migrated

The following were intentionally not migrated:

- `buildingos-modular-interface\bomi`
- `buildingos-modular-interface\tests`
- `buildingos-modular-interface\examples`
- `buildingos-modular-interface\schemas`
- `buildingos-modular-interface\verify.py`
- `buildingos-modular-interface\pyproject.toml`
- `buildingos-modular-interface\docs\docs`
- root IPI package folders: `ipi`, `schemas`, `tests`
- root IPI module docs under `docs`

Reason:

The normalization task is for BuildingOS specification, governance, roadmap,
and architecture documents. Runtime code, tests, examples, schemas, duplicated
nested docs, and IPI module artifacts are outside this workspace-normalization
scope.

## Source-of-Truth Folders

| Folder | Status | Purpose |
| --- | --- | --- |
| `BuildingOS\docs` | Active | BuildingOS specification, governance, roadmap, architecture, review, and freeze records. |

## Deprecated Folders Not To Use

| Deprecated Path | Reason |
| --- | --- |
| `buildingos-modular-interface` | Old mixed BOMI / BuildingOS engineering working folder. |
| root `docs` | IPI module documentation, not normalized BuildingOS source of truth. |
| root `ipi` | IPI Python package, not BuildingOS M1 specification workspace. |

## Git Validity

Git repository initialized successfully in the new workspace.

Local branch:

```text
main
```

Local remote:

```text
origin https://github.com/simon947161/BuildingOS.git
```

Known Git environment issue handled:

- Git reported `dubious ownership` because the Codex sandbox user differs from
  the Windows user.
- The baseline commit was created using a per-command `safe.directory`
  override.
- Repository-local Git identity was configured only inside this new workspace.

## Commit Hash

Normalization baseline commit:

```text
689f4d3 Initialize BuildingOS workspace
```

## Remaining Risks

1. GitHub remote reachability was not verified from this sandboxed environment.
2. The new workspace currently lives under the old task folder because that is
   the available writable root in this Codex session.
3. The official GitHub repository may need an initial push from this local
   repository after user approval.
4. Future migration to a higher-level local path such as
   `C:\Users\doras\Documents\Codex\BuildingOS` may be desirable if workspace
   permissions allow it later.

## Recommended Next Action

1. Treat `BuildingOS` as the active local BuildingOS workspace.
2. Do not continue C01-D work in `buildingos-modular-interface`.
3. Verify remote repository availability when network permissions allow.
4. Push `main` to `simon947161/BuildingOS` only after explicit user approval.
5. Resume BuildingOS M1 from C01-D approval/freeze workflow inside the new
   `BuildingOS` workspace.

