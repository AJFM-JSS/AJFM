#!/usr/bin/env python3
"""
Main application entry point for AJFM - Job application made easy
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 