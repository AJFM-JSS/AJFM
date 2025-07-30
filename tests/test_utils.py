"""
Tests for the utils module
"""

import pytest
from app.utils import allowed_file

def test_allowed_file_valid_extensions():
    """Test that valid file extensions are allowed"""
    valid_files = [
        'resume.pdf',
        'document.doc',
        'cv.docx',
        'RESUME.PDF',
        'Document.DOC'
    ]
    
    for filename in valid_files:
        assert allowed_file(filename) == True

def test_allowed_file_invalid_extensions():
    """Test that invalid file extensions are rejected"""
    invalid_files = [
        'resume.txt',
        'document.jpg',
        'cv.png',
        'file.exe',
        'script.py'
    ]
    
    for filename in invalid_files:
        assert allowed_file(filename) == False

def test_allowed_file_no_extension():
    """Test that files without extensions are rejected"""
    invalid_files = [
        'resume',
        'document',
        'cv',
        ''
    ]
    
    for filename in invalid_files:
        assert allowed_file(filename) == False

def test_allowed_file_dot_only():
    """Test that files with only a dot are rejected"""
    assert allowed_file('.') == False
    assert allowed_file('file.') == False 