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

    for field in fields:
        pattern = pattern = rf'({field}={separator}?)\S+'
    return re.sub(pattern, rf'\1{redaction}', message)
