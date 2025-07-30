# Apply Boost Studio - Modular Structure

This document describes the new modular structure of the Apply Boost Studio application.

## Project Structure

```
apply-boost-studio/
├── app/                          # Main application package
│   ├── __init__.py              # App factory and configuration
│   ├── routes.py                # Route handlers (blueprints)
│   └── utils.py                 # Utility functions (email, file handling)
├── tests/                       # Test suite
│   ├── __init__.py              # Test package
│   ├── conftest.py              # Pytest configuration
│   ├── test_email.py            # Email configuration tests
│   ├── test_routes.py           # Route tests
│   ├── test_utils.py            # Utility function tests
│   └── README.md                # Test documentation
├── templates/                    # HTML templates
├── static/                      # Static files (CSS, JS, images)
├── uploads/                     # File upload directory
├── config.py                    # Configuration settings
├── run.py                       # New application entry point
├── app.py                       # Legacy entry point (backward compatibility)
├── app.py.backup               # Original monolithic app.py backup
└── requirements.txt             # Dependencies
```

## Key Improvements

### 1. Modular Architecture
- **Separation of Concerns**: Each module has a specific responsibility
- **Application Factory Pattern**: Uses Flask's recommended factory pattern
- **Blueprint Organization**: Routes are organized into logical blueprints

### 2. Test Organization
- **Dedicated Test Directory**: All tests moved to `tests/` directory
- **Comprehensive Test Suite**: Unit tests, integration tests, and configuration tests
- **Pytest Integration**: Modern testing framework with fixtures

### 3. Code Organization

#### `app/__init__.py`
- Application factory function (`create_app()`)
- Configuration setup
- Blueprint registration
- Template and static folder configuration

#### `app/routes.py`
- Main routes blueprint (`main_bp`)
- API routes blueprint (`api_bp`)
- All route handlers organized by functionality

#### `app/utils.py`
- File validation functions
- Email sending functions
- Utility functions separated from route logic

## Running the Application

### Using the New Modular Structure (Recommended)
```bash
# Activate virtual environment
source venv/bin/activate

# Run with the new entry point
python run.py
```

### Using Legacy Entry Point (Backward Compatibility)
```bash
# Activate virtual environment
source venv/bin/activate

# Run with the legacy entry point
python app.py
```

## Running Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_routes.py

# Run tests with coverage
pytest --cov=app
```

## Development Workflow

### Adding New Routes
1. Add route handlers to `app/routes.py`
2. Use appropriate blueprint (`main_bp` for main routes, `api_bp` for API routes)
3. Write tests in `tests/test_routes.py`

### Adding New Utilities
1. Add utility functions to `app/utils.py`
2. Write tests in `tests/test_utils.py`
3. Import and use in route handlers

### Adding New Tests
1. Create test file in `tests/` directory
2. Follow naming convention `test_*.py`
3. Use provided fixtures (`client`, `app`, `runner`)

## Benefits of the New Structure

### Maintainability
- **Single Responsibility**: Each module has one clear purpose
- **Easier Testing**: Isolated functions are easier to test
- **Better Organization**: Related code is grouped together

### Scalability
- **Blueprint Support**: Easy to add new route groups
- **Modular Design**: Easy to add new features without affecting existing code
- **Factory Pattern**: Supports multiple app instances (testing, development, production)

### Code Quality
- **Separation of Concerns**: Business logic separated from route handling
- **Reusability**: Utility functions can be reused across routes
- **Testability**: Each component can be tested independently

## Migration Notes

### From Monolithic to Modular
- Original `app.py` is backed up as `app.py.backup`
- New entry point is `run.py` (recommended)
- Legacy `app.py` still works for backward compatibility
- All functionality preserved, just reorganized

### Testing
- All test files moved to `tests/` directory
- Added pytest and pytest-flask to requirements
- Comprehensive test coverage for all modules

## Configuration

The application uses the same `config.py` file for configuration. The modular structure makes it easier to:
- Add new configuration options
- Use different configs for different environments
- Test with different configurations

## Best Practices

1. **Use Blueprints**: Organize routes by functionality
2. **Keep Routes Thin**: Move business logic to utility functions
3. **Write Tests**: Every new feature should have corresponding tests
4. **Use Application Factory**: Supports testing and multiple environments
5. **Follow Naming Conventions**: Use clear, descriptive names for modules and functions 