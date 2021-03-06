# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-28 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_promotion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='amount',
        ),
        migrations.AddField(
            model_name='promotion',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='promotion',
            name='reward_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
