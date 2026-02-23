---
description: "Python + LangGraph conventions for this repository"
applyTo: "**/*.py"
---

# Python + LangGraph Instructions

- Use `langgraph.graph.StateGraph` with explicit state typing.
- Keep node functions small and side-effect minimal.
- Keep provider-specific model code isolated from deterministic graph examples.
- Prefer reusable functions in `src/langgraph_expts/` over notebook-only helpers.
- Use `python-dotenv` and environment variables for API keys.
- Include docstrings for public functions and graph builders.
- Keep example code easy to run locally with `uv`.
