#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.review import Review
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', secondary='place_amenity', 
                             backref='places', viewonly=False)

    @property
    def reviews(self):
        """Getter"""
        rev_list = []
        rev_dict = models.storage.all(Review)
        for rev in rev_dict.values():
            if rev.place_id == self.id:
                rev_list.append(rev)
        return rev_list

    @property
    def amenities(self):
        """Getter"""
        amen_list = []
        amen_dict = models.storage.all(Amenity)
        for ame in amen_dict.values():
            if ame.id in self.amenity_ids:
                amen_list.append(amenity)
        return amen_list

    @amenities.setter
    def amenities(self, obj):
        """Setter"""
        if type(obj) == Amenity:
            self.amenity_ids.append(obj.id)
