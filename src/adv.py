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
new_player = Player("Chaz", Room('outside', ["hat", "bookbag"]), ['coat', 'phone'])
print(new_player)

def update_room(new_room):
    if new_room == room['foyer']:
        new_player.room.set_name('foyer')
    elif new_room == room['outside']:
        new_player.room.set_name('outside')
    elif new_room == room['overlook']:
        new_player.room.set_name('overlook')
    elif new_room == room['narrow']:
        new_player.room.set_name('narrow')
    elif new_room == room['treasure']:
        new_player.room.set_name('treasure')

    print(f"You are now in location {new_room}")
    print(new_player.room.get_name())

def drop_item(item):
    new_player.drop_item(item)
    print(f"you just dropped {item}")
    print(new_player)

def add_item(item):
    new_player.pickup_item(item)
    print(f"you just picked up {item}")
    print(new_player)
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
selection = ""
while selection is not "q":
    
    selection = selection + input(f"Please choose n, s, e, w to move your player in that direction to a new room.\
You can also drop an item in your hand by typing 'drop', or pick up an item from the current room by typing 'pickup': ")

    if selection == 'n':
        try:
            new_room = room[new_player.room.get_name()].n_to
            selection = ""
            update_room(new_room)
        except:
            print("sorry you cant go that way")
            selection = ""
    elif(selection == 'e'):
        try:
            new_room = room[new_player.room.get_name()].e_to
            selection = ""
            update_room(new_room)
        except:
            print("sorry you cant go that way")
            selection = ""
    elif(selection == 's'):
        try:
            new_room = room[new_player.room.get_name()].s_to
            selection = ""
            update_room(new_room)
        except:
            print("sorry you cant go that way")
            selection = ""
    elif(selection == 'w'):
        try:
            new_room = room[new_player.room.get_name()].w_to
            selection = ""
            update_room(new_room)
        except:
            print("sorry you cant go that way")
            selection = ""
    elif(selection == 'drop'):
        item = input(f"please enter the name of the item you wish to drop: ")
        drop_item(item)
    elif(selection == 'pickup'):
        item = input(f"please enter the name of the item you wish to pick up: ")
        add_item(item)
    else:
        print("Sorry your entry is invalid.")
        selection = ""


    #my_room = room[new_player.room.get_name()]
    #my_room = str(my_room) + selection

    

    