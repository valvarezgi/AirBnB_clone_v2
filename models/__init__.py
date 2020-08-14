#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
