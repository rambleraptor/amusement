# encoding: utf-8
import requests
import dateutil
from amusement.park import Park
from amusement.ride import Ride
from amusement.show import Show
from amusement.config.usj import strings as names

class UniversalJapan(Park):
    def __init__(self):
        super(UniversalJapan, self).__init__()

    def getName(self):
        return 'Universal Studios Japan'

    def _buildPark(self):
        page = self._get_page() 

        if 'list' not in page:
            print('USJ - nothing appeared')
            return

        for list_thing in page['list']:
            time = list_thing['wait']
            if u'分' in time:
                try:
                    time = int(unicode(time).replace(u'分', ''))
                except Exception:
                    time = '-2'
            elif u'休止中' in time or u'本日終了' in time:
                time = '-1'

            for thing in list_thing['rows']:
                attr = self._build_attraction(thing, time, names)

        # Showtimes
        page = self._get_showpage()

        shows_so_far = []
        for list_thing in page['list']:
            for show in list_thing['rows']:
                if show['text'] not in shows_so_far:

                    shows_so_far.append(show['text'])
                    try:
                        show_doc = self._build_show(show, names)
                    except:
                        pass


    def _get_page(self):
        r = requests.get('http://ar02.biglobe.ne.jp/app/waittime/waittime.json', timeout=3)
        return r.json()

    def _get_showpage(self):
        r = requests.get('http://ar02.biglobe.ne.jp/app/waittime/schedule.json', timeout=3)
        return r.json()

    def _build_attraction(self, attr, time, names):
        try:
            name = names[attr['text']]
        except:
            name = attr['text']

        attraction = Ride()
        attraction.setName(name)

        if time == 'CLOSED':
            attraction.setClosed()
        else:
            attraction.setOpen()
            attraction.setTime(time)
        
        self.addRide(attraction)

    def _build_show(self, show, names):
        try:
            name = names[show['text']]
        except:
            name = show['text']

        attraction = Show()
        attraction.setName(name)

        showtimes = show['schedule'].replace('/', ' ').split()
        for show in showtimes:
            time_obj = dateutil.parser.parse(show)
            attraction.setTime(time_obj)

        self.addShow(attraction)

