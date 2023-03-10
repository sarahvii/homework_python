import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Mercury Room")
        self.guest = Guest("Michael Jackson")

    def test_room_has_name(self):
        self.assertEqual("Mercury Room", self.room.name)

    def test_room_is_empty(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, self.room.guest_count())

    def test_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, self.room.guest_count())

        


    