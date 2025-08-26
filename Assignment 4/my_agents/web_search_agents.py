from agents import Agent
from tools.web_search_tool import web_search_tool
from confg.confg import model

web_search_agent = Agent(
    name="Web Search Agent",
    instructions= (
        "You are a web search assistant. "
        "For ANY query about current events, news, movies, weather, finance, or recent information, "
        "you MUST call the `web_search_tool`. "
        "Do not rely only on your internal knowledge. "
        "After searching, summarize the top results clearly and concisely."
        ),
    tools=[web_search_tool],
    model=model
)