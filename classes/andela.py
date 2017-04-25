from classes.staff import Staff
from classes.fellow import Fellow
from classes.dojo import Dojo

class Andela():
	def __init__(self):
		self.people = {}
		self.allocations = {}
		self.dojo = Dojo()

	def addPerson(self, name, role, requires_living_space = False):
		if name is not None and role is not None:
			roles = ['staff','fellow']
			if (isinstance(name, str) and isinstance(role, str) and isinstance(requires_living_space, bool)):
				if(role.lower() in roles):
					identifier = len(self.people) + 1
					living_space = None
					if(role == "staff"):
						if requires_living_space is False:
							new_person = Staff(name)
							office_space = self.dojo.getFreeOfficeSpace()
							new_person.allocateOfficeSpace(office_space)
						else:
							raise ValueError("Unexpected input: Living Space not provided for staff")
					else:
						new_person = Fellow(name, requires_living_space)
						if requires_living_space:
							living_space = self.dojo.getFreeLivingSpace()
							new_person.allocateLivingSpace(living_space)
					self.people[identifier]	= {'person':new_person, 'office':'','living_space':'ABCD'}
					return identifier
			else:
				raise TypeError("One or more invalid inputs")
		else:
			raise ValueError("One or more required inputs missing")

	def rellocatePerson():
		pass