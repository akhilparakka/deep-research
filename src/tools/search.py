from src.tools.tavily_search.tavily_search_result_with_images import (
    TavilySearchResultsWithImages,
)
from src.config import SEARCH_MAX_RESULTS
import json

tavily_search_tool = TavilySearchResultsWithImages(
    name="web_search",
    max_results=SEARCH_MAX_RESULTS,
    include_raw_content=True,
    include_images=True,
    include_image_descriptions=True,
)

if __name__ == "__main__":
    results = tavily_search_tool.invoke("cute panda")
    print(json.dumps(results, indent=2, ensure_ascii=False))
