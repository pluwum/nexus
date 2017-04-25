from classes.person import Person

class Fellow(Person):
	def __init__(self, name, requires_living_space):
		self.role = 'fellow'
		self.requires_living_space = requires_living_space

	def allocateLivingSpace(self, room):
		if self.requires_living_space:
			self.living_space = room