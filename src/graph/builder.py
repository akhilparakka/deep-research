from langgraph.graph import StateGraph, START, END
from src.graph.nodes import (
    coordinator_node,
    planner_node,
    background_investigation_node,
    reporter_node,
    human_feedback_node,
    research_team_node,
    researcher_node,
    coder_node,
)
from src.graph.types import State
from langgraph.checkpoint.memory import MemorySaver


def build_graph():
    builder = StateGraph(State)

    builder.add_edge(START, "coordinator")
    builder.add_node("coordinator", coordinator_node)
    builder.add_node("background_investigator", background_investigation_node)
    builder.add_node("planner", planner_node)
    builder.add_node("reporter", reporter_node)
    builder.add_node("research_team", research_team_node)
    builder.add_node("researcher", researcher_node)
    builder.add_node("coder", coder_node)
    builder.add_node("human_feedback", human_feedback_node)
    builder.add_edge("coordinator", END)

    memory = MemorySaver()

    # return builder.compile(checkpointer=memory)
    return builder.compile()


graph = build_graph()
