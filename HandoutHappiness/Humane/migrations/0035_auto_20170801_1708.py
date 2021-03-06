# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-01 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0034_auto_20170801_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donatinguserdetail',
            old_name='name',
            new_name='donor_name',
        ),
        migrations.RemoveField(
            model_name='donatinguserdetail',
            name='mobile',
        ),
        migrations.AddField(
            model_name='donationitemdetail',
            name='goods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.GoodsDetail'),
            preserve_default=False,
        ),
    ]
