from unittest import TestCase
from classes.andela import Andela

class TestPrintRoom(TestCase):
	def setUp(self):
		self.andela = Andela()
		self.andela.createRoom("Blue","office")
		self.andela.createRoom("Yellow","livingspace")

		self.andela.addPerson('patrick','fellow',True)
		self.andela.addPerson('alvin','staff')
		self.andela.addPerson('calvin','fellow')
		self.andela.addPerson('Dalvin','staff')


	def test_method_successfully_returns_room_occupants(self):
		office_occupants = self.andela.getRoomOccupants("Blue")
		livingspace_occupants = self.andela.getRoomOccupants("Blue")

		self.assertListEqual([True, 4, 1], [isinstance(office_occupants, list), len(office_occupants), len(livingspace_occupants)])

	def test_method_raises_exception_if_room_given_doesnt_exist():
		self.assertRaises(ValueError, self.andela.getRoomOccupants, "Red")