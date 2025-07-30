# Tests

This directory contains all test files for the Apply Boost Studio application.

## Structure

- `__init__.py` - Makes this a Python package
- `conftest.py` - Pytest configuration and fixtures
- `test_email.py` - Email configuration tests
- `test_routes.py` - Route handler tests
- `test_utils.py` - Utility function tests

## Running Tests

To run all tests:
```bash
pytest
```

To run tests with verbose output:
```bash
pytest -v
```

To run a specific test file:
```bash
pytest tests/test_routes.py
```

To run tests with coverage:
```bash
pytest --cov=app
```

## Test Categories

### Unit Tests
- `test_utils.py` - Tests for utility functions like file validation
- `test_email.py` - Tests for email configuration validation

### Integration Tests
- `test_routes.py` - Tests for Flask route handlers and API endpoints

## Adding New Tests

When adding new functionality:

1. Create a new test file following the naming convention `test_*.py`
2. Import the modules you want to test
3. Write test functions that start with `test_`
4. Use the provided fixtures (`client`, `app`, `runner`) as needed

## Test Configuration

The `conftest.py` file provides:
- Flask app fixture for testing
- Test client fixture for making requests
- CLI runner fixture for testing commands
- Test upload folder configuration 