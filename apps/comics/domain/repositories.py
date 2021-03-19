import abc

from typing import List

from .entities import Comic


class ComicRepository(abc.ABC):
    @abc.abstractmethod
    def all(self) -> List[Comic]:
        pass
