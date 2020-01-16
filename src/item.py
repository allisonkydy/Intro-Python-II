
class Item:
    def __init__(self, name, description, is_interactable, is_gettable):
        self.name = name
        self.description = description
        self.is_interactable = is_interactable
        self.is_gettable = is_gettable

    def on_take(self):
        print(f"You picked up the {self.name}")

    def on_drop(self):
        print(f"You dropped the {self.name}")


class LightSource(Item):
    def __init__(self, name, description, is_interactable, is_gettable):
        super().__init__(name, description, is_interactable, is_gettable)
        self.is_lit = False

    def on_drop(self):
        print("It's unwise to drop your source of light")
        print(f"You dropped the {self.name}")

class UsableItem(Item):
    def __init__(self, name, description, is_interactable, is_gettable, used_on):
        super().__init__(name, description, is_interactable, is_gettable)
        self.used_on = used_on
