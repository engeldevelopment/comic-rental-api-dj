import abc

from typing import List

from .entities import Comic, Rental
from .vo import ComicId


class ComicRepository(abc.ABC):
    @abc.abstractmethod
    def all(self) -> List[Comic]:
        pass

    @abc.abstractmethod
    def find_by_id_or_fail(self, id: ComicId) -> Comic:
        pass


class RentalRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, rental: Rental) -> bool:
        pass

    @abc.abstractmethod
    def last_rental(self) -> Rental:
        pass
