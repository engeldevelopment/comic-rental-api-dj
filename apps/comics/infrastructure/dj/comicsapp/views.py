from rest_framework import generics

from injector import inject

from apps.comics.domain.repositories import ComicRepository

from .models import Comic
from .serializers import ComicSerializer


class ComicListAPIView(generics.ListAPIView):
    serializer_class = ComicSerializer

    @inject
    def __init__(self, repository: ComicRepository, *args, **kwargs):
        self.repository = repository
        return super().__init__(*args, **kwargs)

    def get_queryset(self):
        queryset = self.repository.all()
        return queryset
