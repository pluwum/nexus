from classes.person import Person

class Staff(Person):

	def __init__(self, name, identifier):
		self.role = 'staff'
		super(Staff, self).__init__(name, identifier, self.role)