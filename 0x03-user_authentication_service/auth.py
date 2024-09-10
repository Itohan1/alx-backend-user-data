#!/usr/bin/env python3
"""Returned bytes is a salted hash of the input password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes"""

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user"""

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            check = _hash_password(password)
            return(self._db.add_user(email, check))
        raise ValueError(f'User {email} already exists')
