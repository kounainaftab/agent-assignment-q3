from agents import Agent
from my_confg.confg import model
from dynamic_instructions.dynamic_instructions import hotel_dynamic_instructions  # type: ignore
from guardrail_function.guardrail_input_function import guardrial_input_function

hotel_assistant = Agent(
    name="Hotel Customer Care",
    instructions=hotel_dynamic_instructions,
    model=model,
    input_guardrails=[guardrial_input_function],
    output_guardrails=[]
)
