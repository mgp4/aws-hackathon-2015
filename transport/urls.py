from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.all_trips_stops, name='all_trips_stops'),
]
