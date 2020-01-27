# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:

    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = items

    def get_name(self):
        return self.name
    
    def get_items(self):
        return self.items
    
    def drop_item(self, item):
        self.items.remove(item)
        self.room.set_item(item)
    
    def pickup_item(self, item):
        self.items.append(item)
        self.room.remove_item(item)
    
    def set_item(self, new_item):
        self.item = new_item
    
    def change_room(self, new_room):
        self.room.set_room(new_room)

    def __str__(self):
        return f"{self.name}'s current location is the {self.room.get_name()} and is holding {self.items} and the room has items {self.room.get_items()}"

