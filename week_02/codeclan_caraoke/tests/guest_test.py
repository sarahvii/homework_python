import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Michael Jackson", 37)
        self.guest_2 = Guest("Boris Johnson", 72)
        self.guest_3 = Guest("Maggie Thatcher", 104)

    def test_guest_has_name(self):
        self.assertEqual("Michael Jackson", self.guest_1.guest_name)

    def test_guest_has_age(self):
        self.assertEqual(37, self.guest_1.guest_age)