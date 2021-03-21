import factory

from apps.comics.domain.entities import Comic
from apps.comics.domain.vo import ComicStatus


class ComicFactory(factory.Factory):
    class Meta:
        model = Comic

    id = 23
    name = factory.Faker('name')
    price = 50.0
    status = ComicStatus.EXCELLENT.value
