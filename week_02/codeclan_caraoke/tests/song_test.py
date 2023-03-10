import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Final Countdown")

    def test_song_has_name(self):
        self.assertEqual("Final Countdown", self.song.name)