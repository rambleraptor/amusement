#!/usr/bin/env python
from amusement.parks.disney.DisneyPark import DisneyPark
class Disneyland(DisneyPark):

    def __init__(self):
        super(Disneyland, self).__init__()

    def getId(self):
        return '330339'

    def getName(self):
        return "Disneyland"
