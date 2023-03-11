import unittest
from classes.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Satisfaction", "The Rolling Stones")
        self.song_2 = Song("Living on a Prayer", "Bon Jovi")
        self.song_3 = Song("Wonderwall", "Oasis")

    def test_song_has_name(self):
        self.assertEqual("Satisfaction", self.song_1.song_name)

    def test_song_has_artist(self):
        self.assertEqual("The Rolling Stones", self.song_1.artist_name)