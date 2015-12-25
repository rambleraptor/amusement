#!/usr/bin/env python
from SeaworldPark import SeaworldPark

class SeaworldSanDiego(SeaworldPark):
    def __init__(self):
        super(SeaworldSanDiego, self).__init__()

    def getId(self):
        return 'SW_SAN'
