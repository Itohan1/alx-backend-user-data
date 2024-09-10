#!/usr/bin/env python3
"""Returned bytes is a salted hash of the input password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Takes in a password string arguments and returns bytes"""

        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), salt)

        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """Register user"""

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            check = self._hash_password(password)
            return(self._db.add_user(email, check))
        raise ValueError(f'User {email} already exists')
