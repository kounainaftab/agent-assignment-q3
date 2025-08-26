from agents import Runner
from my_agents.web_search_agents import web_search_agent
import asyncio


async def main():
        try:
            print(f"\n--- Sending prompt to the Agent:")
            prompt = "What are the best sci-fi movies released in 2025?"
            result = await Runner.run(web_search_agent, prompt)
            print(result.final_output)
            print("✅ Conversation ended without error.")
        except:
            print("🚫 Conversation stopped due to error.")

asyncio.run(main())