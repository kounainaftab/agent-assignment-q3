from agents import function_tool
from confg.confg import tavily_client

@function_tool
def web_search_tool(query: str) -> str:
    """Web Search Query Provider"""
    print("[DEBUG] Tavily Search")
    response = tavily_client.search(query)
    return response