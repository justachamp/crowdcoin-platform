# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-07 17:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20170107_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='airtimedepositlead',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 1, 7, 19, 39, 55, 204633)),
        ),
    ]