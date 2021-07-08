#  API_CAL_refresh.py

`API_CAL_refresh.py` is a script in **Python** to clear **all** events in
Google calendar and send new events from a `.ics` file. That idea is
from a need to send my appointments from
[EMACS](https://www.gnu.org/software/emacs/) to Google calendar. Before
I was sending the `.ics` file by mean the Google web mail (gmail), now
is peace of cake, just run `API_CAL_refresh.py`.

## Requirement library

- from __future__ import print_function
- import httplib2
- import os
- from googleapiclient.discovery import build
- from apiclient import discovery
- from oauth2client import client
- from oauth2client import tools
- from oauth2client.file import Storage
- import datetime
- from icalendar import Calendar, Event

### Fron conda

`conda install -c conda-forge httplib2`
`conda install -c conda-forge google-api-python-client`
`conda install -c conda-forge httplib2`

### From pip

- `pip3 install --user google-api-python-client` or
- `pip3 install --upgrade google-api-python-client`
- `pip3 install --user oauth2client`
- `pip3 install --user icalendar`

- more information about Google API is available [Here](https://developers.google.com/api-client-library/python/start/installation) 

## Google calendar requirement

- Use [this wizard](https://console.developers.google.com/start/api?id=calendar) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
- On the Add credentials to your project page, click the Cancel button.
- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
- Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.
- Click OK to dismiss the resulting dialog.
- Click the file_download (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it client_secret.json.
- Prepare your `.ics` file

## How to run

Once the requirements are done, just

`python API_CAL_refresh.py`

## Testing

If your browser is on a different machine then exit and re-run this
application with the command-line parameter

`--noauth_local_webserver`

