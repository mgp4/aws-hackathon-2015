from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from . import models

def places_map(request):
    places = []
    for place in models.Place.objects.all():
        places.append((place.lat, place.lng, place.total))
    return JsonResponse(places, safe=False)
