from langchain_openai import ChatOpenAI
from src.config import load_yaml_config
from src.config.agents import LLMType
from typing import Dict, Any
from pathlib import Path

_llm_cache: dict[LLMType, ChatOpenAI] = {}


def _create_llm(llm_type: LLMType, conf: Dict[str, Any]) -> ChatOpenAI:
    llm_type_map = {
        "reasoning": conf.get("REASONING_MODEL"),
        "basic": conf.get("BASIC_MODEL"),
        "vision": conf.get("VISION_MODEL"),
    }

    llm_conf = llm_type_map.get(llm_type)
    if not llm_conf:
        raise ValueError(f"Unknown LLM Type: {llm_type}")

    if not isinstance(llm_conf, dict):
        raise ValueError(f"Invalid LLM Conf: {llm_type}")

    return ChatOpenAI(**llm_conf)


def get_llm_by_type(llm_type: LLMType) -> ChatOpenAI:
    """Get LLM instance buy type. Returns Cached if available"""
    if llm_type in _llm_cache:
        return _llm_cache[llm_type]

    conf = load_yaml_config(
        str((Path(__file__).parent.parent.parent / "conf.yaml").resolve())
    )

    llm = _create_llm(llm_type, conf)
    _llm_cache[llm_type] = llm
    return llm


basic_llm = get_llm_by_type("basic")

if __name__ == "__main__":
    print(basic_llm.invoke("Hello"))
