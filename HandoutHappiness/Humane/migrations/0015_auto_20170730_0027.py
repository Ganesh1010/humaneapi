# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0014_auto_20170730_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsdetail',
            old_name='is_satisfied',
            new_name='is_good_satisfied',
        ),
        migrations.AddField(
            model_name='goodsitemdetail',
            name='is_good_item_satisfied',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
