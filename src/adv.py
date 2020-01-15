from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declare items

item = {
    'fork': Item('fork', "It's a little rusty"),
    'chicken': Item('chicken', "It stares at you blankly")
}

# Add items to rooms

room['outside'].add_item(item['fork'])
room['outside'].add_item(item['chicken'])

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
    # make a new player that is currently in the 'outside' room
    player = Player(input("Enter your name: "), room['outside'])

    while True:
        current_room = player.current_room
        # print the current room name
        print(f"Current location: {current_room.name}")
        # print current room description
        print(current_room.description)
        # print all items in the room
        current_room.print_items()

        # wait for user input
        user_input = input(">>> ")
        input_length = len(user_input.split(' '))

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
                    player.change_room(attempted_room)
                # print error message if movement is not allowed
                else:
                    print("You cannot move in that direction")

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
            user_input = user_input.split(' ')
            verb = user_input[0]
            object_name = user_input[1]

            # pick up item: supports 'get' and 'take'
            if verb == 'get' or verb == 'take':
                # check if item is in the room
                for i in current_room.items:
                    if i.name == object_name:
                        # remove from room and add to player's inventory
                        current_room.remove_item(i)
                        player.add_item(i)
                        i.on_take()
                        break
                # print error message
                else:
                    print("There is nothing called that here")

            # drop item
            elif verb == 'drop':
                # check if item is in player's inventory
                for i in player.inventory:
                    if i.name == object_name:
                        # add to room and remove from inventory
                        current_room.add_item(i)
                        player.remove_item(i)
                        i.on_drop()
                        break
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

        # print error message if user enters invalid input
        else:
            print("Too many words, please try again")

        print()


if __name__ == '__main__':
    main()
