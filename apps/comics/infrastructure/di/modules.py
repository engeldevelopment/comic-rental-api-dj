from injector import Module, singleton

from apps.comics.domain.services import ObtainAmountToPayService
from apps.comics.domain.repositories import ComicRepository, RentalRepository
from apps.comics.application.finders import ComicAllFinder, LastRentalFinder, AllRentalFinder
from apps.comics.application.services import RentComicService

from ..dj.repositories import ComicDjangoRepository, RentalDjangoRepository


class ComicModule(Module):

    def configure(self, binder):
        binder.bind(AllRentalFinder, to=AllRentalFinder)
        binder.bind(ComicAllFinder, scope=singleton)
        binder.bind(ComicRepository, to=ComicDjangoRepository)
        binder.bind(LastRentalFinder, to=LastRentalFinder)
        binder.bind(ObtainAmountToPayService, to=ObtainAmountToPayService)
        binder.bind(RentComicService, to=RentComicService)
        binder.bind(RentalRepository, to=RentalDjangoRepository)
