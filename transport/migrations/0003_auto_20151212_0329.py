# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_auto_20151212_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stop',
            old_name='stop_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='stop',
            old_name='stop_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='stop',
            old_name='stop_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='stop',
            old_name='stop_district',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='stop',
            old_name='stop_region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='stop',
            old_name='stop_timezone',
            new_name='timezone',
        ),
    ]
