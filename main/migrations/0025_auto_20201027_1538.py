# Generated by Django 3.0.7 on 2020-10-27 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20201026_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reviewDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 12, 38, 47, 926395, tzinfo=utc)),
        ),
    ]
