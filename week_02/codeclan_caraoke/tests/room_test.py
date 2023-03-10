import unittest
from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Mercury Room")

    def test_room_has_name(self):
        self.assertEqual("Mercury Room", self.room.name)