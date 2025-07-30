# Email Configuration for Apply Boost Studio
# Update these settings with your actual email credentials

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',  # Gmail SMTP server
    'smtp_port': 587,  # TLS port
    'sender_email': 'your-email@gmail.com',  # Your Gmail address
    'sender_password': 'your-app-password',  # Gmail App Password (not regular password)
    'admin_email': 'admin@applybooststudio.com'  # Admin email to receive consultation requests
}

# Google Drive Configuration
GOOGLE_DRIVE_CONFIG = {
    'credentials_file': 'credentials.json',  # Path to your Google Drive API credentials
    'token_file': 'token.json',  # Path to store OAuth token
    'folder_id': '10SdBlXu6SfS9K0ou6akgTNvSFbO0auWW',  # Google Drive folder ID where files will be uploaded
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

# Instructions for Gmail setup:
# 1. Enable 2-factor authentication on your Gmail account
# 2. Generate an App Password: Google Account > Security > App Passwords
# 3. Use the generated 16-character password as sender_password
# 4. Make sure "Less secure app access" is disabled

# Instructions for Google Drive setup:
# 1. Go to Google Cloud Console (https://console.cloud.google.com/)
# 2. Create a new project or select existing one
# 3. Enable Google Drive API
# 4. Create credentials (Service Account or OAuth 2.0)
# 5. Download credentials.json file
# 6. Update GOOGLE_DRIVE_CONFIG with your file paths and folder ID

# For production, use environment variables:
# import os
# EMAIL_CONFIG = {
#     'smtp_server': os.environ.get('SMTP_SERVER', 'smtp.gmail.com'),
#     'smtp_port': int(os.environ.get('SMTP_PORT', 587)),
#     'sender_email': os.environ.get('SENDER_EMAIL'),
#     'sender_password': os.environ.get('SENDER_PASSWORD'),
#     'admin_email': os.environ.get('ADMIN_EMAIL')
# }
# GOOGLE_DRIVE_CONFIG = {
#     'credentials_file': os.environ.get('GOOGLE_CREDENTIALS_FILE'),
#     'token_file': os.environ.get('GOOGLE_TOKEN_FILE'),
#     'folder_id': os.environ.get('GOOGLE_DRIVE_FOLDER_ID'),
#     'scopes': ['https://www.googleapis.com/auth/drive.file']
# }
# NOTIFICATION_CONFIG = {
#     'notification_email': os.environ.get('NOTIFICATION_EMAIL'),
#     'notification_subject': os.environ.get('NOTIFICATION_SUBJECT', 'New Resume Submission'),
#     'notification_template': os.environ.get('NOTIFICATION_TEMPLATE', 'Default template')
# } 