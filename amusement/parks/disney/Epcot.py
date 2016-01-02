#!/usr/bin/env python
from amusement.parks.disney.DisneyPark import DisneyPark
class Epcot(DisneyPark):

    def __init__(self):
        super(Epcot, self).__init__()

    def getId(self):
        return '80007838'

    def getName(self):
        return "Epcot"
