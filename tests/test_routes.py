"""
Tests for the main application routes
"""

import pytest
from flask import url_for

def test_home_route(client):
    """Test that the home route returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_get_started_route(client):
    """Test that the get-started route returns 200"""
    response = client.get('/get-started')
    assert response.status_code == 200

def test_login_route(client):
    """Test that the login route returns 200"""
    response = client.get('/login')
    assert response.status_code == 200

def test_profile_route(client):
    """Test that the profile route returns 200"""
    response = client.get('/profile')
    assert response.status_code == 200

def test_resume_builder_route(client):
    """Test that the resume-builder route returns 200"""
    response = client.get('/resume-builder')
    assert response.status_code == 200

def test_testimonials_api(client):
    """Test that the testimonials API returns 200 and valid JSON"""
    response = client.get('/api/testimonials')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'name' in data[0]
    assert 'role' in data[0]
    assert 'content' in data[0] 