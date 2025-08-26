from agents import Agent
from confg.confg import model
from guardrails_functions.input_guardrail import check_input
from guardrails_functions.output_guardrail import check_output


# Agent specialized for math-related queries
math_agent = Agent(
    "MathAgent",
    instructions="You are a math agent",
    model=model,
    input_guardrails=[check_input],  # Guardrail checks before processing
)

# General-purpose helper agent
general_agent = Agent(
    "GeneralAgent",
    instructions="You are a helpful agent",
    model=model,
    output_guardrails=[check_output] # Guardrail add for political content 
)