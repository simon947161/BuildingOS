# Agent Profile Standard Addendum 001

## Purpose

This addendum clarifies the first implementation of the BuildingOS agent profile standard.

## Runtime file naming

The original standard names the final required file as `runtime.md`.

For the first concrete agent profile, the implementation uses:

```text
execution.md
```

This file serves the same purpose:

- task intake
- execution order
- handoff rules
- reporting rules

## Effective rule

For v0.1, either of the following is acceptable:

```text
runtime.md
execution.md
```

Future cleanup may standardize the name after more agents are added.

## First applied agent

```text
agents/daikexing/
```
