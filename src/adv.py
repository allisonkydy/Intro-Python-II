from room import Room
from player import Player
from item import Item, LightSource, UsableItem
from actions import Actions

# Declare all the rooms

room = {
    'shack':  Room("Shack",
                   """The thin wooden walls are rotting and the floor is nothing but dirt. 
It smells pretty bad in here. Light filters in from the door to the south.""",
                   True),

    'garden':    Room("Overgrown Garden", """It used to be a garden, but weeds have sprung up between the neatly planted rows. 
The air carries a light floral fragrance. You hear the rustling of chickens to the west. 
To the south is a large forest. A wrought-iron gate lies east. The small shack is just north.""",
                      True),

    'coop': Room("Chicken Coop", """Cozy stalls hold about twenty dozing chickens. They look well-fed and content. 
East is the door to the garden.""",
                 True),

    'ruins':   Room("Ancient Ruins", """Smooth, mossy rocks are scattered about. Some are still loosely connected, 
forming the remains of a circular tower. An engraved pedastel lies in the center of the tower. 
On its surface is an oblong indentation.""",
                    True),

    'forest': Room("Forest", """Trees tower over your head and the floor is thick with underbrush. 
The canopy blocks out all light from above. You try not to look directly at the shadows. 
A faint bubbling sound comes from the south. A small dirt path leads west.""",
                   False),

    'glen':   Room("Secluded Glen", """Mossy rocks slope gently down to a narrow stream. 
The air is cool and damp. The path bends from east to south.""",
                   True),

    'river':   Room("Bubbling River", """The river bubbles excitedly, flowing from east to west. 
A small cluster of lily pads clings to rocks in the shallows.""",
                    True),

    'waterfall':   Room("Waterfall", """Water cascades down from the cliff with a dull roar. 
You squint your eyes against the spray. The path stretches to the north.""",
                        True),

    'cave':   Room("Secret Cave", """Aha, a hidden cave! The walls seem to glow with a faint light. 
Water drops gently from cracks in the ceiling. The entrance is the to the north.""",
                   True),
}


# Link rooms together

room['shack'].s_to = room['garden']
room['garden'].n_to = room['shack']
room['garden'].w_to = room['coop']
room['garden'].e_to = room['ruins']
room['garden'].s_to = room['forest']
room['coop'].e_to = room['garden']
room['forest'].n_to = room['garden']
room['forest'].w_to = room['glen']
room['forest'].s_to = room['river']
room['river'].n_to = room['forest']
room['glen'].e_to = room['forest']
room['glen'].s_to = room['waterfall']
room['waterfall'].s_to = room['cave']
room['waterfall'].n_to = room['glen']
room['cave'].n_to = room['waterfall']
room['ruins'].w_to = room['garden']


# Declare items

item = {
    'wood': Item('wood', "A plank of soft wood, perfect for carving"),
    'lantern': LightSource('lantern', "It's one of those vintage ones that burn oil"),
    'egg': UsableItem('egg', "Brown with some dark speckles", ('pedastel')),
    'knife': UsableItem('knife', "The blade is short, but sharp", ('wood')),
    'oil': UsableItem('oil', "A small canister of oil", ('lantern')),
    'mushroom': Item('mushroom', "A little brown mushroom"),
    'beaver': UsableItem('beaver', "It won't stop chattering", ('river')),
    'flute': UsableItem('flute', "A hand-carved wooden flute. It's a little out of tune.", ('beaver')),
    'lily': UsableItem('lily', "A beautiful white water lily", ('beaver')),
    'key': UsableItem('key', "An old iron key. It's a bit rusty.", ('gate', 'lock')),
}

# Add items to rooms

room['shack'].add_item(item['wood'])
room['shack'].add_item(item['lantern'])
room['garden'].add_item(item['mushroom'])
room['coop'].add_item(item['egg'])
room['coop'].add_item(item['oil'])
room['forest'].add_item(item['knife'])
room['glen'].add_item(item['beaver'])
room['river'].add_item(item['lily'])
room['cave'].add_item(item['key'])

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
    player = Player(input("Enter your name: "), room['shack'])

    prev_room = None

    # actions = Actions()

    while True:
        current_room = player.current_room

        # if the current room is lit or the player has a light source that is lit
        if current_room.is_lit or player.is_lit:
            # print the current room name
            print(f"Current location: {current_room.name}")
            # print current room description
            print(current_room.description)
            
        else:
            print("It's pitch black. You hear strange whispers coming from the darkness...")

        # wait for user input
        user_input = input(">>> ")
        input_length = len(user_input.split(' '))

        if input_length > 1:
            user_input = user_input.split(' ')

        print()

        # if the form of the input is 'verb'
        if input_length == 1:
            directions = ('n', 's', 'e', 'w')
            # if user enters a cardinal direction, attempt to move there
            if user_input in directions:
                attempted_room = getattr(
                    current_room, f"{user_input}_to")
                # if movement is allowed, update the current room
                if attempted_room != None:
                    if (current_room.is_lit or player.is_lit) or attempted_room == prev_room:
                        player.change_room(attempted_room)
                        prev_room = current_room
                    else:
                        print("It's too dark to see that way")
                # print error message if movement is not allowed
                else:
                    print("You cannot move in that direction")

            # print list of items in room if player looks around ('l' or 'look')
            elif user_input == 'l' or user_input == 'look':
                current_room.print_items()

            # show list of items in inventory if player enters 'i' or 'inventory'
            elif user_input == 'i' or user_input == 'inventory':
                player.print_inventory()

            # if user enters q, quit the game
            elif user_input == 'q':
                break

            # print error message if user enters invalid input
            else:
                print("Input not valid, please try again")

        # if the form of the input is 'verb object'
        elif input_length == 2:
            verb = user_input[0]
            object_name = user_input[1]

            # pick up item: supports 'get' and 'take'
            if verb == 'get' or verb == 'take':
                # check if item is in the room
                if current_room.is_lit or player.is_lit:
                    if object_name in item and not item[object_name] in player.inventory:
                        i = item[object_name]
                        # remove from room and add to player's inventory
                        current_room.remove_item(i)
                        player.add_item(i)
                        i.on_take()
                        # light up player if item is a lit light source
                        if isinstance(i, LightSource) and i.is_lit:
                            player.is_lit = True

                    # print error message
                    else:
                        print("There is nothing called that here")
                else:
                    print("Good luck finding that in the dark")

            # drop item
            elif verb == 'drop':
                # check if item is in player's inventory
                if object_name in item and item[object_name] in player.inventory:
                    i = item[object_name]
                    # add to room and remove from inventory
                    current_room.add_item(i)
                    player.remove_item(i)
                    i.on_drop()
                    # darken player if item is a lit light source
                    if isinstance(i, LightSource) and i.is_lit:
                        player.is_lit = False
                else:
                    print("You don't have that in your inventory")

            # look at item
            elif verb == 'look':
                # if the item is in the room or the player's inventory, print the description
                if object_name in [i.name for i in current_room.items] or object_name in [i.name for i in player.inventory]:
                    print(item[object_name].description)
                else:
                    print("You don't see that")

            # print error message if user enters invalid input
            else:
                print("Input not valid, please try again")

        # if the form of the input is 'use [item] on [item]'
        # elif input_length == 4 and user_input[0] == "use" and user_input[2] == "on":
        #     item_used = user_input[1]
        #     item_target = user_input[3]

        #     # check if player has the item used
        #     # check if that item is usable
        #     # check if the item used can be used on the target item

        #     if 

        # print error message if user enters invalid input
        else:
            print("Too many words, please try again")

        print()


if __name__ == '__main__':
    main()
