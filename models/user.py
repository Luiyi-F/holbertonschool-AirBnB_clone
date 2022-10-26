#!/usr/bin/python3
"""
Module user with defines user Class
"""
from .base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""