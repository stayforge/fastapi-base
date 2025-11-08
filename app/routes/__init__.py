# Routes package initialization
from fastapi import APIRouter

from app.routes import tenant

router = APIRouter()

router.include_router(tenant.router)
