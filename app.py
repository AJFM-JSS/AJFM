#!/usr/bin/env python3
"""
Legacy app.py file - now using modular structure
This file is kept for backward compatibility but the main application
should be run using run.py instead.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 