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
