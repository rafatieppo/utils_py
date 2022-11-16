#  API_CAL_refresh.py

`API_CAL_refresh.py` is a script in **Python** to clear **all** events in
Google calendar and send new events from a `.ics` file. That idea is
from a need to send my appointments from
[EMACS](https://www.gnu.org/software/emacs/) to Google calendar. Before
I was sending the `.ics` file by means the Google web mail (gmail), now
is peace of cake, just run `./api_cal_refresh.py`.

## Logs

### Mon 2021-09-06 15:45:37 -04
- Some changes was made by google to access the API. The old script was change to `api_cal_refresh_old.py`. To run the new approach just type `./api_cal_refresh.py` (*Python3 is necessary*)

## Requirement library

from __future__ import print_function
import datetime as dt
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

### Fron conda

`conda install -c conda-forge httplib2`
`conda install -c conda-forge google-api-python-client`
`conda install -c conda-forge httplib2`

### From pip

- `pip3 install --user google-api-python-client` or
- `pip3 install --upgrade google-api-python-client`
- `pip3 install --user oauth2client`
- `pip3 install --user icalendar`

- more information about Google API is available:
  - [Here](https://developers.google.com/api-client-library/python/start/installation) 
  - [Here](https://developers.google.com/calendar/api/v3/reference/calendars/update)
  - [Here](https://developers.google.com/calendar/api/v3/reference/events/insert)
  - [Here](https://console.cloud.google.com/apis/credentials?folder=&organizationId=&project=coordfromaddress)
  - [Here](https://developers.google.com/calendar/api/quickstart/python)

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

`./python api_cal_refresh.py`

## Testing

If your browser is on a different machine then exit and re-run this
application with the command-line parameter

`--noauth_local_webserver`

