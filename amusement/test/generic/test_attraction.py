import unittest
from nose.tools import *
from amusement.attraction import Attraction

class AttractionTest(unittest.TestCase):

    @raises(Exception)
    def test_invalidget(self):
        attr = Attraction()
        attr['invalid_name']

    @raises(Exception)
    def test_invalidset(self):
        attr = Attraction()
        attr['invalid_name'] = 'invalid_set'

    def test_setName(self):
        attr = Attraction()
        name = 'test_name'
        attr.setName(name)
        self.assertEquals(attr.getName(), name)

    def test_addKeys(self):
        key_name = 'newkey1'
        keys = [key_name]
        attr = Attraction()
        attr._addKeys(keys)
        attr[key_name]
        self.assertEquals(len(attr.attributes()), 2)
        
