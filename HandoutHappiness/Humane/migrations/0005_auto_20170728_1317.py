# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-28 07:47
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Humane', '0004_auto_20170721_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinatorDetail',
            fields=[
                ('coordinator_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DonationDetail',
            fields=[
                ('donation_id', models.AutoField(primary_key=True, serialize=False)),
                ('promised_date', models.DateTimeField()),
                ('received_date', models.DateTimeField()),
                ('received_by', models.CharField(max_length=250)),
                ('is_volunteer_required', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DonationItemDetail',
            fields=[
                ('donation_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('promised_quantity', models.IntegerField()),
                ('delivered_quantity', models.IntegerField()),
                ('donation_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.DonationDetail')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationDetail',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_reg_no', models.IntegerField()),
                ('org_name', models.CharField(max_length=100)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('org_type', models.CharField(max_length=200)),
                ('org_desc', models.CharField(max_length=500)),
                ('org_logo', models.CharField(max_length=300)),
                ('people_count', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='requesttypelookup',
            old_name='rquest_type_name',
            new_name='request_type_name',
        ),
        migrations.RemoveField(
            model_name='goodsdetail',
            name='main_item_id',
        ),
        migrations.RemoveField(
            model_name='goodsdetail',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='subitemtypelookup',
            name='main_item_code',
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='main_item_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.MainItemTypeLookUp'),
        ),
        migrations.AddField(
            model_name='subitemtypelookup',
            name='main_item_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.MainItemTypeLookUp'),
        ),
        migrations.AlterField(
            model_name='allowedunitlookup',
            name='sub_item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.SubItemTypeLookUp'),
        ),
        migrations.AlterField(
            model_name='allowedunitlookup',
            name='unit_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.UnitLookUp'),
        ),
        migrations.AlterField(
            model_name='goodsdetail',
            name='request_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.RequestTypeLookUp'),
        ),
        migrations.AlterField(
            model_name='goodsitemdetail',
            name='goods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.GoodsDetail'),
        ),
        migrations.AlterField(
            model_name='goodsitemdetail',
            name='sub_item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.SubItemTypeLookUp'),
        ),
        migrations.AlterField(
            model_name='goodsitemdetail',
            name='unit_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.UnitLookUp'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AddField(
            model_name='donationitemdetail',
            name='goods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.GoodsDetail'),
        ),
        migrations.AddField(
            model_name='donationitemdetail',
            name='goods_item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.GoodsItemDetail'),
        ),
        migrations.AddField(
            model_name='donationitemdetail',
            name='unit_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.UnitLookUp'),
        ),
        migrations.AddField(
            model_name='donationdetail',
            name='goods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.GoodsDetail'),
        ),
        migrations.AddField(
            model_name='coordinatordetail',
            name='organisation_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.OrganisationDetail'),
        ),
        migrations.AddField(
            model_name='coordinatordetail',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='org_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Humane.OrganisationDetail'),
        ),
    ]