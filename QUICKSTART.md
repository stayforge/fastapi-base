# Quick Start Guide

This is a 5-minute quick start guide to get you up and running with FastAPI Base.

## Step 1: Install Dependencies (1 minute)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure Environment (30 seconds)

```bash
# The project already includes a .env file, you can use it directly
# If you need to customize, you can edit the .env file
```

## Step 3: Start Application (30 seconds)

```bash
# Method 1: Using Makefile
make run

# Method 2: Using Python
python run.py

# Method 3: Using uvicorn
uvicorn app.main:app --reload
```

## Step 4: Test API (1 minute)

Open your browser and visit:

- **API Documentation**: http://localhost:8000/docs
- **Root Endpoint**: http://localhost:8000

Try the following APIs:

### Health Check
```bash
curl http://localhost:8000/api/v1/health
```

### Create User
```bash
curl -X POST http://localhost:8000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "password123"
  }'
```

### Get User List
```bash
curl http://localhost:8000/api/v1/users
```

## Step 5: Run Tests (1 minute)

```bash
# Run all tests
make test

# Or use pytest
pytest tests/ -v
```

## 🎉 Done!

You have successfully run FastAPI Base!

## Next Steps

- Read the complete [README.md](README.md)
- Explore the [API Documentation](http://localhost:8000/docs)
- Review project structure and code
- Start adding your own features

## Using Docker (Optional)

If you prefer using Docker:

```bash
# Using Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Frequently Asked Questions

### Q: Port 8000 is already in use?
A: Modify the PORT value in the .env file

### Q: How to connect to PostgreSQL?
A: Modify DATABASE_URL in .env:
```
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
```

### Q: How to add new API endpoints?
A: Create a new file in `app/api/v1/endpoints/`, then import it in `app/api/v1/router.py`

Happy coding! 🚀
