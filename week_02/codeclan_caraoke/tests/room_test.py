import unittest
from classes.room import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Mercury Room")
        self.guest = Guest("Michael Jackson")

    def test_room_has_name(self):
        self.assertEqual("Mercury Room", self.room.name)

    def test_guests_in_room_empty(self):
        self.assertEqual(0, self.room.guest_count())

    def test_one_guest_in_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, self.room.guest_count())
    