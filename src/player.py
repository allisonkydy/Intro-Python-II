# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.is_lit = False

    def change_room(self, new_room):
        self.current_room = new_room

    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        self.inventory.remove(item)

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("You're not carrying anything")
        else:
            print(f"You're carrying: {', '.join([item.name for item in self.inventory])}")