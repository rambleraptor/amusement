#!/usr/bin/env python
from amusement.parks.disney.DisneyPark import DisneyPark
class HollywoodStudios(DisneyPark):

    def __init__(self):
        super(HollywoodStudios, self).__init__()

    def getId(self):
        return '80007998'

    def getName(self):
        return "Disney's Hollywood Studios"
