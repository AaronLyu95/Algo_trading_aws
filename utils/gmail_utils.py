import os.path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from googleapiclient.errors import HttpError
import base64
from utils.config import from_gmail_address, to_gmail_address


def gmail_service():
    '''

    :return:
    '''
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
    cur_path = os.path.dirname(os.path.realpath(__file__))
    token_file = os.path.join(cur_path, 'gmail_token.json')

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file,
                                                      SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Algo_trading_alert.json', SCOPES)
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(token_file, 'w') as token:
        token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service



def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}



def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """
    try:
        send_message = (service.users().messages().send(userId=user_id, body=message)
                        .execute())
        print('Message Id: %s' % send_message['id'])
        return send_message
    except HttpError as err:
        print('An error occurred: %s' % err)



def send_message_gmail(subject, message_text):
    service = gmail_service()
    message = create_message(from_gmail_address,
                             to_gmail_address,
                             subject,
                             message_text)
    return  send_message(service, 'me', message)













