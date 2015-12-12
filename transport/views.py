from django.http import JsonResponse
from django.shortcuts import render

from . import models


def stops_map(request):
    return render(request, 'transport/map.html')


def all_trips_stops(request):
    trips = []
    for trip in models.Trip.objects.all():
        stops = []
        for stop_time in trip.stop_times.all().select_related('stop'):
            stops.append((stop_time.stop.lat, stop_time.stop.lon))
        trips.append(stops)
    return JsonResponse(trips, safe=False)
