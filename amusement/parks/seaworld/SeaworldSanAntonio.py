#!/usr/bin/env python
from amusement.parks.seaworld.SeaworldPark import SeaworldPark

class SeaworldSanAntonio(SeaworldPark):
    def __init__(self):
        super(SeaworldSanAntonio, self).__init__()

    def getId(self):
        return 'SW_SAT'

    def getName(self):
        return 'Seaworld San Antonio'
