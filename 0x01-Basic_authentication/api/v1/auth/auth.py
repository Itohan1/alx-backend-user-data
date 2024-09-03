#!/usr/bin/env python3
"""A class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication"""

    def require_auth(
            self, path: str, excluded_paths: List[str]) -> bool:

        """ Returns False - path"""

        self.path = False

        return self.path

    def authorization_header(self, request=None) -> str:
        """Returns None - request"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request"""

        return None
