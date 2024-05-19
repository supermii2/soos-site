from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon

def api_get_all_pokemon(request):
    pokemon = Pokemon.objects.all()
    data = {}
    for p in pokemon:
        data[p.slug] = p.serialize()
    return JsonResponse(data)

def api_get_pokemon(request, slug):
    pokemon = Pokemon.objects.get(slug=slug)
    return JsonResponse(pokemon.serialize())

def pokedex_get_pokemon(request, slug):
    pokemon = Pokemon.objects.get(slug=slug).serialize()
    return render(request, 'dex_entry.html', pokemon)