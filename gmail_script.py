# https://developers.google.com/gmail/api/quickstart/python

import asyncio
import os.path
import re
import pandas as pd

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
EMAIL_REGEX = '<.*>'
PATH_TO_EXCEL = 'emails.xlsx'
EXCLUDE_EMAIL_PATTERN = '(info)|(Info)|(noreply)|(newsletter)|(Newsletter)|(notifications)'


def parse_name_email(value):
    """Parse value 'Loc Nguyen <locnt1195@gmail.com>' to dict {'name': 'Loc Nguyen', 'email': 'locnt1195@gmail.com'}."""
    match = re.search(EMAIL_REGEX, value)
    result = {}
    if match:
        name, email = value.split('<')
        email = email[:-1]
        username_domain = email.split('@')
        result['name'] = name[:-1]
        result['email'] = email
        result['username'] = username_domain and username_domain[0] or ''
        result['domain'] = username_domain and username_domain[-1] or ''
    return result


async def read_email_detail(service, user_id, msg_id):
    print(f'Reading message {msg_id}')

    temp_dict = {}

    try:

        message = service.users().messages().get(userId=user_id, id=msg_id).execute()  # fetch the message using API
        payld = message['payload']  # get payload of the message
        headrs = payld['headers']  # get header of the payload

        for headr in headrs:
            match headr['name']:
                case 'Date':
                    temp_dict['Date'] = headr['value']
                case 'From':
                    temp_dict['From'] = parse_name_email(headr['value'])
                case 'To':
                    temp_dict['To'] = headr['value']

    except Exception as e:
        print(e)
        temp_dict = {}
        pass

    finally:
        return temp_dict


async def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print('Reading credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        user_id = 'me'

        results = service.users().labels().list(userId=user_id).execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels found.")
            return

        labels_index = {index: label for index, label in enumerate(labels)}
        print("Available Labels:")
        for index, label in labels_index.items():
            print(f'{index + 1}. {label["name"]}')

        selected_lable_index = input("Get messages from labels index. E.g: 1,3,4 :")
        if not labels_index:
            return

        selected_labels = [
            labels_index[int(index) - 1]
            for index in selected_lable_index.split(',')
            if labels_index.get(int(index) - 1)
        ]
        selected_labels_name = ','.join([label['name'] for label in selected_labels])
        print(f'Select labels: {selected_labels_name}')

        maxResults = 500  # maximum 500
        data = []
        for label in selected_labels:
            print(f'Start getting messages from label {label["name"]}')
            response = (
                service.users().messages().list(userId=user_id, maxResults=maxResults, labelIds=label["id"]).execute()
            )

            if 'messages' in response:
                data.extend(await handle_messages(service, user_id, response['messages']))
            while 'nextPageToken' in response:
                page_token = response['nextPageToken']

                response = (
                    service.users().messages().list(userId=user_id, pageToken=page_token, maxResults=maxResults).execute()
                )

                data.extend(await handle_messages(service, user_id, response['messages']))

                print(
                    '... total %d emails on next page [page token: %s]. Totally %s'
                    % (len(response['messages']), page_token, len(data))
                )

        if data:
            await write_to_xlsx(data)
        else:
            print('No messages.')

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


async def handle_messages(service, user_id, messages):
    tasks = set()
    for message in messages:
        tasks.add(read_email_detail(service, user_id, message['id']))

    data = await asyncio.gather(*tasks)
    result = []
    for message in data:
        if not message:
            continue
        if message['From'].get('email') and not re.search(EXCLUDE_EMAIL_PATTERN, message['From']['email']):
            result.append(
                [
                    message['Date'],
                    message['From']['name'],
                    message['From']['email'],
                    message['From']['username'],
                    message['From']['domain'],
                    message.get('To', '')
                ]
            )
        else:
            print(f'Ignore email from {message["From"].get("email")} to {message.get("To", "")}')
    return result


async def write_to_xlsx(messages_data):
    df = pd.DataFrame(
        messages_data,
        index=None,
        columns=[
            'Date',
            'From Name',
            'From Email',
            'From Username',
            'From Domain',
            'To',
        ],
    )
    df.to_excel(PATH_TO_EXCEL, index=None, sheet_name='sheet1')


if __name__ == "__main__":
    print('Start script')
    # check excel file exist
    if os.path.exists(PATH_TO_EXCEL):
        print(f'File {PATH_TO_EXCEL} is exist. Please delete before running script.')
    else:
        asyncio.run(main())
    print('End script')
