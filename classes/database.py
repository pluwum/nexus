import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.tables import *


class Database(object):
	def __init__(self):
		self.engine = create_engine('sqlite:///data/andela.db', echo=False)
		"""create a Session"""
		Session = sessionmaker(bind=self.engine)
		self.session = Session()

	def saveState(self, people, rooms):
		"""Create db objects in prepration for pushing to database"""
		for room in rooms:
			room = TableRoom(rooms[room].name, 'rooms[room].occupants', rooms[room].max_capacity, rooms[room].room_type)
			self.session.add(room)

		for person in people:
			person = TablePeople(people[person].identifier, "{}".format(people[person].name), people[person].office_space, people[person].living_space, people[person].role)

			self.session.add(person)
			self.session.commit()

	def	retrieveState(self):
		people = self.session.query(TablePeople).order_by(TablePeople.id)
		rooms = self.session.query(TableRoom).order_by(TableRoom.id)
		return {'people':people, 'rooms':rooms}
