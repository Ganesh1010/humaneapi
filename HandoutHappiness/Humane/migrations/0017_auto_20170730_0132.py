# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0016_auto_20170730_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsdetail',
            name='org_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.OrganisationDetail'),
        ),
    ]