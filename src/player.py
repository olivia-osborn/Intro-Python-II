# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_location, items):
        self.name = name
        self.current_location = current_location
        self.item_bag = []

    def pick_up(self, item):
        self.item_bag.append(item)
