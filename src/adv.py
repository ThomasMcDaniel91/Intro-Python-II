from room import Room
from player import Player
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def moving(valuetopair, search_dict=room):
    keys_list = []
    items_list = search_dict.items()
    for item in search_dict:
        if item[1] == valuetopair:
            keys_list.append(item[0])
    print(keys_list)

# Make a new player object that is currently in the 'outside' room.

player_1 = Player(input("Hello, what is your name?"), room['outside'])
player_1.starting_room = room['outside']

print(player_1.current_room)
print(moving(player_1.current_room))
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# running = True

# while running:
#     print(f"Hello {player_1.p_name}, your current location is {player_1.current_room}")
#     movement = input('Which direction would you like to go? (north, south, east or west)')
#     if movement == 'q':
#         running = False
    # if movement == 'north':
    #     player_1.current_room = 