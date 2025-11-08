"""Main API v1 router that includes all endpoint routers."""

from fastapi import APIRouter

from app.api.v1.endpoints import health, users

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(health.router, tags=["health"])
api_router.include_router(users.router, tags=["users"])

