# PROJECT_ROUTING.md

**Status:** v0.1  
**Repository:** BuildingOS  
**Purpose:** Define the standard entry path for humans, Codex, ChatGPT, QCloud/QClaw, and future execution agents working inside BuildingOS and related OS projects.

---

## 1. Start Here

Before planning or editing, every agent should read this file first.

BuildingOS is the parent infrastructure governance framework. Wagga ClimateOS is currently the first regional climate adaptation application. Future OS projects such as WaterOS, EnergyOS, LandOS, CarbonOS and other application layers should reuse this routing logic unless a project-specific routing file overrides it.

---

## 2. Required Reading Order

For every non-trivial task, read in this order:

```text
README.md
  ↓
PROJECT_ROUTING.md
  ↓
ENGINEERING_PRINCIPLES.md
  ↓
AGENTS.md
  ↓
WORKFLOW.md
  ↓
CURRENT_SPRINT.md, if present
  ↓
Relevant task, issue, PR, CRP note or design document
```

Do not jump directly into implementation before this reading sequence unless the user explicitly requests a tiny isolated edit.

---

## 3. Repository Role

BuildingOS is the parent governance platform for infrastructure and built-environment operating systems.

It may host or guide:

- regional ClimateOS applications
- WaterOS and drainage / water-balance applications
- EnergyOS and community energy applications
- CarbonOS and ESG / disclosure applications
- Building interface and modular construction governance
- PPP / BOT / infrastructure procedure governance
- Community Lighthouse and resilience infrastructure models

---

## 4. Default Task Mode

Unless the user clearly says otherwise, use this default mode:

```text
Mode: plan first, then report
Edit: only after plan is clear
Push: never push or merge unless explicitly instructed
Decision: human owner decides next step
```

---

## 5. Escalation Rules

Escalate to ChatGPT / Chief Strategist review before editing when a task involves:

- architecture changes
- new runtime design
- governance model changes
- cross-repository implications
- legal, financial, environmental approval, insurance, emergency or public-safety interpretation
- deletion or rewriting of existing conceptual material

Local implementation details may proceed through Codex and execution agents after the plan is reviewed.

---

## 6. Completion Rule

A task is not complete when a file is created.

A task is complete only when it reports:

1. what changed
2. why it changed
3. what was not changed
4. risks or uncertainties
5. recommended next task
6. whether ChatGPT / owner review is needed

---

## 7. Relationship to Future Governance Repository

This repository currently acts as the parent operating framework. In the future, these shared rules may be extracted into a separate governance repository, for example:

```text
ClimateOS-Governance
```

Until that exists, BuildingOS is the practical home for shared engineering principles and agent workflow rules.
