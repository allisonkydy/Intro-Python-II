
class Item:
    def __init__(self, name, description, is_gettable, location_desc=None):
        self.name = name
        self.description = description
        self.is_gettable = is_gettable
        self.location_desc = location_desc

    def on_take(self):
        print(f"You pick up the {self.name}")

    def on_drop(self):
        print(f"You drop the {self.name}")


class LightSource(Item):
    def __init__(self, name, description, is_gettable, location_desc):
        super().__init__(name, description, is_gettable, location_desc)
        self.is_lit = False

    def on_drop(self):
        print("It's unwise to drop your source of light")
        print(f"You drop the {self.name}")

class LockedItem(Item):
    def __init__(self, name, description, is_gettable, location_desc):
        super().__init__(name, description, is_gettable, location_desc)
        self.is_locked = True
        self.key = None

