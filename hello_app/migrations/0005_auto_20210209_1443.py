# Generated by Django 3.1.6 on 2021-02-09 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0004_auto_20210209_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 5, 43, 20, 696115, tzinfo=utc)),
        ),
    ]
