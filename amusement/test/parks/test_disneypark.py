import unittest
from .parkcheck import park_valid

from amusement.parks.disney.MagicKingdom import MagicKingdom
from amusement.parks.disney.AnimalKingdom import AnimalKingdom
from amusement.parks.disney.CaliforniaAdventure import CaliforniaAdventure
from amusement.parks.disney.Disneyland import Disneyland
from amusement.parks.disney.Epcot import Epcot
from amusement.parks.disney.HollywoodStudios import HollywoodStudios
from amusement.parks.disney.DisneylandParis import DisneylandParis

class DisneyParkTest(unittest.TestCase):

    def test_magickingdom(self):
        mk = MagicKingdom()
        self.assertEqual(park_valid(mk), True)

    def test_epcot(self):
        ep = Epcot()
        self.assertEqual(park_valid(ep), True)

    def test_hollywoodstudios(self):
        hs = HollywoodStudios()
        self.assertEqual(park_valid(hs), True)

    def test_animalkingdom(self):
        ak = AnimalKingdom()
        self.assertEqual(park_valid(ak), True)

    def test_disneyland(self):
        dl = Disneyland()
        self.assertEqual(park_valid(dl), True)

    def test_californiaadventure(self):
        ca = CaliforniaAdventure()
        self.assertEqual(park_valid(ca), True)

    def test_disneylandparis(self):
        dlp = DisneylandParis()
        self.assertEqual(park_valid(dlp), True)

