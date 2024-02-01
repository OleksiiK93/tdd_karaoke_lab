import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self) -> None:
        self.song = Song('White Rabbit', 'Jefferson Airplane', 'Rock', 1967)
    
    def test_initialization(self):
        self.assertEqual('White Rabbit', self.song.title)
        self.assertEqual('Jefferson Airplane', self.song.artist)
        self.assertEqual('Rock', self.song.genre)
        self.assertEqual(1967, self.song.released)