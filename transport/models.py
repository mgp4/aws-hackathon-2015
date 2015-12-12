from __future__ import unicode_literals

from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    timezone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class Calendar(models.Model):
    # service = models.ForeignKey('Service', related_name='calendars')
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '%s-%s (%s)' % (self.start_date, self.end_date, self.service)


class CalendarDate(models.Model):
    # service = models.ForeignKey('Service', related_name='calendar_dates')
    date = models.DateField()
    exception_type = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.date)


class Department(models.Model):
    agency = models.ForeignKey('Agency', related_name='departments')
    name = models.CharField(max_length=255)
    url = models.URLField()
    timezone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class Route(models.Model):
    agency = models.ForeignKey('Agency', related_name='routes')
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.short_name)


class Stop(models.Model):
    name = models.CharField(max_length=255)
    # stop_lat =
    # stop_lon =
    wheelchair_boarding = models.BooleanField()
    border = models.BooleanField()
    stop_description = models.TextField()
    gps_of_city = models.BooleanField()
    stop_timezone = models.CharField(max_length=20)
    stop_district = models.CharField(max_length=50)
    stop_region = models.CharField(max_length=50)
    stop_country = models.CharField(max_length=30)
    stop_city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class StopTime(models.Model):
    trip = models.ForeignKey('Trip', related_name='stop_times')
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    sequence = models.PositiveSmallIntegerField()
    pickup_type = models.PositiveSmallIntegerField()
    drop_off_type = models.PositiveSmallIntegerField()
    shape_dist_traveled = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s (%s)' % (self.trip, self.arrival_time)


class Trip(models.Model):
    route = models.ForeignKey('Route', related_name='trips')
    # service = models.ForeignKey('Service', related_name='trips')
    short_name = models.CharField(max_length=30)
    buyable = models.BooleanField()
    wheelchair_accessible = models.BooleanField()
    bike = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return '%s (%s)' % (self.short_name, self.route)
