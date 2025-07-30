#!/usr/bin/env python3
"""
Test script for email functionality
Run this to test if email configuration is working properly
"""

import os
import sys
from config import EMAIL_CONFIG

def test_email_config():
    """Test email configuration"""
    print("Testing Email Configuration...")
    print("=" * 40)
    
    # Check if config values are set
    required_fields = ['smtp_server', 'smtp_port', 'sender_email', 'sender_password', 'admin_email']
    
    for field in required_fields:
        value = EMAIL_CONFIG.get(field)
        if not value or (isinstance(value, str) and value.startswith('your-')):
            print(f"❌ {field}: {value} (needs to be configured)")
        else:
            print(f"✅ {field}: {value}")
    
    print("\n" + "=" * 40)
    print("To configure email:")
    print("1. Edit config.py with your actual email credentials")
    print("2. For Gmail: Enable 2FA and generate an App Password")
    print("3. Update sender_email and sender_password in config.py")
    print("4. Update admin_email to receive consultation requests")
    print("\nFor production, use environment variables instead of hardcoded values.")

if __name__ == "__main__":
    test_email_config() 