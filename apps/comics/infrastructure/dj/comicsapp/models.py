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
    
    @property
    def price_with_discount(self):
        discount = 0
        DISCOUNTS = {
            'excelent': self.percent_of_discount(percent=10),
            'good': self.percent_of_discount(percent=20),
            'acceptable': self.percent_of_discount(percent=25),
            'impaired': self.percent_of_discount(percent=30),
            'damaged': self.percent_of_discount(percent=50)
        }

        discount = DISCOUNTS.get(self.status)
        return self.price - discount
    
    def percent_of_discount(self, percent):
        return (self.price * percent) / 100


class Rent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    days = models.PositiveIntegerField() 
    client = models.CharField(max_length=80)
    amount = models.FloatField()
    price = models.FloatField()
    rented_at = models.DateTimeField(editable=False)
    finished_at = models.DateTimeField(editable=False)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='rents')

    def save(self, *args, **kwargs):
        self.amount = self.comic.price_with_discount
        self.price = self.comic.price
        transform = datetime.strptime(self.rented_at, '%Y-%m-%d %H:%M:%S')
        self.finished_at = transform  + timedelta(days=int(self.days))
        return super().save(*args, **kwargs)
