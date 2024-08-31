#!/usr/bin/env python3
"""
    Write a function called filter_datum
    that returns the log message obfuscated
"""
import logging
import re
import csv
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")
patterns = {
    'collect': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """A logged message"""

    collect, replace = (patterns["collect"], patterns["replace"])
    return re.sub(collect(fields, separator), replace(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Update the class to accept a list
            of strings fields constructor argument
        """

        message = super(RedactingFormatter, self).format(record)
        incoming = filter_datum(
                self.fields, RedactingFormatter.REDACTION,
                message, RedactingFormatter.SEPARATOR)
        return incoming


def get_logger(self) -> logging.Logger:
    """
        Function that takes no arguments
        and returns a logging.Logger object
    """

    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger
