from langgraph.graph import StateGraph, START, END
from src.graph.nodes import (
    coordinator_node,
    planner_node,
    background_investigation_node,
    reporter_node,
)
from src.graph.types import State


def _build_graph():
    builder = StateGraph(State)

    builder.add_edge(START, "coordinator")
    builder.add_node("coordinator", coordinator_node)
    builder.add_node("background_investigator", background_investigation_node)
    builder.add_node("planner", planner_node)
    builder.add_node("reporter", reporter_node)
    builder.add_edge("coordinator", END)

    return builder.compile()


graph = _build_graph()
