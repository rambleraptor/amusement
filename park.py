import datetime
from ride import Ride
from show import Show
class Park(object):
    def __init__(self):
        self._rides = []
        self._shows = []
        self._time = datetime.datetime.now()
        self.name = ''

    def rides(self):
        return self._rides

    def update_time(self):
        return self._time

    def shows(self):
        return self._shows

    def addRide(self, ride):
        self._rides.append(ride)

    def addShow(self, show):
        self._shows.append(show)

    def setName(self, name):
        self.name = name

    def getName(self, name):
        return self.name
