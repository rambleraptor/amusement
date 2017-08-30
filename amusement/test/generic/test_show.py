import unittest

from amusement.show import Show

class ShowTestCase(unittest.TestCase):
    
    def test_showtimeKey(self):
        show_obj = Show()
        self.assertEqual('showtimes' in show_obj.attributes(), True)

    def test_addTime(self):
        show_obj = Show()
        show_obj.addTime('12:00 PM')
        self.assertEqual(len(show_obj.getTimes()), 1)

