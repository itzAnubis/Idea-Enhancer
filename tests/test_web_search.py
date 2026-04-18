# tests/test_web_search.py
import pytest
from idea_enhancer.tools.custom_tool import WebSearchTool

@pytest.fixture
def search_tool():
    return WebSearchTool()

class TestWebSearchTool:
    def test_returns_clean_string(self, search_tool):
        # Use a broader, high-traffic query that DDG reliably indexes
        result = search_tool._run("Python 3.13 new features")
        assert isinstance(result, str)
        assert len(result) > 100  # Should return multiple results
        # Ensure no raw HTML leaked through
        assert "<div" not in result.lower() and "<script" not in result.lower()

    def test_handles_empty_query(self, search_tool):
        result = search_tool._run("")
        assert isinstance(result, str)
        assert len(result) > 0  # Should return fallback message

    def test_tool_metadata(self, search_tool):
        assert search_tool.name == "web_search"
        assert "internet" in search_tool.description.lower()
        assert hasattr(search_tool, "args_schema")