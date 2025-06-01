# routes/rating.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Models.RatingModel import Rating
from Config import get_db
from Schemas.rating import OrderRatingCreate

router = APIRouter()

@router.post("/order")
def rate_order(data: OrderRatingCreate, db: Session = Depends(get_db)):
    rating = Rating(
        user_id=data.user_id,
        order_id=data.order_id,
        restaurant_id=data.restaurant_id,
        restaurent_rating=data.order_rating
    )
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return {"message": "Order rating submitted", "rating_id": rating.id}
