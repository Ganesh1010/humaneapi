# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-31 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0029_auto_20170731_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationdetail',
            name='delivered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationdetail',
            name='received_by',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
