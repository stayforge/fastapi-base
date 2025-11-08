# FastAPI Base
An elegant, modern FastAPI project template that follows best practices.

## ✨ Features

- 🚀 **FastAPI** - High-performance asynchronous web framework
- 🏗️ **Clear Architecture** - Layered design, easy to maintain and expand
- 🔐 **Security** - JWT authentication, password encryption
- 🗄️ **Database** - SQLAlchemy 2.0 with async support
- 📝 **Log system** - Structured log (JSON/text format)
- 🎯 **Middleware** - Request tracking, performance monitoring
- ✅ **TESTING** - Pytest with complete test coverage
- 🐳 **Docker** - multi-stage build, production ready
- 📦 **Dependency Management** - Poetry or pip
- 🔧 **Development Tools** - Black, Ruff, MyPy

## 📁 Project structure

```
fastapi-base/
├── app/
│ ├── __init__.py
│ ├── main.py # Application entrance
│ ├── dependencies.py # Shared dependencies
│ ├── api/ # API routing
│ │ └── v1/ # API v1 version
│ │ ├── endpoints/ # Endpoint module
│ │ │ ├── health.py # Health check
│ │ │ └── users.py # User management
│ │ └── router.py # Route aggregation
│ ├── core/ # Core function
│ │ ├── config.py # Configuration management
│ │ ├── security.py # Security tool
│ │ ├── logging.py # Log configuration
│ │ └── exceptions.py # Exception handling
│ ├── db/ # database
│ │ ├── base.py # Basic model
│ │ ├── session.py # Session management
│ │ └── models/ # Data model
│ │ └── user.py
│ ├── schemas/ # Pydantic schemas
│ │ └── user.py
│ ├── services/ # Business logic
│ │ └── user_service.py
│ ├── middleware/ # middleware
│ │ ├── logging.py # Logging middleware
│ │ └── timing.py # Performance monitoring
│ └── utils/ # Utility function
│ └── helpers.py
├── tests/ # tests
│ ├── conftest.py
│ ├── test_health.py
│ └── test_users.py
├── .env.example # Environment variable example
├── .gitignore
├── requirements.txt # Python dependencies
├── pyproject.toml # Poetry configuration
├── Dockerfile # Docker image
├── docker-compose.yml # Docker Compose
├── Makefile # Common commands
└── README.md
```

## 🚀 Quick Start

### Prerequisites

-Python 3.11+
-pip or Poetry

### Installation

1. **Clone Project**

```bash
git clone <repository-url>
cd fastapi-base
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
# or
venv\Scripts\activate # Windows
```

3. **Install dependencies**

Use pip:
```bash
pip install -r requirements.txt
```

Or use Poetry:
```bash
poetry install
```

4. **Configure environment variables**

```bash
cp .env.example .env
# Edit the .env file and set your configuration
```

5. **Run the application**

```bash
# Use Makefile
make run

# Or use uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The application will be launched at http://localhost:8000

- API documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🐳 Using Docker

### Docker Compose (recommended)

```bash
docker-compose up -d
```

This will start:
- FastAPI application (port 8000)
- PostgreSQL database (port 5432)
- Redis (port 6379)

### Using Docker alone

```bash
# Build image
docker build -t fastapi-base .

# Run container
docker run -p 8000:8000 fastapi-base
```

## 📝 API Documentation

### Health Check Endpoints

- `GET /` - root endpoint
- `GET /api/v1/health` - health check
- `GET /api/v1/readiness` - readiness check
- `GET /api/v1/liveness` - liveness check

### User Endpoints

- `POST /api/v1/users` - create users
- `GET /api/v1/users` - Get user list
- `GET /api/v1/users/{user_id}` - Get a specific user
- `PATCH /api/v1/users/{user_id}` - update user
- `DELETE /api/v1/users/{user_id}` - delete user

Complete API documentation is available at http://localhost:8000/docs

## 🧪 Test

Run all tests:

```bash
# Use Makefile
make test

# Or use pytest
pytest tests/ -v --cov=app
```

## 🛠️ Development tools

### Code formatting

```bash
make format
```

### Code inspection

```bash
make lint
```

### Clear cache

```bash
make clean
```

## 📦 Available commands (Makefile)

```bash
make help # show all available commands
make install #Install production dependencies
make dev #Install development dependencies
make run # Run the application
make test # run test
make format # format code
make lint # run linters
make clean # Clean cache files
```

## 🔧 Configuration

All configuration is managed in `app/core/config.py` and can be overridden through environment variables.

Main configuration items:

- `PROJECT_NAME` - project name
- `VERSION` - API version
- `DATABASE_URL` - database connection string
- `SECRET_KEY` - JWT key
- `ALLOWED_ORIGINS` - CORS allowed origins
- `LOG_LEVEL` - log level
- `LOG_FORMAT` - log format (json/text)

Check out `.env.example` for all available configurations.

## 🔐 Security

- **JWT Authentication** - using python-jose
- **Password encryption** - using passlib + bcrypt
- **CORS Configuration** - Configurable cross-domain policies
- **Input Validation** - Pydantic model validation
- **SQL injection protection** - SQLAlchemy ORM

## 📊 Log

The application supports two log formats:

1. **JSON format** - suitable for production environments and easy to parse
2. **Text format** - suitable for development environment, with color output

Switched via the `LOG_FORMAT` environment variable.

## 🚀 Deployment

### Environment variables

Make sure to set the following variables in your production environment:

```bash
SECRET_KEY=<strong-random-key>
DEBUG=false
DATABASE_URL=<production-database-url>
ALLOWED_ORIGINS=https://yourdomain.com
LOG_LEVEL=INFO
LOG_FORMAT=json
```

### Database migration

It is recommended to use Alembic for database migration:

```bash
#Initialize Alembic
alembic init alembic

#Create migration
alembic revision --autogenerate -m "Initial migration"

# Application migration
alembic upgrade head
```

## 🤝 Contribute

Welcome to submit Pull Requests!

## 📄 Authorization

MIT License

## 📞 Support

If you have any questions, please create an Issue or contact the maintainer.

---

Built with ❤️ using FastAPI