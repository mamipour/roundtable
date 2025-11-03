"""
External knowledge tools for roundtable discussions.

Provides access to:
- Web search (Tavily)
- Wikipedia summaries
- Academic papers (arXiv)
"""

import os
from typing import List
from langchain_core.tools import Tool

try:
    import wikipedia
except ImportError:
    wikipedia = None

try:
    import arxiv
except ImportError:
    arxiv = None

try:
    from tavily import TavilyClient
except ImportError:
    TavilyClient = None


# --- Tavily Web Search Tool ---
def _create_tavily_tool() -> Tool:
    """Create Tavily search tool if API key is configured."""
    api_key = os.getenv('TAVILY_API_KEY')
    
    if not api_key or not TavilyClient:
        return None
    
    tavily_client = TavilyClient(api_key=api_key)
    
    def tavily_search(query: str) -> str:
        """Search the web using Tavily AI search engine."""
        try:
            results = tavily_client.search(query=query, search_depth="basic")
            if not results.get("results"):
                return f"No results found for: {query}"
            
            # Format results
            output = []
            for r in results.get("results", []):
                output.append(f"• {r.get('title', 'No title')}")
                output.append(f"  {r.get('content', 'No content')}")
                output.append(f"  Source: {r.get('url', 'No URL')}")
            
            return "\n".join(output)
        except Exception as e:
            return f"Tavily search error: {str(e)}"
    
    return Tool(
        name="tavily_search",
        func=tavily_search,
        description=(
            "Search the web for current information and recent news. "
            "Use for up-to-date facts, current events, and real-time data. "
            "Input: search query (str)"
        )
    )


# --- Wikipedia Tool ---
def _create_wikipedia_tool() -> Tool:
    """Create Wikipedia search tool if library is installed."""
    if not wikipedia:
        return None
    
    def wikipedia_search(query: str) -> str:
        """Get a summary of a topic from Wikipedia."""
        try:
            summary = wikipedia.summary(query, sentences=5)
            return f"Wikipedia Summary for '{query}':\n\n{summary}"
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Disambiguation needed for '{query}'. Options: {', '.join(e.options[:5])}"
        except wikipedia.exceptions.PageError:
            return f"Wikipedia page not found for: {query}"
        except Exception as e:
            return f"Wikipedia search error: {str(e)}"
    
    return Tool(
        name="wikipedia_search",
        func=wikipedia_search,
        description=(
            "Get information from Wikipedia for general knowledge topics, "
            "historical facts, and biographical information. "
            "Input: topic or person name (str)"
        )
    )


# --- ArXiv Academic Papers Tool ---
def _create_arxiv_tool() -> Tool:
    """Create arXiv search tool if library is installed."""
    if not arxiv:
        return None
    
    def arxiv_search(query: str) -> str:
        """Search for academic papers on arXiv."""
        try:
            search = arxiv.Search(
                query=query,
                max_results=3,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )
            
            papers = list(search.results())
            
            if not papers:
                return f"No papers found on arXiv for: {query}"
            
            output = []
            for i, paper in enumerate(papers, 1):
                output.append(f"\n{i}. {paper.title}")
                output.append(f"   Authors: {', '.join([a.name for a in paper.authors[:3]])}")
                output.append(f"   Published: {paper.published.strftime('%Y-%m-%d')}")
                output.append(f"   Summary: {paper.summary[:300]}...")
                output.append(f"   URL: {paper.pdf_url}")
            
            return "\n".join(output)
        except Exception as e:
            return f"ArXiv search error: {str(e)}"
    
    return Tool(
        name="arxiv_search",
        func=arxiv_search,
        description=(
            "Search for academic papers and research on arXiv. "
            "Use for scientific research, technical papers, and cutting-edge findings. "
            "Input: research topic or query (str)"
        )
    )


def get_available_tools() -> List[Tool]:
    """
    Get all available external tools.
    
    Returns:
        List of Tool objects for use in roundtable
    """
    tools = []
    
    # Try to create each tool
    tavily = _create_tavily_tool()
    if tavily:
        tools.append(tavily)
    
    wikipedia_t = _create_wikipedia_tool()
    if wikipedia_t:
        tools.append(wikipedia_t)
    
    arxiv_t = _create_arxiv_tool()
    if arxiv_t:
        tools.append(arxiv_t)
    
    return tools


def print_tools_status():
    """Print status of available tools."""
    print("\n📚 Available Tools Status:\n")
    
    # Tavily
    if TavilyClient and os.getenv('TAVILY_API_KEY'):
        print("✅ Tavily Web Search - AVAILABLE")
    else:
        print("❌ Tavily Web Search - NOT CONFIGURED")
        if not TavilyClient:
            print("   (Install: pip install tavily-python)")
        else:
            print("   (Set TAVILY_API_KEY in .env)")
    
    # Wikipedia
    if wikipedia:
        print("✅ Wikipedia Search - AVAILABLE")
    else:
        print("❌ Wikipedia Search - NOT INSTALLED")
        print("   (Install: pip install wikipedia-api)")
    
    # ArXiv
    if arxiv:
        print("✅ ArXiv Search - AVAILABLE")
    else:
        print("❌ ArXiv Search - NOT INSTALLED")
        print("   (Install: pip install arxiv)")
    
    print()


# Pre-create all available tools
AVAILABLE_TOOLS = get_available_tools()
