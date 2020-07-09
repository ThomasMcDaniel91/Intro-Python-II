# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, p_name, current_room):
        self.p_name = p_name
        self.current_room = current_room

    def __str__(self):
        return f"You are {self.p_name}, your current location is {self.current_room}"




