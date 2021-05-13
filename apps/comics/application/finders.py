from injector import inject

from ..domain.repositories import ComicRepository, RentalRepository


class ComicAllFinder:
    @inject
    def __init__(self, repository: ComicRepository):
        self.repository = repository

    def __call__(self):
        return self.repository.all()


class LastRentalFinder:

    @inject
    def __init__(self, repository: RentalRepository):
        self.repository = repository
    
    def __call__(self):
        return self.repository.last_rental()


class AllRentalFinder:
    @inject
    def __init__(self, repository: RentalRepository):
        self.repository = repository

    def __call__(self):
        return self.repository.all()
