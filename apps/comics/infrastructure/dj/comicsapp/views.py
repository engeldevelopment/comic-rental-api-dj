from rest_framework import generics

from injector import inject

from apps.comics.application.finders import ComicAllFinder

from .serializers import ComicSerializer


class ComicListAPIView(generics.ListAPIView):
    serializer_class = ComicSerializer

    @inject
    def __init__(self, finder: ComicAllFinder, *args, **kwargs):
        self.finder = finder
        return super().__init__(*args, **kwargs)

    def get_queryset(self):
        return self.finder()
