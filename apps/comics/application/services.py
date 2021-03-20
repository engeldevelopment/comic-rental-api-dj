from injector import inject

from ..application.commands import RentComicCommand
from ..application.finders import LastRentFinder
from ..domain.entities import Rent
from ..domain.exceptions import ComicNotFound
from ..domain.services import ObtainAmountToPayService
from ..domain.repositories import ComicRepository, RentRepository
from ..domain.vo import ComicId


class RentComicService:
    @inject
    def __init__(self,
        comic_repository: ComicRepository,
        rent_repository: RentRepository,
        last_rent_finder: LastRentFinder,
        obtain_amount_to_pay: ObtainAmountToPayService
    ):
        self.comic_repository = comic_repository
        self.rent_repository = rent_repository
        self.last_rent_finder = last_rent_finder
        self.obtain_amount_to_pay = obtain_amount_to_pay

    def __call__(self, command: RentComicCommand):
        comic = self.comic_repository.findByIdOrFail(
            id=ComicId(command.comicId)
        )
        
        amount = self.obtain_amount_to_pay(
            comic=comic
        )

        rent = Rent(
            id=command.id,
            days=command.days,
            client=command.client,
            rented_at=command.rented_at,
            comicId=ComicId(command.comicId),
            amount=amount
        )

        self.rent_repository.save(rent)
        return self.last_rent_finder()
