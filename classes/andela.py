from classes.staff import Staff
from classes.fellow import Fellow
from classes.dojo import Dojo

class Andela():
	def __init__(self):
		self.people = {}
		self.allocations = {}
		self.dojo = Dojo()

	def createRoom(self, name, room_type):
		self.dojo.createRoom(name, room_type)

	def getRoomOccupants(self, room_name):
		room = self.dojo.getRoom(room_name)
		if not room:
			raise ValueError("Room Doesnt Exist")
		else:
			return room.getOccupants()	

	def getRoomAllocations(self):
		pass

	def getUnallocated(self):
		pass

	def addPerson(self, name, role, requires_living_space=False):
		if name is not None and role is not None:
			roles = ['staff','fellow']
			if (isinstance(name, str) and isinstance(role, str) and isinstance(requires_living_space, bool)):
				if(role.lower() in roles):
					identifier = len(self.people) + 1
					living_space = None
					office_space = self.dojo.getFreeOfficeSpace()
					if(role == "staff"):
						if requires_living_space is False:
							new_person = Staff(name, identifier)
						else:
							raise ValueError("Unexpected input: Living Space not provided for staff")
					else:
						new_person = Fellow(name, identifier, requires_living_space)
						if requires_living_space:
							living_space = self.dojo.getFreeLivingSpace()
							
					if office_space is not None:
						new_person.allocateOfficeSpace(office_space)
						office_space.addOccupant(identifier)

					if living_space is not None:
						new_person.allocateLivingSpace(living_space)
						living_space.addOccupant(identifier)

					self.people[identifier]	= {'person':new_person, 'office':new_person.office_space,'living_space':new_person.living_space}
					return identifier
			else:
				raise TypeError("One or more invalid inputs")
		else:
			raise ValueError("One or more required inputs missing")

	def rellocatePerson():
		pass