# src/idea_enhancer/tools/custom_tool.py
import re
from ddgs import DDGS  # ← Updated import (was: from duckduckgo_search import DDGS)
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class SearchInput(BaseModel):
    query: str = Field(..., description="Concise, keyword-focused search query.")

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the internet for tech specs, legal regulations, market data, or competitor analysis."
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
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
            return "\n\n".join(formatted)
            
        except Exception as e:
            return f"Search failed: {str(e)}"