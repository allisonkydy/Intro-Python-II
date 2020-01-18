import textwrap

wrapper = textwrap.TextWrapper(initial_indent="    ", subsequent_indent="    ")

class Item:
    def __init__(self, name, description, is_gettable, location_desc):
        self.name = name
        self.description = description
        self.is_gettable = is_gettable
        self.location_desc = location_desc

    def on_take(self):
        print(wrapper.fill(f"You pick up the {self.name}"))

    def on_drop(self):
        self.location_desc = f"The {self.name} lies on the ground."
        print(wrapper.fill(f"You drop the {self.name}"))


class LightSource(Item):
    def __init__(self, name, description, is_gettable, location_desc):
        super().__init__(name, description, is_gettable, location_desc)
        self.is_lit = False

    def on_drop(self):
        print(wrapper.fill("It's unwise to drop your source of light"))
        print(wrapper.fill(f"You drop the {self.name}"))

    def light_on(self):
        self.is_lit = True
        self.description += " It's currently lit."

class LockedItem(Item):
    def __init__(self, name, description, is_gettable, location_desc, locked_message):
        super().__init__(name, description, is_gettable, location_desc)
        self.is_locked = True
        self.key = None
        self.locked_message = locked_message

    def print_locked_message(self):
        print(wrapper.fill(self.locked_message))

