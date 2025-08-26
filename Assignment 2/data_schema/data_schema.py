from pydantic import BaseModel

class MyDataType(BaseModel):
    is_query_about_hotel: bool
    reason: str