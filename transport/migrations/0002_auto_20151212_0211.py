# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stoptime',
            old_name='shape_dist_traveled',
            new_name='shape_dist_travelled',
        ),
        migrations.AddField(
            model_name='stoptime',
            name='stop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stop_times', to='transport.Stop'),
            preserve_default=False,
        ),
    ]
