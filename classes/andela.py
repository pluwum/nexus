from classes.person import Fellow
from classes.person import Staff
from classes.room import LivingSpace
from classes.room import Office

class Dojo():
	def __init__(self):
		self.people = {}
		self.allocations = {}
		self.rooms = {}
		#self.free_rooms = {}
		self.room_types = ['office','livingspace']

	def getRoomOccupants(self, room_name):
		room = self.getRoom(room_name)
		return room.getOccupants()

	def getRoomAllocations(self):
		rooms = self.getAllRoomsWithAtleastOneOccupant()
		return rooms

	def getUnallocatedPeople(self):
		unallocated = []
		for person in self.people:
			person_object = self.people[person]['person']

			if(person_object.office_space is None):
				unallocated.append(person_object)

			if(person_object.role == "fellow" and person_object.requires_living_space and person_object.living_space is None):
				if person_object not in unallocated:
					unallocated.append(person_object)

		return unallocated

	def addPerson(self, name, role, requires_living_space=False):
		if name is not None and role is not None:
			roles = ['staff','fellow']

			if (isinstance(name, str) and isinstance(role, str) and isinstance(requires_living_space, bool)):
				if(role.lower() in roles):
					identifier = len(self.people) + 1
					living_space = None
					office_space = self.getFreeOfficeSpace()

					if(role == "staff"):
						if requires_living_space is False:
							new_person = Staff(name, identifier)
						else:
							raise ValueError("Unexpected input: Living Space not provided for staff")
					else:
						new_person = Fellow(name, identifier, requires_living_space)
						if requires_living_space:
							living_space = self.getFreeLivingSpace()
							
					if office_space is not None:
						new_person.allocateOfficeSpace(office_space.name)
						office_space.addOccupant(identifier)

					if living_space is not None:
						new_person.allocateLivingSpace(living_space.name)
						living_space.addOccupant(identifier)

					self.people[identifier]	= {'person':new_person, 'office':new_person.office_space,'living_space':new_person.living_space}
					return identifier
			else:
				raise TypeError("One or more invalid inputs")
		else:
			raise ValueError("One or more required inputs missing")

	def rellocatePerson(self, person_identifier, room_name):
		if(isinstance(room_name, str)):
			if(person_identifier in self.people):
				person = self.people[person_identifier]['person']
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
							
						else:
							raise ValueError("New room is the same as the old room")
					else:
						if room_name != self.people[person_identifier]['person'].living_space:
							living_space = self.getFreeLivingSpace(person.living_space)
														
							#Add to New and Evict from old room when succesfully found a office room
							if(living_space is not None):
								old_room = self.getRoom(person.office_space)
								living_space.addOccupant(person_identifier)
								person.allocateLivingSpace(living_space.name)
								old_room.evictOccupant(person_identifier)	
						else:
							raise ValueError("New room is the same as the old room")								
				else:
					raise ValueError("Room does not exist")
			else:
				raise ValueError("person with given ID does not exist")

		return False

	def allocateFromFile(self):
		path_to_file = "data\people.txt"
		try:
			file = open(path_to_file, 'r')

			for line in file:
				args = line.split()
				requires_living_space = False

				if(len(args) >= 3):
					name = args[0] + args[1]
					role = args[2]

					if(len(args) > 3):
						requires_living_space = args[3]
						if(requires_living_space):
							requires_living_space = True
				else:
					print("You have arguments missing, please check and try again{}".format(args))

				self.addPerson(name, role, requires_living_space)
		except Exception as ex:
			print('{}\n'.format(ex))

	def getRoom(self, room_name):
		if room_name in self.rooms:
			return self.rooms[room_name]
		raise ValueError("Sorry, Room does not exist")

	def getAllRooms(self):
		return self.rooms

	def createRoom(self, name, room_type):
		if (not(name is None) and not(room_type is None)):
			if (isinstance(name, str) and isinstance(room_type, str)):
				if room_type.lower() in self.room_types:
					if name in self.rooms:
						raise ValueError(name+" Room already exists")
					else:
						if room_type == "office":
							 new_room = Office(name)
						else:
							new_room = LivingSpace(name)

						self.rooms[name] = new_room
						return True
				else:
					raise ValueError("Room must be either type 'office' or 'livingspace' ")	
			else:
				raise TypeError("Room name must be string")
		else:		
			raise ValueError("One or more arguments required is not given")

	def getAllRoomsWithAtleastOneOccupant(self):
		rooms = []
		for room in self.rooms:
			room_obj = self.rooms[room]
			
			if len(room_obj.occupants) > 0:
				rooms.append(room_obj)

		return rooms

	def getFreeRoom(self, room_type, room_to_ignore=None):
		for room in self.rooms:
			room_obj = self.rooms[room]
			if room_obj.name != room_to_ignore and room_obj.room_type == room_type:
				if len(room_obj.occupants) < room_obj.max_capacity:
					return room_obj
		return None

	def getFreeOfficeSpace(self, room_to_ignore=None):
		return self.getFreeRoom("office", room_to_ignore)

	def getFreeLivingSpace(self, room_to_ignore=None):
		return self.getFreeRoom("livingspace", room_to_ignore)
		
	def allocateRoom():
		pass
