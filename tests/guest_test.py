import unittest
from datetime import datetime
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.song_1 = Song('White Rabbit', 'Jefferson Airplane', 'Rock', 1967)
        self.song_2 = Song('My Generation', 'The Who', 'Rock', 1965)
        self.song_3 = Song('Stand!', 'Sly and the Family Stone', 'Soul', 1969)
        self.guest = Guest('Oleksii', '07756593890', 30.0, self.song_3)
        self.room = Room('Woodstock', 2, 15.0)
    
    def test_initialization(self):
        self.assertEqual('Oleksii', self.guest.name)
        self.assertEqual('07756593890', self.guest.phone_number)
        self.assertEqual(30.0, self.guest.wallet)
        self.assertEqual('Stand!', self.guest.fav_song.title)
        self.assertEqual(0.0, self.guest.spending)

    def test_guest_can_pay_room_fee(self):
        self.guest.pay_fee(self.room)
        self.assertEqual(15.0, self.guest.wallet)
        self.assertEqual(15.0, self.guest.spending)

    def test_guest_cheers_if_their_fav_song_is_in_room(self):
        self.room.add_song(self.song_3)
        self.assertEqual("Whoo!", self.guest.check_songs(self.room))
    
    def test_guest_can_buy_drink(self):
        self.room.check_in(self.guest)
        self.guest.buy_drink(self.room, 'gin')
        self.assertEqual(11.0, self.guest.wallet)
        self.assertEqual(19.0, self.guest.spending)