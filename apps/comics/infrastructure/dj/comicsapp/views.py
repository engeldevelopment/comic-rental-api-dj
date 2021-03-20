from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from injector import inject

from apps.comics.application.commands import ComicRentCommand
from apps.comics.application.finders import ComicAllFinder
from apps.comics.application.finders import LastRentFinder
from apps.comics.application.services import ComicRentService
from apps.comics.domain.exceptions import ComicNotFound

from .models import Comic, Rent
from .serializers import ComicSerializer


class ComicListAPIView(generics.ListAPIView):
    serializer_class = ComicSerializer

    @inject
    def __init__(self, finder: ComicAllFinder, *args, **kwargs):
        self.finder = finder
        return super().__init__(*args, **kwargs)

    def get_queryset(self):
        return self.finder()


class ComicRentAPIView(APIView):

    @inject
    def __init__(
        self,
        comic_rent_service: ComicRentService,
        last_rent_finder: LastRentFinder,
        *args,
        **kwargs
    ):
        self.comic_rent_service = comic_rent_service
        self.last_rent_finder = last_rent_finder
        return super().__init__(*args, **kwargs)
    
    def post(self, request, pk):
        command = ComicRentCommand(
            id=request.data.get('id', None),
            days=request.data['days'],
            client=request.data['client'],
            rented_at=request.data['rented_at'],
            comicId=pk
        )

        try:
            self.comic_rent_service(command=command)
            new_rent = self.last_rent_finder()
            return Response(
                data=new_rent.to_json,
                status=status.HTTP_201_CREATED
            )
        except ComicNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
