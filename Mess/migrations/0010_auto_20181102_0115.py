# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0009_auto_20181101_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messfeedback',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 1, 15, 58, 932502)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='indate',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='refund',
            name='outdate',
            field=models.DateField(default=None),
        ),
    ]