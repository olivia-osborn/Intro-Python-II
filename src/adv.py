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


def drop_item(item):
    if item in player.item_bag:
        player.drop_item(item)
        player.current_location.add_item(item)
        print(f"You dropped {item}!")
    else:
        print("That item is not in your bag")


def get_item(item):
    if item in player.current_location.item_list:
        player.current_location.remove_item(item)
        player.pick_up(item)
        print(f"You picked up {item}! (type 'drop item' to drop this item")
    else:
        print("That item is not in the room")


def item_handler(items):
    if len(items) > 0:
        print("You find the following items in the room: ")
        for i in items:
            print(i)
        item_response = input(
            "Type 'get item' to pick up item, or press 'enter' to skip: ")
        if len(item_response) > 0:
            split_response = item_response.split()
            cmd = split_response[0]
            item_name = split_response[1]
            if cmd == "get":
                get_item(item_name)
                item_handler(items)
            elif cmd == "drop":
                get_item(item_name)
                item_handler(items)
            else:
                print("Type in a valid command: 'get', 'drop', or press 'enter' to skip")
                item_handler(items)


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
