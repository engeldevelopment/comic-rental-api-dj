from factory.django import DjangoModelFactory

from apps.comics.domain.vo import ComicStatus

from .models import Comic


class ComicFactory(DjangoModelFactory):
    class Meta:
        model = Comic
    
    name = 'Comic'
    price = 100
    status = ComicStatus.ACCEPTABLE.value
