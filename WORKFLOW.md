# WORKFLOW.md

**Status:** v0.1  
**Repository:** BuildingOS  
**Purpose:** Define the standard engineering loop for BuildingOS and related OS projects.

---

## Standard Loop

```text
Read
  ↓
Understand
  ↓
Consult
  ↓
Plan
  ↓
Execute
  ↓
Verify
  ↓
Review
  ↓
Decide
  ↓
Compact
  ↓
Continue
```

---

## 1. Read

Read the required context before planning.

Default reading order:

```text
README.md
PROJECT_ROUTING.md
ENGINEERING_PRINCIPLES.md
AGENTS.md
WORKFLOW.md
CURRENT_SPRINT.md, if present
Relevant task or design document
```

---

## 2. Understand

Summarise the current goal, constraints, known risks and expected output.

Do not begin implementation until the task boundary is clear.

---

## 3. Consult

For major architecture or cross-repository changes, consult the architecture reviewer or owner before editing.

For small local edits, proceed to planning.

---

## 4. Plan

Use a plan-first pattern. The plan should identify files, actions, risks and review needs.

---

## 5. Execute

Codex or an execution agent may implement the approved plan.

Execution should stay inside the approved scope.

---

## 6. Verify

Check the result.

Verification may include:

- diff review
- tests
- link checks
- documentation consistency checks
- output review

---

## 7. Review

Review the result from both engineering and architecture perspectives.

Ask whether the change still fits the parent framework.

---

## 8. Decide

The owner decides whether to continue, revise, pause, merge or open the next task.

---

## 9. Compact

At the end of a meaningful session, produce a compact summary with decisions, files changed, risks and next actions.

---

## 10. Continue

Open the next task only after the previous task has a clear completion report and next-step recommendation.
