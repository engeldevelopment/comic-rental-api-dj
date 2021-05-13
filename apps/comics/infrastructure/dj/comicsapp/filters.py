from django_filters import rest_framework as filters

from .models import Comic


class ComicFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status")

    class Meta:
        model = Comic
        fields = ('status', )
