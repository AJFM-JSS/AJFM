#!/usr/bin/env python3
"""
Google Drive Setup Script for Apply Boost Studio
This script helps you set up Google Drive API credentials
"""

import os
import json
from pathlib import Path

def create_credentials_template():
    """Create a template credentials.json file"""
    template = {
        "installed": {
            "client_id": "your-client-id.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "your-client-secret",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    with open('credentials_template.json', 'w') as f:
        json.dump(template, f, indent=2)
    
    print("✅ Created credentials_template.json")
    print("📝 Please rename it to credentials.json and update with your actual values")

def create_config_template():
    """Create a template config file with Google Drive settings"""
    config_template = """# Google Drive Configuration
GOOGLE_DRIVE_CONFIG = {
    'credentials_file': 'credentials.json',  # Path to your Google Drive API credentials
    'token_file': 'token.json',  # Path to store OAuth token
    'folder_id': 'your-google-drive-folder-id',  # Google Drive folder ID where files will be uploaded
    'scopes': ['https://www.googleapis.com/auth/drive.file']  # Required scopes
}

# Notification Configuration
NOTIFICATION_CONFIG = {
    'notification_email': 'notifications@applybooststudio.com',  # Email to receive new signup notifications
    'notification_subject': 'New Resume Submission - Apply Boost Studio',
    'notification_template': '''
    New Resume Submission Received!
    
    User Email: {email}
    Resume File: {filename}
    Submission Time: {timestamp}
    
    View in Google Drive: {drive_link}
    '''
}
"""
    
    with open('config_template.py', 'w') as f:
        f.write(config_template)
    
    print("✅ Created config_template.py")
    print("📝 Please update your config.py with these settings")

def print_setup_instructions():
    """Print detailed setup instructions"""
    print("\n" + "="*60)
    print("🔧 GOOGLE DRIVE API SETUP INSTRUCTIONS")
    print("="*60)
    
    print("\n📋 Step 1: Create Google Cloud Project")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Create a new project or select existing one")
    print("3. Enable Google Drive API:")
    print("   - Go to 'APIs & Services' > 'Library'")
    print("   - Search for 'Google Drive API'")
    print("   - Click 'Enable'")
    
    print("\n📋 Step 2: Create Credentials")
    print("1. Go to 'APIs & Services' > 'Credentials'")
    print("2. Click 'Create Credentials' > 'OAuth 2.0 Client IDs'")
    print("3. Choose 'Desktop application'")
    print("4. Download the JSON file")
    print("5. Rename it to 'credentials.json' and place in project root")
    
    print("\n📋 Step 3: Get Google Drive Folder ID")
    print("1. Create a folder in Google Drive")
    print("2. Open the folder in browser")
    print("3. Copy the folder ID from URL:")
    print("   https://drive.google.com/drive/folders/FOLDER_ID_HERE")
    print("4. Update config.py with the folder ID")
    
    print("\n📋 Step 4: Update Configuration")
    print("1. Update config.py with your settings:")
    print("   - credentials_file: 'credentials.json'")
    print("   - token_file: 'token.json'")
    print("   - folder_id: 'your-folder-id'")
    print("   - notification_email: 'your-notification-email'")
    
    print("\n📋 Step 5: Install Dependencies")
    print("Run: pip install -r requirements.txt")
    
    print("\n📋 Step 6: Test Setup")
    print("1. Start the application: python run.py")
    print("2. Submit a resume through the form")
    print("3. Check console logs for Google Drive upload status")
    
    print("\n⚠️  Important Notes:")
    print("- Keep credentials.json secure and don't commit to version control")
    print("- The first time you run the app, it will open a browser for OAuth")
    print("- After authentication, a token.json file will be created")
    print("- The token will be reused for subsequent requests")
    
    print("\n" + "="*60)

def check_setup():
    """Check if setup is complete"""
    print("\n🔍 CHECKING SETUP STATUS")
    print("-" * 30)
    
    # Check credentials file
    if os.path.exists('credentials.json'):
        print("✅ credentials.json found")
    else:
        print("❌ credentials.json not found")
        print("   Run: python setup_google_drive.py --create-credentials")
    
    # Check config file
    if os.path.exists('config.py'):
        print("✅ config.py found")
    else:
        print("❌ config.py not found")
    
    # Check requirements
    if os.path.exists('requirements.txt'):
        print("✅ requirements.txt found")
    else:
        print("❌ requirements.txt not found")
    
    # Check uploads folder
    if os.path.exists('uploads'):
        print("✅ uploads folder found")
    else:
        print("❌ uploads folder not found")
        print("   Creating uploads folder...")
        os.makedirs('uploads', exist_ok=True)
        print("✅ uploads folder created")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--create-credentials":
            create_credentials_template()
        elif sys.argv[1] == "--create-config":
            create_config_template()
        elif sys.argv[1] == "--check":
            check_setup()
        else:
            print("Usage:")
            print("  python setup_google_drive.py --create-credentials")
            print("  python setup_google_drive.py --create-config")
            print("  python setup_google_drive.py --check")
    else:
        print_setup_instructions()
        check_setup() 