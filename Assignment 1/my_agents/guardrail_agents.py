from agents import Agent
from confg.confg import model
from data_schema.data_output import MathOutPut, DataOutputCheck

input_agent = Agent(
        "InputGuardrailAgent",
        instructions="Check and verify if input is related to math",
        model=model,
        output_type=MathOutPut,
    )

output_agent = Agent(
        "OutputGuardrailAgent",
        instructions=(
            "Check the response and verify if the response contains political topics."
            "or references to political figures."
            "Return safe=True if no such content exists."
        ),
        model=model,
        output_type=DataOutputCheck,
    )