#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__= "cities"
    state_id = Column(String(60),  Foreign_Key("states.id", nullable=False,)
    name = Column(String(128), nullable=False)
