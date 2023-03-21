#!/usr/bin/python3
"""This module instantiates an object of Storage"""
from os import getenv
store_type = getenv('HBNB_TYPE_STORAGE')

if store_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
