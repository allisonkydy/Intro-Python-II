
class Item:
    def __init__(self, name, description, is_gettable, location_desc):
        self.name = name
        self.description = description
        self.is_gettable = is_gettable
        self.location_desc = location_desc

    def on_take(self):
        print(f"You pick up the {self.name}")

    def on_drop(self):
        self.location_desc = f"The {self.name} lies on the ground."
        print(f"You drop the {self.name}")


class LightSource(Item):
    def __init__(self, name, description, is_gettable, location_desc):
        super().__init__(name, description, is_gettable, location_desc)
        self.is_lit = False

    def on_drop(self):
        print("It's unwise to drop your source of light")
        print(f"You drop the {self.name}")

    def light_on(self):
        self.is_lit = True
        self.description += " It's currently lit."

class LockedItem(Item):
    def __init__(self, name, description, is_gettable, location_desc):
        super().__init__(name, description, is_gettable, location_desc)
        self.is_locked = True
        self.key = None

