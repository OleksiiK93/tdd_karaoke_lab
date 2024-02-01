class Guest:
    def __init__(self, name, phone_number, wallet) -> None:
        self.name = name
        self.phone_number = phone_number
        self.wallet = wallet

    def pay_fee(self, room):
        if self.wallet >= room.fee:
            self.wallet -= room.fee