"""Tests for user endpoints."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    """Test creating a new user."""
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123",
    }

    response = await client.post("/api/v1/users", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["username"] == user_data["username"]
    assert "id" in data
    assert "hashed_password" not in data


@pytest.mark.asyncio
async def test_create_duplicate_user(client: AsyncClient):
    """Test creating a user with duplicate email."""
    user_data = {
        "email": "duplicate@example.com",
        "username": "duplicate",
        "password": "testpassword123",
    }

    # Create first user
    response = await client.post("/api/v1/users", json=user_data)
    assert response.status_code == 201

    # Try to create duplicate
    response = await client.post("/api/v1/users", json=user_data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_get_user(client: AsyncClient):
    """Test getting a user by ID."""
    # Create user first
    user_data = {
        "email": "getuser@example.com",
        "username": "getuser",
        "password": "testpassword123",
    }
    create_response = await client.post("/api/v1/users", json=user_data)
    user_id = create_response.json()["id"]

    # Get user
    response = await client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == user_data["email"]


@pytest.mark.asyncio
async def test_get_nonexistent_user(client: AsyncClient):
    """Test getting a user that doesn't exist."""
    response = await client.get("/api/v1/users/99999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_user(client: AsyncClient):
    """Test updating a user."""
    # Create user first
    user_data = {
        "email": "updateuser@example.com",
        "username": "updateuser",
        "password": "testpassword123",
    }
    create_response = await client.post("/api/v1/users", json=user_data)
    user_id = create_response.json()["id"]

    # Update user
    update_data = {"username": "updatedusername"}
    response = await client.patch(f"/api/v1/users/{user_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == update_data["username"]


@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient):
    """Test deleting a user."""
    # Create user first
    user_data = {
        "email": "deleteuser@example.com",
        "username": "deleteuser",
        "password": "testpassword123",
    }
    create_response = await client.post("/api/v1/users", json=user_data)
    user_id = create_response.json()["id"]

    # Delete user
    response = await client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 204

    # Verify user is deleted
    get_response = await client.get(f"/api/v1/users/{user_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_get_users_list(client: AsyncClient):
    """Test getting list of users."""
    # Create multiple users
    for i in range(3):
        user_data = {
            "email": f"user{i}@example.com",
            "username": f"user{i}",
            "password": "testpassword123",
        }
        await client.post("/api/v1/users", json=user_data)

    # Get users list
    response = await client.get("/api/v1/users")
    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert "total" in data
    assert len(data["users"]) >= 3

