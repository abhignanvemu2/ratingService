# routes/rating.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Models.RatingModel import Rating
from Config import get_db
from Schemas.rating import DeliveryRatingCreate

router = APIRouter()

@router.post("/delivery")
def rate_delivery(data: DeliveryRatingCreate, db: Session = Depends(get_db)):
    rating = db.query(Rating).filter(
        Rating.order_id == data.order_id,
        Rating.user_id == data.user_id
    ).first()

    if not rating:
        raise HTTPException(status_code=404, detail="Rating for this order not found. Please rate order first.")

    rating.delivery_agent_id = data.delivery_agent_id
    rating.order_rating = data.delivery_rating
    db.commit()
    
    return {"message": "Delivery agent rating submitted", "rating_id": rating.id}
