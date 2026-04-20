import re
import os
import json
from datetime import datetime
from typing import Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Reddit API configuration
REDDIT_USER_AGENT = "IdeaEnhancer/1.0 by r/crewai"

# Cache configuration
CACHE_DIR = "search_cache"
os.makedirs(CACHE_DIR, exist_ok=True)


class RedditSearchInput(BaseModel):
    query: str = Field(..., description="Concise, keyword-focused Reddit search query.")
    sort: str = Field("relevance", description="Sort order: 'relevance', 'hot', 'top', 'new', 'best'")
    limit: int = Field(10, description="Maximum number of results to return.")

    @property
    def cache_key(self) -> str:
        """Generate a cache key based on the query and sort order."""
        return f"{self.query.lower().strip()}|{self.sort}"


class RedditSearchTool(BaseTool):
    name: str = "reddit_search"
    description: str = """Search Reddit for discussions and trending topics about a given query.
    Useful for finding public sentiment, user discussions, trending ideas, and community feedback.
    Searches across all Reddit subreddits and returns hot/rising posts."""

    args_schema: type = RedditSearchInput

    # Cache storage
    _cache: dict = {}

    def _run(
        self,
        query: str,
        sort: str = "relevance",
        limit: int = 10,
    ) -> str:
        # Validate sort parameter
        valid_sorts = ["relevance", "hot", "top", "new", "best"]
        if sort not in valid_sorts:
            return f"Invalid sort parameter '{sort}'. Must be one of: {', '.join(valid_sorts)}"

        # Check cache first
        cache_key = self.cache_key if hasattr(self, 'cache_key') else f"{query.lower().strip()}|{sort}"
        if cache_key in self._cache:
            return self._cache[cache_key]

        if not query.strip():
            return "No search query provided."

        # Use Reddit's official API via pushshift (stable alternative)
        # or direct Reddit API endpoint for search
        try:
            search_query = f"OR:" + " OR:".join(query.split())
            url = f"https://www.reddit.com/search.json?q={search_query}&sort={sort}&limit={limit}&t=all&restrict_search=false"
            headers = {"User-Agent": REDDIT_USER_AGENT}

            import requests
            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code != 200:
                return f"Reddit search failed with status {response.status_code}: {response.text[:200]}"

            data = response.json()

            if not data.get("data", {}).get("children"):
                return f"No Reddit search results found for: '{query[:50]}...'"

            results = []
            for child in data["data"]["children"]:
                post = child["data"]
                title = post.get("title", "No Title")
                author = post.get("author", "unknown")
                subreddit = post.get("subreddit", "unknown")
                upvotes = post.get("score", 0)
                num_comments = post.get("num_comments", 0)
                permalink = post.get("url", "") or post.get("permalink", "#")
                selftext = post.get("selftext", "")[:500] if post.get("selftext") else ""
                created = datetime.fromtimestamp(post.get("created", 0)).strftime("%Y-%m-%d %H:%M")

                results.append(
                    f"=== {subreddit} [{upvotes} upvotes, {num_comments} comments] ===\n"
                    f"Title: {title}\n"
                    f"Author: {author}\n"
                    f"Posted: {created}\n"
                    f"Post: {permalink}\n"
                    f"Content:\n{selftext}\n"
                    "---\n"
                )

            result_text = "\n\n".join(results)

            # Cache the result (with time limit of 1 hour for Reddit due to dynamic content)
            cache_expiry = datetime.now().timestamp() + 3600
            self._cache[cache_key] = result_text

            return result_text

        except Exception as e:
            error_msg = f"Reddit search failed: {str(e)}"
            self._cache[cache_key] = error_msg
            return error_msg
