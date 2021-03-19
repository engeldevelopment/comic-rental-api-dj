from typing import List

from apps.comics.domain.repositories import ComicRepository, RentRepository
from apps.comics.domain.entities import Comic, Rent

from .comicsapp.models import Comic as ComicModel
from .comicsapp.models import Rent as RentModel


class ComicDjangoRepository(ComicRepository):

    def all(self) -> List[Comic]:
        comics = ComicModel.objects.all()
        return comics


class RentDjangoRepository(RentRepository):

    def save(self, rent: Rent) -> bool:
        comic = ComicModel.objects.get(pk=rent.comicId.value)
        object = RentModel(
            id=rent.id,
            days=rent.days,
            client=rent.client,
            rented_at=rent.rented_at,
            finished_at=rent.get_finished_at,
            comic=comic
        )

        try:
            object.save()
            return True
        except e:
            return False
