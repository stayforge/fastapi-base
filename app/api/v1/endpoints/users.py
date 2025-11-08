"""User management endpoints."""

from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.user import User, UserCreate, UserList, UserUpdate
from app.services.user_service import UserService

router = APIRouter()


@router.post(
    "/users",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
    summary="Create a new user",
)
async def create_user(
    user_create: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new user."""
    service = UserService(db)
    return await service.create_user(user_create)


@router.get(
    "/users",
    response_model=UserList,
    status_code=status.HTTP_200_OK,
    tags=["users"],
    summary="Get list of users",
)
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    """Get list of users with pagination."""
    service = UserService(db)
    users = await service.get_users(skip=skip, limit=limit)
    return {"users": users, "total": len(users)}


@router.get(
    "/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["users"],
    summary="Get user by ID",
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get a specific user by ID."""
    service = UserService(db)
    return await service.get_user_by_id(user_id)


@router.patch(
    "/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["users"],
    summary="Update user",
)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db),
):
    """Update a user's information."""
    service = UserService(db)
    return await service.update_user(user_id, user_update)


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["users"],
    summary="Delete user",
)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Delete a user."""
    service = UserService(db)
    await service.delete_user(user_id)

