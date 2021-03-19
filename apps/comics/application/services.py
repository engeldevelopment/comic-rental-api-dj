from injector import inject

from ..application.commands import ComicRentCommand
from ..domain.repositories import RentRepository

from ..domain.entities import Rent
from ..domain.vo import ComicId


class ComicRentService:
    @inject
    def __init__(self, repository: RentRepository):
        self.repository = repository

    def __call__(self, command: ComicRentCommand):
        rent = Rent(
            id=command.id,
            days=command.days,
            client=command.client,
            rented_at=command.rented_at,
            comicId=ComicId(command.comic.id),
        )

        if self.repository.save(rent):
            return True

