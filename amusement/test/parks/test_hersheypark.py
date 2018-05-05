import unittest
from .parkcheck import park_valid

from amusement.parks.HersheyPark import HersheyPark

class HersheyTest(unittest.TestCase):

    def test_hersheypark(self):
        hp = HersheyPark()
        self.assertEqual(park_valid(hp), True)
