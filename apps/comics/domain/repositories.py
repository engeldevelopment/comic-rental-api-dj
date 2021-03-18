import abc


class ComicRepository(abc.ABC):
    @abc.abstractmethod
    def all(self):
        pass
