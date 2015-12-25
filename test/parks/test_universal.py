import unittest
from nose.tools import *
from parkcheck import park_valid

from parks.universal.UniversalStudiosFlorida import UniversalStudiosFlorida
from parks.universal.IslandsOfAdventure import IslandsOfAdventure

class UniversalParkTest(unittest.TestCase):

    def test_universalstudiosflorida(self):
        usf = UniversalStudiosFlorida()
        self.assertEqual(park_valid(usf), True)

    def test_islandsofadventure(self):
        ioa = IslandsOfAdventure()
        self.assertEqual(park_valid(ioa), True)
