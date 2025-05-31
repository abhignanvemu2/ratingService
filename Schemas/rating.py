# schemas/rating.py

from pydantic import BaseModel, Field
from typing import Optional

class OrderRatingCreate(BaseModel):
    user_id: int
    order_id: int
    restaurant_id: int
    order_rating: float = Field(..., ge=1.0, le=5.0)

class DeliveryRatingCreate(BaseModel):
    user_id: int
    order_id: int
    delivery_agent_id: int
    delivery_rating: float = Field(..., ge=1.0, le=5.0)
