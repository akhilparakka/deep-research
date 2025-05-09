from langchain_community.tools.tavily_search import TavilySearchResults


tavilly_tool = TavilySearchResults(
    max_results=5,
)
