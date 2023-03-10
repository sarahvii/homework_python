import unittest
from classes.venue import *

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke")

    def test_venue_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)