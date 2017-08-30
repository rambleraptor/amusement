import unittest

from amusement.park import Park
from amusement.show import Show
from amusement.ride import Ride

class ParkTestCase(unittest.TestCase):
    def test_rides_no_rides(self):
        park = Park()
        with self.assertRaises(Exception):
            self.assertEqual(park.rides(), [])

    def test_shows_no_shows(self):
        park = Park()
        with self.assertRaises(Exception):
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
