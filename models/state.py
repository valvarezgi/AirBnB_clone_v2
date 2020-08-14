#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        """getter for cities"""

        result = []
        cities_dict = models.storage.all(City)
        for key, city in cities_dict.items():
            if city.state_id == self.id:
                result.append(city)
        return result
