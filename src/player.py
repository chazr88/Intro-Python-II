# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def get_name(self):
        return self.name
    
    def change_room(self, new_room):
        self.room.set_room(new_room)

    def __str__(self):
        return f"{self.name}'s current location is the {self.room.get_name()} and its color is {self.room.get_color()}"

