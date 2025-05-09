from typing import Literal

LLMType = Literal["basic", "reasoning", "vision"]

AGENT_LLM_MAP: dict[str, LLMType] = {
    "coordinator": "basic",
    "planner": "reasoning",
    "supervisor": "basic",
    "researcher": "basic",
    "coder": "basic",
    "browser": "vision",
    "reporter": "basic",
}
