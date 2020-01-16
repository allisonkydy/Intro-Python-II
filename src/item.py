
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You picked up the {self.name}")

    def on_drop(self):
        print(f"You dropped the {self.name}")


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)