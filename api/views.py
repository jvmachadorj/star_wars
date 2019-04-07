from rest_framework import generics, filters

from api.models import Planet
from api.serializers import PlanetListSerializer, PlanetCreateSerializer
from api.star_wars_api_communication import get_movie_appearance_by_name


class PlanetListView(generics.ListAPIView):
    """
    Return a list of registered Star Wars Planets in the database
    You can search with ?search= in the end of url
    """
    queryset = Planet.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')
    serializer_class = PlanetListSerializer


class PlanetCreateView(generics.CreateAPIView):
    """
    Create a new Planet and automatically search how many movie appearance
    it has
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetCreateSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name', None)
        movie_appearance = get_movie_appearance_by_name(name)
        serializer.save(movie_appearance=movie_appearance)


class PlanetRetriveDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Update and delete a planet instance
    """
    serializer_class = PlanetCreateSerializer
    lookup_field = 'pk'
    queryset = Planet.objects.all()
