import uuid

from django.db import models

from apps.comics.domain.vo import ComicStatus

COMIC_STATUS = (
    (ComicStatus.EXCELLENT.value, 'Excelente'),
    (ComicStatus.GOOD.value, 'Buena'),
    (ComicStatus.ACCEPTABLE.value, 'Aceptable'),
    (ComicStatus.IMPAIRED.value, 'Deteriorada'),
    (ComicStatus.DAMAGED.value, 'Dañada'),
)


class Comic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.0)
    status = models.CharField(max_length=11, choices=COMIC_STATUS)

    def __str__(self):
        return self.name


class Rental(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    days = models.PositiveIntegerField() 
    client = models.CharField(max_length=80)
    amount = models.FloatField()
    price = models.FloatField()
    rented_at = models.DateTimeField(editable=False)
    finished_at = models.DateTimeField(editable=False)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='rents')
