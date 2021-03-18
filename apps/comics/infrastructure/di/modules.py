from injector import Module

from apps.comics.domain.repositories import ComicRepository

from ..dj.repositories import ComicDjangoRepository


class ComicModule(Module):

    def configure(self, binder):
        binder.bind(ComicRepository, to=ComicDjangoRepository)
