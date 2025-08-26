from typing import Any
from my_agents.guardrail_agents import input_agent, output_agent
from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    output_guardrail,
)

@output_guardrail
async def check_output(
    ctx: RunContextWrapper[Any], 
    agent: Agent[Any], 
    output_data: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    """ Blocks political topics and mentions to political figures. """
    result = await Runner.run(output_agent, output_data, context=ctx.context)
    final_output = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.safe
    )