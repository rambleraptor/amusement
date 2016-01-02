#!/usr/bin/env python
from amusement.parks.disney.DisneyPark import DisneyPark
class MagicKingdom(DisneyPark):

    def __init__(self):
        super(MagicKingdom, self).__init__()

    def getId(self):
        return '80007944'

    def getName(self):
        return "Disney's Magic Kingdom"
