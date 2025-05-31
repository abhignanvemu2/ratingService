from pydantic import BaseModel

class RestaurantOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
