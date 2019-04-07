from requests import request
from rest_framework import status

from start_wars.settings import STAR_WARS_BASE_PLANET_URL


def get_movie_appearance_by_name(name: str) -> int:
    url = '{}?search={}'.format(STAR_WARS_BASE_PLANET_URL, name)
    method = 'GET'
    response = request(method, url)
    results = response.json().get('results')

    if response.status_code == status.HTTP_200_OK and results:
        for planet in results:
            if planet.get('name') == name:
                movie_appearance = len(planet.get('films')) \
                    if planet.get('films') \
                    else 0

                return movie_appearance
    else:
        return 0
