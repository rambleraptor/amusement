import datetime

# Required to supress some insecure cert warnings
# Normally, this is bad.
import requests

class Park(object):
    def __init__(self):
        self._rides = []
        self._shows = []
        self._time = datetime.datetime.now()

    def rides(self):
        if self._rides == []:
            self._buildPark()
        return self._rides

    def update_time(self):
        return self._time

    def shows(self):
        if self._shows == []:
            self._buildPark()
        return self._shows

    def addRide(self, ride):
        self._rides.append(ride)

    def addShow(self, show):
        self._shows.append(show)

    def setName(self, name):
        self.name = name

    def getName(self):
        raise('This must be implemented')

    def _buildPark(self):
        raise('This must be implemented')
