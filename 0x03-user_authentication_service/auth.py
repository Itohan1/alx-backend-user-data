#!/usr/bin/env python3
"""Returned bytes is a salted hash of the input password"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes"""

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
