from apps.comics.domain.repositories import ComicRepository

from .comicsapp.models import Comic


class ComicDjangoRepository(ComicRepository):

    def all(self):
        return Comic.objects.all()
