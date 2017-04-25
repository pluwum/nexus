class Person(object):
	def __init__(self, name, identifier, role):
		self.name = name;
		self.identifier = identifier
		self.role = role
		self.office_space = None
		self.living_space = None

	def allocateOfficeSpace(self, room):
		self.office_space = room

	def getRole():
		return self.role