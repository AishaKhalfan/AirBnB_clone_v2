#!/usr/bin/python3
"""DB STORAGE MANAGEMENT"""
from sqlalchemy import create_engine
import os


class DBStorage():
    """A class defining methods and attributes for the database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the Object"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database,
                                       pool_pre_ping=True)
