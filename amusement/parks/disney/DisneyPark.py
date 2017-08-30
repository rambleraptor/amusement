#!/usr/bin/env python
import requests
from amusement.park import Park
from amusement.ride import Ride

URL_TEMPLATE = 'https://api.wdpro.disney.go.com/facility-service/theme-parks/%s;entityType=theme-park/wait-times'

class DisneyPark(Park):

    def __init__(self):
        self._id = self.getId()
        self._url = URL_TEMPLATE % self._id
        self.name = self.getName()
        super(DisneyPark, self).__init__()

    def getId(self):
        raise('This must be implemented in a subclass')

    def getName(self):
        raise('This must be implemented in a subclass')

    def _buildPark(self):
        self._auth_token = self._authorize()
        page = self._get_page()

        for attraction in page['entries']:
            if attraction['type'] != 'Attraction':
                continue
            self._build_attraction(attraction)

    def _build_attraction(self, attraction):
        attraction_obj = Ride()

        attraction_obj.setName(attraction['name'])
        self._waitTime(attraction_obj, attraction)

        self.addRide(attraction_obj)

    def _get_page(self):
        # Make page request, return dictionary of a park's waittimes.
        headers = {
            'Accept-Language' : 'en_US',
            'User-Agent': 'UIEPlayer/2.1 iPhone OS 6.0.1',
            'Accept' : 'application/json;apiversion=1',
            'Connection' : 'keep-alive',
            'x-UJinn-Devcap' : '2048,1496,true,32',
            'x-UJinn-Copyright' : 'Copyright UIEvolution Inc.',
            'Proxy-Connection' : 'keep-alive',
            'Accept-Encoding' :'compress, gzip',
            'Authorization' : 'BEARER ' + self._auth_token,
            'X-Conversation-Id' : '~WDPRO-MOBILE.CLIENT-PROD'
        }

        response = requests.get(self._url, headers=headers, verify=False)
        page = response.json()
        return page

    def _waitTime(self,attraction_doc, attraction):
        if 'waitTime' in attraction:
            attraction_doc.setOpen()
            attraction_doc.setTime(0)
            if 'status' in attraction['waitTime'] and attraction['waitTime']['status'] == 'Closed':
                attraction_doc.setClosed()
            if 'actualWaitMinutes' in attraction['waitTime']:
                attraction_doc.setTime(attraction['waitTime']['actualWaitMinutes'])
            elif 'postedWaitMinutes' in attraction['waitTime']:
                attraction_doc.setTime(attraction['waitTime']['postedWaitMinutes'])
        else:
            attraction_doc.setClosed()
        

    def _fastPass(self,attraction_doc, attraction):
        if 'waitTime' in attraction:
            if 'fastpass' in attraction['waitTime']:
                attraction_doc.setFastPass(attraction['waitTime']['fastpass'])

    def _singleRider(self,attraction_doc, attraction):
        if 'singleRider' in attraction:
            attraction_doc.setSingleRider(attraction['singleRider'])
        

    def _authorize(self):
        # Returns authorization token
        url = 'https://authorization.go.com/token'

        headers = {
            'Accept-Language' : 'en_US',
            'Cache-Control' : 0,
            'User-Agent': 'UIEPlayer/2.1 iPhone OS 6.0.1',
            'Accept' : 'application/json;apiversion=1',
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Connection' : 'keep-alive',
            'x-UJinn-Devcap' : '2048,1496,true,32',
            'x-UJinn-Copyright' : 'Copyright UIEvolution Inc.',
            'Proxy-Connection' : 'keep-alive',
            'Content-Length' : 77,
            'Accept-Encoding' : 'gzip, deflate'
        }

        data = 'grant_type=assertion&assertion_type=public&client_id=WDPRO-MOBILE.CLIENT-PROD'
        r = requests.post(url, data=data, headers=headers, verify=False)
        response = r.json()
        auth_token = response['token_type'] + ' ' + response['access_token']
        return auth_token
