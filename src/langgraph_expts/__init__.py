"""Package entrypoint for LangGraph experiments."""

from langgraph_expts.graphs.basic_graph import run_basic_text_graph


def main() -> None:
    """Run a deterministic starter graph from the CLI entrypoint."""

    result = run_basic_text_graph("getting started with")
    print(result)
