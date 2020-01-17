from room import Room
from player import Player
from item import Item, LightSource, LockedItem

# Declare all the rooms

room = {
    'shack':  Room("Shack",
                   """The thin wooden walls are rotting and the floor is nothing but dirt. 
It smells pretty bad in here. Light filters in from the door to the south.""",
                   True),

    'garden':    Room("Overgrown Garden", """It used to be a garden, but weeds have sprung up between the neatly planted rows. 
The air carries a light floral fragrance. You hear the rustling of chickens to the west. 
An iron gate guards the path east. To the south is a large forest. The small shack is just north.""",
                      True),

    'coop': Room("Chicken Coop", """Cozy stalls hold about twenty dozing chickens. They look well-fed and content. 
East is the door to the garden.""",
                 True),

    'ruins':   Room("Ancient Ruins", """Smooth, mossy rocks are scattered about. Some are still loosely connected, 
forming the remains of a circular tower.""",
                    True),

    'forest': Room("Forest", """Trees tower over your head and the floor is thick with underbrush. 
The canopy blocks out all light from above. You try not to look directly at the shadows. 
A faint bubbling sound comes from the south. A small dirt path leads west.""",
                   False),

    'glen':   Room("Secluded Glen", """Mossy rocks slope gently down to a narrow stream. 
The air is cool and damp. The path bends from east to south.""",
                   True),

    'river':   Room("River", """The river bubbles excitedly, flowing from east to west. 
A small cluster of lily pads clings to rocks in the shallows.""",
                    True),

    'cliff':   Room("Tall Cliff", """Water cascades down from the cliff with a dull roar. 
You squint your eyes against the spray. The path stretches to the north and south.""",
                        True),

    'cave':   Room("Secret Cave", """Aha, a hidden cave! The walls seem to glow with a faint light. 
Water drops gently from cracks in the ceiling. The entrance is to the north.""",
                   True),
}


# Link rooms together

room['shack'].s_to = room['garden']
room['garden'].n_to = room['shack']
room['garden'].w_to = room['coop']
room['garden'].e_to = 'locked'
room['garden'].s_to = room['forest']
room['coop'].e_to = room['garden']
room['forest'].n_to = room['garden']
room['forest'].w_to = room['glen']
room['forest'].s_to = room['river']
room['river'].n_to = room['forest']
room['glen'].e_to = room['forest']
room['glen'].s_to = room['cliff']
room['cliff'].s_to = 'locked'
room['cliff'].n_to = room['glen']
room['cave'].n_to = room['cliff']
room['ruins'].w_to = room['garden']


# Declare items

item = {
    'wood': Item('wood', "A plank of soft wood, perfect for carving", True, "A fresh plank of wood leans against the far wall."),
    'lantern': LightSource('lantern', "It's one of those vintage ones that burn oil.", True, "A lantern sits in the corner."),
    'egg': Item('egg', "Brown with some dark speckles", True, "An egg sits in one of the empty nests."),
    'knife': Item('knife', "The blade is short, but sharp.", True, "A sharp knife pokes out from under a bush."),
    'oil': Item('oil', "A small canister of oil", False, "There's an oil canister where the chicken was sitting."),
    'mushroom': Item('mushroom', "A little brown mushroom", True, "A single mushroom pokes out of an old stump."),
    'beaver': LockedItem('beaver', "It won't stop chattering.", False, "There's a beaver on the far bank. It's chattering nervously."),
    'flute': Item('flute', "A hand-carved wooden flute. It's a little out of tune.", True, "A wooden flute lies on the ground."),
    'lily': Item('lily', "A beautiful white water lily", True, "You see a lily in bloom on the lily pads."),
    'key': Item('key', "An old iron key. It's a bit rusty.", True, "A single key lies at the bottom of a shallow pool."),
    'chicken': Item('chicken', "It stares at you blankly. It must be hiding something...", False, "One of the chickens is awake and looks at you intently."),
    'gate': LockedItem('gate', "A large, imposing wrought-iron gate. It's closed and locked.", False, "The gate is closed and locked."),
    'river': Item('river', "Shallow and rocky. The water foams and bubbles and it flows by.", False, "The river flows by."),
    'waterfall': Item('waterfall', "It's falling at a tremendous rate. It could crush you easily.", False, "The large waterfall blocks your path in the southern direction."),
    'dam': Item('dam', "Built with love from sticks and mud", False, "A large dam blocks the flow of the river."),
    'pedastel': LockedItem('pedastel', "It's covered in strange markings. On its surface is an oblong indentation.", False, "An engraved pedastel lies in the center of the tower."),
}

# Add items to rooms

room['shack'].add_item(item['wood'])
room['shack'].add_item(item['lantern'])
room['garden'].add_item(item['mushroom'])
room['garden'].add_item(item['gate'])
room['coop'].add_item(item['egg'])
room['coop'].add_item(item['chicken'])
room['forest'].add_item(item['knife'])
room['glen'].add_item(item['beaver'])
room['river'].add_item(item['lily'])
room['river'].add_item(item['river'])
room['cliff'].add_item(item['waterfall'])
room['cave'].add_item(item['key'])
room['ruins'].add_item(item['pedastel'])

# Add keys to locks

item['beaver'].key = item['flute']
item['gate'].key = item['key']
item['pedastel'].key = item['egg']


# Define actions

class Actions:
    def __init__(self, player):
        self.player = player
        self.result = None

    def oil_lantern(self, oil, lantern):
        self.player.remove_item(oil)
        self.player.is_lit = True
        lantern.light_on()
        print("You fill the lantern with oil.\nThe lantern is now lit.")

    def knife_wood(self, knife, wood):
        self.player.remove_item(knife)
        self.player.remove_item(wood)
        self.player.add_item(item['flute'])

        display_string = ""
        display_string += "You start carving the soft wood with the knife."
        display_string += "\nA mysterious creative energy guides your hand."
        display_string += "\nYou are compelled to whittle a flute. It plays a calming tune."
        print(display_string)

    def mushroom_chicken(self, mushroom, chicken):
        self.player.remove_item(mushroom)
        self.player.current_room.remove_item(chicken)
        self.player.current_room.add_item(item['oil'])
        item['oil'].is_gettable = True

        display_string = ""
        display_string += "You offer the mushroom to the chicken."
        display_string += "\nThe chicken snatches it out of your hand and gobbles it up in two quick gulps."
        display_string += "\nIt bends its head to you in a deep bow and flaps its wings as it rushes out of the coop."
        display_string += "\nYou try to see where it's headed, but all you see is the garden, deserted."
        display_string += "\nA small canister of oil sits where the chicken was nesting."
        print(display_string)

    def flute_beaver(self, flute, beaver):
        beaver.is_locked = False
        beaver.description = "It looks at you expectantly."
        beaver.location_desc = "The beaver sits on a rock near you."
        print("The beaver is drawn to the sound of the flute. It looks friendly now.")

    def lily_beaver(self, lily, beaver):
        beaver.is_gettable = True
        self.player.remove_item(lily)
        beaver.description = "It chatters playfully."
        beaver.location_desc = "The beaver is right at your feet, thumping its tail with excitement."

        display_string = ""
        display_string += "You offer the water lily to the beaver."
        display_string += "\nThe beaver sniffs at it then eats it right out of your hand."
        display_string += "\nIts eyes are filled with trust. It will follow you anywhere."
        print(display_string)

    def beaver_river(self, beaver, river):
        self.player.current_room.add_item(beaver)
        self.player.remove_item(beaver)
        beaver.is_gettable = False
        beaver.is_locked = False
        beaver.description = "It's resting happily."
        beaver.location_desc = "The beaver is sitting on top of the dam"
        self.player.current_room.add_item(item['dam'])
        room['cliff'].remove_item(item['waterfall'])
        room['cliff'].s_to = room['cave']
        room['cliff'].description = """The cliff towers above you, silent and serene. A small trickle of water runs 
down its face. There's a small opening in the rock where the waterfall once was. 
The path stretches to the north and south."""
        river.description = "Shallow and rocky. It's blocked by the beavers' dam."
        river.location_desc = "The river no longer flows."
        room['river'].description = """A large beaver dam spans the river, stopping the flow. 
A small cluster of lily pads clings to rocks in the shallows."""

        display_string = ""
        display_string += "You place the beaver in the river."
        display_string += "\nIt chatters rapidly. A large group of beavers emerges from the surrounding woods."
        display_string += "\nYou feel something hit your head. You collapse on the river bank."
        display_string += "\nWhen you wake up, the beaver is sitting alone atop a large dam."
        display_string += "\nThe dam completely blocks the flow of the river."
        print(display_string)

    def key_gate(self, key, gate):
        self.player.remove_item(key)
        gate.is_locked = False
        room['garden'].e_to = room['ruins']
        gate.description = "A large, imposing wrought-iron gate. It's swung open."
        gate.location_desc = "The gate is open."

        display_string = ""
        display_string += "You insert the key into the lock."
        display_string += "\nThe gate swings open with a groan."
        print(display_string)

    def egg_pedastel(self, egg, pedastel):
        pedastel.is_locked = False
        self.player.remove_item(egg)
        self.player.current_room.add_item(egg)

        display_string = ""
        display_string += "You insert the egg into the indentation on the pedastel."
        display_string += "\nYour hands glow blue for a few seconds, then return to normal."
        display_string += "\nThe pedastel starts to vibrate, slowly at first, then faster and faster until"
        display_string += "\nit stops abruptly with the sound of a gong. You pick up the egg and gently tap"
        display_string += "\nthe shell against the worn stone. A perfect hard boil. You groan."
        display_string += "\n\nYou hate hard-boiled eggs."
        print(display_string)

        self.result = 'good end'


# Controls

controls = """
    Controls:

    move using 'n', 's', 'e', 'w'
    'get [item]' or 'take [item]' to pick up items
    'drop [item]' to drop items
    'look' or 'l' to look around
        you can also 'look [item]'
    'use [item] on [item]' to use an item
    'inventory' or 'i' to see what you're carrying
    'help' or 'h' to view controls
    'quit' or 'q' to quit the game
"""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def main():

    # make a new player that is currently in the shack
    player = Player(input("\n\nEnter your name: "), room['shack'])

    # Ending screens

    good_end = f"\n\n\n\n\n\nYou reached the end, {player.name}. You survived.\n\nI hope you enjoyed yourself.\n\n\n\n"
    # bad_end = ""

    actions = Actions(player)

    directions = ('n', 's', 'e', 'w')

    print("\n   Welcome to...\n")
    print("""
     _   _                                     _   
    | |_(_)_ __  _   _    __ _ _   _  ___  ___| |_ 
    | __| | '_ \| | | |  / _` | | | |/ _ \/ __| __|
    | |_| | | | | |_| | | (_| | |_| |  __/\__ \ |_ 
     \__|_|_| |_|\__, |  \__, |\__,_|\___||___/\__|
                 |___/      |_|                    
""")
    print(controls)

    while True:
        # check if player has reached an end state
        if actions.result == 'good end':
            print(good_end)
            break
        # elif actions.result == 'bad end':

        current_room = player.current_room

        # if the current room is lit or the player has a light source that is lit
        if player.is_player_or_room_lit():
            print(player.current_room)

        else:
            display_string = ""
            display_string += "\n---------------------------------------------------------------------------\n"
            display_string += "\nIt's pitch black. You hear strange whispers coming from the darkness...\n\n"
            print(display_string)

        # wait for user input
        user_input = input(">>> ")
        input_length = len(user_input.split(' '))

        if input_length > 1:
            user_input = user_input.split(' ')

        print("\n---------------------------------------------------------------------------\n\n")

        # if the form of the input is 'verb'
        if input_length == 1:
            # if user enters a cardinal direction, attempt to move there
            if user_input in directions:
                player.change_room(user_input)

            # print list of items in room if player looks around ('l' or 'look')
            elif user_input == 'l' or user_input == 'look':
                current_room.print_items()

            # show list of items in inventory if player enters 'i' or 'inventory'
            elif user_input == 'i' or user_input == 'inventory':
                player.print_inventory()

            # show controls if 'help' or 'h' entered
            elif user_input == 'h' or user_input == 'help':
                print(controls)

            # if user enters q, quit the game
            elif user_input == 'q':
                print(f"Thank you for playing, {player.name}")
                break

            # print error message if user enters invalid input
            else:
                print("Input not valid, please try again")

        # if the form of the input is 'verb object'
        elif input_length == 2:
            verb = user_input[0]
            object_name = user_input[1]

            if not object_name in item:
                print("That item does not exist")

            # pick up item: supports 'get' and 'take'
            elif verb == 'get' or verb == 'take':
                player.take_item(item[object_name])

            # drop item
            elif verb == 'drop':
                player.drop_item(item[object_name])

            # look at item
            elif verb == 'look' or verb == 'l':
                player.look_item(item[object_name])

            # error message for improper usage of 'use'
            elif verb == 'use':
                print("What should I use this on?")

            # print error message if user enters invalid input
            else:
                print("Input not valid, please try again")

        # if the form of the input is 'use [item] on [item]'
        elif input_length == 4 and user_input[0] == "use" and user_input[2] == "on":
            item_used = user_input[1]
            item_target = user_input[3]

            # check if items exist
            if item_used in item and item_target in item:
                player.use_item_on_item(item[item_used], item[item_target], actions)

            else:
                print("Whoops, that won't work")

        # print error message if user enters invalid input
        else:
            print("Too many words, please try again")

        print()



if __name__ == '__main__':
    main()
