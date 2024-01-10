#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
import models
from models.base_model import Base, BaseModel
from models.city import City

class State(BaseModel):
    """ State class """
    name = ""
    if environ.get('HBNB_TYPE_STORAGE') == 'db':

        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan",
                              passive_deletes=True)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """This function initializes state"""
        super().__init__(*args, **kwargs)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ This function return the list of City objects from storage linked to the current State

            Returns: cities in a state
            """
            return [city for city in models.storage.all(
                City).values() if city.state_id == self.id]
