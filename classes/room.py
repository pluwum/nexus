"""These classes defines/models the behaviour of room objects
"""

class Room():
    """Models the generic behaviour of a room"""
    def __init__(self, name, max_capacity):
        self.name = name
        self.occupants = []
        self.max_capacity = max_capacity

    def addOccupant(self, person_identifier):
        """Adds Occupant to a room"""
        if len(self.occupants) < self.max_capacity:
            if person_identifier not in self.occupants:
                self.occupants.append(person_identifier)
                return self
            else:
                return False

    def evictOccupant(self, person_identifier):
        """Removes occupant from the room object"""
        if person_identifier in self.occupants:
            self.occupants.remove(person_identifier)
            return self

    def getOccupants(self):
        """Returns the List of occupants within the room object"""
        return self.occupants


class LivingSpace(Room):
    """Defines room behaviour specific to Living Space"""
    def __init__(self, name):
        self.room_type = "livingspace"
        super(LivingSpace, self).__init__(name, 4)


class Office(Room):
    """Defines room behaviour specific to and Office"""
    def __init__(self, name):
        self.room_type = "office"
        super(Office, self).__init__(name, 6)
