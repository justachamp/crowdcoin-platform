# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_crowdcoinpaymentlead_cancel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
