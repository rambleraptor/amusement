import unittest
from nose.tools import *
from parkcheck import park_valid

from parks.seaworld.BuschGardensTampa import BuschGardensTampa
from parks.seaworld.BuschGardensWilliamsburg import BuschGardensWilliamsburg
from parks.seaworld.SeaworldOrlando import SeaworldOrlando
from parks.seaworld.SeaworldSanAntonio import SeaworldSanAntonio
from parks.seaworld.SeaworldSanDiego import SeaworldSanDiego

class SeaworldTest(unittest.TestCase):

    def test_buschgardenstampa(self):
        mk = BuschGardensTampa()
        self.assertEqual(park_valid(mk), True)

    def test_seaworldsandiego(self):
        ep = SeaworldSanDiego()
        self.assertEqual(park_valid(ep), True)

    def test_buschgardenswilliamsburg(self):
        ak = BuschGardensWilliamsburg()
        self.assertEqual(park_valid(ak), True)

    def test_seaworldsanantonio(self):
        dl = SeaworldSanAntonio()
        self.assertEqual(park_valid(dl), True)

    def test_seaworldorlando(self):
        ca = SeaworldOrlando()
        self.assertEqual(park_valid(ca), True)

