# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_auto_20171120_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
