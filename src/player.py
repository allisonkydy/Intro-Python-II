# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

wrapper = textwrap.TextWrapper(initial_indent="    ", subsequent_indent="    ")

from item import LightSource, LockedItem


class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.prev_room = None
        self.inventory = []
        self.is_lit = False

    def change_room(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)

        if next_room is not None :
            if next_room != 'locked':
                if (self.current_room.is_lit or self.is_lit) or next_room == self.prev_room:
                    self.prev_room = self.current_room
                    self.current_room = next_room
                    
                    if direction == 'n':
                        print(wrapper.fill("You move north"))
                    elif direction == 's':
                        print(wrapper.fill("You move south"))
                    elif direction == 'e':
                        print(wrapper.fill("You move east"))
                    elif direction == 'w':
                        print(wrapper.fill("You move west"))

                else:
                    print(wrapper.fill("It's too dark to see that way"))
            else:
                print(wrapper.fill("Your path is blocked"))
        else:
            print(wrapper.fill("You cannot move in that direction"))

    def remove_item(self, item):
        self.inventory.remove(item)

    def add_item(self, item):
        self.inventory.append(item)

    def take_item(self, item):
        # check if room or player is lit
        if self.is_player_or_room_lit():
            # check if item is in the room
            if item in self.current_room.items:
                # check if item is gettable
                if item.is_gettable:
                    # remove from room and add to player's inventory
                    self.current_room.remove_item(item)
                    self.inventory.append(item)
                    item.on_take()
                    # light up player if item is a lit light source
                    if isinstance(item, LightSource) and item.is_lit:
                        self.is_lit = True
                else:
                    print(wrapper.fill("You can't get that right now"))

            else:
                print(wrapper.fill("There is no such thing here"))

        else:
            print(wrapper.fill("Good luck finding that in the dark"))

    def drop_item(self, item):
        # check if item is in inventory
        if item in self.inventory:
            # add to room and remove from inventory
            self.current_room.add_item(item)
            self.inventory.remove(item)
            item.on_drop()
            # darken player if item is a lit light source
            if isinstance(item, LightSource) and item.is_lit:
                self.is_lit = False
        else:
            print(wrapper.fill("You don't have that in your inventory"))

    def print_inventory(self):
        if len(self.inventory) == 0:
            print(wrapper.fill("You're not carrying anything"))
        else:
            print(
                f"You're carrying: {', '.join([item.name for item in self.inventory])}")

    def is_player_or_room_lit(self):
        if self.is_lit or self.current_room.is_lit:
            return True
        return False

    def look_item(self, item):
        # if the item is in the room or the player's inventory, print the description
        if item in self.current_room.items or item in self.inventory:
            print(wrapper.fill(item.description))
        else:
            print(wrapper.fill("You don't see that"))

    def use_item_on_item(self, item_used, item_target, actions):
        # check if player has the item used
        if item_used in self.inventory:
            # check that target item is not locked
            if not isinstance(item_target, LockedItem) or not item_target.is_locked:
                # check if the item used can be used on the target item
                if hasattr(actions, f"{item_used.name}_{item_target.name}"):
                    getattr(actions, f"{item_used.name}_{item_target.name}")(item_used, item_target)

                else:
                    print(wrapper.fill("That's not a good idea"))
            elif item_target.is_locked and item_target.key is item_used:
                getattr(actions, f"{item_used.name}_{item_target.name}")(item_used, item_target)
            else:
                item_target.print_locked_message()
        else:
            print(wrapper.fill("You don't have that"))
