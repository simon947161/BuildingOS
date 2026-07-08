# BuildingOS Agent Profile Standard v0.1

**Project:** BuildingOS  
**Status:** Draft v0.1  
**Purpose:** Define a unified configuration format for all BuildingOS agents so that human contributors, Codex, QClaw, Review Agents, and future automation agents can share the same operating grammar.

---

## 1. Why this standard exists

BuildingOS is no longer a single-agent workflow.

It is an engineering organization composed of different roles:

- Simon as Chief Product Owner
- ChatGPT as Chief Architect
- Codex as Engineering Manager
- QClaw / Dai Kexing as Software Engineer Agent
- Future Review Agents for architecture, evidence, documentation, security, and release review

Without a shared profile format, each agent may describe its role, limits, working style, and execution rules differently. That creates drift.

This standard makes agent configuration explicit, reviewable, and version-controlled.

---

## 2. Core principle

Every BuildingOS agent must be configured as a role with:

```text
Identity
Soul
Responsibilities
Constraints
Coding / Execution Style
Review Rules
Runtime Rules
```

The goal is not personality decoration.

The goal is operational consistency.

An agent profile should answer:

1. Who is this agent?
2. What is this agent responsible for?
3. What must this agent never do?
4. How does this agent execute tasks?
5. How does this agent review its own output?
6. How does this agent interact with BuildingOS runtime, evidence, and governance rules?

---

## 3. Required folder structure

Each agent must live under:

```text
agents/<agent_id>/
```

Required files:

```text
agents/<agent_id>/
├── identity.md
├── soul.md
├── responsibilities.md
├── constraints.md
├── coding_style.md
├── review_rules.md
└── runtime.md
```

Optional files:

```text
agents/<agent_id>/
├── prompts.md
├── task_scope.md
├── escalation_rules.md
├── memory_policy.md
└── changelog.md
```

---

## 4. File definitions

### 4.1 identity.md

Defines the agent's name, role, background, domain, and position in the BuildingOS organization.

It should be short, stable, and specific.

It must not contain task-specific temporary instructions.

---

### 4.2 soul.md

Defines the agent's working temperament and decision style.

This file is allowed to describe behavior, but must remain operational.

It should not become fictional decoration.

Good content:

- pragmatic
- evidence-first
- review-oriented
- careful with claims
- direct in code review

Bad content:

- vague motivational slogans
- magical abilities
- unverifiable personality claims

---

### 4.3 responsibilities.md

Defines what the agent owns.

Examples:

- repository implementation
- schema design
- API development
- test writing
- evidence review
- documentation review
- sprint planning
- release notes

This file should make accountability clear.

---

### 4.4 constraints.md

Defines hard limits.

Examples:

- must not treat weak evidence as confirmed fact
- must not implement autonomous approval
- must not remove governance checks to pass tests
- must not introduce heavy dependencies unless approved
- must not silently change architecture decisions

Constraints are more important than style.

---

### 4.5 coding_style.md

Defines engineering preferences.

Examples:

- simple functions
- clear names
- small modules
- explicit validators
- testable helpers
- no magic logic
- no stale TODO placeholders
- no unnecessary framework

For non-coding agents, this file may be renamed to `execution_style.md`.

---

### 4.6 review_rules.md

Defines how the agent reviews work before completion.

Minimum review questions:

1. Does this follow Evidence-first Architecture?
2. Are Source, Evidence, Claim, Review, Decision, and Ledger separated where relevant?
3. Are assumptions clearly marked?
4. Are tests or smoke checks present?
5. Are docs aligned with implementation?
6. Are there any stale placeholders?
7. Is the output safe for future agents to extend?

---

### 4.7 runtime.md

Defines how the agent behaves during execution.

It should include:

- task intake rules
- execution order
- handoff rules
- error handling
- commit/report format
- interaction with Codex, QClaw, and Review Agents

---

## 5. Standard agent execution flow

All BuildingOS agents should follow this flow unless explicitly overridden:

```text
Task Intake
↓
Scope Check
↓
Architecture Alignment
↓
Implementation / Drafting
↓
Self Review
↓
Evidence / Test Check
↓
Documentation Update
↓
Handoff Report
```

For code tasks:

```text
Task
↓
Schema / Model
↓
Helper Functions
↓
Examples
↓
Tests
↓
Docs
↓
CI
↓
Report
```

---

## 6. Naming convention

Agent IDs should use lowercase kebab-case:

```text
daikexing
codex-engineering-manager
review-agent
architecture-reviewer
evidence-reviewer
```

Human-readable names may use Chinese or English.

Example:

```text
agent_id: daikexing
name: 代可行
role: Software Engineer Agent
```

---

## 7. Governance rule

Agent profiles are governance documents.

They should be reviewed before major changes.

Any profile change that modifies responsibility, authority, or constraints should be recorded in `changelog.md` or commit message.

---

## 8. Relationship to BuildingOS architecture

The agent profile standard supports the wider BuildingOS architecture:

```text
Knowledge
↓
Policy
↓
Procedure
↓
Evidence
↓
Review
↓
Decision
↓
Ledger
↓
Continuous Governance
```

Agents are not outside this architecture.

Agents are governed participants inside it.

---

## 9. First implementation target

The first concrete agent profile using this standard is:

```text
agents/daikexing/
```

This agent represents the Software Engineer Agent responsible for implementing BuildingOS modules under Codex direction.

---

## 10. Status

This is v0.1.

It is intentionally simple.

Future versions may add:

- machine-readable YAML front matter
- agent capability registry
- permission model
- review agent routing
- task-specific prompt overlays
- evidence-based agent performance logs
