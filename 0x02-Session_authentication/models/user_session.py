#!/usr/bin/env python3
"""Create a new model UserSession"""
from models.base import Base


class UserSession(Base):
    """Create a new model UserSession"""

    def __init__(self, *args: list, **kwargs: dict):
        """Overload the base __init__ method"""

        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
