import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_name = Room("Mercury Room")
        self.guest_1 = Guest("Michael Jackson", 37)
        self.guest_2 = Guest("Boris Johnson", 72)
        self.guest_3 = Guest("Maggie Thatcher", 104)
        self.song_1 = Song("Final Countdown", "Europe")
        self.song_2 = Song("Smells Like Teen Spirit", "Nirvana")
        self.song_3 = Song("Ruby Tuesday", "The Rolling Stones")

    # ROOM

    def test_room_has_name(self):
        self.assertEqual("Mercury Room", self.room_name.room_name)

    # GUEST_LIST

    def test_room_is_empty(self):
        self.assertEqual(0, self.room_name.guest_count())

    def test_can_check_in_guest(self):
        self.room_name.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_name.guest_count())

    def test_can_check_out_guest(self):
        self.room_name.check_in_guest(self.guest_1)
        self.room_name.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room_name.guest_count())
    
    # PLAY_LIST

    def test_playlist_is_empty(self):
        self.assertEqual(0, self.room_name.song_count())

    def test_can_add_song(self):
        self.room_name.add_song(self.song_1)
        self.assertEqual(1, self.room_name.song_count())

    def test_can_remove_song(self):
        self.room_name.add_song(self.song_2)
        self.room_name.remove_song(self.song_2)
        self.assertEqual(0, self.room_name.song_count())


        


    