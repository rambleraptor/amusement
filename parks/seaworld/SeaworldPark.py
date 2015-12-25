#!/usr/bin/env python
import requests
import datetime
import time
from dateutil.parser import parse
from park import Park
from ride import Ride
from show import Show

PARK_URL_FORMAT = 'https://seas.te2.biz/v1/rest/venue/{0}/poi/all/status'
SHOW_URL_FORMAT = 'https://seas.te2.biz/v1/rest/venue/{0}/shows/{1}'

class SeaworldPark(Park):
    def getId(self):
        raise('Must be implemented in a subclass')

    def __init__(self):
        super(SeaworldPark, self).__init__()
        self._park_url = PARK_URL_FORMAT.format(self.getId())

        ts = time.time()
        today = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        self._show_url = SHOW_URL_FORMAT.format(self.getId(), today)

        self._build_page()

    def _build_page(self):
        parsed_page = self._get_page(self._park_url)
        for poi in parsed_page:
            self._build_ride(poi)

        parsed_page = self._get_page(self._show_url)
        for poi in parsed_page:
            self._build_show(poi)

    def _get_page(self, url):
        # Make page request, return Beautiful Soup request
        response = requests.get(url, auth=('seaworld', '1393288508')) 
        return response.json()

    def _build_ride(self, row):
        # Create dictionary with attraction information
        result = Ride()
        if 'label' in row:
            result.setName(row['label'])
        else:
            return

        if row['status']['isOpen']:
            result.setOpen()
        else:
            result.setClosed()
        
        if 'waitTime' in row['status']:
            result.setTime(row['status']['waitTime'])
        elif result.isOpen():
            result.setTime(0)

        self.addRide(result)

    def _build_show(self, row):
        result = Show()

        if 'title' in row:
            result.setName(row['title'])
        else:
            return

        for time_dict in row['schedule']['entries']:
            format_string = 'YYYY-MM-DDTHH:MM:SS.mmmmmm'
            time_obj = parse(time_dict['start'])
            result.addTime(time_obj)

        self.addShow(result)
