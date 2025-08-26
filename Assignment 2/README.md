Assignment 2 : Convert static instructions into dynamic instruction
objective
Convert static instructions into dynamic ones using OpenAI’s Agent SDK.

Base your work on the bilal_fareed_code example for hotel booking and information retrieval.

Update it so a single agent can store and retrieve details for multiple hotels.

Use context to return the correct hotel information based on the user’s query.

How to Run
# Clone This Respository

# Then Go to the Assignment Folder Directory
cd "Assignment 2"


# Install dependencies
uv add openai-agents python-dotenv

# Add API KEY in .env File
add GEMINI_API_KEY="YOUR_API_KEY_HERE" IN .env file 

# Run Dynamic Hotel Assistant
uv run main.py
