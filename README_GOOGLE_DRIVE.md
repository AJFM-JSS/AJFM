# Google Drive Integration for Apply Boost Studio

This document explains how to set up and use the Google Drive integration for automatically uploading resume files and sending notifications.

## 🚀 Features

- **Async File Upload**: Resume files are uploaded to Google Drive asynchronously
- **Automatic Notifications**: Email notifications are sent when new resumes are uploaded
- **Secure Authentication**: OAuth 2.0 authentication with token caching
- **Error Handling**: Comprehensive error handling and logging
- **File Organization**: Files are organized with timestamps and user emails

## 📋 Prerequisites

1. **Google Cloud Project**: You need a Google Cloud project with Google Drive API enabled
2. **OAuth 2.0 Credentials**: Download credentials.json from Google Cloud Console
3. **Google Drive Folder**: Create a folder in Google Drive to store uploaded files
4. **Python Dependencies**: Install required packages

## 🔧 Setup Instructions

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Set Up Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable Google Drive API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Drive API"
   - Click "Enable"

### Step 3: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. Choose "Desktop application"
4. Download the JSON file
5. Rename it to `credentials.json` and place in project root

### Step 4: Get Google Drive Folder ID

1. Create a folder in Google Drive
2. Open the folder in browser
3. Copy the folder ID from URL:
   ```
   https://drive.google.com/drive/folders/FOLDER_ID_HERE
   ```

### Step 5: Update Configuration

Update `config.py` with your settings:

```python
# Google Drive Configuration
GOOGLE_DRIVE_CONFIG = {
    'credentials_file': 'credentials.json',  # Path to your credentials file
    'token_file': 'token.json',  # Path to store OAuth token
    'folder_id': 'your-folder-id-here',  # Your Google Drive folder ID
    'scopes': ['https://www.googleapis.com/auth/drive.file']
}

# Notification Configuration
NOTIFICATION_CONFIG = {
    'notification_email': 'notifications@yourdomain.com',  # Your notification email
    'notification_subject': 'New Resume Submission - Apply Boost Studio',
    'notification_template': '''
    New Resume Submission Received!
    
    User Email: {email}
    Resume File: {filename}
    Submission Time: {timestamp}
    
    View in Google Drive: {drive_link}
    '''
}
```

### Step 6: Test Setup

1. Start the application: `python run.py`
2. Submit a resume through the form
3. Check console logs for Google Drive upload status

## 📁 File Structure

```
apply-boost-studio/
├── app/
│   ├── google_drive_utils.py    # Google Drive utilities
│   ├── routes.py                # Updated with async upload
│   └── utils.py                 # Email utilities
├── config.py                    # Updated with Google Drive config
├── requirements.txt             # Updated with Google API dependencies
├── setup_google_drive.py       # Setup helper script
├── credentials.json            # Your Google API credentials
└── token.json                 # OAuth token (created automatically)
```

## 🔄 How It Works

### 1. File Upload Process

When a user submits a resume:

1. **File Validation**: Check file type and size
2. **Local Save**: Save file to local uploads folder
3. **Email Notifications**: Send confirmation emails
4. **Async Google Drive Upload**: Upload file to Google Drive
5. **Notification Email**: Send notification about new upload

### 2. Google Drive Upload

```python
# Async upload process
drive_result = await process_resume_upload(file_path, filename, email)

# Result includes:
{
    'success': True,
    'drive_upload': {
        'file_id': '1ABC...',
        'file_name': '20250729_170449_user@email.com_resume.pdf',
        'web_view_link': 'https://drive.google.com/file/d/...',
        'created_time': '2025-07-29T17:04:49.043Z',
        'user_email': 'user@email.com',
        'original_filename': 'resume.pdf'
    },
    'notification_sent': True
}
```

### 3. File Naming Convention

Files are named with timestamp and user email:
```
YYYYMMDD_HHMMSS_user@email.com_original_filename.pdf
```

Example: `20250729_170449_user@example.com_resume.pdf`

## 📧 Notification System

### Email Notifications

1. **User Confirmation**: Sent to user confirming submission
2. **Admin Notification**: Sent to admin with resume attachment
3. **Drive Notification**: Sent to notification email about Google Drive upload

### Notification Template

```python
subject = "New Resume Uploaded to Google Drive"
message = f"""
New resume has been uploaded to Google Drive!

User Email: {email}
File Name: {filename}
Upload Time: {timestamp}

View in Google Drive: {drive_link}
"""
```

## 🛠️ Configuration Options

### Google Drive Configuration

```python
GOOGLE_DRIVE_CONFIG = {
    'credentials_file': 'credentials.json',  # OAuth credentials
    'token_file': 'token.json',             # Token cache
    'folder_id': 'your-folder-id',          # Target folder
    'scopes': ['https://www.googleapis.com/auth/drive.file']  # Permissions
}
```

### Notification Configuration

```python
NOTIFICATION_CONFIG = {
    'notification_email': 'notifications@domain.com',
    'notification_subject': 'New Resume Submission',
    'notification_template': 'Custom template...'
}
```

## 🔍 Debugging

### Console Logs

The system provides detailed logging:

```
=== GOOGLE DRIVE AUTHENTICATION ===
Loading existing token...
Google Drive authentication successful!

=== UPLOADING TO GOOGLE DRIVE ===
File: /path/to/uploads/resume.pdf
Filename: resume.pdf
User Email: user@example.com
Starting file upload...
File uploaded successfully!
File ID: 1ABC...
File Name: 20250729_170449_user@example.com_resume.pdf
Web View Link: https://drive.google.com/file/d/...

Resume upload processed successfully!
Drive upload: {...}
Notification sent: True
```

### Common Issues

1. **Authentication Error**: Check credentials.json and token.json
2. **Permission Error**: Ensure Google Drive API is enabled
3. **Folder Not Found**: Verify folder_id in config.py
4. **Token Expired**: Delete token.json to re-authenticate

## 🔒 Security Considerations

1. **Credentials Security**: Never commit credentials.json to version control
2. **Token Storage**: token.json contains sensitive data
3. **File Permissions**: Use minimal required scopes
4. **Error Handling**: Don't expose sensitive information in error messages

## 📝 Environment Variables

For production, use environment variables:

```python
import os

GOOGLE_DRIVE_CONFIG = {
    'credentials_file': os.environ.get('GOOGLE_CREDENTIALS_FILE'),
    'token_file': os.environ.get('GOOGLE_TOKEN_FILE'),
    'folder_id': os.environ.get('GOOGLE_DRIVE_FOLDER_ID'),
    'scopes': ['https://www.googleapis.com/auth/drive.file']
}
```

## 🚀 Production Deployment

1. **Use Service Account**: For production, use service account instead of OAuth
2. **Secure Storage**: Store credentials securely (not in code)
3. **Monitoring**: Add monitoring for upload failures
4. **Rate Limiting**: Implement rate limiting for API calls
5. **Backup**: Regular backup of uploaded files

## 📞 Support

If you encounter issues:

1. Check console logs for detailed error messages
2. Verify Google Cloud Console settings
3. Test with setup script: `python setup_google_drive.py --check`
4. Review Google Drive API documentation 