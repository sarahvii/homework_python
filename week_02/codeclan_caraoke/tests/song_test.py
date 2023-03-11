import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Final Countdown", "Europe")

    def test_song_has_name(self):
        self.assertEqual("Final Countdown", self.song.song_name)

    def test_song_has_artist(self):
        self.assertEqual("Europe", self.song.artist_name)