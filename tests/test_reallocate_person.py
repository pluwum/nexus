from unittest import TestCase
from classes.andela import Andela

#TODO: Implement tests for this
class TestPrintRoom(TestCase):
	def setUp(self):
		self.andela = Andela()
		self.andela.createRoom("Blue","office")
		self.andela.createRoom("Pink","office")
		self.andela.createRoom("Yellow","livingspace")

		self.patrick = self.andela.addPerson('patrick','fellow',True)
		self.alvin =self.andela.addPerson('alvin','staff')
		self.calvin =self.andela.addPerson('calvin','fellow')
		self.dalvin =self.andela.addPerson('Dalvin','staff')

	def test_method_successfully_relocates_person(self):
		andela = Andela()
		andela.createRoom("Blue","office")
		alvin = andela.addPerson('alvin','staff')

		andela.createRoom("Pink","office")
		andela.rellocatePerson(alvin,'Pink')

		self.assertEqual('Pink', andela.people[alvin]['person'].office_space)

	def test_method_allocates_room_if_person_unlocated(self):
		pass

	def test_method_raises_exception_if_room_is_full(self):
		pass

	def test_method_raises_exception_if_room_doesnt_exist(self):
		self.assertRaises(ValueError, self.andela.rellocatePerson, self.alvin, 'White')

	def test_method_raise_exception_if_new_room_is_same_as_old_room(self):
		andela = Andela()
		andela.createRoom("Blue","office")
		alvin = andela.addPerson('alvin','staff')
		self.assertRaises(ValueError, andela.rellocatePerson, alvin, 'Blue')

	def	test_method_maintains_same_room_if_no_free_room_available(self):
		pass

	def test_method_successfully_removes_person_from_previously_allocated_room(self):
		pass