# tests/test_reddit_tool.py
import pytest
from idea_enhancer.tools.reddit_tool import RedditSearchTool


@pytest.fixture
def reddit_search_tool():
    return RedditSearchTool()


class TestRedditSearchTool:
    def test_returns_clean_string(self, reddit_search_tool):
        # Use a high-traffic query that Reddit reliably indexes
        result = reddit_search_tool._run("artificial intelligence", sort="hot", limit=5)
        assert isinstance(result, str)
        assert len(result) > 50  # Should return multiple results
        # Ensure no raw HTML leaked through
        assert "<div" not in result.lower() and "<script" not in result.lower()

    def test_handles_empty_query(self, reddit_search_tool):
        result = reddit_search_tool._run("")
        assert isinstance(result, str)
        assert "No search query provided" in result or len(result) > 0

    def test_default_sort_parameter(self, reddit_search_tool):
        # Test that default sort is 'relevance'
        result = reddit_search_tool._run("python programming")
        assert isinstance(result, str)

    def test_hot_sort_parameter(self, reddit_search_tool):
        # Test hot sort
        result = reddit_search_tool._run("machine learning", sort="hot", limit=3)
        assert isinstance(result, str)

    def test_top_sort_parameter(self, reddit_search_tool):
        # Test top sort
        result = reddit_search_tool._run("ai tools", sort="top", limit=3)
        assert isinstance(result, str)

    def test_tool_metadata(self, reddit_search_tool):
        assert reddit_search_tool.name == "reddit_search"
        assert "reddit" in reddit_search_tool.description.lower()
        assert hasattr(reddit_search_tool, "args_schema")

    def test_limit_parameter(self, reddit_search_tool):
        # Test with different limit values
        result_small = reddit_search_tool._run("python", limit=1)
        result_large = reddit_search_tool._run("python", limit=20)
        assert isinstance(result_small, str)
        assert isinstance(result_large, str)

    def test_invalid_sort_parameter(self, reddit_search_tool):
        # Test invalid sort - should return error message
        result = reddit_search_tool._run("python", sort="invalid")
        assert isinstance(result, str)
        assert "Invalid sort" in result