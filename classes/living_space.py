from classes.room import Room

class LivingSpace(Room):
	def __init__(self, name):
		self.max_capacity = 4
		self.room_type = "livingspace"