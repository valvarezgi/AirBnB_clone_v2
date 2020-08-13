#!/usr/bin/python3
"""Data Storage"""
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """Data Base Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Init"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB'),
                                      pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Shows all the objects"""
        object_dict = {}
        if cls:
            for obj in self.__session.query((cls).all()):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                object_dict[key] = obj
        else: 
            for subclass in Base.__subclasses__():
                for obj in self.__session.query(subclass).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    object_dict[key] = obj
        return object_dict
    
    def new(self, obj):
        """adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes objects from the database"""
        if obj is not None:
            self.__session.__delete(obj)

    def reload(self):
        """creates all databases and a new session in SQLAlchemy"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
    
    def close(self):
        """Clses the session"""
        self.__session.remove()
