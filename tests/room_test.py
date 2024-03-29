import unittest
from datetime import datetime

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.song_1 = Song('White Rabbit', 'Jefferson Airplane', 'Rock', 1967)
        self.song_2 = Song('My Generation', 'The Who', 'Rock', 1965)
        self.song_3 = Song('Stand!', 'Sly and the Family Stone', 'Soul', 1969)
        self.guest_1 = Guest('Oleksii', '07756593890', 24.00, self.song_1)
        self.guest_2 = Guest('Ana', '07756593891', 15.0, self.song_1)
        self.guest_3 = Guest('Bob', '07756793890', 21.50, self.song_1)
        self.room = Room('Woodstock', 2, 15.0)

    
    def test_initialization(self):
        self.assertEqual('Woodstock', self.room.name)
        self.assertEqual(2, self.room.capacity)
        self.assertEqual(0, len(self.room.songs))
        self.assertEqual(0, len(self.room.guests))
        self.assertEqual(3, len(self.room.drinks))

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
        poor_customer = Guest("Matt", "99984849", 11.0, self.song_1)
        self.room.check_in(poor_customer)
        self.assertEqual(0, len(self.room.guests))
        self.assertEqual(11.0, poor_customer.wallet)
    
    def test_room_can_keep_track_of_guests_spending(self):
        self.room.check_in(self.guest_1)
        self.guest_1.buy_drink(self.room, 'cola')
        self.assertEqual(17.0, self.room.get_spending(self.guest_1))

    def test_room_can_be_booked(self):
        self.room.create_booking(self.guest_1, datetime(2024, 2, 9, 19, 0))
        self.assertEqual(1, len(self.room.bookings))

    def test_room_cannot_be_booked_if_time_unavailable(self):
        self.room.create_booking(self.guest_1, datetime(2024, 2, 9, 19, 0))
        self.room.create_booking(self.guest_3, datetime(2024, 2, 9, 19, 30))
        self.room.create_booking(self.guest_2, datetime(2024, 2, 9, 19, 0))
        self.assertEqual(2, len(self.room.bookings))        