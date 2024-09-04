#!/usr/bin/env python3
"""Create a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class instead of Auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization"""

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        check = authorization_header.split(" ")
        if check[0] != "Basic":
            return None

        check.remove("Basic")
        for i in check:
            return i
