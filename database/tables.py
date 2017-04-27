from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///database/andela.db', echo=True)
Base = declarative_base()
 
########################################################################
class TablePeople(Base):
    """"""
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    office_id = Column(Integer)
    living_space_id = Column(Integer)
    requires_living_space = Column(Integer)
    role = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, name, office_id, living_space_id, role):
        """"""
        self.name = name
        self.office_id = office_id
        self.living_space_id = living_space_id
        self.role = role


class TableRoom(Base):
    """"""
    __tablename__ = "room"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capacity = Column(Integer)
    type_id = Column(Integer)
 
    #----------------------------------------------------------------------
    def __init__(self, name, capacity, type_id):
        """"""
        self.name = name
        self.capacity = capacity
        self.type_id = type_id
  
# create tables
Base.metadata.create_all(engine)