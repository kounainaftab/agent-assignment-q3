Assignment 1: Implement output guardrail functionality
Objective
Extend the guardrails.py example to add output guardrails using OpenAI’s Agent SDK.

Current code blocks non-math queries (input guardrails).

Add rules so agent responses avoid political topics and references to political figures.

How to Run
# Clone This Respository

# Then Go to the Assignment Folder Directory
cd "Assignment 1"

# Install dependencies
uv add openai-agents python-dotenv

# Add API KEY in .env File
add GEMINI_API_KEY="YOUR_API_KEY_HERE" IN .env file 

# Run Guardrails assignment
uv run main.py
