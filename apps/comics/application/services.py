from injector import inject

from ..application.commands import ComicRentCommand
from ..domain.entities import Rent
from ..domain.exceptions import ComicNotFound
from ..domain.services import ObtainAmountToPayService
from ..domain.repositories import ComicRepository, RentRepository
from ..domain.vo import ComicId


class ComicRentService:
    @inject
    def __init__(self,
        comic_repository: ComicRepository,
        rent_repository: RentRepository,
        obtain_amount: ObtainAmountToPayService
    ):
        self.comic_repository = comic_repository
        self.rent_repository = rent_repository
        self.obtain_amount = obtain_amount

    def __call__(self, command: ComicRentCommand):
        try:
            comic = self.comic_repository.findById(
                id=ComicId(command.comicId)
            )
        except ComicNotFound as e:
            raise e
        
        amount = self.obtain_amount(
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
