import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.song_1 = Song('White Rabbit', 'Jefferson Airplane', 'Rock', 1967)
        self.song_2 = Song('My Generation', 'The Who', 'Rock', 1965)
        self.song_3 = Song('Stand!', 'Sly and the Family Stone', 'Soul', 1969)
        self.guest_1 = Guest('Oleksii', '07756593890')
        self.room = Room('Woodstock', 3)

    
    def test_initialization(self):
        self.assertEqual('Woodstock', self.room.name)
        self.assertEqual(3, self.room.capacity)
        self.assertEqual(0, len(self.room.songs))
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_check_in_guest(self):
        self.room.check_in(self.guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_room_can_check_out_guest(self):
        self.room.check_in(self.guest_1)
        self.room.check_out(self.guest_1)
        self.assertEqual(0, len(self.room.guests))