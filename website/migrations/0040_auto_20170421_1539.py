# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-21 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_userprofile_referrer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='registered_name',
        ),
        migrations.AddField(
            model_name='merchant',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]