import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_name_1 = Room("60's Room", 2)
        self.room_name_2 = Room("80's Room", 4)
        self.room_name_3 = Room("90's Room", 10)
        self.guest_1 = Guest("Michael Jackson", 37, 10)
        self.guest_2 = Guest("Boris Johnson", 72, 50)
        self.guest_3 = Guest("Maggie Thatcher", 104, 100)
        self.song_1 = Song("Final Countdown", "Europe")
        self.song_2 = Song("Smells Like Teen Spirit", "Nirvana")
        self.song_3 = Song("Ruby Tuesday", "The Rolling Stones")

    # ROOM

    def test_room_has_name(self):
        self.assertEqual("60's Room", self.room_name_1.room_name)

    # GUEST_LIST

    def test_room_is_empty(self):
        self.assertEqual(0, self.room_name_1.guest_count())

    def test_can_check_in_guest(self):
        self.room_name_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_name_1.guest_count())

    def test_can_check_out_guest(self):
        self.room_name_1.check_in_guest(self.guest_1)
        self.room_name_1.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room_name_1.guest_count())
    
    # PLAY_LIST

    def test_playlist_is_empty(self):
        self.assertEqual(0, self.room_name_1.song_count())

    def test_can_add_song(self):
        self.room_name_1.add_song(self.song_1)
        self.assertEqual(1, self.room_name_1.song_count())

    def test_can_remove_song(self):
        self.room_name_1.add_song(self.song_2)
        self.room_name_1.remove_song(self.song_2)
        self.assertEqual(0, self.room_name_1.song_count())

    # CAPACITY

    # def test_room_has_capacity(self):
    #     self.assertEqual(2, self.room_name_1.capacity)

    # def test_guest_list_less_than_capacity(self):
    #     self.room_name_1.check_in_guest(self.guest_1)
    #     self.assertEqual(True, )

    # ENTRY FEE


        


    