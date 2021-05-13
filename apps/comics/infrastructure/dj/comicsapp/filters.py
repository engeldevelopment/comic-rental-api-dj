from django_filters import rest_framework as filters

from .models import Comic
from .models import COMIC_STATUS


class ComicFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=COMIC_STATUS)

    class Meta:
        model = Comic
        fields = ('status', )
