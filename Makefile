.PHONY: venv install lint run

venv:
	uv venv .venv

install: venv
	uv sync

lint:
	uvx ruff check src

run:
	uv run langgraph-expts
