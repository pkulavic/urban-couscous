# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0004_availability_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='day',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=200),
        ),
    ]
