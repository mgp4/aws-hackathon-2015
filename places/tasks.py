import csv
import json

from django.conf import settings
import boto3

from . import models

PLACES = '/tmp/data.json'

def download_places_data():
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(
        settings.AWS_STORAGE_BUCKET_NAME,
        'data.json',
        PLACES
    )

def import_places():
    with open(PLACES, 'r') as data:
        records = json.load(data)
        for r in records:
            models.Place.objects.create(**r)
            print('.'),
