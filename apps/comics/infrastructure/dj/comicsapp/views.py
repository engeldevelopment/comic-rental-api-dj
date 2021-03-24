from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from injector import inject

from apps.comics.application.commands import RentComicCommand
from apps.comics.application.finders import ComicAllFinder
from apps.comics.application.services import RentComicService
from apps.comics.domain.exceptions import ComicNotFound, InvalidDays

from .serializers import ComicSerializer


class ComicListAPIView(generics.ListAPIView):
    serializer_class = ComicSerializer

    @inject
    def __init__(self, finder: ComicAllFinder, **kwargs):
        super().__init__(**kwargs)
        self.finder = finder

    def get_queryset(self):
        return self.finder()


class ComicRentAPIView(APIView):

    @inject
    def __init__(self, rent_comic_service: RentComicService, **kwargs):
        super().__init__(**kwargs)
        self.rent_comic_service = rent_comic_service

    def post(self, request, pk):
        command = RentComicCommand(
            id=request.data.get('id', None),
            days=request.data.get('days', ""),
            client=request.data['client'],
            rented_at=request.data['rented_at'],
            comic_id=pk
        )

        try:
            new_rent = self.rent_comic_service(command=command)
            return Response(
                data=new_rent.to_json,
                status=status.HTTP_201_CREATED
            )
        except ComicNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except InvalidDays as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
