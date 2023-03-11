import unittest
from classes.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Satisfaction", "The Rolling Stones")

    def test_song_has_name(self):
        self.assertEqual("Satisfaction", self.song.song_name)

    def test_song_has_artist(self):
        self.assertEqual("The Rolling Stones", self.song.artist_name)