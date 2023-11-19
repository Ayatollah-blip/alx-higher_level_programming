#!/usr/bin/python3

"""

This script lists all states with name with N from the

database `hbtn_0e_0_usa`.

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class



    Attributes:

        __tablename__ (str): The table name of the class

        id (int): The State id of the class

        name (str): The State name of the class

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, state_id, name):
        self.id = state_id
        self.name=name
