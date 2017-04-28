from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///data/andela.db', echo=False)
Base = declarative_base()

########################################################################
class TablePeople(Base):
    """"""
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    identifier = Column(String, nullable=True, unique=False)
    name = Column(String)
    office_space = Column(String, nullable=True)
    living_space = Column(String, nullable=True)
    requires_living_space = Column(String, nullable=True)
    role = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, identifier, name, office_space, living_space, role):
        """"""
        self.name = name
        self.office_space = office_space
        self.living_space = living_space
        self.role = role
        self.identifier = identifier


class TableRoom(Base):
    """"""
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupants = Column(String)
    max_capacity = Column(String)
    room_type = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, name, occupants, max_capacity, room_type):
        """"""
        self.name = name
        self.max_capacity = max_capacity
        self.room_type = room_type
        self.occupants = occupants

# create tables
Base.metadata.create_all(engine)