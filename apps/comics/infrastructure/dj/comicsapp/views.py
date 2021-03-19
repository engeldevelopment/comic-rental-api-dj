from datetime import date

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from injector import inject

from apps.comics.application.finders import ComicAllFinder

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


@api_view(['POST'])
def rent_comic(request, pk):
    comic = get_object_or_404(Comic,pk=pk)

    rent = Rent(
        id=request.data['id'],
        days=request.data['days'],
        client=request.data['client'],
        rented_at=request.data['rented_at'],
        comic=comic
    )

    rent.save()
    data = {
        'id': str(rent.id),
        'days': rent.days,
        'amount': rent.amount,
        'price': rent.price,
        'client': rent.client,
        'rented_at': rent.rented_at,
        'finished_at': rent.finished_at
    }

    return Response(data, status=status.HTTP_201_CREATED)
