# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-31 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0027_auto_20170731_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationdetail',
            name='promised_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
