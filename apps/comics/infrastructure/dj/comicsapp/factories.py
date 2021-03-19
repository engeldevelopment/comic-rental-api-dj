from factory.django import DjangoModelFactory

from .models import Comic


class ComicFactory(DjangoModelFactory):
    class Meta:
        model = Comic
    
    name = 'Comic'
    price = 100
    status = 'acceptable'
