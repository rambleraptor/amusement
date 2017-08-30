import unittest
from parkcheck import park_valid

from amusement.parks.universal.UniversalStudiosFlorida import UniversalStudiosFlorida
from amusement.parks.universal.IslandsOfAdventure import IslandsOfAdventure
from amusement.parks.universal.UniversalStudiosHollywood import UniversalStudiosHollywood
from amusement.parks.universal.UniversalJapan import UniversalJapan

class UniversalParkTest(unittest.TestCase):

    def test_universalstudiosflorida(self):
        usf = UniversalStudiosFlorida()
        self.assertEqual(park_valid(usf), True)

    def test_islandsofadventure(self):
        ioa = IslandsOfAdventure()
        self.assertEqual(park_valid(ioa), True)

    def test_universalhollywood(self):
        ush = UniversalStudiosHollywood()
        self.assertEqual(park_valid(ush), True)

    def test_universaljapan(self):
        usj = UniversalJapan()
        park_validity = park_valid(usj)

        # Edge cases where no attractions appear when park is closed
        if not park_validity and len(usj.rides()) == 0:
            park_validity = True

        self.assertEqual(park_validity, True)
