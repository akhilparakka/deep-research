from src.agents.llm import reasoning_llm

if __name__ == "__main__":
    stream = reasoning_llm.stream("what is model context protocol?")
    full_response = ""
    for chunk in stream:
        full_response += chunk.content
    print(full_response)
