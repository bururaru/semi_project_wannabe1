# Generated by Django 3.1.6 on 2021-02-09 06:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0007_auto_20210209_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 6, 12, 42, 676933, tzinfo=utc)),
        ),
    ]
