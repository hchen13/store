# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20160815_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]