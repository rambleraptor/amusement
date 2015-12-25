import unittest
from park import Park
from show import Show
from ride import Ride

class ParkTestCase(unittest.TestCase):
    def test_rides_exist(self):
        park = Park()
        self.assertEqual(park.rides(), [])

    def test_shows_exist(self):
        park = Park()
        self.assertEqual(park.shows(), [])

    def test_addRide(self):
        park = Park()
        ride = Ride()
        park.addRide(ride)
        self.assertEqual(len(park.rides()), 1)

    def test_addShow(self):
        park = Park()
        show = Show()
        park.addShow(show)
        self.assertEqual(len(park.shows()), 1)
