---
agent: 'agent'
description: 'Generate an implementation checklist for a new LangGraph experiment in this repo'
---

Given a new experiment idea, generate:

1. A short problem statement.
2. A `src/` module plan under `src/langgraph_expts/graphs/`.
3. A matching notebook plan under `notebooks/`.
4. Required env vars and dependency checks.
5. Validation steps runnable with `uv`.
6. A short README update proposal.

Favor deterministic examples first, then model-backed variants.
