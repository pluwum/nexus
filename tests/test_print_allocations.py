from unittest import TestCase
from classes.andela import Andela

class TestPrintRoomAllocations(TestCase):
	def setUp(self):
		self.andela = Andela()
		self.andela.createRoom("Blue","office")
		self.andela.createRoom("Yellow","livingspace")

		self.andela.addPerson('patrick','fellow',True)
		self.andela.addPerson('alvin','staff')
		self.andela.addPerson('calvin','fellow')
		self.andela.addPerson('Dalvin','staff')

	def test_method_successfully_returns_room_allocations(self):
		allocations = self.andela.getRoomAllocations()

		self.assertListEqual([True, 2], [isinstance(allocations, list), len(allocations)])
	def test_method_returns_empty_when_no_rooms_allocated(self):
		andela = Andela()
		andela.createRoom("Blue","office")
		andela.createRoom("Yellow","livingspace")

		allocations = andela.getRoomAllocations()
		self.assertEqual(0, len(allocations))