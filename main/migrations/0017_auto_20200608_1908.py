# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-08 16:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200608_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='reviewDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 16, 8, 21, 921926, tzinfo=utc)),
        ),
    ]
