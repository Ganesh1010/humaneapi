# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0002_auto_20170717_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedUnitLookUp',
            fields=[
                ('allowed_unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_item_id', models.IntegerField()),
                ('unit_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoordinatorDetail',
            fields=[
                ('coordinator_id', models.AutoField(primary_key=True, serialize=False)),
                ('organisation_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('user_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DonationDetail',
            fields=[
                ('donation_id', models.AutoField(primary_key=True, serialize=False)),
                ('need_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('promised_date', models.DateTimeField()),
                ('received_date', models.DateTimeField()),
                ('received_by', models.CharField(max_length=500)),
                ('is_volunteer_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DonationItemDetail',
            fields=[
                ('donation_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('donation_id', models.IntegerField()),
                ('goods_item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('delivered_quantity', models.IntegerField()),
                ('unit_id', models.IntegerField()),
                ('goods_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsItemDetail',
            fields=[
                ('goods_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('posted_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('subitem_id', models.IntegerField()),
                ('unit_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MainItemTypeLookUp',
            fields=[
                ('main_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('main_item_name', models.CharField(max_length=100)),
                ('request_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestTypeLookUp',
            fields=[
                ('request_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('rquest_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubItemTypeLookUp',
            fields=[
                ('sub_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_item_name', models.CharField(max_length=100)),
                ('main_item_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UnitLookUp',
            fields=[
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('country_id', models.IntegerField()),
                ('zipcode', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('registered_date', models.DateTimeField()),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(max_length=500)),
                ('region_id', models.IntegerField()),
                ('state_id', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='goodsdetail',
            old_name='need_id',
            new_name='goods_id',
        ),
        migrations.RenameField(
            model_name='goodsdetail',
            old_name='need_txt_desc',
            new_name='goods_txt_desc',
        ),
        migrations.RenameField(
            model_name='goodsdetail',
            old_name='need_type',
            new_name='request_type',
        ),
    ]
