import requests
import time
import datetime
import hmac
import base64
import re
import hashlib
import json
import dateutil
from park import Park
from ride import Ride
from show import Show
SHARED_HEADERS = {
    'Accept'                          : 'application/json',
    'Accept-Language'                 : 'en-US',
    'X-UNIWebService-AppVersion'      : '1.2.1',
    'X-UNIWebService-Platform'        : 'Android',
    'X-UNIWebService-PlatformVersion' : '4.4.2',
    'X-UNIWebService-Device'          : 'samsung SM-N9005',
    'X-UNIWebService-ServiceVersion'  : '1',
    'User-Agent'                      : 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-N9005 Build/KOT49H)',
    'Connection'                      : 'keep-alive',
    'Accept-Encoding'                 : 'gzip'
  }

RIDE_URL = 'https://services.universalorlando.com/api/pointsofinterest/rides?pageSize=all'
SHOW_URL = 'https://services.universalorlando.com/api/pointsofinterest/Shows'
class UniversalPark(Park):
    def __init__(self):
        super(UniversalPark, self).__init__()
        self._build_park()

    def _build_park(self):
        token = self._get_token()
        ride_page = self._get_request(token, RIDE_URL)
        show_page = self._get_request(token, SHOW_URL)
        print ride_page
        print show_page
        for ride in ride_page['Results']:
            if ride['VenueId'] == self.getId():
                self._make_attraction(ride)

        """
        for show in page['Shows']:
            if show['VenueId'] == self.getId():
                self._make_show(show)
        """

    def _make_attraction(self, ride):
        attraction = Ride()
        attraction.setName(ride['MblDisplayName'])

        if ride['WaitTime'] is None:
            attraction.setClosed()
        else:
            attraction.setOpen()

        if ride['WaitTime'] == -50:
            attraction.setTime(0)

        elif ride['WaitTime'] < 0:
            attraction.setClosed()

        elif ride['WaitTime'] is not None:
            attraction.setTime(ride['WaitTime'])

        self.addRide(attraction)

    def _make_show(self, show):
        show_obj = Show()
        show_obj.setName(show['MblDisplayName'])
        for time in show['StartTimes']:
            show_obj.addTime(time)

        self.addShow(show_obj)


    def _get_request(self, token, url):
        headers = {
            'X-UNIWebService-ApiKey' : 'AndroidMobileApp',
            'X-UNIWebService-Token' : token 
        }
        headers.update(SHARED_HEADERS)
        r = requests.get(url, headers=headers)
        return r.json()

    def _get_token(self):
        # Thanks to lloydpick for the Key / Secret
        KEY    = 'AndroidMobileApp'
        SECRET = 'AndroidMobileAppSecretKey182014'

        date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
        secret_test = "{KEY}\n{date}\n".format(KEY=KEY, date=date)
        digest = hmac.new(SECRET, secret_test, hashlib.sha256)
        signature = base64.b64encode(digest.digest()).strip()
        signature = re.sub('/\=$/', "\u003d", signature)
        params = { 
                'apikey': 'AndroidMobileApp', 
                'signature': signature 
        }
        headers = {
            'Date' :date,
            'Content-Type' : 'application/json; charset=UTF-8'
        }

        headers.update(SHARED_HEADERS)

        r = requests.post('https://services.universalorlando.com/api', headers=headers, data=json.dumps(params, ensure_ascii=False), verify=False)
        return r.json()['Token']
