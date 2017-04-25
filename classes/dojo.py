from classes.living_space import LivingSpace
from classes.office import Office

class Dojo(object):
	def __init__(self):
		self.rooms = {}
		#self.free_rooms = {}
		self.room_types = ['office','livingspace']

	def createRoom(self, name, room_type):
		if (not(name is None) and not(room_type is None)):
			if (isinstance(name, str) and isinstance(room_type, str)):
				if room_type.lower() in self.room_types:
					if name in self.rooms:
						raise ValueError("Room already exists")
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

	def getFreeRoom(self, room_type, room_to_ignore=None):
		for room in self.rooms:
			if room != room_to_ignore and room.room_type == room_type:
				if room.occupants < room.max_capacity:
					return room.name
		return None

	def getFreeOfficeSpace(self, room_to_ignore=None):
		return self.getFreeRoom("office")

	def getFreeLivingSpace(self):
		return self.getFreeRoom("livingspace")
		
	def allocateRoom():
		pass	