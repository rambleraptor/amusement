#!/usr/bin/env python
from SeaworldPark import SeaworldPark

class SeaworldOrlando(SeaworldPark):
    def __init__(self):
        super(SeaworldOrlando, self).__init__()

    def getId(self):
        return 'SW_MCO'

    def getName(self):
        return 'Seaworld Orlando'
