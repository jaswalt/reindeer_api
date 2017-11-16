# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=30)
    price_in_cents = models.IntegerField()
    sku = models.IntegerField()


class Wishlist(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    gifts = models.ManyToManyField(Gift)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    friends = models.ManyToManyField("self")
