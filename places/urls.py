from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^source/$', views.places_map, name='source'),
]
