import csv
import zipfile

from django.conf import settings
import boto3

from . import models

DOWNLOADED = '/tmp/result.zip'
EXTRACTED = '/tmp/result-extracted'


def download_unzip(number):
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(
        settings.AWS_STORAGE_BUCKET_NAME,
        'transportation/result%d.zip' % number,
        DOWNLOADED
    )

    zfile = zipfile.ZipFile(DOWNLOADED)
    zfile.extractall(EXTRACTED)


def parse_extracted():
    csv_mapping = {
        'agency': models.Agency,
        'calendar': models.Calendar,
        'calendar_dates': models.CalendarDate,
        'departments': models.Department,
        'routes': models.Route,
        'stops': models.Stop,
        'stop_times': models.StopTime,
        'trips': models.Trip,
    }
    for source, target in csv_mapping.items():
        with open('%s/%s.txt' % (EXTRACTED, source)) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    target.objects.get_or_create_csv(row)
                except Exception as e:
                    print(row)
