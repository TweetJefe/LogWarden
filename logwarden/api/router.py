from fastapi import APIRouter
from logwarden.incidents.router import router as incident_router
from logwarden.health.router import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(incident_router)
