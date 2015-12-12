# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lng', models.DecimalField(decimal_places=24, max_digits=32)),
                ('lat', models.DecimalField(decimal_places=24, max_digits=32)),
                ('men', models.IntegerField()),
                ('women', models.IntegerField()),
                ('total', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
    ]
