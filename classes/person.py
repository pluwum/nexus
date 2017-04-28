"""This class defines the template for Person, Staff and fellow classes
Staff and Fellow inherit from Person
"""

class Person(object):

    def __init__(self, name, identifier, role):
        """Iniitalises Person Object"""
        self.name = name
        self.identifier = identifier
        self.role = role
        self.office_space = None
        self.living_space = None

    def allocateOfficeSpace(self, room):
        """Assign office Space"""
        self.office_space = room

    def getRole():
        """Getter Method to Return Role of the object"""
        return self.role


class Staff(Person):
    """Defines a person enrolled to the dojo as a staff member"""
    def __init__(self, name, identifier):
        self.role = 'staff'
        super(Staff, self).__init__(name, identifier, self.role)


class Fellow(Person):
    """Defines a person enrolled to the Dojo as a staff member"""
    def __init__(self, name, identifier, requires_living_space):
        self.role = 'fellow'
        self.requires_living_space = requires_living_space
        super(Fellow, self).__init__(name, identifier, self.role)

    def allocateLivingSpace(self, room):
        """Alocates Living Space to fellow object"""
        if self.requires_living_space:
            self.living_space = room

    def requiresLivingSpace(self):
        """Return Y if fellow requires living space and No otherwise"""
        if self.requires_living_space:
            return "Y"
        else:
            return "N"
