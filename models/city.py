#!/usr/bin/python3
"""A module that contains a class `City` that inherits from BaseModel

Public class attribute:
    state_id (string) - empty string: it will be the State.id
    name (string) - empty string
"""
from models.base_model import BaseModel


# Task 9
class City(BaseModel):
    """A class City that inherits from BaseModel
    """
    state_id = ''
    name = ''
