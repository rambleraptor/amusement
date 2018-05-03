#!/usr/bin/env python
import requests
from amusement.park import Park
from amusement.ride import Ride

class HersheyPark(Park):
    _park_url = 'https://hpapp.hersheypa.com/v1/rides'
    _wait_url = 'https://hpapp.hersheypa.com/v1/rides/wait' 


    def __init__(self):
        super(HersheyPark, self).__init__()

    def getName(self):
        return 'Hersheypark'

    def _buildPark(self):
        park_page = self.get_page(self._park_url)
        wait_page = self.get_page(self._wait_url)
        # Deal with attractions
        for poi in park_page:
            self._build_attr(poi, wait_page)


    def get_page(self, url):
        # Make page request, return Beautiful Soup request
        response = requests.get(url, timeout=3)
        return response.json()

    def _build_attr(self, row, wait_page):
        # Create dictionary with attraction information
        result = Ride()

        result.setName(row['name'])        
        result.setOpen()
        result.setTime(0)

        if 'wait' in wait_page:
            for wait_dict in wait_page['wait']:
                if wait_dict['id'] == row['id']:
                    result.setTime(wait_dict['wait'])

        if 'closed' in wait_page:
            for wait in wait_page['closed']:
                if wait == row['id']:
                    result.setClosed()

        if 'wait' in wait_page and len(wait_page['wait']) == 0:
            result.setClosed()

        self.addRide(result)
