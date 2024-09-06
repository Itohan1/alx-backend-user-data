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

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get user id from session_id key"""

        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Get a User based on his session ID"""

        from api.v1.views.users import User

        user = User()
        if not self.session_cookie(request):
            return None

        session_id = self.session_cookie(request)

        if not session_id:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if not user:
            return None

        return user
