# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0003_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(default='', max_length=15),
        ),
    ]