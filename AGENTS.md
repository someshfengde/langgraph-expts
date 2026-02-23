# Agentic Repository Guide

This repository uses a three-layer structure for AI-assisted development:

1. **Foundation**: `.github/copilot-instructions.md`
2. **Instructions**: `.github/instructions/*.instructions.md`
3. **Project Code**: `src/` and `notebooks/`

## Scope
- Build and compare LangGraph agent patterns.
- Keep experiments reproducible in notebooks.
- Promote stable examples into `src/langgraph_expts/`.

## Working Rules
- Use `uv` for all Python environment and dependency workflows.
- Keep secrets in `.env` only.
- Prefer incremental, testable graph experiments.
- Document each experiment in `README.md`.
