from injector import inject

from ..application.commands import RentComicCommand
from ..application.finders import LastRentalFinder
from ..domain.entities import Rental
from ..domain.exceptions import ComicNotFound
from ..domain.services import ObtainAmountToPayService
from ..domain.repositories import ComicRepository, RentalRepository
from ..domain.vo import ComicId


class RentComicService:
    @inject
    def __init__(self,
        comic_repository: ComicRepository,
        rental_repository: RentalRepository,
        last_rental_finder: LastRentalFinder,
        obtain_amount_to_pay: ObtainAmountToPayService
    ):
        self.comic_repository = comic_repository
        self.rental_repository = rental_repository
        self.last_rental_finder = last_rental_finder
        self.obtain_amount_to_pay = obtain_amount_to_pay

    def __call__(self, command: RentComicCommand):
        comic = self.comic_repository.findByIdOrFail(
            id=ComicId(command.comicId)
        )
        
        amount = self.obtain_amount_to_pay(
            comic=comic
        )

        rent = Rental(
            id=command.id,
            days=command.days,
            client=command.client,
            rented_at=command.rented_at,
            comicId=ComicId(command.comicId),
            amount=amount
        )

        self.rental_repository.save(rent)
        return self.last_rental_finder()
