from datetime import datetime, timedelta

import uuid

from django.db import models


COMIC_STATUS = (
    ('excelent', 'Excelente'),
    ('good', 'Buena'),
    ('acceptable', 'Aceptable'),
    ('damaged', 'Deteriorada'),
    ('impaired', 'Dañada'),
)

class Comic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.0)
    status = models.CharField(max_length=11, choices=COMIC_STATUS)

    def __str__(self):
        return self.name


class Rent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    days = models.PositiveIntegerField() 
    client = models.CharField(max_length=80)
    amount = models.FloatField()
    price = models.FloatField()
    rented_at = models.DateTimeField(editable=False)
    finished_at = models.DateTimeField(editable=False)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='rents')
