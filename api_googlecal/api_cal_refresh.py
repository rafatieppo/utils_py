#!/usr/bin/env python3

# ======================================================================
# Rafael Tieppo
# rafaeltieppo@yahoo.com.br
# https://rafatieppo.github.io/
# 11-12-2017
# Google cal API - Script to clear and add Events
# ======================================================================

from __future__ import print_function
import datetime as dt
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from icalendar import Calendar, Event

# If modifying these scopes, delete your previously saved credentials
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
# SCOPES = 'https://www.googleapis.com/auth/calendar'
# SCOPES = 'https://www.googleapis.com/auth/calendar.events'
# SCOPES = 'https://www.googleapis.com/auth/admin.directory.resource.calendar'
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Erase all events and send a new ics file from Emacs.
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/home/rafatieppo/.credentials/token.json'):
        creds = Credentials.from_authorized_user_file(
            '/home/rafatieppo/.credentials/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or creds.valid:
        print('There is no CREDS')
        print(str(creds.valid))
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/rafatieppo/client_secret.json',
                SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('/home/rafatieppo/.credentials/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

# ------------------------------------------------------------
# Clear all events
    service.calendars().clear(calendarId='primary').execute()

# ------------------------------------------------------------
# Add event one by one
    count = 0
    g = open('/home/rafatieppo/Dropbox/emacs_org_mode/rafa.ics', 'rb')
    gcal = Calendar.from_ical(g.read())
    for component in gcal.walk():
        # print(u'', component.name)
        if component.name == "VEVENT":
            # print(str(component.get('summary')))
            envent_summary = str(component.get('summary'))
            event_dtstart = (component.get(
                'dtstart').dt.isoformat() + '-04:00')
            event_dtend = (component.get(
                'dtend').dt.isoformat() + '-04:00')
            event = {'end': {'dateTime': event_dtend},
                     'start': {'dateTime': event_dtstart},
                     'summary': envent_summary
                     }
            count = count + 1
            print('# ', str(count), ' - event: ', event)
            service.events().insert(
                calendarId='primary', body=event).execute()


if __name__ == '__main__':
    main()
