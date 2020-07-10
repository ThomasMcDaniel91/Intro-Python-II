# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, p_name, current_room):
        self.p_name = p_name
        self.current_room = current_room

    def movement(self, command):
        attribute = command + '_to'

        if hasattr(self.current_room, attribute) == False:
            print('Sorry, you cannot go in that direction. Try another.\n')
            print()
            print()

        elif hasattr(self.current_room, attribute):

            self.current_room = getattr(self.current_room, attribute)
    def __str__(self):
        return f"You are {self.p_name}, your current location is {self.current_room}"

    # need to use hassttr and getattr to move player




