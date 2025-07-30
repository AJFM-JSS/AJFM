"""
Pytest configuration for Apply Boost Studio tests
"""

import pytest
import os
import sys

# Add the parent directory to the Python path so we can import app modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def app():
    """Create a test Flask app instance"""
    from app import create_app
    app = create_app()
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = 'test_uploads'
    
    # Ensure test upload folder exists
    os.makedirs('test_uploads', exist_ok=True)
    
    return app

@pytest.fixture
def client(app):
    """Create a test client for the Flask app"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the Flask app"""
    return app.test_cli_runner() 