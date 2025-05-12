from langchain_community.tools.tavily_search.tool import TavilySearchResults
from src.tools.tavily_search.taviy_search_api_wrapper import (
    EnhancedTavilySearchAPIWrapper,
)
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from pydantic import Field
from typing import Optional, Tuple, Union, List, Dict
import json


class TavilySearchResultsWithImages(TavilySearchResults):
    include_image_descriptions: bool = False

    api_wrapper: EnhancedTavilySearchAPIWrapper = Field(
        default_factory=EnhancedTavilySearchAPIWrapper
    )

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> Tuple[Union[List[Dict[str, str]], str], Dict]:
        try:
            raw_results = self.api_wrapper.raw_results(
                query,
                self.max_results,
                self.search_depth,
                self.include_domains,
                self.exclude_domains,
                self.include_answer,
                self.include_raw_content,
                self.include_images,
                self.include_image_descriptions,
            )
        except Exception as e:
            return repr(e), {}

        cleaned_results = self.api_wrapper.clean_results_with_images(raw_results)
        print("sync", json.dumps(cleaned_results, indent=2, ensure_ascii=False))
        return cleaned_results, raw_results

    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> Tuple[Union[List[Dict[str, str]], str], Dict]:
        """Use the tool asynchronously."""
        try:
            raw_results = await self.api_wrapper.raw_results_async(
                query,
                self.max_results,
                self.search_depth,
                self.include_domains,
                self.exclude_domains,
                self.include_answer,
                self.include_raw_content,
                self.include_images,
                self.include_image_descriptions,
            )
        except Exception as e:
            return repr(e), {}
        cleaned_results = self.api_wrapper.clean_results_with_images(raw_results)
        print("async", json.dumps(cleaned_results, indent=2, ensure_ascii=False))
        return cleaned_results, raw_results
