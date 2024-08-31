#!/usr/bin/env python3
"""
    Implement a hash_password function
    that expects one string argument name password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        returns a salted, hashed password,
        which is a byte string
    """

    salt = bcrypt.gensalt()

    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        validate that the provided password
        matches the hashed passwor
    """

    password = password.encode('utf-8')
    salt = bcrypt.gensalt()

    new_password = bcrypt.hashpw(password, salt)

    return (hashed_password == new_password)
