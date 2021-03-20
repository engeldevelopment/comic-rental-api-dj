from typing import List

from apps.comics.domain.entities import Comic, Rent
from apps.comics.domain.exceptions import ComicNotFound
from apps.comics.domain.repositories import ComicRepository, RentRepository
from apps.comics.domain.vo import ComicId

from .comicsapp.models import Comic as ComicModel
from .comicsapp.models import Rent as RentModel



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


class RentDjangoRepository(RentRepository):

    def save(self, rent: Rent) -> bool:
        comic = ComicModel.objects.get(pk=rent.comicId.value)
        object = RentModel(
            id=rent.id,
            days=rent.days,
            price=comic.price,
            amount=rent.amount,
            client=rent.client,
            rented_at=rent.rented_at,
            finished_at=rent.get_finished_at,
            comic=comic
        )

        try:
            object.save()
            return True
        except:
            return False

    def last_rent(self) -> Rent:
        object = RentModel.objects.last()
        return Rent(
            id=object.id,
            days=object.days,
            client=object.client,
            rented_at=object.rented_at,
            finished_at=object.finished_at,
            price=object.price,
            amount=object.amount,
            comicId=ComicId(object.comic.id)
        )
