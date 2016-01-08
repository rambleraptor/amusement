import requests
import datetime
import dateutil
from bs4 import BeautifulSoup
from amusement.park import Park
from amusement.ride import Ride
from amusement.show import Show

class UniversalHollywood(Park):
    def __init__(self):
        super(UniversalHollywood, self).__init__()

    def getName(self):
        return 'Universal Studios Hollywood'

    def _buildPark(self):
        page = self.get_page() 

        for table_row in page.find_all('tr'):
            if table_row.find_all('td', 'ride'):
                try:
                    name = table_row.contents[1].contents[0].text
                    time = table_row.contents[3].text
                    self._build_attraction(name, time)
                except Exception as e:
                    print "%s - row invalid" % table_row
                    pass

    def get_page(self):
        r = requests.get('http://m.universalstudioshollywood.com/waittimes')
        return BeautifulSoup(r.text)

    def _build_attraction(self, name, time):
        attraction = Ride()
        attraction.setName(name)

        if 'CLOSED' in time:
            attraction.setClosed()
        elif 'OPENS' in time or 'OPENING SOON' in time:
            attraction.setClosed()
        else:
            attraction.setOpen()

        if 'LAST SHOW' in time:
            attraction = Show()
            attr_time = time.split()[-2:]
            attr_time = ''.join(attr_time)
            attr_time = datetime.date.today().strftime("%B %d, %Y") + ' ' + attr_time
            attr_time = dateutil.parser.parse(attr_time)
            attraction.addTime(attr_time)
        elif 'AM' in time or 'PM' in time:
            try:
                attraction = Show()
                time2 = time[0:2]
                time_obj = dateutil.parser.parse(time2)
                attraction.setTime(time_obj)
            except:
                attraction = Show()
                time_obj = dateutil.parser.parse(time)
                attraction.setTime(time_obj)

        else:
            waittime = int(time.split()[0])
            attraction.setTime(waittime)

        if isinstance(attraction, Show):
            self.addShow(attraction)
        else:
            self.addRide(attraction)
