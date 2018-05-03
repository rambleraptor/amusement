import requests
import dateutil
from bs4 import BeautifulSoup

from amusement.park import Park
from amusement.show import Show
from amusement.ride import Ride

"""
This is expirimental! It is a work in progress and probably will not work. USS's API has been very tempermental.
"""
class UniversalSingapore(Park):
    _url = 'http://cma.rwsentosa.com/Service.svc/GetUSSContent?languageID=1&filter=Show,Ride,MeetAndGreet,&Latitude=1.254251&Longitude=103.823797'

    _headers = {
        'Proxy-Connection' : 'keep-alive',
        'Accept-Encoding' : 'gzip',
        'Accept' : '*/*',
        'Accept-Language' : 'en-us',
        'Connection' : 'keep-alive',
        'User-Agent' : 'RWS/1.11 CFNetwork/758.1.6 Darwin/15.0.0'
    }
    def __init__(self):
        super(UniversalSingapore, self).__init__()

    def getName(self):
        return 'Universal Studios Singapore'

    def _buildPark(self):
        page = self.get_page(self._url)

        zone_list = page.html.body.responseofuss.result.find_all('usszonelist')[0]
        for zone in zone_list.find_all('usszone'):
            for attraction in zone.content.find_all('usscontent'):
                self._build_attr(attraction)

    def _build_attr(self, attraction):
        print(attraction.contenttype.text)
        if attraction.contenttype.text == 'USSShow':
            document = Show()
            document.setName(attraction.find('name').text)
            if 'ashx' in attraction.showtime.text:
                return

            showtimes = self.get_showtimes(attraction.showtime.text)
            for show in showtimes:
                try:
                    time_obj = dateutil.parser.parse(show)
                    document.addTime(time_obj)
                except:
                    pass
            self.addShow(document)

        if attraction.contenttype.text == 'Ride':
            document = Ride()
            document.setName(attraction.find('name').text)
            document.setRide()
            if 'Guests' in attraction.queuetime.text:
                document.setTime(0)
            else:
                document.setTime(attraction.queuetime.text)

            if attraction.availability.text == 'True':
                document.setOpen()
            else:
                document.setClosed()

            self.addRide(document)
            
    def get_showtimes(self, showtimes):
        showtimes = showtimes.replace('and', '')
        showtimes = showtimes.replace(',', '')
        showtimes = showtimes.split(' ')
        array_times = []
        for x in showtimes:
            time_obj = None
            if x != '':
                if 'pm' in x:
                    time_obj = ' pm'.join(x.split('pm'))
                if 'am' in x:
                    time_obj = ' am'.join(x.split('am'))

            if time_obj:
                array_times.append(time_obj)
           
        return array_times

    def get_page(self, url):
        r = requests.get(url, headers=self._headers)
        return BeautifulSoup(r.text)
