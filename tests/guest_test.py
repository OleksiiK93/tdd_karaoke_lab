import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.guest = Guest('Oleksii', '07756593890', 15.0)
        self.room = Room('Woodstock', 2, 15.0)
    
    def test_initialization(self):
        self.assertEqual('Oleksii', self.guest.name)
        self.assertEqual('07756593890', self.guest.phone_number)
        self.assertEqual(15.0, self.guest.wallet)

    def test_guest_can_pay_room_fee(self):
        self.guest.pay_fee(self.room)
        self.assertEqual(0.0, self.guest.wallet)