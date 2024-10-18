from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io
import os
from datetime import datetime


class GoogleDriveUploader:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive.file']
        self.credentials = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=self.SCOPES)
        self.service = build('drive', 'v3', credentials=self.credentials)
        
    def get_or_create_folder(self, folder_name):
        """Get or create a folder in Google Drive"""
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
        results = self.service.files().list(q=query).execute()
        items = results.get('files', [])
        
        if not items:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = self.service.files().create(body=file_metadata, fields='id').execute()
            return folder.get('id')
            
        return items[0]['id']
        
    def upload_file(self, content, filename, folder_id, mime_type):
        """Upload a file to Google Drive"""
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        
        media = MediaIoBaseUpload(
            io.BytesIO(content.encode('utf-8')),
            mimetype=mime_type,
            resumable=True
        )
        
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        return file.get('id')

    def upload_expense(self, json_content, xml_content, expense_id):
        """Upload both JSON and XML versions of an expense"""
        folder_id = self.get_or_create_folder('harcamalar')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Upload JSON
        json_filename = f'expense_{expense_id}_{timestamp}.json'
        self.upload_file(json_content, json_filename, folder_id, 'application/json')
        
        # Upload XML
        xml_filename = f'expense_{expense_id}_{timestamp}.xml'
        self.upload_file(xml_content, xml_filename, folder_id, 'application/xml')
