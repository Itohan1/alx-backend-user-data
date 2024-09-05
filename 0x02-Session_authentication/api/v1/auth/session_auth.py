#!/usr/bin/env python3
"""Create a class SessionAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Create a class SessionAuth that inherits from Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            The same user_id can have multiple
            Session ID - indeed, the user_id
            is the value in the dictionary
            user_id_by_session_id
        """

        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id

        return session_id
