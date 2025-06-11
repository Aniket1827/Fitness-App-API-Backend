from fastapi import APIRouter
from app.api.api_v1.endpoints import fitness_booking_api

api_router = APIRouter()
api_router.include_router(fitness_booking_api.router, prefix="/fitness", tags=["fitness"])