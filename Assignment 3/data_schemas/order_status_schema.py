from pydantic import BaseModel

class OrderStatusSchema(BaseModel):
    order_id: str