from fastapi import APIRouter
from .OrderRating import router as orderRating
from .DeliveryRating import router as deliveryRating
router = APIRouter()

router.include_router(orderRating)
router.include_router(deliveryRating)


