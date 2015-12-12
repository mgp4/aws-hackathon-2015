from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^map/$', views.stops_map, name='map'),
    url(r'^source/$', views.all_trips_stops, name='all_trips_stops'),
]
