from unittest import TestCase
from classes.dojo import Dojo

class TestCreateRoom(TestCase):
	def setUp(self):
		self.dojo = Dojo()

	def test_method_creates_room_succesfully(self):
		initial_room_count = len(self.dojo.rooms)
		blue_room = self.dojo.createRoom("Blue","office")
		new_room_count = len(self.dojo.rooms)

		self.assertListEqual([new_room_count, blue_room], [initial_room_count + 1, True])

	def test_method_raises_error_no_room_name_arg(self):
		self.assertRaises(ValueError,self.dojo.createRoom,None,"office")

	def test_method_raises_error_no_room_type_arg(self):
		self.assertRaises(ValueError,self.dojo.createRoom,"Yellow",None)

	def test_method_raises_error_invalid_room_type(self):
		self.assertRaises(ValueError,self.dojo.createRoom,"Yellow","kitchen")

	def test_method_raises_error_room_name_exists(self):
		white_room = self.dojo.createRoom("White","office")
		self.assertRaises(ValueError,self.dojo.createRoom,"White","office")

	def test_method_raises_error_room_name_not_string(self):
		self.assertRaises(TypeError,self.dojo.createRoom,1000,"office")

	def test_method_raises_error_room_type_not_string(self):
		self.assertRaises(TypeError,self.dojo.createRoom,"Pink",2000)