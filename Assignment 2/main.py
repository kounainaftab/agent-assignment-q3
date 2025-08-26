from agents import Runner, set_tracing_disabled,InputGuardrailTripwireTriggered
from my_agent.hotel_assistant import hotel_assistant

set_tracing_disabled(True)

try:
    user_context = {"hotel_name": "Pearl Continental Karachi"}
    res = Runner.run_sync(
        starting_agent=hotel_assistant, 
        input="tell me about pc hotel?",
        context=user_context
    )
    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(e)