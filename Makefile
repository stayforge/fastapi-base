.PHONY: help install dev run test format lint clean

help:
	@echo "FastAPI Base - Available commands:"
	@echo "  make install    - Install production dependencies"
	@echo "  make dev        - Install development dependencies"
	@echo "  make run        - Run the application"
	@echo "  make test       - Run tests"
	@echo "  make format     - Format code with black and ruff"
	@echo "  make lint       - Run linters"
	@echo "  make clean      - Clean up cache and build files"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest tests/ -v --cov=app --cov-report=term-missing

format:
	black app/ tests/
	ruff check app/ tests/ --fix

lint:
	black app/ tests/ --check
	ruff check app/ tests/
	mypy app/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.db" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf build/ dist/ .coverage htmlcov/

