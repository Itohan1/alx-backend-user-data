#!/usr/bin/env python3
"""Returned bytes is a salted hash of the input password"""
import bcrypt
from db import DB
from user import User
from typing import Optional, Union
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes"""

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """Generate uuids"""

    new_id = str(uuid.uuid4())
    return new_id


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

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""

        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(
                        password.encode('utf-8'),
                        user.hashed_password)
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """Create session ID"""

        try:
            user = self._db.find_user_by(email=email)
            new_id = _generate_uuid()
            user.session_id = new_id
            return new_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Find user by session ID"""

        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            if user is None:
                return None
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy session"""

        if user_id is None:
            return None

        try:
            user = self._db.find_user_by(id=user_id)
            if user is None:
                return None
            user["session_id"] = None
            return user["session_id"]
        except NoResultFound:
            return None
