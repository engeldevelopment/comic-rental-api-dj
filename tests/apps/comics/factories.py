from datetime import datetime

import factory

from apps.comics.domain.entities import Comic, Rental, Days
from apps.comics.domain.vo import ComicStatus, ComicId


class ComicFactory(factory.Factory):
    class Meta:
        model = Comic

    id = 23
    name = factory.Faker('name')
    price = 50.0
    status = ComicStatus.EXCELLENT.value


class RentalFactory(factory.Factory):
    class Meta:
        model = Rental

    id = None
    days = Days("3")
    client = 'Engel Pinto'
    rented_at = datetime.now()
    comic_id = ComicId(12)
