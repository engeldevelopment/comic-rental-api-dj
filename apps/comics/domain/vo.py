from enum import Enum
from dataclasses import dataclass


@dataclass
class ComicId:
    value: str


class ComicStatus(Enum):
    EXCELLENT = 'excellent'
    GOOD = 'good'
    ACCEPTABLE = 'acceptable'
    IMPAIRED = 'impaired'
    DAMAGED = 'damaged'
