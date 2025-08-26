import os
from dotenv import load_dotenv
import asyncio
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

set_tracing_disabled(True)
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY is not set in the environment variables.")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=provider,
)

agent = Agent(
    name="FAQ Bot",
    model=model,
    instructions="You are a helpful FAQ bot. Only answer questions from the predefined set: "
                 "1. What is your name? "
                 "2. What can you do? "
                 "3. Who created you? "
                 "4. How can I use you? "
                 "5. Say goodbye."
)

runner = Runner()

test_questions = [
    "What is your name?",
    "What can you do?",
    "Who created you?",
    "How can I use you?",
    "Say goodbye."
]

async def main():
    for q in test_questions:
        print(f"\n🟢 User: {q}")
        response = await runner.run(agent, q)
        print(f"🤖 Bot: {response.final_output}")

if __name__ == "__main__":
    asyncio.run(main())