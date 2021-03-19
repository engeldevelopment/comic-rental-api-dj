from injector import inject

from ..application.commands import ComicRentCommand
from ..domain.repositories import RentRepository

from ..domain.entities import Rent
from ..domain.services import ObtainAmountToPayService
from ..domain.vo import ComicId


class ComicRentService:
    @inject
    def __init__(self,
        repository: RentRepository,
        obtain_amount: ObtainAmountToPayService
    ):
        self.repository = repository
        self.obtain_amount = obtain_amount

    def __call__(self, command: ComicRentCommand):
        amount = self.obtain_amount(
            comicId=ComicId(command.comicId)
        )

        rent = Rent(
            id=command.id,
            days=command.days,
            client=command.client,
            rented_at=command.rented_at,
            comicId=ComicId(command.comicId),
            amount=amount
        )

        if self.repository.save(rent):
            return True
