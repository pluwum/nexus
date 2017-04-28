"""Summary
"""
from classes.database import Database
from classes.person import Fellow, Staff
from classes.room import LivingSpace, Office
from classes.database import Database

class Dojo():
    """initialises a dojo object"""
    def __init__(self):
        self.people = {}
        self.allocations = {}
        self.rooms = {}
        #self.free_rooms = {}
        self.room_types = ['office', 'livingspace']
        self.database = Database()

    def getRoomOccupants(self, room_name):
        """Returns a list with room occupants"""
        room = self.getRoom(room_name)
        return room.getOccupants()

    def getRoomAllocations(self):
        """Returns all the list of room objects with atleast one occupant"""
        rooms = self.getAllRoomsWithAtleastOneOccupant()
        return rooms

    def getUnallocatedPeople(self):
        """
        Finds all Persons without an office or living space
        returns a list of Person child objects
        """
        unallocated = []
        for person in self.people:
            person_object = self.people[person]

            if(person_object.office_space is None):
                unallocated.append(person_object)

            if(person_object.role == "fellow" and person_object.requires_living_space and person_object.living_space is None):
                if person_object not in unallocated:
                    unallocated.append(person_object)

        return unallocated

    def addPerson(self, name, role, requires_living_space=False):
        """Enrolls person to Dojo

        Args:
            name (str): Name of Person being enrolled
            role (str): fellow or staff
            requires_living_space (bool, optional): Specifies need for living space

        Returns:
            int: Unique Person ID number
        """
        if name is not None and role is not None:
            roles = ['staff', 'fellow']
            #check if name is a string
            if (isinstance(name, str) and isinstance(role, str) and isinstance(requires_living_space, bool)):
                if(role.lower() in roles):
                    identifier = len(self.people) + 1
                    living_space = None
                    office_space = self.getFreeOfficeSpace()
                    #check if enrollee is staff or fellow
                    if(role.lower() == "staff"):
                        if requires_living_space is False:
                            new_person = Staff(name, identifier)
                        else:
                            raise ValueError("Unexpected input: Living Space not provided for staff")
                    else:
                        #Enroll fellow
                        new_person = Fellow(name, identifier, requires_living_space)
                        if requires_living_space:
                            living_space = self.getFreeLivingSpace()

                    if office_space is not None:
                        #Assign office space is free room is found
                        new_person.allocateOfficeSpace(office_space.name)
                        office_space.addOccupant(identifier)

                    if living_space is not None:
                        #Assign living space if found and is required
                        new_person.allocateLivingSpace(living_space.name)
                        living_space.addOccupant(identifier)

                    self.people[identifier] = new_person
                    return identifier
                raise ValueError("Invalide Role argument")
            raise TypeError("One or more invalid inputs")
        raise ValueError("One or more required inputs missing")

    def rellocatePerson(self, person_identifier, room_name):
        """Relocates person to room_name

        Args:
            person_identifier (int): Persons ID Number
            room_name (str): Room Name

        Returns:
            bool: True if successful
        """
        if(isinstance(room_name, str)):
            if(person_identifier in self.people):
                person = self.people[person_identifier]
                rooms = self.getAllRooms()
                if room_name in rooms:
                    if rooms[room_name].room_type == "office":
                        if room_name != person.office_space:
                            office_space = self.getFreeOfficeSpace(person.office_space)

                            #Add to New and Evict from old room when succesfully found a office room
                            if(office_space is not None):
                                old_room = self.getRoom(person.office_space)
                                office_space.addOccupant(person_identifier)
                                person.allocateOfficeSpace(office_space.name)
                                old_room.evictOccupant(person_identifier)
                                return True
                        raise ValueError("New room is the same as the old room")
                    else:
                        if room_name != self.people[person_identifier].living_space:
                            living_space = self.getFreeLivingSpace(person.living_space)

                            #Add to New and Evict from old room when succesfully found a office room
                            if(living_space is not None):
                                old_room = self.getRoom(person.office_space)
                                living_space.addOccupant(person_identifier)
                                person.allocateLivingSpace(living_space.name)
                                old_room.evictOccupant(person_identifier)
                                return True
                        raise ValueError("New room is the same as the old room")
                raise ValueError("Room does not exist")
            raise ValueError("person with given ID does not exist")
        raise ValueError("Invalid inputs received please try again")

    def allocateFromFile(self):
        """Enrols People to Dojo from a file"""
        path_to_file = "data\people.txt"
        try:
            file = open(path_to_file, 'r')

            for line in file:
                args = line.split()
                requires_living_space = False
                if(len(args) >= 3):
                    name = args[0] + args[1]
                    role = args[2]
                    #check if requires living space
                    if(len(args) > 3):
                        requires_living_space = args[3]
                        if(requires_living_space):
                            requires_living_space = True
                    self.addPerson(name, role, requires_living_space)
                    continue
                print("You have arguments missing, please check file and try again{}".format(args))
                continue
        except Exception as ex:
            print('{}\n'.format(ex))

    def getRoom(self, room_name):
        """Takes room name and returns room object"""
        if room_name in self.rooms:
            return self.rooms[room_name]
        raise ValueError("Sorry, Room does not exist")

    def getAllRooms(self):
        """Returns all rooms in the Dojo"""
        return self.rooms

    def createRoom(self, name, room_type):
        """Creates a new room in the Dojo"""
        if (not(name is None) and not(room_type is None)):
            if (isinstance(name, str) and isinstance(room_type, str)):
                if room_type.lower() in self.room_types:

                    if not(name in self.rooms):
                        if room_type == "office":
                             new_room = Office(name)
                        else:
                            new_room = LivingSpace(name)

                        self.rooms[name] = new_room
                        return new_room
                    raise ValueError(name+" Room already exists")

                raise ValueError("Room must be either type 'office' or 'livingspace' ")
            raise TypeError("Room name must be string")
        raise ValueError("One or more arguments required is not given")

    def getAllRoomsWithAtleastOneOccupant(self):
        """Returns List of All Rooms with Atleast one occupant"""
        rooms = []
        for room in self.rooms:
            room_obj = self.rooms[room]

            if len(room_obj.occupants) > 0:
                rooms.append(room_obj)

        return rooms

    def getFreeRoom(self, room_type, room_to_ignore=None):
        """Returns a random room

        Args:
            room_type (str): Room type
            room_to_ignore (None, optional): Specifies room to skip. useful during reallocation

        Returns:
            TYPE: Description
        """
        for room in self.rooms:
            room_obj = self.rooms[room]
            if room_obj.name != room_to_ignore and room_obj.room_type == room_type:
                if len(room_obj.occupants) < room_obj.max_capacity:
                    return room_obj
        return None

    def getFreeOfficeSpace(self, room_to_ignore=None):
        """Returns one free office space"""
        return self.getFreeRoom("office", room_to_ignore)

    def getFreeLivingSpace(self, room_to_ignore=None):
        """Returns one free living space"""
        return self.getFreeRoom("livingspace", room_to_ignore)

    def allocateRoom(self):
        pass

    def saveState(self):
        """Persists state to the database"""
        self.database.saveState(self.people, self.rooms)

    def loadState(self):
        """Loads Saves state from the database"""
        retrieved_state = self.database.retrieveState()
        rooms_created = []
        for person in retrieved_state['people']:
            person_identifier = self.addPerson(person.name, person.role, person.requires_living_space)
            self.people[person_identifier].allocateOfficeSpace(person.office_space)
            room = createRoom(person.office_space, 'office')
            rooms_created.append(person.office_space)
            room.addOccupant(person_identifier)

            if person.role == "fellow" and person.requires_living_space:
                self.people[person_identifier].allocateLivingSpace(person.living_space)
                self.createRoom()
                room = createRoom(person.living_space, 'livingspace')
                rooms_created.append(person.office_space)
                room.addOccupant(person_identifier)

        for room in retrieved_state['rooms']:
            if room not in rooms_created:
                createRoom(room.name, room.room_type)
