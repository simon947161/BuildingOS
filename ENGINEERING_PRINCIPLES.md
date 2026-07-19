# ENGINEERING_PRINCIPLES.md

**Status:** v0.1  
**Repository:** BuildingOS  
**Purpose:** Define shared engineering principles for BuildingOS and related OS projects.

---

## Core Principles

### 1. Read Before Plan

Every meaningful task begins by reading the project context.

### 2. Plan Before Edit

No substantial implementation should begin without a plan.

### 3. Architecture Before Implementation

Implementation should follow the architecture, not accidentally create a new one.

### 4. Evidence Before Claim

Separate observed facts, claims, inferences, proposals and unverified assumptions.

### 5. Review Before Merge

Meaningful changes should pass engineering review and, when needed, architecture review before merge.

### 6. Diff Before Trust

Inspect the diff before accepting a change.

### 7. Never Stop at Delivery

Every task should end by proposing the next meaningful task.

### 8. Human Accountability

Agents assist, organise, analyse and suggest. Final decisions remain with responsible humans.

### 9. Compact Before Context Overflow

Long sessions should be compacted into durable summaries.

### 10. Document Every Decision

Important decisions should be recorded in Markdown, issues, PRs or CRP notes.

### 11. Additive Upgrade by Default

Do not erase earlier thinking unless explicitly instructed. Upgrade by adding status, clarification and links.

### 12. Parent Governance, Local Application

Shared principles belong at the parent level. Local repositories should reference them and add local rules only when necessary.

---

## Default Checklist

Before editing, confirm:

```text
Context read: yes/no
Plan created: yes/no
Files identified: yes/no
Risk checked: yes/no
Review needed: yes/no
Owner decision needed: yes/no
```

After editing, report:

```text
Summary
Changed files
Diff reviewed
Tests or checks
Risks
Next recommended task
```
