# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0007_auto_20160819_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='place_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
