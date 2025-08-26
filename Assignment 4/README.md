Custom Web Search Tool

📄 Files:

tools/web_search_tool.py

my_agents/web_search_agent.py

confg/confg.py

main.py

.env

🎯 Objective Build a custom web search tool using the Tavily API that integrates with an AI Agent for retrieving and processing live web information.

✨ Features Implemented

🌐 Integrated Tavily API with .env-based API key management.

🛠 @function_tool for web_search_tool(query: str):

Fetches live results from Tavily.

Summarizes top 3 results for clear output.

🤖 Configured WebSearchAgent with:

Strong instructions to always use the search tool for real-world queries.

Gemini model for natural language reasoning.

📊 Handles queries about news, weather, finance, movies, and more.

🧪 Tested Scenarios

✔ “What is the weather in Karachi today?” → Tavily fetches live weather info.

✔ “Latest sci-fi movies in 2025” → Returns up-to-date movie info.

✔ “Current price of Bitcoin” → Fetches financial updates.

✔ “Latest news in Pakistan” → Summarizes top news headlines.

How to Run
Install dependencies
uv add openai-agents python-dotenv tavily-python

Add API KEYS in .env File
GEMINI_API_KEY="YOUR_GEMINI_KEY" TAVILY_API_KEY="YOUR_TAVILY_KEY"

Run Custom Web Search Tool
cd "Assignment 4" uv run main.py
