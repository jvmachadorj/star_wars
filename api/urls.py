from django.urls import path

from api.views import *

urlpatterns = [
    path('planet/', PlanetListView.as_view(),
         name='planet_list'),
    path('planet/create', PlanetCreateView.as_view(),
         name='planet_create'),
    path('planet/<pk>/', PlanetRetriveDelete.as_view(),
         name='planet_retrieve_delete'),
]
