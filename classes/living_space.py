from classes.room import Room

class LivingSpace(Room):
	def __init__(self, name):
		self.room_type = "livingspace"
		super(LivingSpace, self).__init__(name, 4)