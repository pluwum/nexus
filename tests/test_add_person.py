from unittest import TestCase
from classes.andela import Andela


class TestAddPerson(TestCase):
	def setUp(self):
		self.andela = Andela()
		self.andela.createRoom("Blue","office")
		self.andela.createRoom("Yellow","livingspace")

	def test_method_creates_person_successfully_and_assigns_office(self):
		initial_people_count = len(self.andela.people)
		identifier = self.andela.addPerson("Patrick",'staff')
		current_people_count = len(self.andela.people)

		self.assertListEqual([current_people_count, str],[initial_people_count + 1,type(self.andela.people[identifier]["office"])], msg = 'Person not added to people list or office room not assigned') 

	def test_method_creates_fellow_successfully_and_assigns_living_space(self):
		initial_people_count = len(self.andela.people)
		identifier = self.andela.addPerson("Alvin",'fellow',True)
		current_people_count = len(self.andela.people)

		self.assertListEqual([current_people_count, str],[initial_people_count + 1,type(self.andela.people[identifier]["living_space"])], msg = 'Fellow not added to fellow list or living space not assigned') 

	def test_method_defaults_to_N_if_living_space_not_specified(self):
		identifier = self.andela.addPerson("Alvin",'fellow')
		#self.assertEqual(None, type(self.andela.people[identifier]["living_space"]))

	def test_method_raises_error_if_staff_wants_accomodation(self):
		self.assertRaises(ValueError,self.andela.addPerson,"Patricia",'staff',True)

	def test_method_raises_error_if_person_already_exists(self):
		pass

	def test_method_raises_error_if_person_name_arg_missing(self):
		self.assertRaises(ValueError,self.andela.addPerson,None,'staff')

	def test_method_raises_error_if_role_arg_missing(self):
		self.assertRaises(ValueError,self.andela.addPerson,'Malvin',None)