import unittest
from nose.tools import *
from ride import Ride

class RideTestCase(unittest.TestCase):

    def test_setOpen(self):
        ride = Ride()
        ride.setOpen()
        self.assertEqual(ride['isOpen'], True)

    def test_setClosed(self):
        ride = Ride()
        ride.setClosed()
        self.assertEqual(ride['isOpen'], False)

    def test_isOpen(self):
        ride = Ride()
        ride.setClosed()
        self.assertEqual(ride.isOpen(), False)

    def test_setTimeString(self):
        ride = Ride()
        test_time_str = '10'
        test_time_int = int(test_time_str)
        ride.setTime(test_time_str)
        self.assertEquals(ride['wait'], test_time_int)

    def test_setTimeInt(self):
        ride = Ride()
        test_time_str = '10'
        test_time_int = int(test_time_str)
        ride.setTime(test_time_int)
        self.assertEquals(ride['wait'], test_time_int)
