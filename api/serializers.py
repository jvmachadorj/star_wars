from rest_framework import serializers

from api.models import Planet


class PlanetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        exclude = ()


class PlanetCreateSerializer(serializers.ModelSerializer):
    movie_appearance = serializers.IntegerField(read_only=True)

    class Meta:
        model = Planet
        exclude = ()
