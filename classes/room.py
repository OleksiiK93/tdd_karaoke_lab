class Room:
    def __init__(self, name, capacity, fee) -> None:
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.songs = set()
        self.guests = list()
        self.drinks = {
            'gin': 4.0,
            'whisky': 4.50,
            'cola': 2.0
        }
        self.bookings = dict()
    
    def check_in(self, guest):
        if len(self.guests) < self.capacity and guest.wallet >= self.fee:
            guest.check_songs(self)
            guest.pay_fee(self)
            self.guests.append(guest)            
    
    def check_out(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.add(song)

    def get_spending(self, guest):
        return guest.spending
    
    def create_booking(self, guest, datetime):
        if datetime not in self.bookings:
            self.bookings[datetime] = guest