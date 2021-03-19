from injector import inject

from ..domain.repositories import ComicRepository, RentRepository


class ComicAllFinder:
    @inject
    def __init__(self, repository: ComicRepository):
        self.repository = repository

    def __call__(self):
        return self.repository.all()


class LastRentFinder:

    @inject
    def __init__(self, repository: RentRepository):
        self.repository = repository
    
    def __call__(self):
        return self.repository.last_rent()
