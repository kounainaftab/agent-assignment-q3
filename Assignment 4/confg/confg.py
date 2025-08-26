import os 
from agents import AsyncOpenAI , OpenAIChatCompletionsModel , set_tracing_disabled
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
set_tracing_disabled(True)

if not gemini_api_key or not tavily_api_key:
    raise ValueError("Please set both GEMINI_API_KEY and TAVILY_API_KEY in the .env file!")

tavily_client = TavilyClient(api_key=tavily_api_key)

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=provider,
)
