import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Michael Jackson")

    def test_guest_has_name(self):
        self.assertEqual("Michael Jackson", self.guest.name)