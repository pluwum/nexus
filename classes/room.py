class Room():
	def __init__(self, name, max_capacity):
		self.name = name
		self.occupants = []
		self.max_capacity = max_capacity

	def addOccupant(self, person_identifier):
		if len(self.occupants) < self.max_capacity:
			if person_identifier not in self.occupants:
				self.occupants.append(person_identifier)
				#return True
				return self
			else:
				return False

	def evictOccupant(self, person_identifier):
		if person_identifier in self.occupants:
			self.occupants.remove(person_identifier)
			return self

	def getOccupants(self):
		return self.occupants

class LivingSpace(Room):
	def __init__(self, name):
		self.room_type = "livingspace"
		super(LivingSpace, self).__init__(name, 4)
		
class Office(Room):
	def __init__(self, name):
		self.room_type = "office"
		super(Office, self).__init__(name, 6)