#!/usr/bin/python3
"""DB STORAGE MANAGEMENT"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """A class defining methods and attributes for the database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the Object"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        environ = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    user, passwd, host, database), pool_pre_ping=True)
        if environ == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on current session all objects or of cls
        return a dictionary
        """
        classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}

        dict = {}
        if cls is None:
            for c in classes.values():
                objects = self.__session.query(c).all()
                for o in objects:
                    key = o.__class__.__name__ + '.' + o.id
                    dict[key] = o
        else:
            objects = self.__session.query(cls).all()
            for o in objects:
                key = o.__class__.__name__ + '.' + o.id
                dict[key] = o
        return dict

    def new(self, obj):
        """
        adds obj to current db session
        """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """
        commit all changes of current session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj from current db session
        """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                    type(obj).id == obj.id).delete()

    def reload(self):
        """
        create all tables, create current db session
        """
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.base_model import Base
        from models.city import City

        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_maker)()

    def close(self)
        """
        closes the session
        """
        self.__session.close()
