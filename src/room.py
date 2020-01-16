# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_lit):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_lit = is_lit

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        if len(self.items) == 0:
            print("Nothing to see here.")
        else:
            print(f"You see: {', '.join([item.name for item in self.items])}")