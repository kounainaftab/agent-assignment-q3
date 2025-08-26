from typing import Any
from agents import (
    Agent,
    GuardrailFunctionOutput,
    Runner,
    RunContextWrapper,
    TResponseInputItem,
    input_guardrail,
)
from my_agents.guardrail_agents import input_agent

@input_guardrail
async def check_input(
    ctx: RunContextWrapper[Any],
    agent: Agent[Any],
    input_data: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    """
    Checks whether the provided input is math-related.
    If not math-related, triggers a tripwire to block further processing.
    """
    

    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_math
    )