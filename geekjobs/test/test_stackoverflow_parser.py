import unittest
from geekjobs.stackoverflow_parser import _check_stackoverflow_json


class SimpleTest(unittest.TestCase):
    def test__check_stackoverflow_json(self):
        self.assertFalse(_check_stackoverflow_json(dict()))
        data = {'DE': '', 'UK': ''}
        self.assertFalse(_check_stackoverflow_json(data))
        data = {'DE': list(), 'UK': list()}
        self.assertFalse(_check_stackoverflow_json(data))
        data = {'DE': [], 'UK': []}
        self.assertFalse(_check_stackoverflow_json(data))
        data = {'DE': None, 'UK': None}
        self.assertFalse(_check_stackoverflow_json(data))




