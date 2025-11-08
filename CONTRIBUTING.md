# Contributing Guide

Thank you for your interest in this project!

## Development Workflow

1. **Fork the Project**

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Development**
   - Follow the existing code style
   - Add necessary tests
   - Update documentation

4. **Run Tests**
   ```bash
   make test
   ```

5. **Format Code**
   ```bash
   make format
   ```

6. **Run Linters**
   ```bash
   make lint
   ```

7. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature"
   ```

8. **Push to Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create Pull Request**

## Commit Message Convention

Use [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation updates
- `style:` - Code formatting (does not affect code execution)
- `refactor:` - Refactoring
- `test:` - Testing related
- `chore:` - Changes to build process or auxiliary tools

## Code Style

- Use Black for code formatting
- Use Ruff for linting
- Use MyPy for type checking
- Follow PEP 8 guidelines

## Testing Requirements

- All new features must include tests
- Maintain test coverage > 80%
- Tests should be clear and easy to understand

## Documentation Requirements

- All public APIs must have docstrings
- Important features need README updates
- Complex logic requires comments

## Issue Reporting

When reporting an issue, please include:
- Detailed description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment information (Python version, OS, etc.)

Thank you for your contribution!
