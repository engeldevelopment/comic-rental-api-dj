from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from injector import inject

from apps.comics.application.commands import RentComicCommand
from apps.comics.application.finders import ComicAllFinder, AllRentalFinder
from apps.comics.application.services import RentComicService
from apps.comics.domain.exceptions import ComicNotFound, InvalidDays, ThisIsNotAValidName

from .serializers import ComicSerializer, RentalSerializer


class ComicListAPIView(generics.ListAPIView):
    serializer_class = ComicSerializer

    @inject
    def setup(self, request, finder: ComicAllFinder, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.finder = finder

    def get_queryset(self):
        return self.finder()


class ComicRentAPIView(APIView):
    @inject
    def setup(
        self,
        request,
        rent_comic_service: RentComicService,
        *args,
        **kwargs
    ):
        super().setup(request, *args, **kwargs)
        self.rent_comic_service = rent_comic_service

    def post(self, request, pk):
        command = RentComicCommand(
            id=request.data.get('id', None),
            days=request.data.get('days', ""),
            client=request.data.get('client', ""),
            rented_at=request.data.get('rented_at', None),
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
        except ThisIsNotAValidName as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RentalListAPIView(generics.ListAPIView):
    serializer_class = RentalSerializer

    @inject
    def setup(self, request, finder: AllRentalFinder, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.finder = finder

    def get_queryset(self):
        return self.finder()
