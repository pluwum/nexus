from classes.room import Room

class Office(Room):
	def __init__(self, name):
		self.max_capacity = 6
		self.room_type = "office"