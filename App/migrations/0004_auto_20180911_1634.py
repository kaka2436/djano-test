# Generated by Django 2.1.1 on 2018-09-11 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20180911_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birth',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 16, 34, 59, 624646), verbose_name='生日'),
        ),
    ]