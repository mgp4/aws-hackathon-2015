# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('timezone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CalendarDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exception_type', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('timezone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='transport.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('long_name', models.CharField(max_length=255)),
                ('type', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='transport.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wheelchair_boarding', models.BooleanField()),
                ('border', models.BooleanField()),
                ('stop_description', models.TextField()),
                ('gps_of_city', models.BooleanField()),
                ('stop_timezone', models.CharField(max_length=20)),
                ('stop_district', models.CharField(max_length=50)),
                ('stop_region', models.CharField(max_length=50)),
                ('stop_country', models.CharField(max_length=30)),
                ('stop_city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StopTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('sequence', models.PositiveSmallIntegerField()),
                ('pickup_type', models.PositiveSmallIntegerField()),
                ('drop_off_type', models.PositiveSmallIntegerField()),
                ('shape_dist_traveled', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=30)),
                ('buyable', models.BooleanField()),
                ('wheelchair_accessible', models.BooleanField()),
                ('bike', models.BooleanField()),
                ('description', models.TextField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='transport.Route')),
            ],
        ),
        migrations.AddField(
            model_name='stoptime',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_times', to='transport.Trip'),
        ),
    ]
