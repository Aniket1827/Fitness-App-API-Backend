import uvicorn
from fastapi import FastAPI, APIRouter
from app.api.api_v1.api import api_router

root_router = APIRouter()

app = FastAPI(title="Fitness Booking API")
app.include_router(api_router, prefix="/api/v1")
app.include_router(root_router)

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Fitness Studio Booking API!"}
