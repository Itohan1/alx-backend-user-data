#!/usr/bin/env python3
"""Create a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string"""

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(
                    base64_authorization_header, validate=True)

        except (base64.binascii.Error, ValueError):
            return None

        return decoded.decode('utf-8')
