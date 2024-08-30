#!/usr/bin/env python3
"""
    Write a function called filter_datum
    that returns the log message obfuscated
"""
import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """A logged message"""

    pattern = rf"""({re.escape(field) for field in fields
    }){re.escape(separator)}[^;]*"""
    return re.sub(pattern, lambda match: f"""
            {match.group(1)}{separator}{redaction}""", message)
