import csv
import json

from django.conf import settings
import boto3

from . import models

PLACES = '/tmp/data.json'


def import_places():
    with open(PLACES, 'r') as data:
        records = json.load(data)
        for r in records:
            models.Place.objects.create(**r)
            print('.'),
