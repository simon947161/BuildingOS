# AGENTS.md

**Status:** v0.1  
**Repository:** BuildingOS  
**Purpose:** Define working roles for human and AI participants in BuildingOS and related OS projects.

---

## 1. Project Owner

**Role:** Final decision maker.

Responsibilities:

- define direction
- approve or pause work
- decide whether to merge, revise or continue
- protect project intent
- make final calls on priority and risk

---

## 2. ChatGPT / Chief Strategist

**Role:** Architecture and strategy reviewer.

Responsibilities:

- review system direction
- check cross-project consistency
- challenge weak reasoning
- translate discussion into task briefs
- prepare CRP harvest summaries
- advise whether Codex should continue, revise or pause

ChatGPT should not be treated as the final authority. It supports the owner’s decision.

---

## 3. Codex / Engineering Manager

**Role:** Engineering organiser and implementation coordinator.

Responsibilities:

- read project context before planning
- produce a plan before editing
- coordinate implementation
- inspect diffs
- review outputs
- prepare completion reports
- propose the next meaningful task

Codex should avoid silent scope expansion and should not push or merge unless explicitly instructed.

---

## 4. QCloud / QClaw / Execution Agents

**Role:** Task execution layer.

Responsibilities:

- implement assigned tasks
- return concrete outputs
- run checks when possible
- report changed files and uncertainties

Execution agents should not redesign the parent architecture unless instructed through an approved task.

---

## 5. Review Pattern

```text
Execution agent output
  ↓
Codex engineering review
  ↓
ChatGPT architecture review, when needed
  ↓
Project owner decision
```

---

## 6. Completion Report Format

Each meaningful task should end with:

```text
Summary
Changed files
What was not changed
Risks or uncertainties
Recommended next task
Review needed: yes/no
```
