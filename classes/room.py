class Room:
    def __init__(self, name, capacity, fee) -> None:
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.songs = set()
        self.guests = list()
    
    def check_in(self, guest):
        if len(self.guests) < self.capacity and guest.wallet >= self.fee:
            guest.check_songs(self)
            guest.pay_fee(self)
            self.guests.append(guest)
    
    def check_out(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.add(song)