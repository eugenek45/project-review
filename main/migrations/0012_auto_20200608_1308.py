# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-08 10:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200608_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reviewDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 10, 8, 41, 742566, tzinfo=utc)),
        ),
    ]
