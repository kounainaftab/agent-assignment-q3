from pydantic import BaseModel

class CheckGuardrailOutput(BaseModel):
    contains_offensive: bool
    reasoning: str