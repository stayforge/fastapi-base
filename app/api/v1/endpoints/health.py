"""Health check endpoints."""

from datetime import datetime

from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["health"],
    summary="Health check",
    description="Check if the API is running",
)
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "fastapi-base",
    }


@router.get(
    "/readiness",
    status_code=status.HTTP_200_OK,
    tags=["health"],
    summary="Readiness check",
    description="Check if the API is ready to serve requests",
)
async def readiness_check():
    """Readiness check endpoint."""
    # Add database connectivity check here if needed
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat(),
    }


@router.get(
    "/liveness",
    status_code=status.HTTP_200_OK,
    tags=["health"],
    summary="Liveness check",
    description="Check if the API is alive",
)
async def liveness_check():
    """Liveness check endpoint."""
    return {
        "status": "alive",
        "timestamp": datetime.utcnow().isoformat(),
    }

