from classes.person import Person

class Fellow(Person):
	def __init__(self, name, identifier, requires_living_space):
		self.role = 'fellow'
		self.requires_living_space = requires_living_space
		super(Fellow, self).__init__(name, identifier, self.role)

	def allocateLivingSpace(self, room):
		if self.requires_living_space:
			self.living_space = room