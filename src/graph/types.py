from langgraph.graph import MessagesState
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import MessagesState

from src.config import TEAM_MEMBERS

OPTIONS = TEAM_MEMBERS + ["FINISH"]


class State(MessagesState):
    """State for the agent system, extends MessagesState with next field."""

    TEAM_MEMBERS: list[str]

    next: str
    full_plan: str
    deep_thinking_mode: bool
    search_before_planning: bool


class Router(TypedDict):
    """Worker to route to next. If no workers needed, route to FINISH."""

    next: Literal[*OPTIONS]
