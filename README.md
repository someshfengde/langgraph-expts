# langgraph-expts

Experiments for learning and comparing LangGraph agent patterns in a clean
`src`-based Python project.

## Goals

- Explore LangGraph fundamentals with deterministic examples first.
- Build model-powered agents incrementally.
- Keep reusable logic in `src/` and exploratory work in `notebooks/`.

## Tech choices

- Python + LangGraph (+ LangChain helpers)
- `uv` for environment management
- `uv` for dependency management

## Project structure

- `src/langgraph_expts/` — reusable package code
- `src/langgraph_expts/graphs/` — graph experiments
- `notebooks/` — exploratory notebooks
- `.github/` — Copilot repo guidance and instructions

## Quick start

1. Install dependencies:
	- `uv sync`
2. Add secrets in `.env` (placeholders are already provided):
	- `OPENAI_API_KEY`
	- `ANTHROPIC_API_KEY`
	- `LANGSMITH_API_KEY` (optional)
3. Run the starter script:
	- `uv run langgraph-expts`
4. Open the starter notebook:
	- `notebooks/01_langgraph_quickstart.ipynb`

## First experiment included

`src/langgraph_expts/graphs/basic_graph.py` contains a tiny deterministic
workflow using `StateGraph` with typed state.

Expected output shape:

```python
{"text": "getting started with hello langgraph"}
```

## Next steps

- Add a tool-calling loop agent with conditional edges.
- Compare Graph API and Functional API in matching notebooks.
- Capture findings and tradeoffs as experiments evolve.
