# ======================================================================
# Rafael Tieppo
# rafaeltieppo@yahoo.com.br
# https://rafatieppo.github.io/
# 11-12-2017
# Google cal API - Script to clear and add Events
# ======================================================================

from __future__ import print_function
import httplib2
import os

# from googleapiclient.discovery import build
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
from icalendar import Calendar, Event

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = '/home/rafatieppo/client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    """Erase all events and send a new ics file from Emacs.

    """

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

# ------------------------------------------------------------
# Clear all events
    service.calendars().clear(calendarId='primary').execute()

# ------------------------------------------------------------
# Add event one by one
    count = 0
    g = open('/home/rafatieppo/Dropbox/EMACS_ORG_MODE/RAFA.ics', 'rb')
    gcal = Calendar.from_ical(g.read())
    for component in gcal.walk():
        if component.name == "VEVENT":
            envent_summary = (component.get('summary'))
            event_dtstart = (component.get(
                'dtstart').dt.isoformat() + '-03:00')
            event_dtend = (component.get('dtend').dt.isoformat() + '-03:00')
            event = {'summary': envent_summary,
                     'start': {'dateTime': event_dtstart},
                     'end': {'dateTime': event_dtend}
                     }
            count = count + 1
            print (str(count))
            print(event)
            service.events().insert(calendarId='primary', body=event).execute()
    g.close()


if __name__ == '__main__':
    main()
