# Project: langgraph-expts

## Overview
This repository is for experimenting with LangGraph in Python, using both scripts and Jupyter notebooks.

## Tech Stack
- Language: Python
- Frameworks/Libraries: LangGraph, LangChain
- Environment manager: uv
- Package manager: uv
- Structure: src-based package layout

## Repository Conventions
- Place Python package code under `src/langgraph_expts/`.
- Keep notebooks under `notebooks/` and make them reproducible.
- Use small, composable graph nodes and typed state (`TypedDict` or Pydantic models).
- Load secrets from `.env` via `python-dotenv`; never hardcode API keys.

## Coding Guidelines
- Follow PEP 8.
- Use type hints and concise docstrings.
- Prefer deterministic examples first; add model-powered variants as optional steps.

## Suggested Workflow
1. Add a graph experiment in `src/langgraph_expts/graphs/`.
2. Add a matching exploratory notebook in `notebooks/`.
3. Validate using `uv run ...`.
4. Document findings in `README.md`.

## Do Not
- Commit real secrets.
- Mix package code directly in notebooks when reusable code belongs in `src/`.
