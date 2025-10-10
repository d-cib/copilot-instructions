# Python Copilot Instructions (Example: UV + pytest + black + ruff + mypy)

## Setup Instructions

To use these Copilot instructions:

1. **Fork this repository** or **copy this file** to your own repository
2. **Answer the survey questions** below to customize the instructions
3. **Replace the placeholders** in the instructions with your preferences
4. **Save the customized file** as `.github/copilot-instructions.md` in your repository
5. **Link with VSCode** by ensuring GitHub Copilot extension is installed and configured

---

## Python Copilot Instructions

You are an expert Python developer assistant. Follow these guidelines when helping with Python code:

### Package Management
Use **uv** for package installation and dependency management:
- Use `uv add <package>` to add dependencies
- Use `uv install` to install from pyproject.toml
- Use `uv run <command>` to run commands in the virtual environment
- Prefer pyproject.toml for project configuration

### Testing
Use **pytest** for writing and running tests:
- Write tests using pytest conventions
- Use fixtures for test setup and teardown
- Organize tests in test_*.py files
- Run tests with `pytest` command
- Use pytest plugins for additional functionality

### Code Style and Formatting
Use **black** for code formatting:
- Format code with `black .` command
- Follow black's formatting decisions without question
- Configure line length to 88 characters (black default)

### Linting
Use **ruff** for code analysis:
- Run linting with `ruff check .`
- Fix auto-fixable issues with `ruff check --fix .`
- Configure rules in pyproject.toml

### Type Checking
Use **mypy** for static type checking:
- Add type hints to all function signatures
- Run type checking with `mypy .`
- Configure mypy in pyproject.toml or mypy.ini

### General Python Best Practices
- Write clean, readable, and maintainable code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Write comprehensive docstrings for modules, classes, and functions
- Handle exceptions appropriately with specific exception types
- Use context managers (with statements) for resource management
- Prefer list/dict comprehensions for simple data transformations
- Use f-strings for string formatting in Python 3.6+
- Follow the principle of least surprise in API design
- Write modular code with single responsibility principle

### Project Structure
Organize Python projects with this recommended structure:
```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── module.py
├── tests/
│   └── test_module.py
├── docs/
├── README.md
├── pyproject.toml  # or requirements.txt
└── .gitignore
```

### Documentation
- Write clear README.md with installation and usage instructions
- Use docstrings in Google, NumPy, or Sphinx style consistently
- Include type hints in docstrings when helpful
- Provide examples in docstrings for complex functions
- Keep documentation up-to-date with code changes