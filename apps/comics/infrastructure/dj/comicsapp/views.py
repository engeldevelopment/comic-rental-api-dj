from rest_framework import generics

from .models import Comic
from .serializers import ComicSerializer


class ComicListAPIView(generics.ListAPIView):
    serializer_class = ComicSerializer
    queryset = Comic.objects.all()
