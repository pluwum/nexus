

class Person(object):

    def __init__(self, name, identifier, role):
        self.name = name
        self.identifier = identifier
        self.role = role
        self.office_space = None
        self.living_space = None

    def allocateOfficeSpace(self, room):
        self.office_space = room

    def getRole():
        return self.role


class Staff(Person):

    def __init__(self, name, identifier):
        self.role = 'staff'
        super(Staff, self).__init__(name, identifier, self.role)


class Fellow(Person):

    def __init__(self, name, identifier, requires_living_space):
        self.role = 'fellow'
        self.requires_living_space = requires_living_space
        super(Fellow, self).__init__(name, identifier, self.role)

    def allocateLivingSpace(self, room):
        if self.requires_living_space:
            self.living_space = room

    def requiresLivingSpace(self):
        if self.requires_living_space:
            return "Y"
        else:
            return "N"
