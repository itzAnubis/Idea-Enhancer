# src/idea_enhancer/tools/custom_tool.py
import re
import os
from ddgs import DDGS
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, Dict

# Cache configuration
CACHE_DIR = "search_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

class SearchInput(BaseModel):
    query: str = Field(..., description="Concise, keyword-focused search query.")
    
    @property
    def cache_key(self) -> str:
        """Generate a cache key based on the query."""
        return self.query.lower().strip()

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the internet for tech specs, legal regulations, market data, or competitor analysis."
    args_schema: Type[BaseModel] = SearchInput
    
    # Cache storage
    _cache: Dict[str, str] = {}
    
    def _run(self, query: str) -> str:
        # Check cache first
        cache_key = self.cache_key if hasattr(self, 'cache_key') else query.lower()
        if cache_key in self._cache:
            return self._cache[cache_key]
            
        if not query.strip():
            return "No relevant search results found."
            
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
            
            if not results:
                # Fallback: try a simplified query
                simplified = query.split()[0:4] if len(query.split()) > 4 else query
                if simplified != query:
                    with DDGS() as ddgs:
                        results = list(ddgs.text(" ".join(simplified), max_results=3))
            
            if not results:
                return f"No results for query: '{query[:50]}...'"
            
            # Clean & structure results
            formatted = []
            for i, r in enumerate(results, 1):
                title = r.get("title", "No Title")
                snippet = r.get("body", "")
                # Remove URLs/HTML artifacts
                snippet = re.sub(r'http\S+|<[^>]+>', '', snippet).strip()
                formatted.append(f"{i}. {title}\n   {snippet[:400]}...")
            result_text = "\n\n".join(formatted)
            
            # Cache the result
            self._cache[cache_key] = result_text
            
            return result_text
            
        except Exception as e:
            error_msg = f"Search failed: {str(e)}"
            self._cache[cache_key] = error_msg
            return error_msg