import os
from dotenv import load_dotenv
from agents import (
    Agent, Runner, AsyncOpenAI,
    OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
)

set_tracing_disabled(True)

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY is not set in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

my_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

@function_tool
def add(a: float, b: float):
    """Returns the sum of two numbers."""
    return a + b

@function_tool
def subtract(a: float, b: float):
    """Returns the difference of two numbers."""
    return a - b

@function_tool
def multiply(a: float, b: float):
    """Returns the product of two numbers."""
    return a * b

@function_tool
def divide(a: float, b: float):
    """Returns the quotient of two numbers."""
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

math_agent = Agent(
    name="Math Agent",
    instructions="""
    You are a helpful math assistant.
    Use the math tools (add, subtract, multiply, divide) to answer user questions.
    Always respond with the computed result in a clear way.
    """,
    model=my_model,
    tools=[add, subtract, multiply, divide],
)

test_questions = [
    "What is 5 + 7?",
    "Multiply 8 by 6",
    "Divide 20 by 4",
]

for q in test_questions:
    print(f"\n🟢 User: {q}")
    result = Runner.run_sync(math_agent, q)
    print(f"🤖 Bot: {result.final_output}")