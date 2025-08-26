from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    input_guardrail,
)
from typing import Any
from confg.confg import model
from data_schemas.check_guardrail_output import CheckGuardrailOutput


# Guardrail agent that checks the user messages
offensive_guardrail_agent = Agent(
    name="Offensive Language Checker",
    instructions="Check if the user's message contains offensive or disrespectful language.",
    output_type=CheckGuardrailOutput,
    model=model
)

# Input guardrail function
@input_guardrail
async def offensive_language_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    input: Any
) -> GuardrailFunctionOutput:
    result = await Runner.run(offensive_guardrail_agent, input=input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_offensive
    )
