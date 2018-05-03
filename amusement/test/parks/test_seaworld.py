import unittest
from .parkcheck import park_valid

from amusement.parks.seaworld.BuschGardensTampa import BuschGardensTampa
from amusement.parks.seaworld.BuschGardensWilliamsburg import BuschGardensWilliamsburg
from amusement.parks.seaworld.SeaworldOrlando import SeaworldOrlando
from amusement.parks.seaworld.SeaworldSanAntonio import SeaworldSanAntonio
from amusement.parks.seaworld.SeaworldSanDiego import SeaworldSanDiego

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

