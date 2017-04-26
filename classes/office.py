from classes.room import Room

class Office(Room):
	def __init__(self, name):
		self.max_capacity = 6
		self.room_type = "office"
		self.name = name
		super(Office, self).__init__(name, self.max_capacity)