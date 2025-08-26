from agents import Runner, InputGuardrailTripwireTriggered
from my_agents.bot_agent import bot_agent
import asyncio


async def main():
        try:
            print(f"\n--- Sending prompt to the Agent:")
            prompt = "Check order status for ID 1015?"
            #prompt = "what is web development"
            result = await Runner.run(bot_agent, prompt)
            print(result.final_output)
            print("✅ Conversation ended without guardrail trigger.")
        except InputGuardrailTripwireTriggered:
            print("🚫 Conversation stopped due to guardrail trigger.")

asyncio.run(main())