# Generated by Django 2.1.1 on 2018-09-11 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_users_生日'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='生日',
        ),
        migrations.AddField(
            model_name='users',
            name='birth',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 16, 34, 21, 478145)),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.NullBooleanField(default=None),
        ),
    ]