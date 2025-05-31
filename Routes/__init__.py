from fastapi import APIRouter
from .Rating import router as rating

router = APIRouter()

router.include_router(rating, prefix="/rating", tags=['rating'])