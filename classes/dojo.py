from classes.room import LivingSpace
from classes.room import Office

class Dojo(object):
	def __init__(self):
		self.rooms = {}
		#self.free_rooms = {}
		self.room_types = ['office','livingspace']

	def getRoom(self, room_name):
		if room_name in self.rooms:
			return self.rooms[room_name]
		else:
			return False

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