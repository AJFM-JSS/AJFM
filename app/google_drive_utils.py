"""
Google Drive Utilities for Apply Boost Studio
Handles file uploads to Google Drive with async functionality
"""

import asyncio
import os
import json
from datetime import datetime
from typing import Optional, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
import aiofiles
from config import GOOGLE_DRIVE_CONFIG


class GoogleDriveManager:
    """Manages Google Drive operations with async support"""
    
    def __init__(self):
        self.creds = None
        self.service = None
        self.folder_id = GOOGLE_DRIVE_CONFIG['folder_id']
        self.credentials_file = GOOGLE_DRIVE_CONFIG['credentials_file']
        self.token_file = GOOGLE_DRIVE_CONFIG['token_file']
        self.scopes = GOOGLE_DRIVE_CONFIG['scopes']
    
    async def authenticate(self) -> bool:
        """Authenticate with Google Drive API"""
        try:
            print("=== GOOGLE DRIVE AUTHENTICATION ===")
            
            # Check if credentials file exists
            if not os.path.exists(self.credentials_file):
                print(f"Credentials file not found: {self.credentials_file}")
                return False
            
            # Load existing token if available
            if os.path.exists(self.token_file):
                print("Loading existing token...")
                async with aiofiles.open(self.token_file, 'r') as f:
                    token_data = await f.read()
                    self.creds = Credentials.from_authorized_user_info(
                        json.loads(token_data), self.scopes
                    )
            
            # If no valid credentials, get new ones
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    print("Refreshing expired token...")
                    self.creds.refresh(Request())
                else:
                    print("Getting new credentials...")
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_file, self.scopes
                    )
                    self.creds = flow.run_local_server(port=0)
                
                # Save credentials for next run
                async with aiofiles.open(self.token_file, 'w') as f:
                    await f.write(self.creds.to_json())
            
            # Build the service
            self.service = build('drive', 'v3', credentials=self.creds)
            print("Google Drive authentication successful!")
            return True
            
        except Exception as e:
            print(f"Google Drive authentication failed: {e}")
            return False
    
    async def upload_file(self, file_path: str, filename: str, email: str) -> Optional[Dict[str, Any]]:
        """Upload file to Google Drive asynchronously"""
        try:
            print(f"=== UPLOADING TO GOOGLE DRIVE ===")
            print(f"File: {file_path}")
            print(f"Filename: {filename}")
            print(f"User Email: {email}")
            
            # Authenticate if not already done
            if not self.service:
                if not await self.authenticate():
                    return None
            
            # Create file metadata
            file_metadata = {
                'name': f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{email}_{filename}",
                'parents': [self.folder_id],
                'description': f'Resume submission from {email} at {datetime.now().isoformat()}'
            }
            
            # Create media upload
            media = MediaFileUpload(file_path, resumable=True)
            
            # Upload file
            print("Starting file upload...")
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id,name,webViewLink,createdTime'
            ).execute()
            
            print(f"File uploaded successfully!")
            print(f"File ID: {file.get('id')}")
            print(f"File Name: {file.get('name')}")
            print(f"Web View Link: {file.get('webViewLink')}")
            
            return {
                'file_id': file.get('id'),
                'file_name': file.get('name'),
                'web_view_link': file.get('webViewLink'),
                'created_time': file.get('createdTime'),
                'user_email': email,
                'original_filename': filename
            }
            
        except HttpError as e:
            print(f"Google Drive upload error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error during upload: {e}")
            return None
    
    async def create_folder_if_not_exists(self, folder_name: str) -> Optional[str]:
        """Create a folder in Google Drive if it doesn't exist"""
        try:
            # Check if folder already exists
            query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and '{self.folder_id}' in parents and trashed=false"
            results = self.service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
            files = results.get('files', [])
            
            if files:
                print(f"Folder '{folder_name}' already exists")
                return files[0]['id']
            
            # Create new folder
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [self.folder_id]
            }
            
            folder = self.service.files().create(body=folder_metadata, fields='id').execute()
            print(f"Created folder '{folder_name}' with ID: {folder.get('id')}")
            return folder.get('id')
            
        except Exception as e:
            print(f"Error creating folder: {e}")
            return None
    
    async def list_files(self, folder_id: str = None) -> list:
        """List files in a Google Drive folder"""
        try:
            if not folder_id:
                folder_id = self.folder_id
            
            query = f"'{folder_id}' in parents and trashed=false"
            results = self.service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name, createdTime, webViewLink)'
            ).execute()
            
            return results.get('files', [])
            
        except Exception as e:
            print(f"Error listing files: {e}")
            return []


# Global instance
drive_manager = GoogleDriveManager()


async def upload_resume_to_drive(file_path: str, filename: str, email: str) -> Optional[Dict[str, Any]]:
    """Upload resume file to Google Drive"""
    return await drive_manager.upload_file(file_path, filename, email)


async def send_drive_notification(upload_result: Dict[str, Any]) -> bool:
    """Send notification about new file upload"""
    try:
        from app.utils import send_email
        
        notification_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'sender_email': 'your-email@gmail.com',  # Update with your email
            'sender_password': 'your-app-password',  # Update with your app password
            'admin_email': 'notifications@applybooststudio.com'  # Update with notification email
        }
        
        subject = "New Resume Uploaded to Google Drive"
        message = f"""
        New resume has been uploaded to Google Drive!
        
        User Email: {upload_result['user_email']}
        File Name: {upload_result['file_name']}
        Original Filename: {upload_result['original_filename']}
        Upload Time: {upload_result['created_time']}
        
        View in Google Drive: {upload_result['web_view_link']}
        
        File ID: {upload_result['file_id']}
        """
        
        return send_email(
            notification_config,
            subject,
            message,
            notification_config['admin_email']
        )
        
    except Exception as e:
        print(f"Error sending drive notification: {e}")
        return False


async def process_resume_upload(file_path: str, filename: str, email: str) -> Dict[str, Any]:
    """Process resume upload to Google Drive and send notifications"""
    result = {
        'success': False,
        'drive_upload': None,
        'notification_sent': False,
        'error': None
    }
    
    try:
        # Upload to Google Drive
        drive_result = await upload_resume_to_drive(file_path, filename, email)
        
        if drive_result:
            result['drive_upload'] = drive_result
            result['success'] = True
            
            # Send notification
            notification_sent = await send_drive_notification(drive_result)
            result['notification_sent'] = notification_sent
            
            print(f"Resume upload processed successfully!")
            print(f"Drive upload: {result['drive_upload']}")
            print(f"Notification sent: {result['notification_sent']}")
        else:
            result['error'] = "Failed to upload to Google Drive"
            
    except Exception as e:
        result['error'] = str(e)
        print(f"Error processing resume upload: {e}")
    
    return result 