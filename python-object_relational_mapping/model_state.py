#!/usr/bin/python3
"""
Script that contains the class definition of a 'State' and
an instance 'Base = declarative_base()':
- 'State' class:
    - inherits from 'Base'
    - links to the MySQL table 'state'
    - class attribute 'id' that represents a column of an auto-generated,
    unique integer, can't be null and is a primary key
    - class attribute 'name' that represents a column of a string with
    maximum 128 characters and can't be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class which inherits from Base"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
