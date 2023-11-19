#!/usr/bin/python3

"""

This script lists all states with name with N from the

database `hbtn_0e_0_usa`.

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    __tablename__ = 'states'

    id = Column(Integer, Primary_key=True)
    name = Column(String(128), nullable=False)

    """def __init__(self, state_id, name):
        self.state_id = state_id
        self.name=name
    """
