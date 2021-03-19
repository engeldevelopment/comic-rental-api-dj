import abc

from typing import List

from .entities import Comic, Rent


class ComicRepository(abc.ABC):
    @abc.abstractmethod
    def all(self) -> List[Comic]:
        pass


class RentRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, rent: Rent) -> bool:
        pass
