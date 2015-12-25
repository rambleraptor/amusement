#!/usr/bin/env python
import urllib
import urllib2
import requests
import database
import datetime
import re
import time
from dateutil.parser import parse
from bs4 import BeautifulSoup

def main():
    park_url = 'https://hpapp.hersheypa.com/v1/rides'
    wait_url = 'https://hpapp.hersheypa.com/v1/rides/wait' 

    document = database.Document('Hersheypark')

    park_page = get_page(park_url)
    wait_page = get_page(wait_url)

    # Deal with attractions
    for poi in park_page:
        results = prep_row(poi, wait_page)
        if results.validate():
            document.append_attraction(results)

    document.submit()

def get_page(url):
    # Make page request, return Beautiful Soup request
    response = requests.get(url)
    return response.json()

def prep_row(row, wait_page):
    # Create dictionary with attraction information
    result = database.Attraction(row['name'])
    
    result.setRide()
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

    return result

if __name__ == '__main__':
    main()


