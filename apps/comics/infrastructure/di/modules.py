from injector import Module, singleton

from apps.comics.domain.repositories import ComicRepository, RentRepository
from apps.comics.application.finders import ComicAllFinder
from apps.comics.application.services import ComicRentService

from ..dj.repositories import ComicDjangoRepository, RentDjangoRepository


class ComicModule(Module):

    def configure(self, binder):
        binder.bind(ComicRepository, to=ComicDjangoRepository)
        binder.bind(ComicAllFinder, scope=singleton)
        binder.bind(ComicRentService, to=ComicRentService)
        binder.bind(RentRepository, to=RentDjangoRepository)
