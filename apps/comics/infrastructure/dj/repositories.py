from typing import List

from apps.comics.domain.repositories import ComicRepository
from apps.comics.domain.entities import Comic

from .comicsapp.models import Comic as ComicModel


class ComicDjangoRepository(ComicRepository):

    def all(self) -> List[Comic]:
        comics = ComicModel.objects.all()
        return comics
