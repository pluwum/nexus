from classes.dojo import Dojo
from unittest import TestCase

class TestAddPerson(TestCase):

    def setUp(self):
        self.dojo = Dojo()
        self.dojo.createRoom("Blue", "office")
        self.dojo.createRoom("Yellow", "livingspace")

    def test_method_creates_person_successfully_and_assigns_office(self):
        initial_people_count = len(self.dojo.people)
        identifier = self.dojo.addPerson("Patrick", 'staff')
        current_people_count = len(self.dojo.people)

        self.assertListEqual([current_people_count, str], [initial_people_count + 1, type(self.dojo.people[identifier].office_space)], msg = 'Person not added to people list or office room not assigned')

    def test_method_creates_fellow_successfully_and_assigns_living_space(self):
        initial_people_count = len(self.dojo.people)
        identifier = self.dojo.addPerson("Alvin", 'fellow', True)
        current_people_count = len(self.dojo.people)

        self.assertListEqual([current_people_count, str], [initial_people_count + 1, type(self.dojo.people[identifier].living_space)], msg = 'Fellow not added to fellow list or living space not assigned')

    def test_method_defaults_to_N_if_living_space_not_specified(self):
        identifier = self.dojo.addPerson("Alvin", 'fellow')
        self.assertEqual(False, self.dojo.people[identifier].requires_living_space)

    def test_method_raises_error_if_staff_wants_accomodation(self):
        self.assertRaises(ValueError,self.dojo.addPerson,"Patricia",'staff',True)

    def test_method_raises_error_if_person_already_exists(self):
        pass

    def test_method_raises_error_if_person_name_arg_missing(self):
        self.assertRaises(ValueError,self.dojo.addPerson, None, 'staff')

    def test_method_raises_error_if_role_arg_missing(self):
        self.assertRaises(ValueError, self.dojo.addPerson, 'Malvin', None)


class TestCreateRoom(TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_method_creates_room_succesfully(self):
        initial_room_count = len(self.dojo.rooms)
        blue_room = self.dojo.createRoom("Blue", "office")
        new_room_count = len(self.dojo.rooms)

        self.assertListEqual([new_room_count, isinstance(blue_room.name, str), blue_room.room_type], [initial_room_count + 1, True, 'office'])

    def test_method_raises_error_no_room_name_arg(self):
        self.assertRaises(ValueError,self.dojo.createRoom, None, "office")

    def test_method_raises_error_no_room_type_arg(self):
        self.assertRaises(ValueError, self.dojo.createRoom, "Yellow", None)

    def test_method_raises_error_invalid_room_type(self):
        self.assertRaises(ValueError, self.dojo.createRoom, "Yellow", "kitchen")

    def test_method_raises_error_room_name_exists(self):
        white_room = self.dojo.createRoom("White", "office")
        self.assertRaises(ValueError, self.dojo.createRoom, "White", "office")

    def test_method_raises_error_room_name_not_string(self):
        self.assertRaises(TypeError, self.dojo.createRoom, 1000, "office")

    def test_method_raises_error_room_type_not_string(self):
        self.assertRaises(TypeError, self.dojo.createRoom, "Pink", 2000)


class TestPrintRoomAllocations(TestCase):

    def setUp(self):
        self.dojo = Dojo()
        self.dojo.createRoom("Blue", "office")
        self.dojo.createRoom("Yellow", "livingspace")

        self.dojo.addPerson('patrick', 'fellow',True)
        self.dojo.addPerson('alvin', 'staff')
        self.dojo.addPerson('calvin', 'fellow')
        self.dojo.addPerson('Dalvin', 'staff')

    def test_method_successfully_returns_room_allocations(self):
        allocations = self.dojo.getRoomAllocations()
        self.assertListEqual([True, 2], [isinstance(allocations, list), len(allocations)])

    def test_method_returns_empty_when_no_rooms_allocated(self):
        andela = Dojo()
        andela.createRoom("Blue", "office")
        andela.createRoom("Yellow", "livingspace")

        allocations = andela.getRoomAllocations()
        self.assertEqual(0, len(allocations))


class TestPrintRoom(TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.createRoom("Blue", "office")
        self.dojo.createRoom("Yellow", "livingspace")

        self.dojo.addPerson('patrick', 'fellow',True)
        self.dojo.addPerson('alvin', 'staff')
        self.dojo.addPerson('calvin', 'fellow')
        self.dojo.addPerson('Dalvin', 'staff')

    def test_method_successfully_returns_room_occupants(self):
        office_occupants = self.dojo.getRoomOccupants("Blue")
        livingspace_occupants = self.dojo.getRoomOccupants("Yellow")

        self.assertListEqual([True, 4, 1], [isinstance(office_occupants, list), len(office_occupants), len(livingspace_occupants)])

    def test_method_raises_exception_if_room_given_doesnt_exist(self):
        self.assertRaises(ValueError, self.dojo.getRoomOccupants, "Red")


class TestPrintUnallocated(TestCase):

    def setUp(self):
        self.dojo = Dojo()
        self.dojo.addPerson('patrick', 'fellow', True)
        self.dojo.addPerson('alvin', 'staff')
        self.dojo.addPerson('calvin', 'fellow')
        self.dojo.addPerson('Dalvin', 'staff')

    def test_method_successfully_returns_unallocated_people(self):
        unallocated_people = self.dojo.getUnallocatedPeople()
        self.assertListEqual([True, 4], [isinstance(unallocated_people, list), len(unallocated_people)])

    def test_method_returns_empty_when_every_one_is_allocated(self):
        andela = Dojo()
        andela.createRoom("Blue", "office")
        self.dojo.createRoom("Yellow", "livingspace")
        self.dojo.addPerson('patrick', 'fellow',True)
        self.dojo.addPerson('alvin', 'staff')
        self.dojo.addPerson('calvin', 'fellow')

        unallocated_people = andela.getUnallocatedPeople()
        self.assertEqual(0, len(unallocated_people))

class TestPrintRoomAllocations(TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.createRoom("Blue", "office")
        self.dojo.createRoom("Yellow", "livingspace")

        self.dojo.addPerson('patrick', 'fellow',True)
        self.dojo.addPerson('alvin', 'staff')
        self.dojo.addPerson('calvin', 'fellow')
        self.dojo.addPerson('Dalvin', 'staff')

    def test_method_successfully_returns_room_allocations(self):
        allocations = self.dojo.getRoomAllocations()
        self.assertListEqual([True, 2], [isinstance(allocations, list), len(allocations)])

    def test_method_returns_empty_when_no_rooms_allocated(self):
        andela = Dojo()
        andela.createRoom("Blue", "office")
        andela.createRoom("Yellow", "livingspace")

        allocations = andela.getRoomAllocations()
        self.assertEqual(0, len(allocations))

class TestReallocate(TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.createRoom("Blue", "office")
        self.dojo.createRoom("Pink", "office")
        self.dojo.createRoom("Yellow", "livingspace")

        self.patrick = self.dojo.addPerson('patrick', 'fellow',True)
        self.alvin =self.dojo.addPerson('alvin', 'staff')
        self.calvin =self.dojo.addPerson('calvin', 'fellow')
        self.dalvin =self.dojo.addPerson('Dalvin', 'staff')

    def test_method_successfully_relocates_person(self):
        andela = Dojo()
        andela.createRoom("Blue", "office")
        alvin = andela.addPerson('alvin', 'staff')

        andela.createRoom("Pink", "office")
        andela.rellocatePerson(alvin, 'Pink')

        self.assertEqual('Pink', andela.people[alvin].office_space)

    def test_method_allocates_room_if_person_unlocated(self):
        pass

    def test_method_raises_exception_if_room_is_full(self):
        pass

    def test_method_raises_exception_if_room_doesnt_exist(self):
        self.assertRaises(ValueError, self.dojo.rellocatePerson, self.alvin, 'White')

    def test_method_raise_exception_if_new_room_is_same_as_old_room(self):
        andela = Dojo()
        andela.createRoom("Blue", "office")
        alvin = andela.addPerson('alvin', 'staff')
        self.assertRaises(ValueError, andela.rellocatePerson, alvin, 'Blue')

    def test_method_maintains_same_room_if_no_free_room_available(self):
        pass

    def test_method_successfully_removes_person_from_previously_allocated_room(self):
        pass