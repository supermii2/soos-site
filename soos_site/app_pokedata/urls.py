from django.urls import path
from .views import (
    api_get_pokemon, api_get_all_pokemon,
    pokedex_get_pokemon,
)
urlpatterns = [
    path('api/', api_get_all_pokemon, name='api_poke_all'),
    path('api/<str:slug>/', api_get_pokemon, name='api_poke'),
    path("dex/<str:slug>/", pokedex_get_pokemon, name="get_poke"),
]