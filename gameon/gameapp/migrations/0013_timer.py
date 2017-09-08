# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0012_auto_20170908_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.IntegerField(default=0)),
                ('id2', models.IntegerField(default=0)),
                ('timetill', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
