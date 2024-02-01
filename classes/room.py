class Room:
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity
        self.songs = set()
        self.guests = list()
    
    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
    
    def check_out(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.add(song)