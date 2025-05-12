from src.prompts.planner_model import Plan
from langgraph.graph import MessagesState

from typing import Annotated
import operator


class State(MessagesState):
    """State for the agent system, extends MessagesState with next field."""

    observations: list[str] = []
    plan_iterations: int = 0
    current_plan: Plan | str = None
    final_report: str = ""
    auto_accepted_plan: bool = False
    enable_background_investigation: bool = True
    background_investigation_results: str = None
