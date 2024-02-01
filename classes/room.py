class Room:
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity
        self.songs = set()
        self.guests = list()