# Generated by Django 3.0.7 on 2020-10-26 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200609_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reviewDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 26, 9, 29, 37, 968841, tzinfo=utc)),
        ),
    ]
