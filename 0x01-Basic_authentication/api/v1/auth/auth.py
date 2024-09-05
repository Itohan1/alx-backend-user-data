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

        for j in excluded_paths:
            check = j.split("/", 3)
            ano = path.split("/", 3)
            if check[3][-1] == "*":
                if ano[3].find(check[3][:-1]) != -1:
                    return False

            if check[-1] == "/":
                if path[-1] != "/":
                    if path == j[:-1]:
                        return False

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
