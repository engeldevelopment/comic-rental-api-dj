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
