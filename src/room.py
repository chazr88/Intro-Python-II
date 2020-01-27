# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __str__(self):
        return self.name

    def get_items(self):
        return self.items

    def set_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


    # def __add__(self, other):
    #     return str(self) + other

    # def __radd__(self, other):
    #     return other + str(self)

