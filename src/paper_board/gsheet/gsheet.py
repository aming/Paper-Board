import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from .. import config

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
TOKEN_FILE = 'token.json'
credentials = None

def init(credentials_file):
    global credentials
    if credentials is None:
        credentials = get_cred(credentials_file)

def get_cred(credentials_file):
    creds = None
    token_file_path = config.config_dir + '/' + TOKEN_FILE
    if os.path.exists(token_file_path):
        creds = Credentials.from_authorized_user_file(token_file_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request()) 
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_path, 'w') as token:
            token.write(creds.to_json())
    return creds

def get_range(spreadsheet_id, sheet_name, sheet_range):
    range_name = sheet_name + '!' + sheet_range
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])

def get_cell(spreadsheet_id, sheet_name, cell_id):
    values = get_range(spreadsheet_id, sheet_name, range_name)
    if not values:
        return "No data found"
    return values[0][0]

