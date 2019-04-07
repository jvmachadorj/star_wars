from unittest.mock import patch, MagicMock

from django.test import TestCase
from rest_framework import status

from api.star_wars_api_communication import get_movie_appearance_by_name
from api.tests.mocks.mocks import STAR_WARS_API


class TestPlanetUrlsTestCase(TestCase):

    @patch('api.star_wars_api_communication.request')
    def test_calculate_movie_appearance(self, request):
        request_object = MagicMock()
        request_object.status_code = status.HTTP_200_OK
        request_object.json.return_value = STAR_WARS_API
        request.return_value = request_object
        result = get_movie_appearance_by_name("Hoth")

        self.assertEqual(result, 1)
