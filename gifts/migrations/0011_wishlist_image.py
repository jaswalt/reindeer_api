# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0010_auto_20171128_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
