#!/usr/bin/python3
"""Class definition of a City and an
instance Base = declarative_base()."""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class that defines the State instances"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
