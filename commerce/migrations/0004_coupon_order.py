# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 05:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0003_auto_20160812_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('r', 'ratio'), ('f', 'fixed')], max_length=1)),
                ('ratio', models.FloatField(default=1)),
                ('amount', models.FloatField(default=0)),
                ('threshold', models.FloatField(default=0)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=16)),
                ('purchase_count', models.IntegerField()),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Coupon')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='commerce.Item')),
                ('placer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placed_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]