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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """Returns the user email and password
        from the Base64 decoded value"""

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        check = decoded_base64_authorization_header.find(":")

        if check == -1:
            return None, None

        seek = decoded_base64_authorization_header.split(":")
        return seek[0], seek[1]
