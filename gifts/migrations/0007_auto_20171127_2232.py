# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0006_auto_20171127_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='photo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gift',
            name='sku',
            field=models.IntegerField(blank=True),
        ),
    ]
