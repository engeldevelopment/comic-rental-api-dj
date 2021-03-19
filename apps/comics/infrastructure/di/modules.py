from injector import Module, singleton

from apps.comics.domain.repositories import ComicRepository
from apps.comics.application.finders import ComicAllFinder

from ..dj.repositories import ComicDjangoRepository


class ComicModule(Module):

    def configure(self, binder):
        binder.bind(ComicRepository, to=ComicDjangoRepository)
        binder.bind(ComicAllFinder, scope=singleton)
