from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from api.models import Planet


def setup_minimum_application():
    planet = Planet()
    planet.name = "Test"
    planet.terrain = "Moutain"
    planet.climate = "Frozen"
    planet.movie_appearance = 3
    planet.save()


class TestPlanetUrlsTestCase(TestCase):
    def setUp(self):
        setup_minimum_application()

        self.planet_data_to_create = {
            'name': 'Hort',
            'terrain': 'Flat',
            'climate': 'Hot'
        }

        self.client = Client()
        self.list = reverse('planet_list')
        self.create_url = reverse('planet_create')

    @patch('api.views.get_movie_appearance_by_name',
           return_value=2)
    def test_success_create_request(self, get_movie_appearance_by_name):
        request = self.client.post(self.create_url, self.planet_data_to_create,
                                   format='json')

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.data.get('movie_appearance'), 2)
        self.assertIsNotNone(Planet.objects.all())

    @patch('api.views.get_movie_appearance_by_name',
           return_value=2)
    def test_failure_create_request(self, get_movie_appearance_by_name):
        self.planet_data_to_create.pop('name')
        request = self.client.post(self.create_url, self.planet_data_to_create,
                                   format='json')

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_success_list_request(self):
        request = self.client.get(self.list)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(request.json())

    def test_success_retrieve_request(self):
        planet = Planet.objects.first()
        url = reverse('planet_retrieve_delete', args=[planet.pk])
        request = self.client.get(url)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json().get('id'), planet.pk)
        self.assertEqual(request.json().get('name'), planet.name)

    def test_failure_retrieve_request(self):
        planet = Planet.objects.first()
        url = reverse('planet_retrieve_delete', args=[planet.pk+6000])
        request = self.client.get(url)

        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_success_delete_request(self):
        planet = Planet.objects.first()
        url = reverse('planet_retrieve_delete', args=[planet.pk])
        request = self.client.delete(url)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

