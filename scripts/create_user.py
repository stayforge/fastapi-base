#!/usr/bin/env python
"""Script to create a test user."""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash
from app.db.models.user import User
from app.db.session import AsyncSessionLocal


async def create_test_user():
    """Create a test user."""
    async with AsyncSessionLocal() as session:
        # Check if user already exists
        from sqlalchemy import select

        result = await session.execute(
            select(User).where(User.email == "admin@example.com")
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            print("❌ User already exists!")
            return

        # Create new user
        user = User(
            email="admin@example.com",
            username="admin",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            is_superuser=True,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

        print("✅ Test user created successfully!")
        print(f"   Email: {user.email}")
        print(f"   Username: {user.username}")
        print(f"   Password: admin123")
        print(f"   ID: {user.id}")


if __name__ == "__main__":
    asyncio.run(create_test_user())

