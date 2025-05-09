from src.config.agents import LLMType
from src.config import OPENAI_API_KEY, REASONING_MODEL_NAME, BASIC_MODEL_NAME
from langchain_openai import ChatOpenAI

_llm_cache: dict[LLMType, ChatOpenAI] = {}


def create_llm(model: str, api_key: str, temperature: float = 1.0) -> ChatOpenAI:
    llm_kwargs = {"model": model, "api_key": api_key, "temperature": temperature}

    return ChatOpenAI(**llm_kwargs)


def get_llm_by_type(llm_type: LLMType) -> ChatOpenAI:
    if llm_type in _llm_cache:
        return _llm_cache[llm_type]

    if llm_type == "reasoning":
        llm = create_llm(model=REASONING_MODEL_NAME, api_key=OPENAI_API_KEY)

    elif llm_type == "basic":
        llm = create_llm(model=BASIC_MODEL_NAME, api_key=OPENAI_API_KEY)

    elif llm_type == "vision":
        llm = create_llm(
            model=BASIC_MODEL_NAME,
            api_key=OPENAI_API_KEY,
        )

    else:
        raise ValueError(f"Unknown LLM type: {llm_type}")

    _llm_cache[llm_type] = llm

    return llm


reasoning_llm = get_llm_by_type("reasoning")
basic_llm = get_llm_by_type("basic")
