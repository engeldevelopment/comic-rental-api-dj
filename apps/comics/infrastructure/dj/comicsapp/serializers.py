from rest_framework import serializers

from .models import Comic, Rental


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = (
            'id',
            'name',
            'price', 
            'status',
        )


class RentalSerializer(serializers.ModelSerializer):
    comic = ComicSerializer(read_only=True, many=False, required=False)

    class Meta:
        model = Rental
        fields = [
            "id",
            "days",
            "client",
            "amount",
            "price",
            "comic",
            "rented_at",
            "finished_at",
        ]
