# Generic Python Development Instructions

## Python Environment Management

### Dependency Management

- Use a package manager like `pip`, `pipenv`, or `poetry` for managing dependencies.
- Create and activate a virtual environment for isolated development.
- Use `pip install <package>` to add dependencies.
- Use `pip freeze > requirements.txt` to save dependencies.

### Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Add new dependency
pip install <package-name>

# Run scripts
python <script>

# Run tests
pytest

# Run with coverage
pytest --cov=<module> --cov-report=term-missing

# Format code with Black
black <directory>

# Lint code with Flake8
flake8 <directory>
```

## Import Path Standards

### For Scripts

```python
from module.submodule import ClassName
```

### Path Manipulation

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
```

## Testing Guidelines

### Test Structure

- Organize tests in a `tests/` directory.
- Use `pytest` for running tests.
- Mock external dependencies.
- Validate edge cases and error handling.

### Example Test Pattern

```python
from unittest.mock import Mock, patch

def test_function():
    mock_dependency = Mock()
    result = function_to_test(mock_dependency)
    assert result == expected_result
```

## Security Notes

- Never commit sensitive data like credentials.
- Use environment variables for secrets.
- Add sensitive files to `.gitignore`.

## Best Practices

- Follow PEP 8 for code style.
- Use type hints for better readability and error checking.
- Write docstrings for all public functions and classes.
- Keep functions small and focused.

---

# Fidelity GraphQL Project-Specific Python Instructions

## Python Environment Management

### UV Package Manager

- **Always use `uv`** for Python execution and dependency management
- Use `uv run python <script>` instead of just `python <script>`
- Use `uv add <package>` for adding dependencies
- Use `uv sync` to install/update dependencies

### Common Commands

```bash
# Install dependencies
uv sync

# Add new dependency
uv add <package-name>

# Run scripts
uv run python trading/scripts/run_positions.py
uv run python trading/scripts/run_option_summary.py
uv run python trading/scripts/run_balance_detail.py

# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=sdk --cov-report=term-missing

# Format code with Black
uv run black c:\git\fidelity-graphql\backend

# Lint code with Ruff
uv run ruff check --fix c:\git\fidelity-graphql\backend
```

## Import Path Standards

### For scripts in trading/scripts/

```python
from core.sdk.client import GraphQLClient
from core.sdk.login import get_fidelity_cookies
```

### For analysis tools

```python
from core.sdk.models import Position, OptionStrategy
```

### Path manipulation when needed

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from fidelity_schema import fidelity_schema as schema
```

## Authentication Flow

1. Scripts check for valid cookies in `config/fidelity_cookies.txt`
2. If cookies are invalid/expired, user must run login process
3. Login saves fresh cookies to config directory
4. All scripts automatically use saved cookies

## Testing Guidelines

### Test Structure

- Test reorganized structure by running individual scripts
- Validate authentication flow before data collection
- Use MCP server for trade analysis and decision support

### Testing Approach

- **Mock response structure**: Ensure test mocks match actual schema
- **Test error cases**: Include validation for error responses
- **Cover all operations**: Each client method should have tests
- **Use schema validation**: Tests should fail if schema changes break compatibility

### Example Test Pattern

```python
@unittest.skipUnless(SCHEMA_AVAILABLE, "Schema not available")
@patch('sdk.sgqlc_client.HTTPEndpoint')
def test_operation(self, mock_endpoint_class) -> None:
    """Test operation building and execution."""
    mock_endpoint = Mock()
    mock_endpoint_class.return_value = mock_endpoint

    # Mock response matching schema structure
    mock_response = {
        "data": {
            "operation": {
                "data": [{"field1": "value1", "field2": 123}],
                "metadata": {"timestamp": "2023-10-08T15:30:00Z"}
            }
        }
    }
    mock_endpoint.return_value = mock_response

    client = SGQLCFidelityClient("X123", str(self.cookie_file))
    result = client.operation({"parameter1": "test"})

    mock_endpoint.assert_called_once()
    self.assertIsNotNone(result)
```

## Updated Python Development Philosophy

### Code Coverage and Testing Philosophy

- **Full Code Coverage**: All code must be fully covered by tests. Use tools like `pytest-cov` to ensure 100% coverage.
- **Testing Flexibility**: While the main codebase should adhere to strict rules for clarity and maintainability, testing code can be more flexible to ensure proper coverage without unnecessary complexity.
  - Example: In the main code, interfaces should be fully defined. In tests, it is acceptable to define only the methods or attributes that are necessary for mocking or patching.
- **Focus on Readability**: Tests should be clean and understandable, but the priority is ensuring comprehensive coverage and validating behavior.

### Static Analysis and Linting

- **Strict Static Analysis**: Apply strict static analysis rules to the main codebase to ensure high-quality, maintainable code.
  - Use tools like `mypy` for type checking and enforce type hints across the codebase.
  - Use `ruff` or `flake8` for linting to enforce PEP 8 compliance and other project-specific rules.
- **Relaxed Rules for Tests**: Testing code can have relaxed rules to avoid unnecessary overhead. For example:
  - Allow dynamic typing or partial type hints in tests where strict typing would add complexity without benefit.
  - Skip certain linting rules in test files if they hinder the ability to write concise and effective tests.

### Clean and Understandable Code

- **Main Codebase**:
  - Prioritize clarity and maintainability.
  - Avoid overly complex patterns or abstractions unless absolutely necessary.
  - Ensure all public methods and classes have clear docstrings.
- **Testing Code**:
  - Focus on validating behavior rather than adhering to strict stylistic rules.
  - Use mocking and patching as needed to isolate units under test.
  - Write descriptive test names and include comments to explain non-obvious test logic.

### Practical Guidelines

1. **Type Hints**:
   - Use type hints for all function signatures in the main codebase.
   - In tests, type hints are optional and should be used only when they improve clarity.

2. **Mocking and Patching**:
   - Mock external dependencies and complex objects in tests to isolate the unit under test.
   - It is acceptable to define minimal mock objects or methods in tests, even if they do not fully adhere to the interface.

3. **Error Handling**:
   - Ensure robust error handling in the main codebase.
   - In tests, focus on validating error scenarios without replicating the full error-handling logic.

4. **Code Coverage**:
   - Use `pytest-cov` to measure coverage and ensure all branches are tested.
   - Write additional tests for edge cases and error scenarios to achieve full coverage.

5. **Static Analysis**:
   - Run `mypy` and `ruff` as part of the CI pipeline to enforce rules in the main codebase.
   - Exclude test files from strict static analysis checks to allow flexibility.

### Example Workflow

1. **Develop Main Code**:
   - Write clean, well-documented, and type-annotated code.
   - Ensure all public methods and classes have clear docstrings.

2. **Write Tests**:
   - Focus on covering all branches and edge cases.
   - Use mocking and patching to isolate the unit under test.
   - Write descriptive test names and include comments for clarity.

3. **Run Static Analysis**:
   - Run `mypy` and `ruff` on the main codebase.
   - Allow relaxed rules for test files.

4. **Measure Coverage**:
   - Use `pytest-cov` to ensure 100% coverage.
   - Add tests for any uncovered branches or scenarios.

By following these principles, the codebase will remain clean and maintainable, while the testing framework will ensure comprehensive coverage without becoming overly restrictive.

## Common Issues

### Import Errors

- **Solution**: Ensure you're using `uv run` and paths are correct

### Authentication Issues

- **Solution**: Check if `config/fidelity_cookies.txt` exists and is valid

### Missing Data

- **Solution**: Run data collection scripts to refresh snapshots

### SGQLC Import Errors

```bash
# Error: ImportError: cannot import name 'schema'
```

**Solution**: Check the import path in `sgqlc_client.py`:

```python
# Add path manipulation if needed
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from fidelity_schema import fidelity_schema as schema
```

### Type Safety Issues

```bash
# Error: 'Query' is not a known attribute of 'None'
```

**Solution**: Ensure schema is properly imported and `SCHEMA_AVAILABLE = True`

## Security Notes

- Never commit actual cookies or credentials
- Use `config/fidelity_cookies.txt` for session storage
- The `config` directory is listed in `.gitignore` for security.
- Config directory is gitignored for security

## Best Practices

### Client Methods

- **Mirror GraphQL operations**: One client method per GraphQL operation
- **Select fields explicitly**: Always specify which fields to retrieve
- **Handle nested data**: Structure field selections to match response nesting
- **Provide type hints**: Use proper return type annotations

### Example Client Method

```python
def new_operation(
    self,
    input_data: Dict[str, Any],
    endpoint_name: str = "default"
) -> Any:
    """
    Description of the new operation.

    Args:
        input_data: Parameters for the operation
        endpoint_name: Which endpoint to use

    Returns:
        Typed results accessible via result.new_operation.field_name
    """
    op = Operation(schema.Query)
    result = op.new_operation(input=input_data)

    # Select fields you want to retrieve
    result.data.field1()
    result.data.field2()
    result.metadata.timestamp()

    return self._execute_operation(op, input_data, endpoint_name)
```

## Development Environment

### Windows-Specific Notes

- Use PowerShell or Command Prompt
- Ensure UV is installed and in PATH
- Python 3.11+ recommended for best compatibility

### VS Code Integration

- Install Python extension
- Configure workspace settings for UV
- Use integrated terminal for UV commands
