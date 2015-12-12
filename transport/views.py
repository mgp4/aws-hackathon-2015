from django.http import JsonResponse

from . import models


def all_trips_stops(request):
    trips = []
    for trip in models.Trip.objects.all()[:10]:
        stops = []
        for stop_time in trip.stop_times.all():
            stops.append((stop_time.stop.lat, stop_time.stop.lon))
        trips.append(stops)
    return JsonResponse(trips, safe=False)
