import re
import uuid
from datetime import datetime
from enum import Enum
from dataclasses import dataclass

from .exceptions import InvalidDays, ThisIsNotAValidName


class ComicClient:
    valid_name = re.compile(r'\w+\D')

    def __init__(self, value):
        if self.valid_name.match(value) is None:
            raise ThisIsNotAValidName(f"This is not a valid name for a client '{value}'.")
        self.value = value


@dataclass
class ComicId:
    value: str


class ComicStatus(Enum):
    EXCELLENT = 'excellent'
    GOOD = 'good'
    ACCEPTABLE = 'acceptable'
    IMPAIRED = 'impaired'
    DAMAGED = 'damaged'


class Days:
    only_number = re.compile(r"(\-\d|\d)+")

    def __init__(self, value):
        if value is None:
            raise InvalidDays('Days is required.')
        if self.only_number.match(str(value)) is None:
            raise InvalidDays(f"This is not a number '{value}.'")
        if int(value) <= 0:
            raise InvalidDays(f"This is not a valid days '{value}'.")
        self.value = int(value)


class UUID:
    def __init__(self, value):
        if value is None:
            value = uuid.uuid4()
        self.value = value


class RentedAt:
    def __init__(self, value):
        if value is None:
            value = datetime.now()
        self.value = value
