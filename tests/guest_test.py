import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.guest = Guest('Oleksii', '07756593890')
    
    def test_initialization(self):
        self.assertEqual('Oleksii', self.guest.name)
        self.assertEqual('07756593890', self.guest.phone_number)