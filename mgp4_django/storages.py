from __future__ import absolute_import
import os

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
