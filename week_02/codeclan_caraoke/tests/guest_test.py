import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Michael Jackson", 37, 10)
        self.guest_2 = Guest("Boris Johnson", 72, 50)
        self.guest_3 = Guest("Maggie Thatcher", 104, 100)

    # GUEST ATTRIBUTES

    def test_guest_has_name(self):
        self.assertEqual("Michael Jackson", self.guest_1.guest_name)

    def test_guest_has_age(self):
        self.assertEqual(37, self.guest_1.guest_age)

    def test_guest_has_cash(self):
        self.assertEqual(10, self.guest_1.guest_cash)