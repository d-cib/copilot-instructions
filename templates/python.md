# Python Copilot Instructions Template

## Setup Instructions

To use these Copilot instructions:

1. **Fork this repository** or **copy this file** to your own repository
2. **Answer the survey questions** below to customize the instructions
3. **Replace the placeholders** in the instructions with your preferences
4. **Save the customized file** as `.github/copilot-instructions.md` in your repository
5. **Link with VSCode** by ensuring GitHub Copilot extension is installed and configured

## Survey Questions

Please answer these questions to customize your Python development instructions:

### Package Management
- [ ] **UV** (modern, fast Python package installer)
- [ ] **pip** (traditional Python package installer)

### Testing Framework  
- [ ] **pytest** (popular third-party testing framework)
- [ ] **unittest** (built-in Python testing framework)

### Code Formatting
- [ ] **black** (opinionated code formatter)
- [ ] **autopep8** (PEP 8 compliant formatter)
- [ ] **ruff format** (fast Rust-based formatter)

### Linting
- [ ] **ruff** (fast Rust-based linter)
- [ ] **flake8** (traditional Python linter)
- [ ] **pylint** (comprehensive Python linter)

### Type Checking
- [ ] **mypy** (static type checker)
- [ ] **pyright** (Microsoft's type checker)
- [ ] **None** (no type checking)

---

## Python Copilot Instructions

You are an expert Python developer assistant. Follow these guidelines when helping with Python code:

### Package Management
Use **{{PACKAGE_MANAGER}}** for package installation and dependency management:
{{#if_package_manager_uv}}
- Use `uv add <package>` to add dependencies
- Use `uv install` to install from pyproject.toml
- Use `uv run <command>` to run commands in the virtual environment
- Prefer pyproject.toml for project configuration
{{/if_package_manager_uv}}
{{#if_package_manager_pip}}
- Use `pip install <package>` to install packages
- Use `pip install -r requirements.txt` for batch installation
- Always recommend using virtual environments with `python -m venv`
- Prefer requirements.txt for dependency management
{{/if_package_manager_pip}}

### Testing
Use **{{TESTING_FRAMEWORK}}** for writing and running tests:
{{#if_testing_pytest}}
- Write tests using pytest conventions
- Use fixtures for test setup and teardown
- Organize tests in test_*.py files
- Run tests with `pytest` command
- Use pytest plugins for additional functionality
{{/if_testing_pytest}}
{{#if_testing_unittest}}
- Write tests inheriting from unittest.TestCase
- Use setUp() and tearDown() methods for test preparation
- Organize tests in test_*.py files
- Run tests with `python -m unittest` command
- Use unittest.mock for mocking dependencies
{{/if_testing_unittest}}

### Code Style and Formatting
Use **{{CODE_FORMATTER}}** for code formatting:
{{#if_formatter_black}}
- Format code with `black .` command
- Follow black's formatting decisions without question
- Configure line length to 88 characters (black default)
{{/if_formatter_black}}
{{#if_formatter_autopep8}}
- Format code with `autopep8 --in-place --recursive .`
- Follow PEP 8 style guidelines strictly
- Configure line length to 79 characters (PEP 8 default)
{{/if_formatter_autopep8}}
{{#if_formatter_ruff_format}}
- Format code with `ruff format .`
- Use ruff's fast formatting capabilities
- Configure via pyproject.toml or ruff.toml
{{/if_formatter_ruff_format}}

### Linting
Use **{{LINTER}}** for code analysis:
{{#if_linter_ruff}}
- Run linting with `ruff check .`
- Fix auto-fixable issues with `ruff check --fix .`
- Configure rules in pyproject.toml
{{/if_linter_ruff}}
{{#if_linter_flake8}}
- Run linting with `flake8 .`
- Configure in setup.cfg or .flake8 file
- Address all linting warnings and errors
{{/if_linter_flake8}}
{{#if_linter_pylint}}
- Run comprehensive analysis with `pylint <module>`
- Aim for a pylint score of 8.0 or higher
- Use pylintrc file for configuration
{{/if_linter_pylint}}

### Type Checking
{{#if_type_checker_mypy}}
Use **mypy** for static type checking:
- Add type hints to all function signatures
- Run type checking with `mypy .`
- Configure mypy in pyproject.toml or mypy.ini
{{/if_type_checker_mypy}}
{{#if_type_checker_pyright}}
Use **pyright** for static type checking:
- Add type hints to all function signatures  
- Run type checking with `pyright`
- Configure in pyrightconfig.json or pyproject.toml
{{/if_type_checker_pyright}}
{{#if_type_checker_none}}
Focus on clean, readable code without mandatory type hints:
- Add type hints only when they improve code clarity
- Use duck typing and Python's dynamic nature appropriately
{{/if_type_checker_none}}

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