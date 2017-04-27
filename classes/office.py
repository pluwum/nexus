from classes.room import Room

class Office(Room):
	def __init__(self, name):
		self.room_type = "office"
		super(Office, self).__init__(name, 6)