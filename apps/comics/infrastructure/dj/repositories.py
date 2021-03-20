from typing import List

from apps.comics.domain.entities import Comic, Rental
from apps.comics.domain.exceptions import ComicNotFound
from apps.comics.domain.repositories import ComicRepository, RentalRepository
from apps.comics.domain.vo import ComicId

from .comicsapp.models import Comic as ComicModel
from .comicsapp.models import Rental as RentalModel



class ComicDjangoRepository(ComicRepository):

    def all(self) -> List[Comic]:
        comics = ComicModel.objects.all()
        return comics
    
    def findByIdOrFail(self, id: ComicId) -> Comic:
        try:
            object = ComicModel.objects.get(pk=id.value)
            return Comic(
                id=object.id,
                name=object.name,
                price=object.price,
                status=object.status
            )
        except ComicModel.DoesNotExist:
            raise ComicNotFound


class RentalDjangoRepository(RentalRepository):

    def save(self, rent: Rental) -> bool:
        comic = ComicModel.objects.get(pk=rent.comicId.value)
        object = RentalModel(
            id=rent.id,
            days=rent.days,
            price=comic.price,
            amount=rent.amount,
            client=rent.client,
            rented_at=rent.rented_at,
            finished_at=rent.get_finished_at,
            comic=comic
        )

        object.save()

    def last_rental(self) -> Rental:
        object = RentalModel.objects.last()
        return Rental(
            id=object.id,
            days=object.days,
            client=object.client,
            rented_at=object.rented_at,
            finished_at=object.finished_at,
            price=object.price,
            amount=object.amount,
            comicId=ComicId(object.comic.id)
        )
