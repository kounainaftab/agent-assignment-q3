import asyncio
from agents import Runner, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from my_agents.agents import general_agent, math_agent


async def main():
    try:
        msg = input("Enter you question : ")
        result = await Runner.run(general_agent, msg)
        print(f"\n\n final output : {result.final_output}")
    except InputGuardrailTripwireTriggered as ex:
        print("Error : invalid prompt")
    except OutputGuardrailTripwireTriggered:
        print("Error: Response contained restricted content (output guardrail triggered)")


asyncio.run(main())