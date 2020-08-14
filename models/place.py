#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, backref


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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade="all, delete",
                                backref=backref("place", cascade="all, delete"),
                                passive_deletes=True)
    else:
        @property
        def reviews(self):
            """REturns a list of instances reviews"""
            from models import storage
            return {key: value for key, value in storage.all().items()
                    if value.place_id == self.id}
