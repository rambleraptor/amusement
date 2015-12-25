#!/usr/bin/env python
from SeaworldPark import SeaworldPark

class BuschGardensTampa(SeaworldPark):
    def __init__(self):
        super(BuschGardensTampa, self).__init__()

    def getId(self):
        return 'BG_TPA'
