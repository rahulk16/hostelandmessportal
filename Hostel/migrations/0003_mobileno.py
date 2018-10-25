# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0002_auto_20181024_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(default=0, max_length=10)),
                ('student', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Hostel.Student')),
            ],
        ),
    ]
