import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.song_1 = Song('White Rabbit', 'Jefferson Airplane', 'Rock', 1967)
        self.song_2 = Song('My Generation', 'The Who', 'Rock', 1965)
        self.song_3 = Song('Stand!', 'Sly and the Family Stone', 'Soul', 1969)
        self.guest_1 = Guest('Oleksii', '07756593890', 24.00)
        self.guest_2 = Guest('Ana', '07756593891', 15.0)
        self.guest_3 = Guest('Bob', '07756793890', 21.50)
        self.room = Room('Woodstock', 2, 15.0)

    
    def test_initialization(self):
        self.assertEqual('Woodstock', self.room.name)
        self.assertEqual(2, self.room.capacity)
        self.assertEqual(0, len(self.room.songs))
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_check_in_guest(self):
        self.room.check_in(self.guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_room_cannot_add_guests_when_at_capacity(self):
        self.room.check_in(self.guest_1)
        self.room.check_in(self.guest_2)
        self.room.check_in(self.guest_3)
        self.assertEqual(2, len(self.room.guests))

    def test_room_can_check_out_guest(self):
        self.room.check_in(self.guest_1)
        self.room.check_out(self.guest_1)
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, len(self.room.songs))
    
    def test_room_cannot_check_in_poor_customer(self):
        poor_customer = Guest("Matt", "99984849", 11.0)
        self.room.check_in(poor_customer)
        self.assertEqual(0, len(self.room.guests))
        self.assertEqual(11.0, poor_customer.wallet)