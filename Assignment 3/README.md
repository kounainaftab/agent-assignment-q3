Assignment 3 : Build a Smart Customer Support Bot using OpenAI Agent SDK
Objective
Create a customer support bot using OpenAI's Agent SDK that can handle basic FAQs, fetch order statuses, and escalate to a human agent when necessary. The bot should also implement guardrails to ensure positive interactions and showcase advanced features of the SDK.

Requirements
You will build a bot that can assist customers with common queries and order tracking. The bot should be able to handle simple requests autonomously, use function tools to fetch data, and escalate to a human agent for complex queries or negative sentiment.

Answer basic product FAQs
Fetch order status using a simulated API (function tool)
Escalate to a human agent if the query is complex or sentiment is negative (handoff)
Enforce a simple guardrail: block or rephrase negative/offensive user input
Showcase usage of model_settings (tool_choice, metadata, etc.)
Showcase advanced use of @function_tool decorator, including is_enabled and error_function
Breakdown of Required Elements
1. Create Two Agents
BotAgent: Handles FAQs, order lookup (function tools).
HumanAgent: For escalation (handoff).
2. Implement Function Tools
@function_tool: get_order_status(order_id): Simulates fetching order status.

Use is_enabled to toggle the tool (e.g., only enabled for "order" queries).
Use error_function to return a friendly error if order_id not found.
3. Guardrails
Use @guardrail to check for offensive or negative language. If detected, return a warning or rephrase the response.
4. Agent Handoff
If the bot detects a query it can’t handle or sentiment is negative, handoff to the HumanAgent.
5. ModelSettings Usage
Set tool_choice="auto" or "required" and pass custom metadata (e.g., store customer ID).
Experiment with the effect of tool_choice and metadata in responses.
6. Bonus: Logging
Log all tool invocations and handoffs for traceability.
How to Run
# Clone This Respository

# Then Go to the Assignment Folder Directory
cd "Assignment 3"

# Install dependencies
uv add openai-agents python-dotenv

# Add API KEY in .env File
add GEMINI_API_KEY="YOUR_API_KEY_HERE" IN .env file 

# Run Smart Customer Support Bot
uv run main.py
