# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0008_auto_20170728_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinatordetail',
            old_name='organisation_id',
            new_name='org_id',
        ),
    ]