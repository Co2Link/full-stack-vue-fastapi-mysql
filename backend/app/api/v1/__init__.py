from fastapi import APIRouter

from app.api.v1.routers import dummy

api_router = APIRouter()
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
