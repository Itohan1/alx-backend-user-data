#!/usr/bin/env python3
"""A class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication"""

    def require_auth(
            self, path: str, excluded_paths: List[str]) -> bool:

        """ Returns False - path"""

        if not excluded_paths:
            return True

        if path is None:
            return True

        if path in excluded_paths:
            return False

        if path[-1] != "*":
            for i in excluded_paths:
                if path == i[:-1]:
                    return False

        if path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """Returns None - request"""

        if request is None:
            return None

        authorization = request.headers.get('Authorization')

        if not authorization:
            return None

        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request"""

        return None
