from __future__ import unicode_literals

from django.core.cache import cache
from datetime import datetime
from django.db import models


def bool_field(csv_attr):
    return lambda csv: csv[csv_attr] != '0'

def date_field(csv_attr):
    return lambda csv: datetime.strptime(csv[csv_attr], '%Y%m%d').date()


class Manager(models.Manager):
    def _map_csv(self, csv):
        obj_dict = {}
        for my_attr, csv_attr in self.csv_mapping.items():
            if callable(csv_attr):
                value = csv_attr(csv)
            else:
                value = csv[csv_attr]
            obj_dict[my_attr] = value
        return obj_dict

    def get_or_create_csv(self, csv):
        if 'id' in self.csv_mapping:
            try:
                return self.get(id=csv[self.csv_mapping['id']])
            except models.ObjectDoesNotExist:
                pass
        return self.create(**self._map_csv(csv))


class AgencyManager(Manager):
    csv_mapping = {
        'id': 'agency_id',
        'name': 'agency_name',
        'url': 'agency_url',
        'timezone': 'agency_timezone',
        'address': 'agency_address',
        'phone': 'agency_phone',
        'email': 'agency_email',
    }


class Agency(models.Model):
    objects = AgencyManager()

    name = models.CharField(max_length=255)
    url = models.URLField()
    timezone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class CalendarManager(Manager):
    csv_mapping = {
        'monday': bool_field('monday'),
        'tuesday': bool_field('tuesday'),
        'wednesday': bool_field('wednesday'),
        'thursday': bool_field('thursday'),
        'friday': bool_field('friday'),
        'saturday': bool_field('saturday'),
        'sunday': bool_field('sunday'),
        'start_date': date_field('start_date'),
        'end_date': date_field('end_date'),
    }


class Calendar(models.Model):
    objects = CalendarManager()

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


class CalendarDateManager(Manager):
    csv_mapping = {
        'date': date_field('date'),
        'exception_type': 'exception_type',
    }


class CalendarDate(models.Model):
    objects = CalendarDateManager()

    # service = models.ForeignKey('Service', related_name='calendar_dates')
    date = models.DateField()
    exception_type = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.date)


class DepartmentManager(Manager):
    csv_mapping = {
        'id': 'department_id',
        'agency_id': 'agency_id',
        'name': 'department_name',
        'url': 'department_url',
        'timezone': 'department_timezone',
        'address': 'department_address',
        'phone': 'department_tel',
        'email': 'department_mail',
    }


class Department(models.Model):
    objects = DepartmentManager()

    agency = models.ForeignKey('Agency', related_name='departments',
                               db_constraint=False)
    name = models.CharField(max_length=255)
    url = models.URLField()
    timezone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class RouteManager(Manager):
    csv_mapping = {
        'id': 'route_id',
        'agency_id': 'agency_id',
        'short_name': 'route_short_name',
        'long_name': 'route_long_name',
        'type': 'route_type',
        'description': 'route_desc',
    }


class Route(models.Model):
    objects = RouteManager()

    agency = models.ForeignKey('Agency', related_name='routes',
                               db_constraint=False)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.short_name)



class StopManager(Manager):
    csv_mapping = {
        'id': 'stop_id',
        'name': 'stop_name',
        'lat': 'stop_lat',
        'lon': 'stop_lon',
        'wheelchair_boarding': bool_field('wheelchair_boarding'),
        'border': bool_field('border'),
        'description': 'stop_desc',
        'gps_of_city': bool_field('gps_of_city'),
        'timezone': 'stop_timezone',
        'district': 'stop_district',
        'region': 'stop_region',
        'country': 'stop_country',
        'city': 'stop_city',
    }


class Stop(models.Model):
    objects = StopManager()

    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=32, decimal_places=24)
    lon = models.DecimalField(max_digits=32, decimal_places=24)
    wheelchair_boarding = models.BooleanField()
    border = models.BooleanField()
    description = models.TextField()
    gps_of_city = models.BooleanField()
    timezone = models.CharField(max_length=20)
    district = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class StopTimeManager(Manager):
    csv_mapping = {
        'trip_id': 'trip_id',
        'arrival_time': 'arrival_time',
        'departure_time': 'departure_time',
        'stop_id': 'stop_id',
        'sequence': 'stop_sequence',
        'pickup_type': 'pickup_type',
        'drop_off_type': 'drop_off_type',
        'shape_dist_travelled': 'shape_dist_traveled',
    }


class StopTime(models.Model):
    objects = StopTimeManager()

    trip = models.ForeignKey('Trip', related_name='stop_times',
                             db_constraint=False)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop = models.ForeignKey('Stop', related_name='stop_times',
                             db_constraint=False)
    sequence = models.PositiveSmallIntegerField()
    pickup_type = models.PositiveSmallIntegerField()
    drop_off_type = models.PositiveSmallIntegerField()
    shape_dist_travelled = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s (%s)' % (self.trip, self.arrival_time)


class TripManager(Manager):
    csv_mapping = {
        'id': 'trip_id',
        'route_id': 'route_id',
        'short_name': 'trip_short_name',
        'buyable': bool_field('buyable'),
        'wheelchair_accessible': bool_field('wheelchair_accessible'),
        'bike': bool_field('bike'),
        'description': 'trip_desc',
    }

    def get_or_create_csv(self, csv):
        trip = super().get_or_create_csv(csv)
        cache.delete('trip_%d_stops' % trip.id)
        return trip


class Trip(models.Model):
    objects = TripManager()

    route = models.ForeignKey('Route', related_name='trips')
    # service = models.ForeignKey('Service', related_name='trips')
    short_name = models.CharField(max_length=30)
    buyable = models.BooleanField()
    wheelchair_accessible = models.BooleanField()
    bike = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return '%s (%s)' % (self.short_name, self.route)
