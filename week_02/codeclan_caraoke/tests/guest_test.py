import unittest
from classes.guest import *
from classes.room import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Andy", 37, 10.00)
        self.guest_2 = Guest("Boris", 72, 50.00)
        self.guest_3 = Guest("Chris", 104, 100.00)

    # GUEST ATTRIBUTES

    def test_guest_has_name(self):
        self.assertEqual("Andy", self.guest_1.guest_name)

    def test_guest_has_age(self):
        self.assertEqual(37, self.guest_1.guest_age)

    def test_guest_has_cash(self):
        self.assertEqual(10.00, self.guest_1.guest_cash)

    # PAY ENTRY FEE

    # def test_customer_can_pay_entry_fee(self):
    #     entry_fee = Room("Room 1", 10.00, 100.00)
    #     self.guest_1.pay_entry_fee(entry_fee)
    #     self.assertEqual(5.00, self.guest_1.guest_cash)