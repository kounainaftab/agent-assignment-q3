from agents import input_guardrail,RunContextWrapper,GuardrailFunctionOutput,Runner
from my_agent.guardrail_agent import guardrail_agent

@input_guardrail
async def guardrial_input_function(ctx:RunContextWrapper,agent,input):
    result = await Runner.run(guardrail_agent, input=input, context=ctx.context )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_about_hotel
    )
