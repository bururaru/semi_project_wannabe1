# Generated by Django 3.1.5 on 2021-02-04 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendApp', '0004_auto_20210203_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_name', models.CharField(max_length=20)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendApp.totalcurriculum')),
            ],
        ),
    ]
