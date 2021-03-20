import abc

from typing import List

from .entities import Comic, Rent
from .vo import ComicId


class ComicRepository(abc.ABC):
    @abc.abstractmethod
    def all(self) -> List[Comic]:
        pass

    @abc.abstractmethod
    def findByIdOrFail(self, id: ComicId) -> Comic:
        pass


class RentRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, rent: Rent) -> bool:
        pass

    @abc.abstractmethod
    def last_rent(self) -> Rent:
        pass
