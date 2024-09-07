#!/usr/bin/env python3
"""A class SessionExpAuth that inherits from SessionAuth"""
from os import getenv
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """a class SessionExpAuth that inherits from SessionAuth"""

    def __init__(self):
        """Assign an instance attribute session_duration"""

        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a Session ID by calling super() - super()"""

        check = super().create_session(user_id)
        if not check:
            return None

        self.user_id_by_session_id[check] = {
                "user_id": user_id,
                "created_at": datetime.now()
        }
        return check

    def user_id_for_session_id(self, session_id=None):
        """Overload from parent class"""

        if session_id is None:
            return None

        session_data = self.user_id_by_session_id.get(session_id)
        if not session_data:
            return None

        if self.session_duration <= 0:
            return session_data.get("user_id")

        created_at = session_data.get("created_at")
        if not created_at:
            return None

        date = datetime.now()
        expire = created_at + \
            timedelta(seconds=self.session_duration)
        if expire < date:
            return None

        return session_data.get("user_id")
