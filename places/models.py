from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Place(models.Model):
    lng = models.DecimalField(max_digits=32, decimal_places=24)
    lat = models.DecimalField(max_digits=32, decimal_places=24)
    men = models.IntegerField()
    women = models.IntegerField()
    total = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return '%s (%s, %s)' % (self.total, self.lng, self.lat)

