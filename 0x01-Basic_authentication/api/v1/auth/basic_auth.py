#!/usr/bin/env python3
"""Create a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
import base64
from models.base import Base
from models.user import User
from typing import TypeVar


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
            return decoded.decode('utf-8')
        except (base64.binascii.Error, ValueError):
            return None

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
        seek = decoded_base64_authorization_header.split(":", 1)
        new_decode = decoded_base64_authorization_header.find(":", check + 1)

        if check == -1:
            return None, None

        return seek[0], seek[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """Basic - User object"""

        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})

            if not users or len(users) == 0:
                return None

            user = users[0]

            if not user.is_valid_password(user_pwd):
                return None
            return user

        except Exception as e:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            overloads Auth and retrieves
            the User instance for a request
        """

        autho = self.authorization_header(request)
        d_base64 = self.extract_base64_authorization_header(autho)
        decode = self.decode_base64_authorization_header(d_base64)
        extract = self.extract_user_credentials(decode)
        cre = self.user_object_from_credentials(extract[0], extract[1])
        return cre
