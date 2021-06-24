from pprint import pprint
from Google import Create_Service
import datetime

# from __future__ import print_function
# import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def newDay(today):
    time = "T23:59:00.00+07:00"
    date = today.split("T")[0] 
    return date + time
    
def startDay(today):
    time = "T00:00:00.00+07:00"
    date = today.split("T")[0] 
    return date + time

def firstDay(today):
    time = "T00:00:00.00+07:00"
    temp = today.split("T")[0]
    temp2 = temp.split("-")
    
    temp2[2] = "1"
    
    date = "-".join(temp2)
    
    return date + time
    # return date

def lastDay(today):
    time = "T00:00:00.00+07:00"
    temp = today.split("T")[0]
    temp2 = temp.split("-")
    
    temp2[2] = "30"
    
    date = "-".join(temp2)
    
    return date + time

def get_event_day():
    """
    10 event tiếp theo trên calendar.
    """
    creds = None
    eventList = []
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    date = datetime.datetime.now().isoformat() + 'Z'  # 'Z' giờ UTC
    # print(date)
    today = startDay(date)
    morrow  = newDay(date)
    
    # print(today)
    # print(morrow)
    
    events_result = service.events().list(calendarId='primary', timeMin=today, timeMax=morrow,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    

    if not events:
        ev = 'No upcoming events found.'
        eventList.append(ev)
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        ev = start +  "->" + event['summary']
        
        eventList.append(ev)
        # print(start, )

#         start = event['start'].get('dateTime')
# #        print(start)
#         start = start[:-9]
# #        print(start)
#         start = datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M")

#         pretty_time = start.strftime("%I:%M")
#         pretty_date = start.strftime("%B %d, %Y")
                
#         print(event['summary'],"at",pretty_time,"on",pretty_date)
    return eventList

def get_event_month():
    """
    10 event tiếp theo trên calendar.
    """
    creds = None
    eventList = []
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    date = datetime.datetime.now().isoformat() + 'Z'  # 'Z' giờ UTC
    # print(date)
    first = firstDay(date)
    last  = lastDay(date)
    
    # print(today)
    # print(morrow)
    
    events_result = service.events().list(calendarId='primary', timeMin=first, timeMax=last,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    

    if not events:
        ev = 'No upcoming events found.'
        eventList.append(ev)
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        ev = start +  "->" + event['summary']
        
        eventList.append(ev)
        # print(start, )

#         start = event['start'].get('dateTime')
# #        print(start)
#         start = start[:-9]
# #        print(start)
#         start = datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M")

#         pretty_time = start.strftime("%I:%M")
#         pretty_date = start.strftime("%B %d, %Y")
                
#         print(event['summary'],"at",pretty_time,"on",pretty_date)
    return eventList

# print(get_event_month())