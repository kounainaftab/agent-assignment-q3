from agents import Agent
from my_confg.confg import model
from data_schema.data_schema import MyDataType

guardrail_agent = Agent(
    name="Guardrail Agent for Hotels",
    instructions="""
    You are a guardrail assistant that validates if the user's query is about hotels in Pakistan. Analyze the query and determine if it pertains to hotel information (e.g., hotel names, locations like Karachi or Hunza, or hotel-related terms like rooms or amenities). Set is_query_about_hotel=True for hotel-related queries, and provide a reason for your decision.
    """,
    model=model,
    output_type=MyDataType
)