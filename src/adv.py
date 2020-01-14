from room import Room
from player import Player

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
        # print the current room name
        print(f"Current location: {player.current_room.name}")
        # print current room description
        print(player.current_room.description)

        # wait for user input
        user_input = input(">>> ")

        directions = ('n', 's', 'e', 'w')
        # if user enters a cardinal direction, attempt to move there
        if user_input in directions:
            attempted_room = getattr(player.current_room, f"{user_input}_to")
            # if movement is allowed, update the current room
            if attempted_room != None:
                player.change_room(attempted_room)
            # print error message if movement is not allowed
            else:
                print("You cannot move in that direction")
        # else if user enters q, quit the game
        elif user_input == 'q':
            break
        # print error message if user enters invalid input
        else:
            print("Input not valid, please try again")

if __name__ == '__main__':
    main()
