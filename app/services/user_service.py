"""User service with business logic."""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import BadRequestException, NotFoundException
from app.core.security import get_password_hash
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    """Service for user-related operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_id(self, user_id: int) -> User:
        """Get user by ID."""
        result = await self.db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise NotFoundException(f"User with id {user_id} not found")
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        result = await self.db.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()

    async def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Get list of users."""
        result = await self.db.execute(select(User).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def create_user(self, user_create: UserCreate) -> User:
        """Create a new user."""
        # Check if user with email already exists
        existing_user = await self.get_user_by_email(user_create.email)
        if existing_user:
            raise BadRequestException("User with this email already exists")

        # Check if user with username already exists
        existing_user = await self.get_user_by_username(user_create.username)
        if existing_user:
            raise BadRequestException("User with this username already exists")

        # Create new user
        user = User(
            email=user_create.email,
            username=user_create.username,
            hashed_password=get_password_hash(user_create.password),
        )
        self.db.add(user)
        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        """Update a user."""
        user = await self.get_user_by_id(user_id)

        # Update fields if provided
        if user_update.email is not None:
            # Check if email is taken by another user
            existing_user = await self.get_user_by_email(user_update.email)
            if existing_user and existing_user.id != user_id:
                raise BadRequestException("Email already taken")
            user.email = user_update.email

        if user_update.username is not None:
            # Check if username is taken by another user
            existing_user = await self.get_user_by_username(user_update.username)
            if existing_user and existing_user.id != user_id:
                raise BadRequestException("Username already taken")
            user.username = user_update.username

        if user_update.password is not None:
            user.hashed_password = get_password_hash(user_update.password)

        if user_update.is_active is not None:
            user.is_active = user_update.is_active

        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> None:
        """Delete a user."""
        user = await self.get_user_by_id(user_id)
        await self.db.delete(user)
        await self.db.flush()

