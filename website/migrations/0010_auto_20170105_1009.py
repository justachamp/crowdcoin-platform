# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-05 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170105_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtimepaymentlead',
            name='sim_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airtime_payment_lead_sim_card', to='website.SimCard'),
        ),
        migrations.AlterField(
            model_name='pocket',
            name='identifiers',
            field=models.ManyToManyField(blank=True, related_name='pocket_identifiers', to='website.UniqueIdentifier'),
        ),
        migrations.AlterField(
            model_name='pocket',
            name='transactions',
            field=models.ManyToManyField(blank=True, related_name='pocket_transactions', to='website.Transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='identifiers',
            field=models.ManyToManyField(blank=True, related_name='transaction_identifiers', to='website.UniqueIdentifier'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='identifier',
            field=models.ManyToManyField(blank=True, related_name='user_profile_identifier', to='website.UniqueIdentifier'),
        ),
    ]
