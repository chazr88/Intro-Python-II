# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def get_color(self):
        return self.color