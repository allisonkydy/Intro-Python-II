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

    def __str__(self):
        display_string = ""
        display_string += "\n---------------------------------------------------------------------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        if len(self.items) == 0:
            print("Nothing to see here.")
        else:
            # print(f"You see: {', '.join([item.name for item in self.items])}")
            for item in self.items:
                print(item.location_desc)