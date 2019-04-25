from player import Player
from item import Item
from room import Room
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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['foyer'].add_item("boots")
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Jack", room["outside"], [])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# while True:
#     print(f"You are currently in the {player.current_location.name}")
#     print(player.current_location.description)
#     direction = input(
#         "Which direction would you like to go? (enter n, e, s, or w):")
#     if direction == "n" or "e" or "s" or "w":
#         if player.current_location.direction is None:
#             print("You cannot go that way. Choose another direction!")
#         else:
#             player.current_location = player.current_location.direction
#     elif direction == "q":
#         print("Thanks for playing!")
#         break
#     else:
#         print("please enter n, e, s, or w to switch rooms, or press q to quit!")

possibleDirections = ["n", "e", "s", "w"]


def item_handler(items):
    if len(items) > 0:
        print("You find the following items in the room:")
        for i in items:
            print(i)
        item_response = input("Enter the item you want")
        if item_response in items:
            player.current_location.remove_item(item_response)
            player.pick_up(item_response)
            item_handler(items)
            print(f"You picked up {item_response}!")
        else:
            print("no item named that")
            item_handler(items)
    else:
        print("no more items!")


while True:
    print(f"You are currently in the {player.current_location.name}")
    print(player.current_location.description)
    item_handler(player.current_location.item_list)
    direction = input(
        "Which direction would you like to go? (enter n, e, s, or w):")
    if direction == "n":
        if player.current_location.n_to is not None:
            player.current_location = player.current_location.n_to
        else:
            print("You cannot go that way! Choose another direction!")
    elif direction == "e":
        if player.current_location.e_to is not None:
            player.current_location = player.current_location.e_to
        else:
            print("You cannot go that way! Choose another direction!")
    elif direction == "s":
        if player.current_location.s_to is not None:
            player.current_location = player.current_location.s_to
        else:
            print("You cannot go that way! Choose another direction!")
    elif direction == "w":
        if player.current_location.w_to is not None:
            player.current_location = player.current_location.w_to
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
