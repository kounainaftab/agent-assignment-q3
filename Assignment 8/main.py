import os
import requests
from dotenv import load_dotenv
from agents import (
    Agent, Runner, AsyncOpenAI,
    OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
)

# Disable tracing for cleaner logs
set_tracing_disabled(True)

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")

if not gemini_api_key or not weather_api_key:
    raise ValueError("❌ Both GEMINI_API_KEY and WEATHER_API_KEY must be set in your .env file.")

# Configure Gemini client with OpenAI compatibility
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Use Gemini model
my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Weather tool
@function_tool
def get_weather(city:str):
    """
    Returns the weather for a given city.
    """

    try:
        response = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}")
        data = response.json()
        return f"The weather in {city} is {data['current']['condition']['text']} with a temperature of {data['current']['temp_c']}°C and humidity of {data['current']['humidity']}%."
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

# Build Weather Agent
weather_agent = Agent(
    name="Weather Agent",
    instructions="""
    You are a helpful weather assistant.
    If the user asks about the weather in a city, use the weather tool.
    Always respond clearly with temperature and conditions.
    """,
    model=my_model,
    tools=[get_weather],
)

test_questions = [
    "What’s the weather in Hyderabad?",
    "Tell me the weather in Karachi",
    "How’s the weather in Lahore?",
]

for question in test_questions:
    print(f"\n🟢 User: {question}")
    result = Runner.run_sync(weather_agent, question)
    print(f"🤖 Bot: {result.final_output}")