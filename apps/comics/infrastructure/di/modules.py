from injector import Module, singleton

from apps.comics.domain.services import ObtainAmountToPayService, ObtainPercentOfDiscount
from apps.comics.domain.repositories import ComicRepository, RentalRepository
from apps.comics.application.finders import ComicAllFinder, LastRentalFinder
from apps.comics.application.services import RentComicService

from ..dj.repositories import ComicDjangoRepository, RentalDjangoRepository


class ComicModule(Module):

    def configure(self, binder):
        binder.bind(ComicRepository, to=ComicDjangoRepository)
        binder.bind(ComicAllFinder, scope=singleton)
        binder.bind(RentComicService, to=RentComicService)
        binder.bind(RentalRepository, to=RentalDjangoRepository)
        binder.bind(ObtainAmountToPayService, to=ObtainAmountToPayService)
        binder.bind(ObtainPercentOfDiscount, to=ObtainPercentOfDiscount)
        binder.bind(LastRentalFinder, to=LastRentalFinder)
