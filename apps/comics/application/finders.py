from injector import inject

from ..domain.repositories import ComicRepository


class ComicAllFinder:
    @inject
    def __init__(self, repository: ComicRepository):
        self.repository = repository

    def __call__(self):
        return self.repository.all()
