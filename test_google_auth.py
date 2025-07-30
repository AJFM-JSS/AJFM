#!/usr/bin/env python3
"""
Test Google Drive Authentication
This script will trigger the authentication process and create token.json
"""

import asyncio
import os
from app.google_drive_utils import drive_manager

async def test_authentication():
    """Test Google Drive authentication"""
    print("🔐 Testing Google Drive Authentication...")
    
    # Check if credentials file exists
    if not os.path.exists('credentials.json'):
        print("❌ credentials.json not found!")
        print("📝 Please download credentials from Google Cloud Console")
        print("   and rename it to 'credentials.json'")
        return False
    
    try:
        # Attempt authentication
        print("🔑 Attempting to authenticate...")
        success = await drive_manager.authenticate()
        
        if success:
            print("✅ Authentication successful!")
            print("✅ token.json has been created")
            print("📁 You can now use Google Drive uploads")
            return True
        else:
            print("❌ Authentication failed")
            print("📝 Check your credentials.json file")
            return False
            
    except Exception as e:
        print(f"❌ Error during authentication: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Google Drive Authentication Test")
    print("=" * 40)
    
    # Run the authentication test
    result = asyncio.run(test_authentication())
    
    if result:
        print("\n✅ Setup complete! You can now use Google Drive uploads.")
    else:
        print("\n❌ Setup incomplete. Please check the requirements above.") 