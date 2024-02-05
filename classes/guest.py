class Guest:
    def __init__(self, name, phone_number, wallet, fav_song) -> None:
        self.name = name
        self.phone_number = phone_number
        self.wallet = wallet
        self.fav_song = fav_song
        self.spending = 0.0

    def pay_fee(self, room):
        if self.wallet >= room.fee:
            self.wallet -= room.fee
            self.spending += room.fee

    def check_songs(self, room):
        if self.fav_song in room.songs:
            return "Whoo!"
        
    def buy_drink(self, room, drink):
        if self in room.guests and drink in room.drinks and self.wallet >= room.drinks[drink]:
            self.wallet -= room.drinks[drink]
            self.spending += room.drinks[drink]
