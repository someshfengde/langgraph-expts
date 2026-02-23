"""Minimal deterministic LangGraph examples for local experimentation."""

from typing_extensions import TypedDict

from langgraph.graph import START, END, StateGraph


class TextState(TypedDict):
    """State passed through the graph."""

    text: str


def append_hello(state: TextState) -> dict[str, str]:
    """Append a greeting token to the input text."""

    return {"text": f"{state['text']} hello".strip()}


def append_langgraph(state: TextState) -> dict[str, str]:
    """Append a LangGraph token to demonstrate node chaining."""

    return {"text": f"{state['text']} langgraph".strip()}


def build_basic_text_graph():
    """Build and compile a deterministic starter graph."""

    graph = StateGraph(TextState)
    graph.add_node("append_hello", append_hello)
    graph.add_node("append_langgraph", append_langgraph)
    graph.add_edge(START, "append_hello")
    graph.add_edge("append_hello", "append_langgraph")
    graph.add_edge("append_langgraph", END)
    return graph.compile()


def run_basic_text_graph(seed_text: str = "") -> TextState:
    """Run the compiled starter graph and return final state."""

    compiled_graph = build_basic_text_graph()
    return compiled_graph.invoke({"text": seed_text})
