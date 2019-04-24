from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["sword"]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["helmet", "gloves"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["bread", "boots"]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["shield"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Jack", room["outside"], [])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    print(f"You are currently in the {player.current_location.name}")
    print(player.current_location.description)
    direction = input(
        "Which direction would you like to go? (enter n, e, s, or w):")
    if direction == "n" or "e" or "s" or "w":
        if player.current_location.direction is not None:
            player.current_location = player.current_location.direction
        else:
            print("You cannot go that way! Choose another direction!")
    elif direction == "q":
        print("Thanks for playing!")
        break
    else:
        print("please enter n, e, s, or w to switch rooms, or press q to quit!")
# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
