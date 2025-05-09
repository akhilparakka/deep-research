from langgraph.prebuilt import create_react_agent
from src.config.agents import AGENT_LLM_MAP
from src.prompts import apply_prompt_template
from src.agents.llm import get_llm_by_type


research_agent = create_react_agent(
    get_llm_by_type(AGENT_LLM_MAP["researcher"]),
    tools=[],
    prompt=lambda state: apply_prompt_template("researcher", state),
)

coder_agent = create_react_agent(
    get_llm_by_type(AGENT_LLM_MAP["coder"]),
    tools=[],
    prompt=lambda state: apply_prompt_template("coder", state),
)

browser_agent = create_react_agent(
    get_llm_by_type(AGENT_LLM_MAP["browser"]),
    tools=[],
    prompt=lambda state: apply_prompt_template("browser", state),
)
