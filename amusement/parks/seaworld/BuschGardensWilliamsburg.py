#!/usr/bin/env python
from amusement.parks.seaworld.SeaworldPark import SeaworldPark

class BuschGardensWilliamsburg(SeaworldPark):
    def __init__(self):
        super(BuschGardensWilliamsburg, self).__init__()

    def getId(self):
        return 'BG_PHF'

    def getName(self):
        return 'Busch Gardens Williamsburg'
