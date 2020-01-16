
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You picked up the {self.name}")

    def on_drop(self):
        print(f"You dropped the {self.name}")


class LightSource(Item):
    def __init__(self, name, description, is_lit):
        super().__init__(name, description)
        self.is_lit = is_lit

    def on_drop(self):
        print("It's unwise to drop your source of light")
        print(f"You dropped the {self.name}")

class UsableItem(Item):
    def __init__(self, name, description, used_on):
        super().__init__(name, description)
        self.used_on = used_on
        self.is_used = False
