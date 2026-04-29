from fastapi import APIRouter
from app.api.endpoints import generate_repo

api_router = APIRouter()
api_router.include_router(generate_repo.router, prefix="/architect", tags=["Architect"])