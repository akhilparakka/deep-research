from langgraph.prebuilt import create_react_agent
from src.llms.llm import get_llm_by_type
from src.config.agents import AGENT_LLM_MAP
from src.prompts import apply_prompt_template
from src.tools import web_search_tool
from src.tools import python_repl_tool


def create_agent(agent_name: str, agent_type: str, tools: list, prompt_template: str):
    return create_react_agent(
        name=agent_name,
        model=get_llm_by_type(AGENT_LLM_MAP[agent_type]),
        tools=tools,
        prompt=lambda state: apply_prompt_template(prompt_template, state),
    )


research_agent = create_agent(
    "researcher", "researcher", [web_search_tool], "researcher"
)

coder_agent = create_agent("coder", "coder", [python_repl_tool], "coder")
